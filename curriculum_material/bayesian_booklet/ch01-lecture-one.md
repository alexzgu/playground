# Chapter 1 — Lecture One
*(PDF pages 6–13; booklet pages 1–8)*

### PDF page 6 (booklet page 1)

# Chapter 1 — Lecture One

Three skills are needed in this course.

a. Data analysis skills
b. Technical skills.
c. Computation skills.

Combine these skills.

Recommend reading material: **The Statistician 32 (1983)**, Theory and Practice of Bayesian Statistics, *Dennis Lindley*. *[the journal reference is hand-underlined]*

"Bayesian statistics is based on one simple idea: The only satisfactory description of uncertainty is by means of probability. We are, all of us, surrounded by uncertainty: it plays a dominant role in our lives. The Bayesian paradigm provides, in probability, a powerful tool for understanding, manipulating and controlling this pervasive and often unpleasant feature of our appreciation of our environment. The practical import is immediate: any unknown quantity should be described probabilistically." *[the final clause is hand-underlined]*

**1.1 Bayesian Paradigm**

Interest is on a quantity, or set of quantities, $\theta$.
Some data $D$ are available and $D$ has some relationship on the uncertainty of $\theta$. (Here $D$ is known, but $\theta$ is unknown.) *[margin note: likelihood function]*
There is also background knowledge pertaining to the situation under study which we denote by $H$ (history). *[margin note: prior distribution]*
The Bayesian view says that the appropriate description of your knowledge of $\theta$ in the presence of $D$ and $H$ is by the probability of $\theta$, given $D$ and $H$, and written as $P(\theta\mid D,H)$.

**Key idea:** Every unknown quantity (like $\theta$) must be described by a distribution. That is every unknown quantity is a random variable. *[margin note at bottom: prior, $\pi(\theta)$]*

### PDF page 7 (booklet page 2)

**1.2 Review background of probability**

**A. Probability Fundamentals:**

Probability space $\{S, \mathcal{B}, P\}$
$S$: all possible outcomes of an experiment;
$\mathcal{B}$: sigma algebra;
$P$: probability measure.

**B. Sigma algebra**

1. $\emptyset \in \mathcal{B}$;
2. $A \in \mathcal{B} \Rightarrow A^c \in \mathcal{B}$;
3. $A_1, A_2, \ldots \in \mathcal{B} \Rightarrow \bigcup_{i=1}^{\infty} A_i \in \mathcal{B}$

**C. Probability measure**

Axioms of probability (Kolmogorov axioms)
$$P : \mathcal{B} \to R, \qquad A \to P(A)$$

1. $P(A) \ge 0$ for all $A \in \mathcal{B}$;
2. $P(S) = 1$;
3. $A_1, A_2, \ldots \in \mathcal{B},\ A_i \cap A_j = \emptyset,\ i \ne j \ \Rightarrow\ P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$.

**Without any assumptions,**

1. $P(\emptyset) = 0$;
2. $P(A) \le 1$ for any $A \in \mathcal{B}$;
3. $P(A^c) = 1 - P(A)$ for any $A \in \mathcal{B}$
4. $P(A) \le P(B)$ if $A \subset B$;
5. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$;
6. $P(A) = P(A \cap B) + P(A \cap B^c)$, $B$ and $B^c$ partition $S$, $A \cap B$ and $A \cap B^c$ partition $A$; $P(A) = \sum_{i=1}^{\infty} P(A \cap C_i)$, $C_1, C_2, \ldots$ partition $S$. *[the word "partition" is hand-underlined in three places]*

> ✔ Verified: properties 1–6 are the standard consequences of the Kolmogorov axioms (each follows from countable additivity + normalization; e.g. 6 is the law of total probability).

### PDF page 8 (booklet page 3)

**1.3 Coherent**

A scientist is called incoherent if he violates any of the axioms of probability.
For us to be coherent we must follow the rules of probability in our arguments.

**Example: Toyota and Honda cars.** Scientist says:
$$P(H) = \tfrac{1}{3}, \qquad P(\text{both}) = \tfrac{1}{12} = P(H \cap T)$$
$$P(T) = \tfrac{2}{3}, \qquad P(\text{either}) = \tfrac{1}{2} = P(H \cup T)$$

Is he coherent?
Since $P(H \cup T) = P(H) + P(T) - P(H \cap T) = \frac{1}{3} + \frac{2}{3} - \frac{1}{12} = \frac{11}{12} \ne \frac{1}{2}$.
So, this scientist is not coherent (incoherent).

> ✔ Verified: $\frac{1}{3}+\frac{2}{3}-\frac{1}{12} = \frac{4+8-1}{12} = \frac{11}{12} \ne \frac12$. The stated incoherence is correct.

Two probability rules are $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ — **Addition rule**; $0 \le P(A) \le 1$, $P(S) = 1$ — **Convexity rule**.

**1.4 Conditional Probability**

Suppose $A, B$, $P(B) > 0$, thus $P(A\mid B) = \dfrac{P(A \cap B)}{P(B)}$.
Hence, $P(A \cap B) = P(A\mid B)P(B)$ — **Multiplication rule**.
This is the third among three rules we use in Bayesian analysis.
Similarly: $P(A) > 0$, $P(B\mid A) = \dfrac{P(A \cap B)}{P(A)}$, so $P(A \cap B) = P(B\mid A)P(A)$.
Therefore, $P(A\mid B)P(B) = P(B\mid A)P(A)$. So $P(A\mid B) = \dfrac{P(B\mid A)P(A)}{P(B)}$.
Since $P(B) = P(B \cap A) + P(B \cap A^c) = P(B\mid A)P(A) + P(B\mid A^c)P(A^c)$.
Thus,
$$P(A\mid B) = \frac{P(B\mid A)P(A)}{P(B\mid A)P(A) + P(B\mid A^c)P(A^c)} \;\text{— Normalization (key quantity)}.$$
This is so called **Bayes' theorem!**

**Remark** *[margin note: $K$ constant]*
$P(B\mid A) = K\,P(A\mid B)P(B)$
$P(B^c\mid A) = K\,P(A\mid B^c)P(B^c)$
Add both sides of the equation, we have:
$P(B\mid A) + P(B^c\mid A) = 1 = K[P(A\mid B)P(B) + P(A\mid B^c)P(B^c)]$.
Hence, $K = \dfrac{1}{P(A\mid B)P(B) + P(A\mid B^c)P(B^c)}$.

> ✔ Verified: the normalization argument is exact — the two displayed equations sum to 1 on the left because $B, B^c$ partition the space given $A$.

Bayes' theorem tells us how to behave (i.e., how to update our past information based on

### PDF page 9 (booklet page 4)

today's data. ). It combines two or more sources of information.

**Example.** Two factories produce 2inch bolts, one factory is twice as large as the other.
$P(F=1) = \frac{1}{3}$, $P(F=2) = \frac{2}{3}$ — \*prior assignments (before data are observed).
$P(D\mid F=1) = \frac{2}{10}$, $P(D\mid F=2) = \frac{1}{10}$ — \*\*likelihood function (data).
A bolt is selected at random from the market, and it is found that it is defective.
What is the probability it came from factory 1?
That is, we want know $P(F=1\mid D)$ — \*\*\* posterior probability.

Using Bayes' theorem,
$$P(F=1\mid D) = \frac{P(D\mid F=1)P(F=1)}{P(D\mid F=1)P(F=1) + P(D\mid F=2)P(F=2)} = \frac{\frac{2}{10}\frac{1}{3}}{\frac{2}{10}\frac{1}{3} + \frac{1}{10}\frac{2}{3}} = \frac{1}{2}.$$

I have updated $P(F=1) = \frac{1}{3}$ to $P(F=1\mid D) = \frac{1}{2}$.

> ✔ Verified: numerator $\frac{2}{30}$; denominator $\frac{2}{30}+\frac{2}{30}=\frac{4}{30}$; ratio $=\frac12$ exactly.

**Random variables**
$$\text{Function } X : S \to R, \qquad A \to X(A) = a, \ \text{s.t.}\ X^{-1}(a) \in \mathcal{B}.$$

**1.5 Distribution Function**

$F$ cumulative distribution function (CDF).
$F(x) = P(X \le x)$ for all $x \in R$.
$f(x) = P(X = x)$, $X$ is discrete.
$f(x) = \frac{d}{dx}F(x)$, $X$ is continuous.
$f(x)$ is a probability measure, $f(x) \ge 0$.
$\int_{-\infty}^{\infty} f(x)dx = 1$, or $\sum_x f(x) = 1$.
$X$ and $Y$ are identically distributed if for any $A$, $P(X \in A) = P(Y \in A)$ or $F_X(x) = F_Y(x)$ for all $x$. Hence, $X$ and $Y$ are interchangeable (exchangeable).
$F$ is continuous and $F(X) \sim U(0,1)$ uniform distribution (**probability integral transform**).

**1.6 Transformations**

If we have $\theta$, $\phi = g(\theta)$, then use transformation to get the distribution of $\phi$. *[this line is hand-underlined/struck through in part]*
$F_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = P(X_1 \le x_1, \ldots, X_n \le x_n)$.
If the joint distribution is $f_{X_1,\ldots,X_n}(x_1,\ldots,x_n)$, then
$P[a_1 \le X_1 \le b_1] = \int_{a_1}^{b_1}\int_{-\infty}^{\infty}\cdots\int_{-\infty}^{\infty} f_{X_1,\ldots,X_n}(x_1,\ldots,x_n)dx_1 \ldots dx_n$.

*[Handwritten work below and in the right margin, partly legible: a change-of-variables example with $y = \frac{1}{x^2}$-type monotone transformation, $x > 0$, "$y$ monotone decreasing, $0<y<\infty$"; the transformation-density formula $f(\phi) = f(g^{-1}(\phi))\left|\frac{d}{d\phi}g^{-1}(\phi)\right|$; a worked sketch $f(y) = y^{\alpha}\cdot\frac{1}{...}$, "$0<y<1$", "$x = \frac{1-y}{y}$", "$dx = -\frac{1}{y^2}dy$", "(one-to-one)". These are lecture scratch notes for the Jacobian rule.]*

### PDF page 10 (booklet page 5)

When $n$ is too big, we move to the computer to do the computation — MCMC, MCI. *[hand check-mark in margin]*

**1.7 Extension theorem**

$X_1, X_2$ are two random variables, and the joint distribution is $f(x_1, x_2)$.
Suppose I want information just about $x_1$, the coherent procedure is used to find the marginal distribution of $x_1$.
$f(x_1) = \int_{-\infty}^{\infty} f(x_1, x_2)dx_2$ — Lindley called this **"the extension rule"**.
$f(x_1, \hat{x}_2)$: $\hat{x}_2$ is my judgment.
Putting a guessing value does not follow from the rules of probability – incoherent.

**1.8 Conditional distribution**

$X, Y$ are two variables.
$$f_{X\mid Y}(x\mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)},\ f_Y(y) > 0; \qquad f_{Y\mid X}(y\mid x) = \frac{f_{X,Y}(x,y)}{f_X(x)},\ f_X(x) > 0.$$
Thus, we have $f_{X,Y}(x,y) = f_{X\mid Y}(x\mid y)f_Y(y) = f_{Y\mid X}(y\mid x)f_X(x)$.
$$f_{X\mid Y}(x\mid y) = \frac{f_{Y\mid X}(y\mid x)f_X(x)}{f_Y(y)} \;\text{— Bayes' Theorem for random variables.}$$
Since $f_Y(y) = \int f_{Y\mid X}(y\mid x)f_X(x)dx$ is a normalization constant,
so, $f_{X\mid Y}(x\mid y) = \dfrac{f_{Y\mid X}(y\mid x)f_X(x)}{\int f_{Y\mid X}(y\mid x)f_X(x)dx} \propto f_{Y\mid X}(y\mid x)f_X(x)$.
Since $\int f_{X\mid Y}(x\mid y)dx = 1 = K\int f_{Y\mid X}(y\mid x)f_X(x)dx$, so $K = \dfrac{1}{\int f_{Y\mid X}(y\mid x)f_X(x)dx}$.
We need the normalization constant to be finite, that is $\int f_{Y\mid X}(y\mid x)f_X(x)dx < \infty$.
That is, $f_{Y\mid X}(y\mid x)$ is **proper**, otherwise it is **improper**. *[margin notes restating: $f_{X\mid Y}(x\mid y) \propto f_{Y\mid X}(y\mid x)f_X(x)$ and $f_{X\mid Y}(x\mid y)\propto f(x,y)$]*

**Examples**

1. $f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$, $-\infty < x < \infty$. Since $\int f(x)dx = 1$, thus it is proper.
2. $f(x) = \frac{1}{1+x}$, $x > 0$. Since $\int \frac{1}{1+x}dx = \infty$, thus it is a improper measure.
3. $f(x) = \frac{1}{(1+x)^2}$, $x \ge 0$.

> ✔ Verified: $\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-x^2/2}dx=1$ (Gaussian integral); $\int_0^{\infty}\frac{dx}{1+x} = \lim_{t\to\infty}\ln(1+t)=\infty$ (improper); example 3 continues on the next page.

### PDF page 11 (booklet page 6)

Since $\int \frac{1}{(1+x)^2}dx = 1$, thus is proper.
(But be careful, in this case $E(X) = \int_0^{\infty} \frac{x}{(1+x)^2}dx = \infty$!) *[hand check-mark in margin]*

> ✔ Verified: $\int_0^\infty (1+x)^{-2}dx = [-(1+x)^{-1}]_0^\infty = 1$ (proper); $\int_0^\infty \frac{x}{(1+x)^2}dx$ diverges logarithmically, so $E(X)=\infty$ — the caution is correct.

**Example: Groceries**

$G$ = \$spent; $E$ = \$earned;
$G\mid E \sim N(E, \sigma^2)$ — likelihood function;
$E \sim N(\theta, \delta^2)$ — prior distribution of $E$. Here *(correction: "In which" is struck through, replaced by handwritten "we assume")* $\theta, \sigma^2, \delta^2$ are known (specified by a scientist). We want $f(E\mid G)$.
From Bayes' theorem, we have
$$f(E\mid G) \propto f(G\mid E)f(E) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2\sigma^2}(G-E)^2}\frac{1}{\sqrt{2\pi\delta^2}}e^{-\frac{1}{2\delta^2}(E-\theta)^2}$$
(since $\frac{1}{\sqrt{2\pi\sigma^2}}$ and $\frac{1}{\sqrt{2\pi\delta^2}}$ are constants)
$$\propto e^{-\frac{1}{2\sigma^2}(G-E)^2 - \frac{1}{2\delta^2}(E-\theta)^2} = e^{-\frac{1}{2\sigma^2}(E-G)^2 - \frac{1}{2\delta^2}(E-\theta)^2}$$
Since
$$\frac{1}{\sigma^2}(E-G)^2 + \frac{1}{\delta^2}(E-\theta)^2 = \frac{1}{(1-\lambda)\delta^2}\big[E - (\lambda G + (1-\lambda)\theta)\big]^2 + \frac{\lambda}{\delta^2}[G-\theta]^2$$
where $\lambda = \dfrac{\delta^2}{\delta^2 + \sigma^2}$ — [HW exercise].
Thus we have
$$f(E\mid G) \propto e^{-\frac{1}{2(1-\lambda)\delta^2}[E-(\lambda G+(1-\lambda)\theta)]^2}\, e^{-\frac{\lambda}{2\delta^2}(G-\theta)^2}$$
(Since $e^{-\frac{\lambda}{2\delta^2}(G-\theta)^2}$ is a constant) $\;\propto e^{-\frac{1}{2(1-\lambda)\delta^2}[E-(\lambda G+(1-\lambda)\theta)]^2}$.
Let $f(E\mid G) = Ke^{-\frac{1}{2(1-\lambda)\delta^2}[E-(\lambda G+(1-\lambda)\theta)]^2}$. Since $\int f(E\mid G)dE = 1$, so $K = \dfrac{1}{\sqrt{2\pi(1-\lambda)\delta^2}}$.
Thus, $E\mid G \sim N\big(\lambda G + (1-\lambda)\theta,\ (1-\lambda)\delta^2\big)$ — **posterior distribution of $E$**. *[hand-underlined; margin arrows label the two factors "prior" and "likelihood"; side scratch note: $\frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2} \sim N(\mu,\sigma^2)$]*

> ✔ Verified symbolically (SymPy): with $\lambda=\delta^2/(\delta^2+\sigma^2)$ the completing-the-square identity holds exactly, so the posterior is $N(\lambda G+(1-\lambda)\theta,(1-\lambda)\delta^2)$ as stated.

**Examples: Laboratory Test** *[margin notes: "COVID-19 PCR"; "$D$: disease"; arrows labeling $P(D)$ "prior" and $P(\text{positive}\mid D)$ "likelihood"]*

$P(D) = 0.005 \Rightarrow P(\bar{D}) = 0.995$
$P(\text{positive}\mid D) = 0.95$, $P(\text{positive}\mid \bar{D}) = 0.01$
$$P(D\mid \text{positive}) = \frac{0.95 \times 0.005}{0.95 \times 0.005 + 0.01 \times 0.995} = 0.323 \qquad \textit{[margin note: "Want this to be huge!"]}$$
$$P(D\mid \text{negtive [sic]}) = \frac{0.05 \times 0.005}{0.05 \times 0.005 + 0.99 \times 0.995} = 0.00025373$$

> ✔ Verified: $\frac{0.00475}{0.00475+0.00995} = \frac{0.00475}{0.01470} = 0.32313 \to 0.323$; $\frac{0.00025}{0.00025+0.98505} = 0.00025373$. Both correct.

**Examples: Missing Plane** *[margin arrows: "prior", "likelihood"]*

Plane is equally likely to be in one of three regions, $R_1, R_2, R_3$.
$P(R_i) = \frac{1}{3}$, $i = 1, 2, 3$
$P(\text{Plane is found in } R_i \mid \text{Plane is in } R_i) = 1 - \alpha_i$

### PDF page 12 (booklet page 7)

*[top-right margin note: "$E\mid R_2$: Plane in $R_2$, Search in $R_1$ must be unsuccessful" — i.e. $P(E\mid R_2)=1$]*

$\alpha_i$ are called **overlook probabilities**.
$E$: a search of region 1 is unsuccessful.
$$P(R_1\mid E) = \frac{P(E\mid R_1)P(R_1)}{P(E\mid R_1)P(R_1) + P(E\mid R_2)P(R_2) + P(E\mid R_3)P(R_3)} = \frac{\alpha_1\frac{1}{3}}{\alpha_1\frac{1}{3} + \frac{1}{3} + \frac{1}{3}} = \frac{\alpha_1}{\alpha_1 + 2} < \frac{1}{3}$$
$$P(R_2\mid E) = P(R_3\mid E) = \frac{1}{\alpha_1 + 2} > \frac{1}{3}$$

> ✔ Verified: the three posteriors sum to $\frac{\alpha_1+2}{\alpha_1+2}=1$; and $\frac{\alpha_1}{\alpha_1+2}<\frac13 \iff \alpha_1<1$, $\frac{1}{\alpha_1+2}>\frac13 \iff \alpha_1<1$ — true since an overlook probability satisfies $0<\alpha_1<1$ (equality would need $\alpha_1=1$).

**Examples: Exam**

$p \sim \mathrm{Beta}(\alpha, \beta)$, $\alpha, \beta$ are fixed and known. *(correction: the symbol "$R$" is struck through and replaced by handwritten "$p$")*
A random sample of $n$ students took the test and $y$ students failed.
$y\mid p \sim \mathrm{Binomial}(n, p)$. *(correction: "iid" is struck through — a single $y$, not a sample)* e.g. $y = 10$, $n = 100$.
*[right-margin handwritten restatement: $f(p) = \frac{p^{\alpha-1}(1-p)^{\beta-1}}{B(\alpha,\beta)}$, $0<p<1$]*

**Likelihood:** $f(y\mid p) = \binom{n}{y}p^y(1-p)^{n-y}$, $y = 0, 1, \ldots, n$
$$\pi(p) = \frac{p^{\alpha-1}(1-p)^{\beta-1}}{B(\alpha,\beta)},\ 0 \le p \le 1, \qquad B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$$

**Prior [sic — this line is the posterior kernel]:** $\pi(p\mid y) \propto p^y(1-p)^{n-y}p^{\alpha-1}(1-p)^{\beta-1} = p^{y+\alpha-1}(1-p)^{n+\beta-y-1}$
$$\pi(p\mid y) = \frac{p^{y+\alpha-1}(1-p)^{n+\beta-y-1}}{\int_0^1 \frac{p^{y+\alpha-1}(1-p)^{n+\beta-y-1}}{B(y+\alpha, n+\beta-y)}d\beta}, \quad 0 < p < 1 \qquad \text{[sic: the differential should be } dp\text{]}$$
$$p\mid y \sim \mathrm{Beta}(y+\alpha,\ n+\beta-y) \to \text{Posterior distribution}$$
$$E(p\mid y) = \frac{y+\alpha}{n+\alpha+\beta} = \frac{n\cdot\frac{y}{n} + (\alpha+\beta)\cdot\frac{\alpha}{\alpha+\beta}}{n+\alpha+\beta} = \lambda\frac{y}{n} + (1-\lambda)\frac{\alpha}{\alpha+\beta}, \qquad \lambda = \frac{n}{n+\alpha+\beta}$$
As $n \to +\infty$, $\lambda \to 1$,
$$\mathrm{Var}(p\mid y) = \frac{\frac{y+\alpha}{n+\alpha+\beta}\cdot\frac{n-y+\beta}{n+\alpha+\beta}}{n+\alpha+\beta+1} \le \frac{1}{4(n+\alpha+\beta+1)} \qquad \textit{[margin: a queried "?" comparison against the prior variance } \tfrac{\frac{\alpha}{\alpha+\beta}\frac{\beta}{\alpha+\beta}}{\alpha+\beta+1}\textit{]}$$

*[Bottom of page: handwritten re-derivation of the shrinkage identity — writing $\frac{y+\alpha}{n+\alpha+\beta} = \lambda\frac{y}{n}+(1-\lambda)\frac{\alpha}{\alpha+\beta}$, noting $\frac{n-y+\beta}{n+\alpha+\beta} = 1-\frac{y+\alpha}{n+\alpha+\beta}$, and $\lambda\to 1 \Rightarrow$ the posterior mean $\to y/n$; left column lists the Bayes'-theorem template $\pi(\theta),\ f(y\mid\theta),\ \pi(\theta\mid y) \propto f(y\mid\theta)\pi(\theta)$.]*

> ✔ Verified symbolically: the weighted-average identity for $E(p\mid y)$ holds exactly; $\mathrm{Var}(p\mid y)$ equals $m(1-m)/(n+\alpha+\beta+1)$ with $m = \frac{y+\alpha}{n+\alpha+\beta}$, and $m(1-m)\le\frac14$ gives the stated bound.

### PDF page 13 (booklet page 8)

*(Blank page — running header only.)*
