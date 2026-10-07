"""Run every question in one AIME JSON dataset through Gemma 4, sequentially."""

import base64
import json
import os
import re
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

DATASET = "aime_2026.json"  # Change the dataset as needed
MODEL = "gemma-4-26b-a4b-it"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
PROMPT = (
    "Solve the math problem carefully. You may show your work. "
    "Ensure you leave at least 50 tokens for your answer; do not use all of "
    "your tokens for thinking. Your final line must be exactly FINAL: "
    "followed by one space and three digits, such as FINAL: 020."
)


def open_with_timeout_retry(request, timeout):
    for attempt in range(2):
        try:
            return urlopen(request, timeout=timeout)
        except (TimeoutError, URLError) as error:
            # urllib sometimes wraps a socket read timeout in URLError.
            if isinstance(error, URLError) and not isinstance(error.reason, TimeoutError):
                raise
            if attempt == 1:
                raise
            print("Read timeout; retrying in 10 seconds...", flush=True)
            time.sleep(10)


def run_question(item, api_key):
    parts = []
    if item.get("image"):
        with open_with_timeout_retry(item["image"], 40) as response:
            parts.append({"inline_data": {
                "mime_type": response.headers.get_content_type(),
                "data": base64.b64encode(response.read()).decode("ascii"),
            }})
    parts.append({"text": item["problem"]})

    payload = {
        "systemInstruction": {"parts": [{"text": PROMPT}]},
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "temperature": 1.0,
            "topP": 0.95,
            "topK": 64,
            "maxOutputTokens": 24576,
            "thinkingConfig": {"thinkingLevel": "high"},
        },
    }
    request = Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
    )
    with open_with_timeout_retry(request, 600) as response:
        data = json.load(response)

    candidate = data["candidates"][0]
    output = "\n".join(
        part.get("text", "")
        for part in candidate["content"]["parts"]
        if not part.get("thought")
    ).strip()
    match = re.search(r"(?:^|\n)FINAL: ([0-9]{3})\s*$", output)
    predicted = match.group(1) if match else None
    expected = str(item["answer"]).zfill(3)
    return {
        "id": item["id"],
        "expected": expected,
        "predicted": predicted,
        "status": "correct" if predicted == expected else "incorrect" if predicted else "unparsed",
        "raw_output": output,
        "finish_reason": candidate.get("finishReason"),
    }

def main():
    api_key = "" # here's where you paste in your API key
    dataset_path = Path(__file__).with_name(DATASET)
    problems = json.loads(dataset_path.read_text(encoding="utf-8"))
    output_path = dataset_path.with_name(dataset_path.stem + "_gemma4_26b_a4b_results.json")

    results = []
    for number, item in enumerate(problems, 1):
        result = run_question(item, api_key)
        results.append(result)
        output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"[{number}/{len(problems)}] {item['id']}: {result['status']}", flush=True)
        if number < len(problems):
            time.sleep(8)

    correct = sum(result["status"] == "correct" for result in results)
    unparsed = sum(result["status"] == "unparsed" for result in results)
    print(f"Score: {correct}/{len(problems)} ({correct / len(problems):.1%}); unparsed: {unparsed}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
