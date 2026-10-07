# Research-Project

This is my GitHub repository for my Regeneron STS Submission.

I investigated whether providing curated reference material (a "cheatsheet") to medium-size language models improves their performance on competition mathematics.

Here are the scripts (you need an API key from Google to run these):

- [base script, without the cheatsheet](base_bench.py)
- [script with the cheathseet](new_bench.py)

Results are here:
- [aime 2025, base](aime_2025_base_results.json)
- [aime 2025, with cheatsheet](aime_2025_new_results.json)
- [aime 2026, base](aime_2026_base_results.json)
- [aime 2026, with cheatsheet](aime_2026_new_results.json)

Here's the datasets:
- [AIME 2025 I](aime_2025.json)
- [AIME 2026 I](aime_2026.json)

Here's the [cheatsheet](aime_cheatsheet.md) that gets sent over automatically when you run the script with the cheatsheet.

The images are also stored in this repository; they get sent over automatically.
