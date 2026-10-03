# AIME 2025–2026: Formula & Technique Sheet

## Algebra & Analysis

- **Newton’s sums.** $P_k=\sum_{i=1}^n r_i^k$, $e_j$ elementary symmetric sums; $P_k=\sum_{j=1}^{k-1}(-1)^{j-1}e_jP_{k-j}+(-1)^{k-1}ke_k$ ($k\le n$); $P_k=\sum_{j=1}^n(-1)^{j-1}e_jP_{k-j}$ ($k>n$). **Trigger:** Find root power sums without solving the polynomial.
- **Linear recurrences.** $u_n=\sum_{j=1}^d c_ju_{n-j}$, $c_d\ne0$; characteristic $t^d-\sum c_jt^{d-j}=0$; $u_n=\sum_i\sum_{h=0}^{m_i-1}A_{ih}n^h\lambda_i^n$, where $m_i$ is root multiplicity. **Trigger:** Constant-coefficient recurrences need closed forms; fit constants from initial values.
- **Cauchy–Schwarz/Engel.** $\sum a_i^2/b_i\ge(\sum a_i)^2/\sum b_i$ ($b_i>0$); equality iff $a_i/b_i$ constant. **Trigger:** Bound sums of fractions with related denominators.
- **Weighted AM–GM.** $\sum w_ix_i\ge\prod x_i^{w_i}$ ($x_i>0,w_i>0,\sum w_i=1$); equality iff all $x_i$ equal. **Trigger:** Optimize fixed sums/products; equality must satisfy every original constraint.
- **Schur.** $\sum_{\rm cyc}a(a-b)(a-c)\ge0$ ($a,b,c\ge0$); equality: all equal, or two equal and the third zero. **Trigger:** Bound symmetric cubic expressions.
- **Roots-of-unity filter.** $\omega=e^{2\pi i/n}$; $\frac1n\sum_{j=0}^{n-1}\omega^{jk}=\mathbf1_{n\mid k}$; for $f(x)=\sum a_kx^k$, $\sum_{k\equiv r\pmod n}a_k=\frac1n\sum_j\omega^{-jr}f(\omega^j)$. **Trigger:** Extract coefficients in residue classes.
- **Unit-circle evaluation.** $z=e^{i\theta}$: $z+z^{-1}=2\cos\theta$, $|z-a|^2=1+a^2-2a\cos\theta$ ($a\in\mathbb R$); $z^n-1=\prod_{j=0}^{n-1}(z-\omega^j)$. **Trigger:** Evaluate cyclic products or reciprocal polynomials.
- **Interpolation.** $f(x)=\sum_{i=0}^d f(t_i)\prod_{j\ne i}\frac{x-t_j}{t_i-t_j}$ ($\deg f\le d$, distinct $t_i$). **Trigger:** Recover polynomial values from sparse data.
- **Reciprocal substitution.** $t=x+x^{-1}$: $x^2+x^{-2}=t^2-2$; $S_{k+1}=tS_k-S_{k-1}$, $S_0=2,S_1=t$. **Trigger:** Reduce palindromic polynomial degree after dividing by its middle power.

## Combinatorics & Probability

- **Bounded stars-and-bars.** $\sum x_i=N$, $\ell_i\le x_i\le u_i$; $M=N-\sum\ell_i$, $b_i=u_i-\ell_i+1$; count $=\sum_{S\subseteq[k]}(-1)^{|S|}\binom{M-\sum_{i\in S}b_i+k-1}{k-1}$; impossible terms zero. **Trigger:** Count integer allocations with bounds; omit unbounded indices from PIE.
- **Inclusion–exclusion.** $|\bigcup A_i|=\sum_{\varnothing\ne S}(-1)^{|S|+1}|\bigcap_{i\in S}A_i|$. **Trigger:** Several forbidden conditions overlap.
- **Indicators.** $E[\sum I_i]=\sum\Pr(I_i=1)$, independence unnecessary; $E_s=g(s)+\sum_t p_{st}E_t$. **Trigger:** Count expected features or solve graph/path states with absorbing boundaries.
- **OGFs.** $[x^N]\prod_i(1-x^{(b_i+1)d_i})/(1-x^{d_i})$ counts indistinguishable size-$d_i$ items with capacities $b_i$; unlimited factor $(1-x^{d_i})^{-1}$. **Trigger:** Count bounded partitions or unordered change-making.
- **Catalan.** $C_n=\frac1{n+1}\binom{2n}{n}$; $C_{n+1}=\sum_{i=0}^nC_iC_{n-i}$. **Trigger:** Count balanced parentheses, noncrossing structures, or paths below the diagonal.
- **Derangements.** $D_n=n!\sum_{k=0}^n(-1)^k/k!$; exactly $r$ fixed points: $\binom nrD_{n-r}$. **Trigger:** Count permutations with restricted fixed points.
- **Finite-state counting.** $v_{n+1}=Tv_n$, $v_n=T^nv_0$. **Trigger:** Local adjacency restrictions allow a small state graph.
- **Burnside.** $\text{orbits}=|G|^{-1}\sum_{g\in G}|\text{Fix}(g)|$. **Trigger:** Count arrangements equivalent under specified rotations/reflections.
- **Conditional probability.** $\Pr(A\mid B)=\Pr(A\cap B)/\Pr(B)$; $\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$ for a partition $(B_i)$. **Trigger:** Conditioning changes the sample space or cases have unequal weights.

## Number Theory

- **LTE, odd prime.** $v_p(t)=\max\{j:p^j\mid t\}$; $v_p(a^n-b^n)=v_p(a-b)+v_p(n)$ if $p\mid a-b$, $p\nmid ab$, $n\ge1$; for odd $n$, replace differences by sums when $p\mid a+b$. **Trigger:** Find prime exponents in powers’ differences/sums.
- **LTE, two.** Odd $a,b$: $v_2(a^n-b^n)=v_2(a-b)$ for odd $n$; for even $n$, $v_2(a-b)+v_2(a+b)+v_2(n)-1$; odd $n$: $v_2(a^n+b^n)=v_2(a+b)$. **Trigger:** Determine exact powers of two dividing exponential expressions.
- **Bézout/CRT.** $au+mv=\gcd(a,m)$; coprime: $a^{-1}\equiv u\pmod m$. Pairwise-coprime $m_i$: $x\equiv\sum a_iM_i(M_i^{-1}\bmod m_i)\pmod M$, $M=\prod m_i$, $M_i=M/m_i$. **Trigger:** Combine congruences; noncoprime pairs require agreement modulo their gcd.
- **Multiplicative functions.** $n=\prod p_i^{\alpha_i}$: $\tau(n)=\prod(\alpha_i+1)$, $\sigma(n)=\prod\frac{p_i^{\alpha_i+1}-1}{p_i-1}$, $\phi(n)=n\prod(1-1/p_i)$; $a^{\phi(n)}\equiv1\pmod n$ if $\gcd(a,n)=1$. **Trigger:** Count/sum divisors or reduce modular exponents.
- **Factorial valuations.** $v_p(n!)=\sum_{j\ge1}\lfloor n/p^j\rfloor$. **Trigger:** Determine factorial/binomial divisibility or trailing zeros.
- **SFFT.** $xy+ax+by=c\iff(x+b)(y+a)=c+ab$; $Axy+Bx+Cy=D\implies(Ax+C)(Ay+B)=AD+BC$. **Trigger:** Convert integer equations into divisor pairs; retain congruence/sign constraints.
- **Pell.** $x^2-Dy^2=1$: $x_k+y_k\sqrt D=(x_1+y_1\sqrt D)^k$ ($D\in\mathbb Z_{>0}$ nonsquare; least positive solution from continued-fraction convergents). **Trigger:** Find integer pairs satisfying quadratic square conditions.
- **Order/residue obstructions.** $a^k\equiv1\pmod m\iff\text{ord}_m(a)\mid k$ ($\gcd(a,m)=1$); squares modulo $8$: $\{0,1,4\}$; modulo $3$: $\{0,1\}$. **Trigger:** Restrict exponential periods or eliminate impossible integer solutions.

## Geometry & Trigonometry

- **Triangle metric toolkit.** $a=BC,b=CA,c=AB,s=(a+b+c)/2$; $K=\sqrt{s(s-a)(s-b)(s-c)}=rs=abc/(4R)$; $OI^2=R(R-2r)$. **Trigger:** Relate area, sides, inradius, circumradius, and centers.
- **Stewart.** $D\in BC$, $BD=m$, $DC=n$, $AD=d$: $b^2m+c^2n=a(d^2+mn)$. **Trigger:** Compute arbitrary cevian lengths.
- **Ceva.** $D\in BC,E\in CA,F\in AB$: $\frac{BD}{DC}\frac{CE}{EA}\frac{AF}{FB}=1$; $\frac{\sin\angle BAD}{\sin\angle DAC}\frac{\sin\angle CBE}{\sin\angle EBA}\frac{\sin\angle ACF}{\sin\angle FCB}=1$. **Trigger:** Prove concurrency of internal cevians.
- **Menelaus.** Directed ratios: $\frac{\overline{BD}}{\overline{DC}}\frac{\overline{CE}}{\overline{EA}}\frac{\overline{AF}}{\overline{FB}}=-1$. **Trigger:** Prove collinearity across three triangle sidelines.
- **Power/radical axis.** $\text{Pow}(P)=PO^2-R^2=\overline{PA}\cdot\overline{PB}=PT^2$; nonconcentric circles’ equal-power locus is a line; pairwise axes concur when two intersect. **Trigger:** Link secants/tangents or several circles; use directed secants.
- **Cyclic quadrilaterals.** $AC\cdot BD=AB\cdot CD+BC\cdot DA$; $K=\sqrt{(s-a)(s-b)(s-c)(s-d)}$, $s=(a+b+c+d)/2$. **Trigger:** Determine cyclic diagonals or area.
- **Shoelace/Pick.** $K=\frac12|\sum_i(x_iy_{i+1}-y_ix_{i+1})|$; lattice polygon: $K=I+B/2-1$. **Trigger:** Compute ordered polygon area or lattice-point counts.
- **Barycentrics.** $(u:v:w)\mapsto(uA+vB+wC)/(u+v+w)$; $G=(1:1:1)$, $I=(a:b:c)$, $H=(\tan A:\tan B:\tan C)$; right triangle: $H$ is right-angle vertex. **Trigger:** Translate centers and cevian ratios into coordinates.
- **Tangent machinery.** $\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$; $\tan3\theta=(3t-t^3)/(1-3t^2)$, $t=\tan\theta$. **Trigger:** Turn angle sums/multiples into rational equations; check poles and angle branches.
