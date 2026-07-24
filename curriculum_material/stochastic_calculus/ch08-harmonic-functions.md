# Chapter 8 — Harmonic functions
*(PDF pages 249–260; book pages 243–254)*

### PDF page 249 (book page 243)

# Chapter 8 — Harmonic functions

## 8.1 Dirichlet problem

Recall that the Laplacian of a function $f$ on $\mathbb{R}^d$ is defined by

$$
\nabla^2 f(x) = \sum_{j=1}^{d} \partial_{jj} f(x).
$$

The Laplacian is closely related to mean values of functions. The *(spherical) mean value of $f$ on the sphere of radius $\epsilon$ about $x$* is defined by

$$
MV(x; \epsilon, f) = \frac{\int_{|y-x|=\epsilon} f(y) \, d\sigma(y)}{\int_{|y-x|=\epsilon} 1 \, d\sigma(y)},
$$

where $\sigma$ denotes $(d-1)$-dimensional surface measure. The mean value can also be described in terms of Brownian motion. Suppose $B_t$ is a $d$-dimensional Brownian motion starting at $x$ and let

$$
\tau_\epsilon = \inf\{t : |B_t - B_0| = \epsilon\}.
$$

Since Brownian motion is rotationally invariant, the distribution of $B_{\tau_\epsilon}$ is uniform over the sphere $\{y : |y - x| = \epsilon\}$. Hence we can write

$$
MV(x; \epsilon, f) = \mathbb{E}^x \left[ f(B_{\tau_\epsilon}) \right]. \tag{8.1}
$$

**Proposition 8.1.1.** *Suppose $f$ is a $C^2$ function in a neighborhood of $x \in \mathbb{R}^d$. Then*

$$
\nabla^2 f(x) = 2d \lim_{\epsilon \downarrow 0} \frac{MV(x; \epsilon, f) - f(x)}{\epsilon^2}.
$$

### PDF page 250 (book page 244)

*Proof.* Without loss of generality, assume $x = 0$ and $f(x) = 0$, and write $MV(\epsilon)$ for $MV(0; f, \epsilon)$. Let $b_j = \partial_j f(0), a_{jk} = \partial_{jk} f(0)$. Taylor's theorem implies that

$$ f(y) = \sum_{j=1}^{d} b_j\, y_j + \frac{1}{2} \sum_{j=1}^{d} a_{jk} y_j y_k + o(|y|^2), \quad y \to 0, $$

where we write $y = (y_1, \ldots, y_d)$. Therefore,

$$ MV(\epsilon) = \sum_{j=1}^{d} b_j\, MV(0; y_j, \epsilon) + \frac{1}{2} \sum_{j=1}^{d} a_{jk}\, MV(0; y_j y_k, \epsilon) + o(\epsilon^2). $$

Note that $MV(0; y_j, \epsilon) = 0$ since $y_j$ is an odd function. Similarly, $MV(0; y_j y_k, \epsilon) = 0$ if $j \neq k$. Linearity of the integral implies that

$$ \sum_{j=1}^{d} MV(0; y_j^2, \epsilon) = MV(0; \sum_{j=1}^{d} y_j^2, \epsilon) = MV(0; \epsilon^2, \epsilon) = \epsilon^2. $$

Symmetriy [sic] implies that $MV(0; y_j^2, \epsilon) = MV(0; y_k^2, \epsilon)$, and hence $MV(y_j^2, \epsilon) = \epsilon/d$. We therefore have

$$ MV(\epsilon) = \frac{1}{2} \sum_{j=1}^{d} a_{jj}\, (\epsilon^2/d) + o(\epsilon^2) = \frac{\epsilon^2}{2d}\, \nabla^2 f(0) + o(\epsilon^2). $$

$\square$

**Definition** Suppose $f$ is a function defined on an open set $D \subset \mathbb{R}^d$.

- $f$ is *harmonic in $D$* if $f$ is $C^2$ and $\nabla^2 f(x) = 0$ for all $x \in D$. $f$ is harmonic at $x$ if it is harmonic in a neighborhood of $x$.

- A function $f$ satisfies the *(spherical) mean value property* on $D$ if for every $x \in D$ and every $\epsilon > 0$ with $\{y : |x - y| \leq \epsilon\} \subset D$ ,

$$ f(x) = MV(f; x, \epsilon). $$

**Proposition 8.1.2.**

### PDF page 251 (book page 245)

- *Suppose $f$ is a harmonic function defined on an open set $D \subset \mathbb{R}^d$. Let $B_t$ be a standard $d$-dimensional Brownian motion starting at $x \in D$ and let*

$$ \tau = \inf\{t : B_t \notin D\}. $$

*Then $M_t := f(B_{t \wedge \tau})$ is a local martingale for $t < \tau$ satisfying*

$$ dM_t = \nabla f(B_t) \cdot dB_t, \quad t < \tau. $$

- *Suppose also that $f$ is defined on $\partial D$ so that $f : \overline{D} \to \mathbb{R}$ is a bounded, continuous function. Then $M_t$ is a bounded continuous martingale. If $\mathbb{P}\{\tau < \infty\} = 1$, then*

$$ f(x) = \mathbb{E}^x \left[ f(B_\tau) \right]. \tag{8.2} $$

*Proof.* The first statement follows from Itô's formula. In fact, we already did this calculation in Theorem 3.7.2. Since bounded local martingales are martingales, the second statement follows from the optional sampling theorem. $\square$

The expression (8.2) is a generalization of the mean value property (8.1). It states that we can take mean values over sets other than spheres as long as integrate with respect to the correct the measure. This measure is often called *harmonic measure (in $D$ starting at $x$)* and is defined by

$$ \mathrm{hm}_D(V; x) = \mathbb{P}^x\{B_\tau \in V\}, \quad V \subset \partial D. $$

Then (8.2) can be written

$$ f(x) = \int_{\partial D} f(y)\, \mathrm{hm}_D(dy; x). $$

The next proposition shows that we could use the mean value propery [sic] to define harmonic functions. In fact, this is the more natural definition.

**Proposition 8.1.3.** *Suppose $f$ is a continuous function on an open set $D \subset \mathbb{R}^d$. Then $f$ is harmonic in $D$ if and only if $f$ satisfies the mean value property on $D$.*

*Proof.* If $f$ is harmonic, then $f$ restricted to a closed ball of radius $\epsilon$ contained in $D$ is bounded. Therefore, the mean value property is a particular case of (8.2).

### PDF page 252 (book page 246)

If $f$ is $C^2$ and satisfies the mean value property, then $\nabla^2 f(x) = 0$ by Proposition 8.1.1. Hence we need only show that $f$ is $C^2$. We will, in fact, show that $f$ is $C^\infty$.

It is a standard exercise in advanced calculus to show that for every $\delta > 0$ we can find a nonnegative radially symmetric $C^\infty$ function $\phi = \phi_\delta$ such that $\phi(y) = 0$ for $|y| \geq \delta$ and

$$ \int \phi(y)\, dy = 1. $$

Here $dy = dy_1 \cdots dy_d$. If $x \in D$ with $\{y : |x - y| \leq \epsilon\} \subset D$, and $\phi = \phi_{\epsilon/2}$, then the mean value property implies that

$$ f(x) = \int f(x + y)\, \phi(y)\, dy = \int f(z)\, \phi(z - x)\, dz. \tag{8.3} $$

Since $f$ is locally bounded and $\phi$ is bounded and $C^\infty$, we can differentiate with respect to $x$ by bringing the derivatives inside the integral. $\square$

The proof showed that we did not need to assume that $f$ is continuous. It suffices for $f$ to be measurable and locally bounded so that derivatives can be taken on the right-hand side of (8.3).

We will solve the classic Dirichlet problem for harmonic functions. Suppose $D$ is a bounded open set and $F : \partial D \to \mathbb{R}$ is a continuous function. The goal is to find a continuous function $f : \overline{D} \to \mathbb{R}$ that is harmonic in $D$ with $f(x) = F(x)$ for $x \in \partial D$. Suppose that such a function $f$ existed. Let $\tau = \tau_D = \inf\{t \geq 0 : B_t \in \partial D\}$. Since $\overline{D}$ is compact, $f$ must be bounded, and hence

$$ M_t = f(B_{t \wedge \tau}) $$

is a continuous, bounded martingale. Arguing as in (8.2) we see that

$$ f(x) = \mathbb{E}^x \left[ f(B_\tau) \right] = \mathbb{E}^x \left[ F(B_\tau) \right]. \tag{8.4} $$

The right-hand side gives the only candidate for the solution. The strong Markov property can be used to see that this candidate satisfies the mean value property and the last proposition gives that $f$ is harmonic in $D$.

It is a little more subtle to check if $f$ is continuous on $\overline{D}$. This requires further assumptions on $D$ which can be described most easily in terms of Brownian motion. Suppose $z \in \partial D$ and $x \in D$ with $x$ near $z$. Can we say that $f(x)$ is near $F(z)$? Since $F$ is continuous, this will be true if $B_\tau$ is near

### PDF page 253 (book page 247)

$z$. To make this precise, one defines a point $z \in \partial D$ to be *regular* if for every $\epsilon > 0$ there exists $\delta > 0$ such that if $x \in D$ with $|x - z| < \delta$, then

$$ \mathbb{P}^x \left\{ |B_\tau - z| \geq \epsilon \right\} \leq \epsilon. $$

**Theorem 8.1.4.** *Suppose $D$ is a bounded open set such that each $z \in \partial D$ is regular. Suppose $F$ is a continuous function on $\partial D$. Then there exists a unique continuous function $f : \overline{D} \to \mathbb{R}$ that is harmonic on $D$ and agrees with $F$ on $\partial D$ given by* (8.4).

**Example 8.1.1.** Let $D$ be the annular region

$$ D = \{x \in \mathbb{R}^d : r < |x| < R\}, $$

and let $F(x) = 1$ if $|x| = R$, $F(x) = 0$ if $|x| = r$. Then for $x \in D$,

$$ f(x; r, R) = \mathbb{E}^x \left[ F(B_\tau) \right] = \mathbb{P}^x \{ |B_\tau| = R \}. $$

We claim that

$$ f(x; r, R) = \frac{x - r}{R - r}, \quad d = 1, $$

$$ f(x; r, R) = \frac{\log |x| - \log r}{\log R - \log r}, \quad d = 2, $$

$$ f(x; r, R) = \frac{r^{d-2} - |x|^{d-2}}{r^{d-2} - R^{d-2}}, \quad d \geq 3. $$

One can check this by noting that $\nabla^2 f(x) = 0$ and $f$ has the correct boundary condition. The theorem implies that there is only one such function. Note that

$$ \lim_{R \to \infty} f(x; r, R) = \left\{ \begin{array}{ll} 0, & d \leq 2 \\ 1 - (r/|x|)^{2-d}, & d \geq 3 \end{array} \right. , $$

$$ \lim_{r \downarrow 0} f(x; r, R) = \left\{ \begin{array}{ll} x/R & d = 1 \\ 1, & d \geq 2 \end{array} \right. . \tag{8.5} $$

We have already seen the $d = 1$ case as the gambler's ruin estimate for Brownian motion.

**Example 8.1.2.** Let $d \geq 2$. It follows from (8.5) that if $x \neq 0$, then the probability that a Brownian motion starting at $x$ ever hits zero is zero. Let $D = \{x \in \mathbb{R}^d : 0 < |x| < 1\}$. Then $0$ is *not* a regular point of $\partial D$, since if we start near the origin the Brownian motion will not exit $D$ near $0$. Let

### PDF page 254 (book page 248)

$F(0) = 0$, $F(y) = 1$ if $|y| = 1$. Then, the only candidate for the solution of the Dirichlet problem is

$$ f(x) = \mathbb{E}^x \left[ F(B_\tau) \right] = 1, \quad x \in D. $$

If $f(0) = 0$, this function is not continuous at the origin.

If $D = U_r = \{x : |x| < r\}$ is the ball of radius $r$ about the origin, then the harmonic measure $\mathrm{hm}_{U_r}(\cdot; x)$ is known explicitly. It is absolutely continuous with respect to $(d-1)$-dimensional surface measure $s$ on $\partial U_r$. Its density is called the *Poisson kernel*,

$$ H_r(x, y) = \frac{r^2 - |x|^2}{r \, \omega_{d-1} \, |x - y|^d}, $$

where

$$ \omega_{d-1} = \int_{|y|=1} ds(y) $$

denotes the surface area of the unit ball. If $F : \partial U_r \to \mathbb{R}$ is continuous, then the unique solution to the Dirichlet problem is

$$ f(x) = \mathbb{E}^x \left[ F(B_{\tau_{U_r}}) \right] = \int_{|y|=r} F(y) \, H_r(x, y) \, ds(y). \tag{8.6} $$

To verify this, one checks by direct computation the following facts:

- If $y \in \partial U_r$, the function $h(x) = H(x, y)$ is harmonic on $U_r$;

- If $x \in U_r$,

$$ \int_{|y|=r} H_r(x, y) \, ds(y) = 1; $$

- For every $\epsilon > 0$, there exists $\delta > 0$ such that if $x \in U_r, y \in \partial U_r$ and $|x - y| < \delta$, then

$$ \int_{|z|=r, |z-y| \geq \epsilon} H_r(x, z) \, ds(z) \leq \epsilon. $$

¿From these one concludes that $f$ as defined by the right-hand side of (8.6) is harmonic in $U_r$ and continuous on $\overline{U}_r$.

### PDF page 255 (book page 249)

The reader may note that we did not need the probabilistic interpretation of the solution in order to verify that (8.6) solves the Dirichlet problem. Indeed, the solution using the Poisson kernel was discovered before the relationship with Brownian motion. An important corollary of this explicit solution is the following theorem; we leave the verification as Exercise 8.1. The key part of the theorem is the fact that the same constant $C$ works for all harmonic functions.

**Theorem 8.1.5.**

1. *For every positive integer $n$, there exists $C = C(d, n) < \infty$ such that if $f$ is a harmonic function on an open set $D \subset \mathbb{R}^d$, $x \in D$, $\{y : |x - y| < r\} \subset D$, and $j_1, \ldots, j_n \in \{1, \ldots, d\}$ then*

$$ \left| \partial_{x_{j_1}} \cdots \partial_{x_{j_n}} f(x) \right| \leq C \, r^{-n} \sup_{|y-x|<r} |f(y)|. $$

2. *(Harnack inequality) For every $0 < u < 1$, there exists $C = C(d, u) < \infty$ such that if $f$ is a positive harmonic function on an open set $D \subset \mathbb{R}^d$, $x \in D$, $\{y : |x - y| < r\} \subset D$, then if $|x - z| \leq ur$,*

$$ C^{-1} f(x) \leq f(z) \leq C \, f(x). $$

## 8.2 $h$-processes

Suppose $h$ is a positive harmonic function on an open set $D \subset \mathbb{R}^d$, and let $B_t$ be a standard Brownian motion starting at $x \in D$. Let $\tau = \tau_D$ be the first time $t$ with $B_t \notin D$. Then $M_t = h(B_t)$ is a positive local martingale for $t < \tau$ satisfying

$$ dM_t = \frac{\nabla h(B_t)}{h(B_t)} \, M_t \, dB_t, \quad t < \tau. $$

Let $\tau_n$ be the minimum of $\tau$ and the first time $t$ with $h(B_t) \geq n$. Then $M_{t \wedge \tau_n}$ is a continuous bounded martingale.

We can use the Girsanov theorem to consider the measure obtained by weighting by the local martingale $M_t$. To be more precise, if $V$ is an event that depends only on $B_t, 0 \leq t \leq \tau_n$, then

$$ \mathbb{P}^*(V) = h(x)^{-1} \, \mathbb{E}^* \left[ M_{\tau_n} \, \mathbf{1}_V \right]. $$

### PDF page 256 (book page 250)

One can use the Girsanov theorem (more precisely, a simple generalization of the theorem to $d$-dimensional Brownian motion), to see that

$$ dB_t = \frac{\nabla h(B_t)}{h(B_t)} \, dt + dW_t, $$

where $W_t$ is a standard Brownian motion with respect to $\mathbb{P}^*$. The process $B_t$ in the new measure $\mathbb{P}^*$ is often called the *(Doob) h-process* associated to the positive harmonic function $h$. It is defined for $t < \tau$.

As an example, suppose that $D$ is the unit ball, $y = (1, 0, \ldots, 0) \in \partial D$ and

$$ h(x) = \omega_{d-1} H_1(x, y) = \frac{1 - |x|^2}{|x - y|^d}, $$

is the Poisson kernel. Then the $h$-process can be viewed as Brownian motion "conditioned so that $B_\tau = y$", where $\tau = \tau_D$. This is not precise because the conditioning is with respect to a event of probability zero. We claim that the $\mathbb{P}^*$-probability that $B_\tau = y$ equals one. To see this, assume that $B_0 = 0$ and let

$$ T_n = \inf\{t : h(B_t) = n^3\}, \quad T'_n = \inf\{t > T_n : h(B_t) = n\}. $$

We claim that $\mathbb{P}^*\{T_n < \tau\} = 1$. Indeed, if we let $\tau_r = \inf\{t : |B_t| = r\}$, then we can check directly that

$$ \lim_{r \uparrow 1} \mathbb{P}^*\{h(B_{\tau_r}) \geq n^3\} = \lim_{r \uparrow 1} \int_{|x|=1, h(rx) \geq n^3} h(rx) \, d\sigma(x) = 1, $$

and hence

$$ \lim_{r \uparrow 1} \mathbb{P}^*\{T_n < \tau_r\} = 1. $$

Also, since $h(B_{T'_n}) = n^{-2} \, h(B_{T_n})$,

$$ \mathbb{P}^*\{T'_n < \tau\} \leq n^{-2}, $$

$$ \sum_{n=1}^{\infty} \mathbb{P}^*\{T'_n < \tau\} < \infty. $$

Therefore, by the Borel-Canelli lemma, we see that with $\mathbb{P}^*$-probability one for all $n$ sufficiently large $h(B_t) \geq n$ for $t \geq T_n$.

### PDF page 257 (book page 251)

**8.3 Time changes**

To prepare for the next section we will consider time changes of Brownian motion. If $B_t$ is a standard Brownian motion and $Y_t = B_{at}$, then $Y_t$ is a Brownian motion with variance parameter $a$. We can write

$$ Y_t = \int_0^t \sqrt{a} \, dW_s, $$

where $W_t = a^{-1/2} \, B_{at}$ is a standard Brownian motion. We generalize this by considering $Y_t = B_{a(t)}$ where $a$ is a strictly increasing continuous function. We allow $a(t)$ to be random, but it must be adapted to the Brownian motion. In other words, for each $t$, the random time $a(t)$ must be a stopping time for the Brownian motion $B_t$. We will make the further assumption that $a$ is a $C^1$ function, that is, we can write

$$ a(t) = \int_0^t \dot{a}(s) \, ds, $$

where $s \mapsto \dot{a}(s)$ is a continuous nonnegative function. The assumption that $a(t)$ is strictly increasing implies that there are no open intervals on which $\dot{a}(s)$ is identically zero. If $Y(t) = B_{a(t)}$, then $Y_t$ is a continuous local martingale and we can write

$$ Y_t = \int_0^t \sqrt{\dot{a}(s)} \, dW_s, $$

where $W_t$ is the standard Brownian motion

$$ W_t = \int_0^t [\dot{a}(s)]^{-1/2} \, dB_{a(s)}. \tag{8.7} $$

One can verify this is a standard Brownian motion by checking that is a martingale with $\langle W \rangle_t = t$. More generally, if $X_t$ satisfies the SDE

$$ dX_t = R_t \, dt + A_t \, dB_t, $$

and $Y_t = X_{a(t)}$, then $Y_t$ satisfies the SDE

$$ dY_t = \dot{a}(t) \, R_{a(t)} \, dt + \sqrt{\dot{a}(t)} \, A_{a(t)} \, dW_t, $$

where $W_t$ is the standard Brownian motion (8.7).

### PDF page 258 (book page 252)

**Example 8.3.1.** Suppose that $X_t$ satisfies the Bessel equation

$$ dX_t = \frac{r}{X_t} \, dt + dB_t, \quad X_0 = 1, $$

where $r \in \mathbb{R}$. This is defined for $t < T = \inf\{s : X_s = 0\}$. For $t < T$, let $L_t = \log X_t$. Then Itô's formula shows that

$$ \begin{aligned} dL_t &= \frac{1}{X_t} \, dX_t - \frac{1}{2 \, X_t^2} \, d\langle X \rangle_t \\ &= \left( r - \frac{1}{2} \right) e^{-2L_t} \, dt + e^{-L_t} \, dB_t. \end{aligned} $$

Consider the time change with $\dot{a}(t) = e^{2L_t}$, and let $Y_t = L_{a(t)}$. Then $Y_t$ satisfies

$$ dY_t = \left( r - \frac{1}{2} \right) dt + dW_t, $$

where $W_t$ is a standard Brownian motion. In other words, $Y_t$ is a Brownian motion with variance parameter 1 and drift $m = r - \frac{1}{2}$. From this we can see that $Y_t \to \infty$ if $r > 1/2$, $Y_t \to -\infty$ if $r < 1/2$, and

$$ -\infty = \liminf_{t \to \infty} Y_t < \limsup_{t \to \infty} Y_t = \infty, $$

if $r = 1/2$. One can use this to give another proof of Proposition 4.2.1. Note that if $r < 1/2$, then in the new time, it take an infinite amount of time for $L = \log X$ to reach $-\infty$. However, in the original time, this happens at time $T < \infty$. In other words,

$$ a(T) = \int_0^T \frac{ds}{\dot{a}(s)} = \infty. $$

**8.4 Complex Brownian motion**

If $B_t^1, B_t^2$ are independent standard Brownian motions then

$$ B_t = B_t^1 + i \, B_t^2 $$

is called a *(standard) complex Brownian motion*. Note that this is the same as a two-dimensional Brownian motion except that the point in the plane is viewed as a complex number.

### PDF page 259 (book page 253)

Suppose $f : \mathbb{C} \to \mathbb{C}$ is a nonconstant holomorphic (complex differentiable) function. We will consider $X_t = f(B_t)$. Near any point $z$ with $f'(z) \neq 0$, the function looks like $f(w) = f(z) + f'(z)\,(w - z)$. Multiplication by $f'(z)$ is the same as a dilation by $|f'(z)|$ and a rotation by $\arg f'(z)$. A rotation of a standard two-dimensional Brownian motion gives a standard two-dimensional Brownian motion and a dilation gives a Brownian motion with a different variance. This leads us to believe that $X_t$ is a time-change of standard Brownian motion.

Let us make this more precise. Let

$$ a(t) = \int_0^t |f'(B_s)|^2 \, ds. $$

We consider the time-change in which it takes time $a(t)$ to traverse $f\,(B[0, t])$. Equivalently, in time $t$ one has traversed $f\,(B[0, a^{-1}(t)])$.

**Theorem 8.4.1.** *Let $Y_t = X_{a^{-1}(t)}$. Then $Y_t$ is a standard complex Brownian motion.*

*Proof.* Write $f = u + iv$, $X_t = U_t + iV_t$, $Y_t = \hat{U}_t + i\hat{V}_t$. The Cauchy-Riemann equations imply that $\partial_x u = \partial_y v$, $\partial_y u = -\partial_x v$ and

$$ \nabla^2 u = \partial_x \partial_x u + \partial_y \partial_y u = \partial_x \partial_y v + \partial_y(-\partial_x v) = 0. $$

Similarly $\nabla^2 v = 0$. Since $U_t = u(B_t^1, B_t^2)$ , $V_t = v(B_t^1, B_t^2)$, then Itô's formula (see Theorem 3.7.2) gives

$$ dU_t = \nabla u(B_t) \cdot dB_t = \partial_x u(B_t) \, dB_t^1 + \partial_y u(B_t) \, dB_t^2. $$

$$
\begin{aligned}
dV_t = \nabla v(B_t) \cdot dB_t &= \partial_x v(B_t) \, dB_t^1 + \partial_y v(B_t) \, dB_t^2 \\
&= -\partial_y u(B_t) \, dB_t^1 + \partial_x u(B_t) \, dB_t^2.
\end{aligned}
$$

Note that

$$
\begin{aligned}
d\langle U \rangle_t &= \left([\partial_x u(B_t)]^2 + [\partial_y u(B_t)]^2\right) dt \\
&= \left([\partial_x u(B_t)]^2 + [-\partial_x v(B_t)]^2\right) dt = |f'(B_t)|^2 \, dt, \\
d\langle V \rangle_t &= |f'(B_t)|^2 \, dt, \\
d\langle U, V \rangle_t &= 0.
\end{aligned}
$$

Therefore, $\hat{U}_t, \hat{V}_t$ are martingales with quadratic variation $t$ and hence are standard Brownian motions. Since $\langle U, V \rangle_t = 0$, we also have $\langle \hat{U}, \hat{V} \rangle_t = 0$, and hence $\hat{U}_t, \hat{V}_t$ are independent. $\square$

### PDF page 260 (book page 254)

The last theorem assumes that the function $f$ is entire, that is, it is defined and holomorphic on all of $\mathbb{C}$. Suppose $D$ is *domain*, that is, an open, connected subset of $\mathbb{C}$, and suppose that $f$ is a nonconstant holomorphic function on $D$. Let $B_t$ be a complex Brownian motion, and let

$$ \tau_D = \inf\{t \geq 0 : B_t \notin D\}. $$

Then the process $X_t$ as above is defined for $t < \tau_D$, and the process $Y_t$ is defined for $t < a(\tau_D-)$ with the processes taking values in $f(D)$.

**Theorem 8.4.2.** *If $f$ is a holomorphic function on a domain $D$, and $X_t, Y_t$ are defined as above, then $Y_t, 0 \leq t < a(\tau_D-)$ is a standard complex Brownian motion.*

One very important case is when $f$ maps $D$ one-to-one onto $f(D)$. Such functions are often called *conformal transformations*. In this case $f^{-1}$ is a conformal transformation from $f(D)$ to $D$, and

$$ a(\tau_D-) = \inf\{t : Y_t \notin f(D)\}. $$

In particular, this shows that harmonic measure is a conformal invariant,

$$ \mathrm{hm}_D(V; z) = \mathrm{hm}_{f(D)}(f(V); f(z)). $$

## **8.5 Exercises**

**Exercise 8.1.** Use (8.6) to prove Theorem 8.1.5.

**Exercise 8.2.** Suppose $D \subset \mathbb{C}$ is a domain and $\phi$ is a harmonic function on $D$ (here we are also viewing $D$ as a subset of $\mathbb{R}^2$). Let $f : D \to f(D)$ be a conformal transformation and let

$$ \psi(w) = \phi(f^{-1}(w)). $$

Show that $\psi$ is a harmonic function on $f(D)$ in two different ways:

- Do a direct computation to show that $\nabla^2 \psi = 0$.

- Use the conformal invariance of harmonic measure and (8.2).
