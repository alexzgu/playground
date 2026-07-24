# Chapter 4 — Randomized Blocks, Latin Squares, and Related Designs
*(PDF pages 155–198; book pages 139–182)*

### PDF page 155 (book page 139)

# Chapter 4 — Randomized Blocks, Latin Squares, and Related Designs

**CHAPTER OUTLINE**

- 4.1 THE RANDOMIZED COMPLETE BLOCK DESIGN
  - 4.1.1 Statistical Analysis of the RCBD
  - 4.1.2 Model Adequacy Checking
  - 4.1.3 Some Other Aspects of the Randomized Complete Block Design
  - 4.1.4 Estimating Model Parameters and the General Regression Significance Test
- 4.2 THE LATIN SQUARE DESIGN
- 4.3 THE GRAECO-LATIN SQUARE DESIGN
- 4.4 BALANCED INCOMPLETE BLOCK DESIGNS
  - 4.4.1 Statistical Analysis of the BIBD
  - 4.4.2 Least Squares Estimation of the Parameters
  - 4.4.3 Recovery of Interblock Information in the BIBD
- SUPPLEMENTAL MATERIAL FOR CHAPTER 4
  - S4.1 Relative Efficiency of the RCBD
  - S4.2 Partially Balanced Incomplete Block Designs
  - S4.3 Youden Squares
  - S4.4 Lattice Designs

The supplemental material is on the textbook website www.wiley.com/college/montgomery.

**4.1 The Randomized Complete Block Design**

In any experiment, variability arising from a nuisance factor can affect the results. Generally, we define a **nuisance factor** as a design factor that probably has an effect on the response, but we are not interested in that effect. Sometimes a nuisance factor is **unknown and uncontrolled**; that is, we don't know that the factor exists, and it may even be changing levels while we are conducting the experiment. **Randomization** is the design technique used to guard against such a "lurking" nuisance factor. In other cases, the nuisance factor is **known but uncontrollable**. If we can at least observe the value that the nuisance factor takes on at each run of the experiment, we can compensate for it in the statistical analysis by using the **analysis of covariance**, a technique we will discuss in Chapter 14. When the nuisance source of variability is **known and controllable**, a design technique called **blocking** can be used to systematically eliminate its effect on the statistical comparisons among treatments. Blocking is an extremely important design technique used extensively in industrial experimentation and is the subject of this chapter.

To illustrate the general idea, reconsider the hardness testing experiment first described in Section 2.5.1. Suppose now that we wish to determine whether or not four different tips produce different readings on a hardness testing machine. An experiment such as this might be part of a

### PDF page 156 (book page 140)

**TABLE 4.1**
**Randomized Complete Block Design for the Hardness Testing Experiment**

*Test Coupon (Block)*

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| Tip 3 | Tip 3 | Tip 2 | Tip 1 |
| Tip 1 | Tip 4 | Tip 1 | Tip 4 |
| Tip 4 | Tip 2 | Tip 3 | Tip 2 |
| Tip 2 | Tip 1 | Tip 4 | Tip 3 |

gauge capability study. The machine operates by pressing the tip into a metal test coupon, and from the depth of the resulting depression, the hardness of the coupon can be determined. The experimenter has decided to obtain four observations on Rockwell C-scale hardness for each tip. There is only one factor—tip type—and a completely randomized single-factor design would consist of randomly assigning each one of the $4 \times 4 = 16$ runs to an **experimental unit**, that is, a metal coupon, and observing the hardness reading that results. Thus, 16 different metal test coupons would be required in this experiment, one for each run in the design.

There is a potentially serious problem with a completely randomized experiment in this design situation. If the metal coupons differ slightly in their hardness, as might happen if they are taken from ingots that are produced in different heats, the experimental units (the coupons) will contribute to the variability observed in the hardness data. As a result, the experimental error will reflect *both* random error *and* variability between coupons.

We would like to make the experimental error as small as possible; that is, we would like to remove the variability between coupons from the experimental error. A design that would accomplish this requires the experimenter to test each tip once on each of four coupons. This design, shown in Table 4.1, is called a **randomized complete block design** (**RCBD**). The word "complete" indicates that each block (coupon) contains all the treatments (tips). By using this design, the blocks, or coupons, form a more homogeneous experimental unit on which to compare the tips. Effectively, this design strategy improves the accuracy of the comparisons among tips by eliminating the variability among the coupons. Within a block, the order in which the four tips are tested is randomly determined. Notice the similarity of this design problem to the paired *t*-test of Section 2.5.1. The randomized complete block design is a generalization of that concept.

The RCBD is one of the most widely used experimental designs. Situations for which the RCBD is appropriate are numerous. Units of test equipment or machinery are often different in their operating characteristics and would be a typical blocking factor. Batches of raw material, people, and time are also common nuisance sources of variability in an experiment that can be systematically controlled through blocking.[^1]

Blocking may also be useful in situations that do not necessarily involve nuisance factors. For example, suppose that a chemical engineer is interested in the effect of catalyst feed rate on the viscosity of a polymer. She knows that there are several factors, such as raw material source, temperature, operator, and raw material purity that are very difficult to control in the full-scale process. Therefore she decides to test the catalyst feed rate factor in blocks, where each block consists of some combination of these uncontrollable factors. In effect, she is using the blocks to test the **robustness** of her process variable (feed rate) to conditions she cannot easily control. For more discussion of this, see Coleman and Montgomery (1993).

[^1]: A special case of blocking occurs where the blocks are experimental units such as people, and each block receives the treatments one time or the treatment effects are measured at different times. These are called **repeated measures** designs. They are discussed in chapter 15.

### PDF page 157 (book page 141)

**FIGURE 4.1** The randomized complete block design *[Figure: a row of vertical rectangles labeled Block 1, Block 2, …, Block b; each rectangle lists the observations of that block in a column — $y_{11}, y_{21}, y_{31}, \ldots, y_{a1}$ in Block 1, $y_{12}, y_{22}, y_{32}, \ldots, y_{a2}$ in Block 2, and $y_{1b}, y_{2b}, y_{3b}, \ldots, y_{ab}$ in Block b — with an ellipsis between Block 2 and Block b.]*

**4.1.1 Statistical Analysis of the RCBD**

Suppose we have, in general, $a$ treatments that are to be compared and $b$ blocks. The randomized complete block design is shown in Figure 4.1. There is one observation per treatment in each block, and the order in which the treatments are run within each block is determined randomly. Because the only randomization of treatments is within the blocks, we often say that the blocks represent a **restriction on randomization**.

The **statistical model** for the RCBD can be written in several ways. The traditional model is an **effects model**:

$$ y_{ij} = \mu + \tau_i + \beta_j + \epsilon_{ij} \qquad \begin{cases} i = 1, 2, \ldots, a \\ j = 1, 2, \ldots, b \end{cases} \tag{4.1} $$

where $\mu$ is an overall mean, $\tau_i$ is the effect of the $i$th treatment, $\beta_j$ is the effect of the $j$th block, and $\epsilon_{ij}$ is the usual NID $(0, \sigma^2)$ random error term. We will initially consider treatments and blocks to be fixed factors. The case of random blocks, which is very important, is considerd in Section 4.1.3. Just as in the single-factor experimental design model in Chapter 3, the effects model for the RCBD is an overspecified model. Consequently, we usually think of the treatment and block effects as deviations from the overall mean so that

$$ \sum_{i=1}^{a} \tau_i = 0 \quad \text{and} \quad \sum_{j=1}^{b} \beta_j = 0 $$

It is also possible to use a **means model** for the RCBD, say

$$ y_{ij} = \mu_{ij} + \epsilon_{ij} \qquad \begin{cases} i = 1, 2, \ldots, a \\ j = 1, 2, \ldots, b \end{cases} $$

where $\mu_{ij} = \mu + \tau_i + \beta_j$. However, we will use the effects model in Equation 4.1 throughout this chapter.

In an experiment involving the RCBD, we are interested in testing the equality of the treatment means. Thus, the hypotheses of interest are

$$
\begin{aligned}
H_0 &: \mu_1 = \mu_2 = \cdots = \mu_a \\
H_1 &: \text{at least one } \mu_i \neq \mu_j
\end{aligned}
$$

Because the $i$th treatment mean $\mu_i = (1/b)\sum_{j=1}^{b} (\mu + \tau_i + \beta_j) = \mu + \tau_i$, an equivalent way to write the above hypotheses is in terms of the treatment effects, say

$$
\begin{aligned}
H_0 &: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \\
H_1 &: \tau_i \neq 0 \text{ at least one } i
\end{aligned}
$$

The analysis of variance can be easily extended to the RCBD. Let $y_{i.}$ be the total of all observations taken under treatment $i$, $y_{.j}$ be the total of all observations in block $j$, $y_{..}$ be the

### PDF page 158 (book page 142)

grand total of all observations, and $N=ab$ be the total number of observations. Expressed mathematically,

$$
y_{i.}=\sum_{j=1}^{b}y_{ij}\qquad i=1,2,\ldots,a \tag{4.2}
$$

$$
y_{.j}=\sum_{i=1}^{a}y_{ij}\qquad j=1,2,\ldots,b \tag{4.3}
$$

and

$$
y_{..}=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}=\sum_{i=1}^{a}y_{i.}=\sum_{j=1}^{b}y_{.j} \tag{4.4}
$$

Similarly, $\bar{y}_{i.}$ is the average of the observations taken under treatment $i$, $\bar{y}_{.j}$ is the average of the observations in block $j$, and $\bar{y}_{..}$ is the grand average of all observations. That is,

$$
\bar{y}_{i.}=y_{i.}/b\qquad \bar{y}_{.j}=y_{.j}/a\qquad \bar{y}_{..}=y_{..}/N \tag{4.5}
$$

We may express the total corrected sum of squares as

$$
\begin{aligned}
\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{..})^2
&=\sum_{i=1}^{a}\sum_{j=1}^{b}\big[(\bar{y}_{i.}-\bar{y}_{..})\\
&\quad+(\bar{y}_{.j}-\bar{y}_{..})+(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})\big]^2
\end{aligned}
\tag{4.6}
$$

By expanding the right-hand side of Equation 4.6, we obtain

$$
\begin{aligned}
\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{..})^2
={}&b\sum_{i=1}^{a}(\bar{y}_{i.}-\bar{y}_{..})^2
+a\sum_{j=1}^{b}(\bar{y}_{.j}-\bar{y}_{..})^2\\
&+\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})^2
+2\sum_{i=1}^{a}\sum_{j=1}^{b}(\bar{y}_{i.}-\bar{y}_{..})(\bar{y}_{.j}-\bar{y}_{..})\\
&+2\sum_{i=1}^{a}\sum_{j=1}^{b}(\bar{y}_{.j}-\bar{y}_{..})(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})\\
&+2\sum_{i=1}^{a}\sum_{j=1}^{b}(\bar{y}_{i.}-\bar{y}_{..})(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})
\end{aligned}
$$

Simple but tedious algebra proves that the three cross products are zero. Therefore,

$$
\begin{aligned}
\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{..})^2
={}&b\sum_{i=1}^{a}(\bar{y}_{i.}-\bar{y}_{..})^2
+a\sum_{j=1}^{b}(\bar{y}_{.j}-\bar{y}_{..})^2\\
&+\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{.j}-\bar{y}_{i.}+\bar{y}_{..})^2
\end{aligned}
\tag{4.7}
$$

represents a partition of the total sum of squares. This is the fundamental ANOVA equation for the RCBD. Expressing the sums of squares in Equation 4.7 symbolically, we have

$$
SS_T=SS_{\text{Treatments}}+SS_{\text{Blocks}}+SS_E \tag{4.8}
$$

Because there are $N$ observations, $SS_T$ has $N-1$ degrees of freedom. There are $a$ treatments and $b$ blocks, so $SS_{\text{Treatments}}$ and $SS_{\text{Blocks}}$ have $a-1$ and $b-1$ degrees of freedom, respectively. The error sum of squares is just a sum of squares between cells minus the sum of squares for treatments and blocks. There are $ab$ cells with $ab-1$ degrees of freedom between them, so $SS_E$ has $ab-1-(a-1)-(b-1)=(a-1)(b-1)$ degrees of freedom. Furthermore, the degrees of freedom on the right-hand side of Equation 4.8 add to the total on the left; therefore, making the usual normality assumptions on the errors, one may use Theorem 3-1 to show

### PDF page 159 (book page 143)

that $SS_{\text{Treatments}}/\sigma^2$, $SS_{\text{Blocks}}/\sigma^2$, and $SS_E/\sigma^2$ are independently distributed chi-square random variables. Each sum of squares divided by its degrees of freedom is a mean square. The expected value of the mean squares, if treatments and blocks are fixed, can be shown to be

$$
\begin{aligned}
E(MS_{\text{Treatments}})&=\sigma^2+\frac{b\sum_{i=1}^{a}\tau_i^2}{a-1}\\
E(MS_{\text{Blocks}})&=\sigma^2+\frac{a\sum_{j=1}^{b}\beta_j^2}{b-1}\\
E(MS_E)&=\sigma^2
\end{aligned}
$$

Therefore, to test the equality of treatment means, we would use the test statistic

$$
F_0=\frac{MS_{\text{Treatments}}}{MS_E}
$$

which is distributed as $F_{a-1,(a-1)(b-1)}$ if the null hypothesis is true. The critical region is the upper tail of the $F$ distribution, and we would reject $H_0$ if $F_0>F_{\alpha,a-1,(a-1)(b-1)}$. A $P$-value approach can also be used.

We may also be interested in comparing block means because, if these means do not differ greatly, blocking may not be necessary in future experiments. From the expected mean squares, it seems that the hypothesis $H_0:\beta_j=0$ may be tested by comparing the statistic $F_0=MS_{\text{Blocks}}/MS_E$ to $F_{\alpha,b-1,(a-1)(b-1)}$. However, recall that randomization has been applied only to treatments within blocks; that is, the blocks represent a **restriction on randomization**. What effect does this have on the statistic $F_0=MS_{\text{Blocks}}/MS_E$? Some differences in treatment of this question exist. For example, Box, Hunter, and Hunter (2005) point out that the usual analysis of variance $F$ test can be justified on the basis of randomization only,[^2] without direct use of the normality assumption. They further observe that the test to compare block means cannot appeal to such a justification because of the randomization restriction; but if the errors are NID$(0,\sigma^2)$, the statistic $F_0=MS_{\text{Blocks}}/MS_E$ can be used to compare block means. On the other hand, Anderson and McLean (1974) argue that the randomization restriction prevents this statistic from being a meaningful test for comparing block means and that this $F$ ratio really is a test for the equality of the block means plus the randomization restriction [which they call a restriction error; see Anderson and McLean (1974) for further details].

In practice, then, what do we do? Because the normality assumption is often questionable, to view $F_0=MS_{\text{Blocks}}/MS_E$ as an exact $F$ test on the equality of block means is not a good general practice. For that reason, we exclude this $F$ test from the analysis of variance table. However, as an approximate procedure to investigate the effect of the blocking variable, examining the ratio of $MS_{\text{Blocks}}$ to $MS_E$ is certainly reasonable. If this ratio is large, it implies that the blocking factor has a large effect and that the noise reduction obtained by blocking was probably helpful in improving the precision of the comparison of treatment means.

The procedure is usually summarized in an ANOVA table, such as the one shown in Table 4.2. The computing would usually be done with a statistical software package. However, computing formulas for the sums of squares may be obtained for the elements in Equation 4.7 by working directly with the identity

$$
y_{ij}-\bar{y}_{..}=(\bar{y}_{i.}-\bar{y}_{..})+(\bar{y}_{.j}-\bar{y}_{..})+(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})
$$

[^2]: Actually, the normal-theory $F$ distribution is an approximation to the randomization distribution generated by calculating $F_0$ from every possible assignment of the responses to the treatments.

### PDF page 160 (book page 144)

**TABLE 4.2** Analysis of Variance for a Randomized Complete Block Design

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments | $SS_{\text{Treatments}}$ | $a-1$ | $\dfrac{SS_{\text{Treatments}}}{a-1}$ | $\dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Blocks | $SS_{\text{Blocks}}$ | $b-1$ | $\dfrac{SS_{\text{Blocks}}}{b-1}$ | |
| Error | $SS_E$ | $(a-1)(b-1)$ | $\dfrac{SS_E}{(a-1)(b-1)}$ | |
| Total | $SS_T$ | $N-1$ | | |

These quantities can be computed in the columns of a spreadsheet (Excel). Then each column can be squared and summed to produce the sum of squares. Alternatively, computing formulas can be expressed in terms of treatment and block totals. These formulas are

$$
SS_T=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2-\frac{y_{..}^2}{N} \tag{4.9}
$$

$$
SS_{\text{Treatments}}=\frac{1}{b}\sum_{i=1}^{a}y_{i.}^2-\frac{y_{..}^2}{N} \tag{4.10}
$$

$$
SS_{\text{Blocks}}=\frac{1}{a}\sum_{j=1}^{b}y_{.j}^2-\frac{y_{..}^2}{N} \tag{4.11}
$$

and the error sum of squares is obtained by subtraction as

$$
SS_E=SS_T-SS_{\text{Treatments}}-SS_{\text{Blocks}} \tag{4.12}
$$

**EXAMPLE 4.1**

A medical device manufacturer produces vascular grafts (artificial veins). These grafts are produced by extruding billets of polytetrafluoroethylene (PTFE) resin combined with a lubricant into tubes. Frequently, some of the tubes in a production run contain small, hard protrusions on the external surface. These defects are known as “flicks.” The defect is cause for rejection of the unit.

The product developer responsible for the vascular grafts suspects that the extrusion pressure affects the occurrence of flicks and therefore intends to conduct an experiment to investigate this hypothesis. However, the resin is manufactured by an external supplier and is delivered to the medical device manufacturer in batches. The engineer also suspects that there may be significant batch-to-batch variation, because while the material should be consistent with respect to parameters such as molecular weight, mean particle size, retention, and peak height ratio, it probably isn’t due to manufacturing variation at the resin supplier and natural variation in the material. Therefore, the product developer decides to investigate the effect of four different levels of extrusion pressure on flicks using a randomized complete block design considering batches of resin as blocks. The RCBD is shown in Table 4.3. Note that there are four levels of extrusion pressure (treatments) and six batches of resin (blocks). Remember that the order in which the extrusion pressures are tested within each block is random. The response variable is yield, or the percentage of tubes in the production run that did not contain any flicks.

### PDF page 161 (book page 145)

**TABLE 4.3** Randomized Complete Block Design for the Vascular Graft Experiment

| Extrusion Pressure (PSI) | Batch of Resin (Block) 1 | 2 | 3 | 4 | 5 | 6 | Treatment Total |
|---|---|---|---|---|---|---|---|
| 8500 | 90.3 | 89.2 | 98.2 | 93.9 | 87.4 | 97.9 | 556.9 |
| 8700 | 92.5 | 89.5 | 90.6 | 94.7 | 87.0 | 95.8 | 550.1 |
| 8900 | 85.5 | 90.8 | 89.6 | 86.2 | 88.0 | 93.4 | 533.5 |
| 9100 | 82.5 | 89.5 | 85.6 | 87.4 | 78.9 | 90.7 | 514.6 |
| Block Totals | 350.8 | 359.0 | 364.0 | 362.2 | 341.3 | 377.8 | $y_{..}=2155.1$ |

To perform the analysis of variance, we need the following sums of squares:

$$
\begin{aligned}
SS_T&=\sum_{i=1}^{4}\sum_{j=1}^{6}y_{ij}^2-\frac{y_{..}^2}{N}\\
&=193{,}999.31-\frac{(2155.1)^2}{24}=480.31
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Treatments}}
&=\frac{1}{b}\sum_{i=1}^{4}y_{i.}^2-\frac{y_{..}^2}{N}\\
&=\frac{1}{6}\big[(556.9)^2+(550.1)^2+(533.5)^2+(514.6)^2\big]
-\frac{(2155.1)^2}{24}=178.17
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Blocks}}
&=\frac{1}{a}\sum_{j=1}^{6}y_{.j}^2-\frac{y_{..}^2}{N}\\
&=\frac{1}{4}\big[(350.8)^2+(359.0)^2+\cdots+(377.8)^2\big]
-\frac{(2155.1)^2}{24}=192.25
\end{aligned}
$$

$$
\begin{aligned}
SS_E&=SS_T-SS_{\text{Treatments}}-SS_{\text{Blocks}}\\
&=480.31-178.17-192.25=109.89
\end{aligned}
$$

The ANOVA is shown in Table 4.4. Using $\alpha=0.05$, the critical value of $F$ is $F_{0.05,3,15}=3.29$. Because $8.11>3.29$, we conclude that extrusion pressure affects the mean yield. The $P$-value for the test is also quite small. Also, the resin batches (blocks) seem to differ significantly, because the mean square for blocks is large relative to error.

**TABLE 4.4** Analysis of Variance for the Vascular Graft Experiment

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Treatments (extrusion pressure) | 178.17 | 3 | 59.39 | 8.11 | 0.0019 |
| Blocks (batches) | 192.25 | 5 | 38.45 | | |
| Error | 109.89 | 15 | 7.33 | | |
| Total | 480.31 | 23 | | | |

It is interesting to observe the results we would have obtained from this experiment had we not been aware of randomized block designs. Suppose that this experiment had been run as a completely randomized design, and (by chance) the same design resulted as in Table 4.3. The incorrect analysis of these data as a completely randomized single-factor design is shown in Table 4.5.

Because the $P$-value is less than 0.05, we would still reject the null hypothesis and conclude that extrusion pressure significantly affects the mean yield. However, note that the mean

### PDF page 162 (book page 146)

**TABLE 4.5** Incorrect Analysis of the Vascular Graft Experiment as a Completely Randomized Design

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Extrusion pressure | 178.17 | 3 | 59.39 | 3.95 | 0.0235 |
| Error | 302.14 | 20 | 15.11 | | |
| Total | 480.31 | 23 | | | |

square for error has more than doubled, increasing from 7.33 in the RCBD to 15.11. All of the variability due to blocks is now in the error term. This makes it easy to see why we sometimes call the RCBD a noise-reducing design technique; it effectively increases the signal-to-noise ratio in the data, or it improves the precision with which treatment means are compared. This example also illustrates an important point. If an experimenter fails to block when he or she should have, the effect may be to inflate the experimental error, and it would be possible to inflate the error so much that important differences among the treatment means could not be identified.

***Sample Computer Output.*** Condensed computer output for the vascular graft experiment in Example 4.1, obtained from Design-Expert and JMP is shown in Figure 4.2. The Design-Expert output is in Figure 4.2a and the JMP output is in Figure 4.2b. Both outputs are very similar, and match the manual computation given earlier. Note that JMP computes an $F$-statistic for blocks (the batches). The sample means for each treatment are shown in the output. At 8500 psi, the mean yield is $\bar{y}_{1.}=92.82$, at 8700 psi the mean yield is $\bar{y}_{2.}=91.68$, at 8900 psi the mean yield is $\bar{y}_{3.}=88.92$, and at 9100 psi the mean yield is $\bar{y}_{4.}=85.77$. Remember that these sample mean yields estimate the treatment means $\mu_1,\mu_2,\mu_3$, and $\mu_4$. The model residuals are shown at the bottom of the Design-Expert output. The residuals are calculated from

$$
e_{ij}=y_{ij}-\hat{y}_{ij}
$$

and, as we will later show, the fitted values are $\hat{y}_{ij}=\bar{y}_{i.}+\bar{y}_{.j}-\bar{y}_{..}$, so

$$
e_{ij}=y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..} \tag{4.13}
$$

In the next section, we will show how the residuals are used in **model adequacy checking**.

***Multiple Comparisons.*** If the treatments in an RCBD are fixed, and the analysis indicates a significant difference in treatment means, the experimenter is usually interested in multiple comparisons to discover *which* treatment means differ. Any of the multiple comparison procedures discussed in Section 3.5 may be used for this purpose. In the formulas of Section 3.5, simply replace the number of replicates in the single-factor completely randomized design ($n$) by the number of blocks ($b$). Also, remember to use the number of error degrees of freedom for the randomized block $[(a-1)(b-1)]$ instead of those for the completely randomized design $[a(n-1)]$.

The Design-Expert output in Figure 4.2 illustrates the Fisher LSD procedure. Notice that we would conclude that $\mu_1=\mu_2$, because the $P$-value is very large. Furthermore, $\mu_1$ differs from all other means. Now the $P$-value for $H_0:\mu_2=\mu_3$ is 0.097, so there is some evidence to conclude that $\mu_2\ne\mu_3$, and $\mu_2\ne\mu_4$ because the $P$-value is 0.0018. Overall, we would conclude that lower extrusion pressures (8500 psi and 8700 psi) lead to fewer defects.

### PDF page 163 (book page 147)

**Response: Yield**

**ANOVA for Selected Factorial Model**

**Analysis of Variance Table [Partial Sum of Squares]**

| Source | Sum of Squares | DF | Mean Square | $F$ Value | Prob $>F$ |
|---|---|---|---|---|---|
| Block | 192.25 | 5 | 38.45 | | |
| Model | 178.17 | 3 | 59.39 | 8.11 | 0.0019 |
| A | 178.17 | 3 | 59.39 | 8.11 | 0.0019 |
| Residual | 109.89 | 15 | 7.33 | | |
| Cor Total | 480.31 | 23 | | | |

| | | | |
|---|---|---|---|
| Std. Dev. | 2.71 | R-Squared | 0.6185 |
| Mean | 89.80 | Adj R-Squared | 0.5422 |
| C.V. | 3.01 | Pred R-Squared | 0.0234 |
| PRESS | 281.31 | Adeq Precision | 9.759 |

**Treatment Means (Adjusted, If Necessary)**

| | Estimated Mean | Standard Error |
|---|---|---|
| 1–8500 | 92.82 | 1.10 |
| 2–8700 | 91.68 | 1.10 |
| 3–8900 | 88.92 | 1.10 |
| 4–9100 | 85.77 | 1.10 |

| Treatment | Mean Difference | DF | Standard Error | $t$ for $H_0$ Coeff=0 | Prob $>|t|$ |
|---|---|---|---|---|---|
| 1 vs. 2 | 1.13 | 1 | 1.56 | 0.73 | 0.4795 |
| 1 vs. 3 | 3.90 | 1 | 1.56 | 2.50 | 0.0247 |
| 1 vs. 4 | 7.05 | 1 | 1.56 | 4.51 | 0.0004 |
| 2 vs. 3 | 2.77 | 1 | 1.56 | 1.77 | 0.0970 |
| 2 vs. 4 | 5.92 | 1 | 1.56 | 3.79 | 0.0018 |
| 3 vs. 4 | 3.15 | 1 | 1.56 | 2.02 | 0.0621 |

**Diagnostics Case Statistics**

| Standard Order | Actual Value | Predicted Value | Residual | Leverage | Student Residual | Cook's Distance | Outlier $t$ | Run Order |
|---|---|---|---|---|---|---|---|---|
| 1 | 90.30 | 90.72 | −0.42 | 0.375 | −0.197 | 0.003 | −0.190 | 1 |
| 2 | 89.20 | 92.77 | −3.57 | 0.375 | −1.669 | 0.186 | −1.787 | 6 |
| 3 | 98.20 | 94.02 | 4.18 | 0.375 | 1.953 | 0.254 | 2.185 | 9 |
| 4 | 93.90 | 93.57 | 0.33 | 0.375 | 0.154 | 0.002 | 0.149 | 13 |
| 5 | 87.40 | 88.35 | −0.95 | 0.375 | −0.442 | 0.013 | −0.430 | 19 |
| 6 | 97.90 | 97.47 | 0.43 | 0.375 | 0.201 | 0.003 | 0.194 | 23 |
| 7 | 92.50 | 89.59 | 2.91 | 0.375 | 1.361 | 0.124 | 1.405 | 4 |
| 8 | 89.50 | 91.64 | −2.14 | 0.375 | −0.999 | 0.067 | −0.999 | 5 |
| 9 | 90.60 | 92.89 | −2.29 | 0.375 | −1.069 | 0.076 | −1.075 | 10 |
| 10 | 94.70 | 92.44 | 2.26 | 0.375 | 1.057 | 0.075 | 1.062 | 16 |
| 11 | 87.00 | 87.21 | −0.21 | 0.375 | −0.099 | 0.001 | −0.096 | 20 |
| 12 | 95.80 | 96.34 | −0.54 | 0.375 | −0.251 | 0.004 | −0.243 | 21 |
| 13 | 85.50 | 86.82 | −1.32 | 0.375 | −0.617 | 0.025 | −0.604 | 3 |
| 14 | 90.80 | 88.87 | 1.93 | 0.375 | 0.902 | 0.054 | 0.896 | 8 |
| 15 | 89.60 | 90.12 | −0.52 | 0.375 | −0.243 | 0.004 | −0.236 | 12 |
| 16 | 86.20 | 89.67 | −3.47 | 0.375 | −1.622 | 0.175 | −1.726 | 15 |
| 17 | 88.00 | 84.45 | 3.55 | 0.375 | 1.661 | 0.184 | 1.776 | 17 |
| 18 | 93.40 | 93.57 | −0.17 | 0.375 | −0.080 | 0.000 | −0.077 | 22 |
| 19 | 82.50 | 83.67 | −1.17 | 0.375 | −0.547 | 0.020 | −0.534 | 2 |
| 20 | 89.50 | 85.72 | 3.78 | 0.375 | 1.766 | 0.208 | 1.917 | 7 |
| 21 | 85.60 | 86.97 | −1.37 | 0.375 | −0.641 | 0.027 | −0.628 | 11 |
| 22 | 87.40 | 86.52 | 0.88 | 0.375 | 0.411 | 0.011 | 0.399 | 14 |
| 23 | 78.90 | 81.30 | −2.40 | 0.375 | −1.120 | 0.084 | −1.130 | 18 |
| 24 | 90.70 | 90.42 | 0.28 | 0.375 | 0.130 | 0.001 | 0.126 | 24 |

Note: Predicted values include block corrections.

(a)

**FIGURE 4.2** Computer output for Example 4.1. (a) Design-Expert; (b) JMP

*[Figure: the Design-Expert ANOVA, treatment-means comparisons, and diagnostics output for the vascular graft yield data.]*

### PDF page 164 (book page 148)

**Oneway Analysis of Yield By Pressure**

Block  
Batch

**Oneway Anova**

**Summary of Fit**

| | |
|---|---|
| Rsquare | 0.771218 |
| Adj Rsquare | 0.649201 |
| Root Mean Square Error | 2.706612 |
| Mean of Response | 89.79583 |
| Observations (or Sum Wgts) | 24 |

**Analysis of Variance**

| Source | DF | Sum of Squares | Mean Square | $F$ Ratio | Prob $>F$ |
|---|---|---|---|---|---|
| Pressure | 3 | 178.17125 | 59.3904 | 8.1071 | 0.0019 |
| Batch | 5 | 192.25208 | 38.4504 | 5.2487 | 0.0055 |
| Error | 15 | 109.88625 | 7.3257 | | |
| C.Total | 23 | 480.30958 | | | |

**Means for Oneway Anova**

| Level | Number | Mean | Std. Error | Lower 95% | Upper 95% |
|---|---|---|---|---|---|
| 8500 | 6 | 92.8167 | 1.1050 | 90.461 | 95.172 |
| 8700 | 6 | 91.6833 | 1.1050 | 89.328 | 94.039 |
| 8900 | 6 | 88.9167 | 1.1050 | 86.561 | 91.272 |
| 9100 | 6 | 85.7667 | 1.1050 | 83.411 | 88.122 |

Std. Error uses a pooled estimate of error variance

**Block Means**

| Batch | Mean | Number |
|---|---|---|
| 1 | 87.7000 | 4 |
| 2 | 89.7500 | 4 |
| 3 | 91.0000 | 4 |
| 4 | 90.5500 | 4 |
| 5 | 85.3250 | 4 |
| 6 | 94.4500 | 4 |

(b)

**FIGURE 4.2** *(Continued)*

We can also use the graphical procedure of Section 3.5.1 to compare mean yield at the four extrusion pressures. Figure 4.3 plots the four means from Example 4.1 relative to a scaled $t$ distribution with a scale factor $\sqrt{MS_E/b}=\sqrt{7.33/6}=1.10$. This plot indicates that the two lowest pressures result in the same mean yield, but that the mean yields for 8700 psi and

**FIGURE 4.3** Mean yields for the four extrusion pressures relative to a scaled $t$ distribution with a scale factor $\sqrt{MS_E/b}=\sqrt{7.33/6}=1.10$

*[Figure: a scaled t-density centered at 90 above a yield axis from 80 to 95. Points labeled 4, 3, 2, and 1 mark the mean yields at approximately 85.77, 88.92, 91.68, and 92.82, respectively.]*

### PDF page 165 (book page 149)

8900 psi ($\mu_2$ and $\mu_3$) are also similar. The highest pressure (9100 psi) results in a mean yield that is much lower than all other means. This figure is a useful aid in interpreting the results of the experiment and the Fisher LSD calculations in the Design-Expert output in Figure 4.2.

**4.1.2 Model Adequacy Checking**

We have previously discussed the importance of checking the adequacy of the assumed model. Generally, we should be alert for potential problems with the normality assumption, unequal error variance by treatment or block, and block–treatment interaction. As in the completely randomized design, residual analysis is the major tool used in this diagnostic checking. The residuals for the randomized block design in Example 4.1 are listed at the bottom of the Design-Expert output in Figure 4.2.

A normal probability plot of these residuals is shown in Figure 4.4. There is no severe indication of nonnormality, nor is there any evidence pointing to possible outliers. Figure 4.5 plots the residuals versus the fitted values $\hat{y}_{ij}$. There should be no relationship between the size of the residuals and the fitted values $\hat{y}_{ij}$. This plot reveals nothing of unusual interest. Figure 4.6 shows plots of the residuals by treatment (extrusion pressure) and by batch of resin or block. These plots are potentially very informative. If there is more scatter in the residuals for a particular treatment, that could indicate that this treatment produces more erratic response readings than the others. More scatter in the residuals for a particular block could indicate that the block is not homogeneous. However, in our example, Figure 4.6 gives no indication of inequality of variance by treatment but there is an indication that there is less variability in the yield for batch 6. However, since all of the other residual plots are satisfactory, we will ignore this.

**FIGURE 4.4** Normal probability plot of residuals for Example 4.1

*[Figure: normal probability plot with 24 residual points lying close to a rising reference line; residuals run from about −3.57 to 4.18 and the probability scale from 1 to 99 percent.]*

**FIGURE 4.5** Plot of residuals versus $\hat{y}_{ij}$ for Example 4.1

*[Figure: scatterplot of residuals against predicted yield from 81.30 to 97.47, with points scattered around the horizontal zero line and no obvious pattern.]*

### PDF page 166 (book page 150)

**FIGURE 4.6** Plot of residuals by extrusion pressure (treatment) and by batches of resin (block) for Example 4.1

*[Figure: two residual scatterplots sharing a vertical scale of approximately −3.57 to 4.18. Panel (a) groups the residuals by four extrusion-pressure treatments; panel (b) groups them by six raw-material batches (blocks).]*

Sometimes the plot of residuals versus $\hat{y}_{ij}$ has a curvilinear shape; for example, there may be a tendency for negative residuals to occur with low $\hat{y}_{ij}$ values, positive residuals with intermediate $\hat{y}_{ij}$ values, and negative residuals with high $\hat{y}_{ij}$ values. This type of pattern is suggestive of **interaction** between blocks and treatments. If this pattern occurs, a transformation should be used in an effort to eliminate or minimize the interaction. In Section 5.3.7, we describe a statistical test that can be used to detect the presence of interaction in a randomized block design.

**4.1.3 Some Other Aspects of the Randomized Complete Block Design**

***Additivity of the Randomized Block Model.*** The linear statistical model that we have used for the randomized block design

$$
y_{ij}=\mu+\tau_i+\beta_j+\epsilon_{ij}
$$

is completely **additive**. This says that, for example, if the first treatment causes the expected response to increase by five units ($\tau_1=5$) and if the first block increases the expected response by 2 units ($\beta_1=2$), the expected increase in response of both treatment 1 and block 1 together is $E(y_{11})=\mu+\tau_1+\beta_1=\mu+5+2=\mu+7$. In general, treatment 1 *always* increases the expected response by 5 units over the sum of the overall mean and the block effect.

Although this simple additive model is often useful, in some situations it is inadequate. Suppose, for example, that we are comparing four formulations of a chemical product using six batches of raw material; the raw material batches are considered blocks. If an impurity in batch 2 affects formulation 2 adversely, resulting in an unusually low yield, but does not affect the other formulations, an **interaction** between formulations (or treatments) and batches (or

### PDF page 167 (book page 151)

blocks) has occurred. Similarly, interactions between treatments and blocks can occur when the response is measured on the wrong scale. Thus, a relationship that is multiplicative in the original units, say

$$
E(y_{ij})=\mu\tau_i\beta_j
$$

is linear or additive in a log scale since, for example,

$$
\ln E(y_{ij})=\ln\mu+\ln\tau_i+\ln\beta_j
$$

or

$$
E(y_{ij}^*)=\mu^*+\tau_i^*+\beta_j^*
$$

Although this type of interaction can be eliminated by a transformation, not all interactions are so easily treated. For example, transformations do not eliminate the formulation–batch interaction discussed previously. Residual analysis and other diagnostic checking procedures can be helpful in detecting nonadditivity.

If interaction is present, it can seriously affect and possibly invalidate the analysis of variance. In general, the presence of interaction inflates the error mean square and may adversely affect the comparison of treatment means. In situations where both factors, as well as their possible interaction, are of interest, **factorial designs** must be used. These designs are discussed extensively in Chapters 5 through 9.

***Random Treatments and Blocks.*** Our presentation of the randomized complete block design thus far has focused on the case when both the treatments and blocks were considered as fixed factors. There are many situations where either treatments or blocks (or both) are random factors. It is very common to find that the blocks are random. This is usually what the experimenter would like to do, because we would like for the conclusions from the experiment to be valid across the population of blocks that the ones selected for the experiments were sampled from. First, we consider the case where the treatments are fixed and the blocks are random. Equation 4.1 is still the appropriate statistical model, but now the block effects are random, that is, we assume that the $\beta_j$, $j=1,2,\ldots,b$ are NID$(0,\sigma_\beta^2)$ random variables. This is a special case of a mixed model (because it contains both fixed and random factors). In Chapters 13 and 14 we will discuss mixed models in more detail and provide several examples of situations where they occur. Our discussion here is limited to the RCBD.

Assuming that the RCBD model Equation 4.1 is appropriate, if the blocks are random and the treatments are fixed we can show that:

$$
\begin{aligned}
E(y_{ij})&=\mu+\tau_i,\qquad i=1,2,\ldots,a\\
V(y_{ij})&=\sigma_\beta^2+\sigma^2\\
\operatorname{Cov}(y_{ij},y_{i'j'})&=0,\qquad j\ne j'\\
\operatorname{Cov}(y_{ij},y_{i'j})&=\sigma_\beta^2,\qquad i\ne i'
\end{aligned}
\tag{4.14}
$$

Thus, the variance of the observations is constant, the covariance between any two observations in different blocks is zero, but the covariance between two observations from the same block is $\sigma_\beta^2$. The expected mean squares from the usual ANOVA partitioning of the total sum of squares are

$$
\begin{aligned}
E(MS_{\text{Treatments}})&=\sigma^2+\frac{b\sum_{i=1}^{a}\tau_i^2}{a-1}\\
E(MS_{\text{Blocks}})&=\sigma^2+a\sigma_\beta^2\\
E(MS_E)&=\sigma^2
\end{aligned}
\tag{4.15}
$$

### PDF page 168 (book page 152)

The appropriate statistic for testing the null hypothesis of no treatment effects (all $\tau_i=0$) is

$$
F_0=\frac{MS_{\text{Treatment}}}{MS_E}
$$

which is exactly the same test statistic we used in the case where the blocks were fixed. Based on the expected mean squares, we can obtain an ANOVA-type estimator of the variance component for blocks as

$$
\hat{\sigma}_\beta^2=\frac{MS_{\text{Blocks}}-MS_E}{a} \tag{4.16}
$$

For example, for the vascular graft experiment in Example 4.1 the estimate of $\sigma_\beta^2$ is

$$
\hat{\sigma}_\beta^2=\frac{MS_{\text{Blocks}}-MS_E}{a}
=\frac{38.45-7.33}{4}=7.78
$$

This is a method-of-moments estimate and there is no simple way to find a confidence interval on the block variance component $\sigma_\beta^2$. The REML method would be preferred here. Table 4.6 is the JMP output for Example 4.1 assuming that blocks are random. The REML estimate of $\sigma_\beta^2$ is exactly the same as the ANOVA estimate, but REML automatically produces the standard error of the estimate (6.116215) and the approximate 95 percent confidence interval. JMP gives the test for the fixed effect (pressure), and the results are in agreement with those originally reported in Example 4.1. REML also produces the point estimate and CI for the error variance $\sigma^2$. The ease with which confidence intervals can be constructed is a major reason why REML has been so widely adopted.

Now consider a situation where there is an interaction between treatments and blocks. This could be accounted for by adding an interaction term to the original statistical model Equation 4.1. Let $(\tau\beta)_{ij}$ be the interaction effect of treatment $i$ in block $j$. Then the model is

$$
y_{ij}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\epsilon_{ij}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b
\end{cases}
\tag{4.17}
$$

The interaction effect is assumed to be random because it involves the random block effects. If $\sigma_{\tau\beta}^2$ is the variance component for the block treatment interaction, then we can show that the expected mean squares are

$$
\begin{aligned}
E(MS_{\text{Treatments}})&=\sigma^2+\sigma_{\tau\beta}^2+\frac{b\sum_{i=1}^{a}\tau_i^2}{a-1}\\
E(MS_{\text{Blocks}})&=\sigma^2+a\sigma_\beta^2\\
E(MS_E)&=\sigma^2+\sigma_{\tau\beta}^2
\end{aligned}
\tag{4.18}
$$

From the expected mean squares, we see that the usual $F$-statistic $F=MS_{\text{Treatments}}/MS_E$ would be used to test for no treatment effects. So another advantage of the random block model is that the assumption of no interaction in the RCBD is not important. However, if blocks are fixed and there is interaction, then the interaction effect is not in the expected mean square for treatments but it is in the error expected mean square, so there would not be a statistical test for the treatment effects.

### PDF page 169 (book page 153)

**TABLE 4.6** JMP Output for Example 4.1 with Blocks Assumed Random

**Response Y**

**Summary of Fit**

| | |
|---|---|
| RSquare | 0.756688 |
| RSquare Adj | 0.720192 |
| Root Mean Square Error | 2.706612 |
| Mean of Response | 89.79583 |
| Observations (or Sum Wgts) | 24 |

**REML Variance Component Estimates**

| Random Effect | Var Ratio | Var Component | Std Error | 95% Lower | 95% Upper | Pct of Total |
|---|---|---|---|---|---|---|
| Block | 1.0621666 | 7.7811667 | 6.116215 | −4.206394 | 19.768728 | 51.507 |
| Residual | | 7.32575 | 2.6749857 | 3.9975509 | 17.547721 | 48.493 |
| Total | | 15.106917 | | | | 100.000 |

**Covariance Matrix of Variance Component Estimates**

| Random Effect | Block | Residual |
|---|---|---|
| Block | 37.408085 | −1.788887 |
| Residual | −1.788887 | 7.1555484 |

**Fixed Effect Tests**

| Source | Nparm | DF | DFDen | $F$ Ratio | Prob $>F$ |
|---|---|---|---|---|---|
| Pressure | 3 | 3 | 15 | 8.1071 | 0.0019* |

***Choice of Sample Size.*** Choosing the **sample size**, or the **number of blocks** to run, is an important decision when using an RCBD. Increasing the number of blocks increases the number of replicates and the number of error degrees of freedom, making design more sensitive. Any of the techniques discussed in Section 3.7 for selecting the number of replicates to run in a completely randomized single-factor experiment may be applied directly to the RCBD. For the case of a fixed factor, the operating characteristic curves in Appendix Chart V may be used with

$$
\Phi^2=\frac{b\sum_{i=1}^{a}\tau_i^2}{a\sigma^2} \tag{4.19}
$$

where there are $a-1$ numerator degrees of freedom and $(a-1)(b-1)$ denominator degrees of freedom.

### PDF page 170 (book page 154)

**EXAMPLE 4.2**

Consider the RCBD for the vascular grafts described in Example 4.1. Suppose that we wish to determine the appropriate number of blocks to run if we are interested in detecting a true maximum difference in yield of 6 with a reasonably high probability and an estimate of the standard deviation of the errors is $\sigma=3$. From Equation 3.45, the minimum value of $\Phi^2$ is (writing $b$, the number of blocks, for $n$)

$$
\Phi^2=\frac{bD^2}{2a\sigma^2}
$$

where $D$ is the maximum difference we wish to detect. Thus,

$$
\Phi^2=\frac{b(6)^2}{2(4)(3)^2}=0.5b
$$

If we use $b=5$ blocks, $\Phi=\sqrt{0.5b}=\sqrt{0.5(5)}=1.58$, and there are $(a-1)(b-1)=3(4)=12$ error degrees of freedom. Appendix Chart V with $\nu_1=a-1=3$ and $\alpha=0.05$ indicates that the $\beta$ risk for this design is approximately 0.55 (power $=1-\beta=0.45$). If we use $b=6$ blocks, $\Phi=\sqrt{0.5b}=\sqrt{0.5(6)}=1.73$, with $(a-1)(b-1)=3(5)=15$ error degrees of freedom, and the corresponding $\beta$ risk is approximately 0.4 (power $=1-\beta=0.6$). Because the batches of resin are expensive and the cost of experimentation is high, the experimenter decides to use six blocks, even though the power is only about 0.6 (actually many experiments work very well with power values of only 0.5 or higher).

***Estimating Missing Values.*** When using the RCBD, sometimes an observation in one of the blocks is missing. This may happen because of carelessness or error or for reasons beyond our control, such as unavoidable damage to an experimental unit. A missing observation introduces a new problem into the analysis because treatments are no longer **orthogonal to blocks**; that is, every treatment does not occur in every block. There are two general approaches to the missing value problem. The first is an **approximate analysis** in which the missing observation is estimated and the usual analysis of variance is performed just as if the estimated observation were real data, with the error degrees of freedom reduced by 1. This approximate analysis is the subject of this section. The second is an **exact analysis**, which is discussed in Section 4.1.4.

Suppose the observation $y_{ij}$ for treatment $i$ in block $j$ is missing. Denote the missing observation by $x$. As an illustration, suppose that in the vascular graft experiment of Example 4.1 there was a problem with the extrusion machine when the 8700 psi run was conducted in the fourth batch of material, and the observation $y_{24}$ could not be obtained. The data might appear as in Table 4.7.

In general, we will let $y'_{..}$ represent the grand total with one missing observation, $y'_{i.}$ represent the total for the treatment with one missing observation, and $y'_{.j}$ be the total for the block with one missing observation. Suppose we wish to estimate the missing observation $x$

**TABLE 4.7** Randomized Complete Block Design for the Vascular Graft Experiment with One Missing Value

| Extrusion Pressures (PSI) | Batch of Resin (Block) 1 | 2 | 3 | 4 | 5 | 6 | |
|---|---|---|---|---|---|---|---|
| 8500 | 90.3 | 89.2 | 98.2 | 93.9 | 87.4 | 97.9 | 556.9 |
| 8700 | 92.5 | 89.5 | 90.6 | $x$ | 87.0 | 95.8 | 455.4 |
| 8900 | 85.5 | 90.8 | 89.6 | 86.2 | 88.0 | 93.4 | 533.5 |
| 9100 | 82.5 | 89.5 | 85.6 | 87.4 | 78.9 | 90.7 | 514.6 |
| Block totals | 350.8 | 359.0 | 364.0 | 267.5 | 341.3 | 377.8 | $y'_{..}=2060.4$ |

### PDF page 171 (book page 155)

**TABLE 4.8** Approximate Analysis of Variance for Example 4.1 with One Missing Value

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Extrusion pressure | 166.14 | 3 | 55.38 | 7.63 | 0.0029 |
| Batches of raw material | 189.52 | 5 | 37.90 | | |
| Error | 101.70 | 14 | 7.26 | | |
| Total | 457.36 | 23 | | | |

so that $x$ will have a minimum contribution to the error sum of squares. Because $SS_E=\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})^2$, this is equivalent to choosing $x$ to minimize

$$
SS_E=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2
-\frac{1}{b}\sum_{i=1}^{a}\left(\sum_{j=1}^{b}y_{ij}\right)^2
-\frac{1}{a}\sum_{j=1}^{b}\left(\sum_{i=1}^{a}y_{ij}\right)^2
+\frac{1}{ab}\left(\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}\right)^2
$$

or

$$
SS_E=x^2-\frac{1}{b}(y'_{i.}+x)^2-\frac{1}{a}(y'_{.j}+x)^2+\frac{1}{ab}(y'_{..}+x)^2+R \tag{4.20}
$$

where $R$ includes all terms not involving $x$. From $dSS_E/dx=0$, we obtain

$$
x=\frac{ay'_{i.}+by'_{.j}-y'_{..}}{(a-1)(b-1)} \tag{4.21}
$$

as the estimate of the missing observation.

For the data in Table 4.7, we find that $y'_{2.}=455.4$, $y'_{.4}=267.5$, and $y'_{..}=2060.4$. Therefore, from Equation 4.16,

$$
x\equiv y_{24}=\frac{4(455.4)+6(267.5)-2060.4}{(3)(5)}=91.08
$$

The usual analysis of variance may now be performed using $y_{24}=91.08$ and reducing the error degrees of freedom by 1. The analysis of variance is shown in Table 4.8. Compare the results of this approximate analysis with the results obtained for the full data set (Table 4.4).

If several observations are missing, they may be estimated by writing the error sum of squares as a function of the missing values, differentiating with respect to each missing value, equating the results to zero, and solving the resulting equations. Alternatively, we may use Equation 4.21 iteratively to estimate the missing values. To illustrate the iterative approach, suppose that two values are missing. Arbitrarily estimate the first missing value, and then use this value along with the real data and Equation 4.21 to estimate the second. Now Equation 4.21 can be used to reestimate the first missing value, and following this, the second can be reestimated. This process is continued until convergence is obtained. In any missing value problem, the error degrees of freedom are reduced by one for each missing observation.

**4.1.4 Estimating Model Parameters and the General Regression Significance Test**

If both treatments and blocks are fixed, we may estimate the parameters in the RCBD model by least squares. Recall that the linear statistical model is

$$
y_{ij}=\mu+\tau_i+\beta_j+\epsilon_{ij}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b
\end{cases}
\tag{4.22}
$$

### PDF page 172 (book page 156)

Applying the rules in Section 3.9.2 for finding the normal equations for an experimental design model, we obtain

$$
\begin{aligned}
\mu:\quad &ab\hat{\mu}+b\hat{\tau}_1+b\hat{\tau}_2+\cdots+b\hat{\tau}_a
+a\hat{\beta}_1+a\hat{\beta}_2+\cdots+a\hat{\beta}_b=y_{..}\\
\tau_1:\quad &b\hat{\mu}+b\hat{\tau}_1+\hat{\beta}_1+\hat{\beta}_2+\cdots+\hat{\beta}_b=y_{1.}\\
\tau_2:\quad &b\hat{\mu}+b\hat{\tau}_2+\hat{\beta}_1+\hat{\beta}_2+\cdots+\hat{\beta}_b=y_{2.}\\
&\vdots\\
\tau_a:\quad &b\hat{\mu}+b\hat{\tau}_a+\hat{\beta}_1+\hat{\beta}_2+\cdots+\hat{\beta}_b=y_{a.}\\
\beta_1:\quad &a\hat{\mu}+\hat{\tau}_1+\hat{\tau}_2+\cdots+\hat{\tau}_a+a\hat{\beta}_1=y_{.1}\\
\beta_2:\quad &a\hat{\mu}+\hat{\tau}_1+\hat{\tau}_2+\cdots+\hat{\tau}_a+a\hat{\beta}_2=y_{.2}\\
&\vdots\\
\beta_b:\quad &a\hat{\mu}+\hat{\tau}_1+\hat{\tau}_2+\cdots+\hat{\tau}_a+a\hat{\beta}_b=y_{.b}
\end{aligned}
\tag{4.23}
$$

Notice that the second through the $(a+1)$st equations in Equation 4.23 sum to the first normal equation, as do the last $b$ equations. Thus, there are two linear dependencies in the normal equations, implying that two constraints must be imposed to solve Equation 4.23. The usual constraints are

$$
\sum_{i=1}^{a}\hat{\tau}_i=0\qquad \sum_{j=1}^{b}\hat{\beta}_j=0 \tag{4.24}
$$

Using these constraints helps simplify the normal equations considerably. In fact, they become

$$
\begin{aligned}
ab\hat{\mu}&=y_{..}\\
b\hat{\mu}+b\hat{\tau}_i&=y_{i.}\qquad i=1,2,\ldots,a\\
a\hat{\mu}+a\hat{\beta}_j&=y_{.j}\qquad j=1,2,\ldots,b
\end{aligned}
\tag{4.25}
$$

whose solution is

$$
\begin{aligned}
\hat{\mu}&=\bar{y}_{..}\\
\hat{\tau}_i&=\bar{y}_{i.}-\bar{y}_{..}\qquad i=1,2,\ldots,a\\
\hat{\beta}_j&=\bar{y}_{.j}-\bar{y}_{..}\qquad j=1,2,\ldots,b
\end{aligned}
\tag{4.26}
$$

Using the solution to the normal equation in Equation 4.26, we may find the estimated or fitted values of $y_{ij}$ as

$$
\begin{aligned}
\hat{y}_{ij}&=\hat{\mu}+\hat{\tau}_i+\hat{\beta}_j\\
&=\bar{y}_{..}+(\bar{y}_{i.}-\bar{y}_{..})+(\bar{y}_{.j}-\bar{y}_{..})\\
&=\bar{y}_{i.}+\bar{y}_{.j}-\bar{y}_{..}
\end{aligned}
$$

This result was used previously in Equation 4.13 for computing the residuals from a randomized block design.

### PDF page 173 (book page 157)

The general regression significance test can be used to develop the analysis of variance for the randomized complete block design. Using the solution to the normal equations given by Equation 4.26, the reduction in the sum of squares for fitting the full model is

$$
\begin{aligned}
R(\mu,\tau,\beta)
&=\hat{\mu}y_{..}+\sum_{i=1}^{a}\hat{\tau}_i y_{i.}+\sum_{j=1}^{b}\hat{\beta}_j y_{.j}\\
&=\bar{y}_{..}y_{..}+\sum_{i=1}^{a}(\bar{y}_{i.}-\bar{y}_{..})y_{i.}
+\sum_{j=1}^{b}(\bar{y}_{.j}-\bar{y}_{..})y_{.j}\\
&=\frac{y_{..}^2}{ab}+\sum_{i=1}^{a}\bar{y}_{i.}y_{i.}-\frac{y_{..}^2}{ab}
+\sum_{j=1}^{b}\bar{y}_{.j}y_{.j}-\frac{y_{..}^2}{ab}\\
&=\sum_{i=1}^{a}\frac{y_{i.}^2}{b}+\sum_{j=1}^{b}\frac{y_{.j}^2}{a}-\frac{y_{..}^2}{ab}
\end{aligned}
$$

with $a+b-1$ degrees of freedom, and the error sum of squares is

$$
\begin{aligned}
SS_E&=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2-R(\mu,\tau,\beta)\\
&=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2-\sum_{i=1}^{a}\frac{y_{i.}^2}{b}
-\sum_{j=1}^{b}\frac{y_{.j}^2}{a}+\frac{y_{..}^2}{ab}\\
&=\sum_{i=1}^{a}\sum_{j=1}^{b}(y_{ij}-\bar{y}_{i.}-\bar{y}_{.j}+\bar{y}_{..})^2
\end{aligned}
$$

with $(a-1)(b-1)$ degrees of freedom. Compare this last equation with $SS_E$ in Equation 4.7.

To test the hypothesis $H_0:\tau_i=0$, the **reduced model** is

$$
y_{ij}=\mu+\beta_j+\epsilon_{ij}
$$

which is just a single-factor analysis of variance. By analogy with Equation 3.5, the reduction in the sum of squares for fitting the reduced model is

$$
R(\mu,\beta)=\sum_{j=1}^{b}\frac{y_{.j}^2}{a}
$$

which has $b$ degrees of freedom. Therefore, the sum of squares due to $\{\tau_i\}$ after fitting $\mu$ and $\{\beta_j\}$ is

$$
\begin{aligned}
R(\tau\mid\mu,\beta)&=R(\mu,\tau,\beta)-R(\mu,\beta)\\
&=R(\text{full model})-R(\text{reduced model})\\
&=\sum_{i=1}^{a}\frac{y_{i.}^2}{b}+\sum_{j=1}^{b}\frac{y_{.j}^2}{a}
-\frac{y_{..}^2}{ab}-\sum_{j=1}^{b}\frac{y_{.j}^2}{a}\\
&=\sum_{i=1}^{a}\frac{y_{i.}^2}{b}-\frac{y_{..}^2}{ab}
\end{aligned}
$$

which we recognize as the treatment sum of squares with $a-1$ degrees of freedom (Equation 4.10).

The block sum of squares is obtained by fitting the **reduced model**

$$
y_{ij}=\mu+\tau_i+\epsilon_{ij}
$$

### PDF page 174 (book page 158)

which is also a single-factor analysis. Again, by analogy with Equation 3.5, the reduction in the sum of squares for fitting this model is

$$
R(\mu,\tau)=\sum_{i=1}^{a}\frac{y_{i.}^2}{b}
$$

with $a$ degrees of freedom. The sum of squares for blocks $\{\beta_j\}$ after fitting $\mu$ and $\{\tau_i\}$ is

$$
\begin{aligned}
R(\beta\mid\mu,\tau)&=R(\mu,\tau,\beta)-R(\mu,\tau)\\
&=\sum_{i=1}^{a}\frac{y_{i.}^2}{b}+\sum_{j=1}^{b}\frac{y_{.j}^2}{a}
-\frac{y_{..}^2}{ab}-\sum_{i=1}^{a}\frac{y_{i.}^2}{b}\\
&=\sum_{j=1}^{b}\frac{y_{.j}^2}{a}-\frac{y_{..}^2}{ab}
\end{aligned}
$$

with $b-1$ degrees of freedom, which we have given previously as Equation 4.11.

We have developed the sums of squares for treatments, blocks, and error in the randomized complete block design using the general regression significance test. Although we would not ordinarily use the general regression significance test to actually analyze data in a randomized complete block, the procedure occasionally proves useful in more general randomized block designs, such as those discussed in Section 4.4.

***Exact Analysis of the Missing Value Problem.*** In Section 4.1.3 an approximate procedure for dealing with missing observations in the RCBD was presented. This approximate analysis consists of estimating the missing value so that the error mean square is minimized. It can be shown that the approximate analysis produces a biased mean square for treatments in the sense that $E(MS_{\text{Treatments}})$ is larger than $E(MS_E)$ if the null hypothesis is true. Consequently, too many significant results are reported.

The missing value problem may be analyzed exactly by using the general regression significance test. The missing value causes the design to be **unbalanced**, and because all the treatments do not occur in all blocks, we say that the treatments and blocks are not **orthogonal**. This method of analysis is also used in more general types of randomized block designs; it is discussed further in Section 4.4. Many computer packages will perform this analysis.

**4.2 The Latin Square Design**

In Section 4.1 we introduced the randomized complete block design as a design to reduce the residual error in an experiment by removing variability due to a known and controllable nuisance variable. There are several other types of designs that utilize the blocking principle. For example, suppose that an experimenter is studying the effects of five different formulations of a rocket propellant used in aircrew escape systems on the observed burning rate. Each formulation is mixed from a batch of raw material that is only large enough for five formulations to be tested. Furthermore, the formulations are prepared by several operators, and there may be substantial differences in the skills and experience of the operators. Thus, it would seem that there are two nuisance factors to be “averaged out” in the design: batches of raw material and operators. The appropriate design for this problem consists of testing each formulation exactly once in each batch of raw material and for each formulation to be prepared exactly once by each of five operators. The resulting design, shown in Table 4.9, is called a **Latin square design**. Notice that the design is a square arrangement and that the five formulations (or treatments) are denoted by the Latin letters $A$, $B$, $C$, $D$, and $E$; hence the name Latin square.

### PDF page 175 (book page 159)

**TABLE 4.9** Latin Square Design for the Rocket Propellant Problem

| Batches of Raw Material | Operators 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | $A=24$ | $B=20$ | $C=19$ | $D=24$ | $E=24$ |
| 2 | $B=17$ | $C=24$ | $D=30$ | $E=27$ | $A=36$ |
| 3 | $C=18$ | $D=38$ | $E=26$ | $A=27$ | $B=21$ |
| 4 | $D=26$ | $E=31$ | $A=26$ | $B=23$ | $C=22$ |
| 5 | $E=22$ | $A=30$ | $B=20$ | $C=29$ | $D=31$ |

We see that both batches of raw material (rows) and operators (columns) are orthogonal to treatments.

The Latin square design is used to eliminate two nuisance sources of variability; that is, it systematically allows blocking in two directions. Thus, the rows and columns actually represent **two restrictions on randomization**. In general, a Latin square for $p$ factors, or a $p\times p$ Latin square, is a square containing $p$ rows and $p$ columns. Each of the resulting $p^2$ cells contains one of the $p$ letters that corresponds to the treatments, and each letter occurs once and only once in each row and column. Some examples of Latin squares are

| $4\times4$ | $5\times5$ | $6\times6$ |
|---|---|---|
| A B D C | A D B E C | A D C E B F |
| B C A D | D A C B E | B A E C F D |
| C D B A | C B E D A | C E D F A B |
| D A C B | B E A C D | D C F B E A |
| | E C D A B | F B A D C E |
| | | E F B A D C |

Latin squares are closely related to a popular puzzle called a sudoku puzzle that originated in Japan (sudoku means “single number” in Japanese). The puzzle typically consists of a $9\times9$ grid, with nine additional $3\times3$ blocks contained within. A few of the spaces contain numbers and the others are blank. The goal is to fill the blanks with the integers from 1 to 9 so that each row, each column, and each of the nine $3\times3$ blocks making up the grid contains just one of each of the nine integers. The additional constraint that a standard $9\times9$ sudoku puzzle have $3\times3$ blocks that also contain each of the nine integers reduces the large number of possible $9\times9$ Latin squares to a smaller but still quite large number, approximately $6\times10^{21}$.

Depending on the number of clues and the size of the grid, sudoku puzzles can be extremely difficult to solve. Solving an $n\times n$ sudoku puzzle belongs to a class of computational problems called NP-complete (the NP refers to non-polynomial computing time). An NP-complete problem is one for which it’s relatively easy to check whether a particular answer is correct but may require an impossibly long time to solve by any simple algorithm as $n$ gets larger.

Solving a sudoku puzzle is also equivalent to “coloring” a graph—an array of points (vertices) and lines (edges) in a particular way. In this case, the graph has 81 vertices, one for each cell of the grid. Depending on the puzzle, only certain pairs of vertices are joined by an edge. Given that some vertices have already been assigned a “color” (chosen from the nine number possibilities), the problem is to “color” the remaining vertices so that any two vertices joined by an edge don’t have the same “color.”

### PDF page 176 (book page 160)

The **statistical model** for a Latin square is

$$
y_{ijk}=\mu+\alpha_i+\tau_j+\beta_k+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,p\\
j=1,2,\ldots,p\\
k=1,2,\ldots,p
\end{cases}
\tag{4.27}
$$

where $y_{ijk}$ is the observation in the $i$th row and $k$th column for the $j$th treatment, $\mu$ is the overall mean, $\alpha_i$ is the $i$th row effect, $\tau_j$ is the $j$th treatment effect, $\beta_k$ is the $k$th column effect, and $\epsilon_{ijk}$ is the random error. Note that this is an **effects model**. The model is completely **additive**; that is, there is no interaction between rows, columns, and treatments. Because there is only one observation in each cell, only two of the three subscripts $i$, $j$, and $k$ are needed to denote a particular observation. For example, referring to the rocket propellant problem in Table 4.8, if $i=2$ and $k=3$, we automatically find $j=4$ (formulation D), and if $i=1$ and $j=3$ (formulation C), we find $k=3$. This is a consequence of each treatment appearing exactly once in each row and column.

The analysis of variance consists of partitioning the total sum of squares of the $N=p^2$ observations into components for rows, columns, treatments, and error, for example,

$$
SS_T=SS_{\text{Rows}}+SS_{\text{Columns}}+SS_{\text{Treatments}}+SS_E \tag{4.28}
$$

with respective degrees of freedom

$$
p^2-1=p-1+p-1+p-1+(p-2)(p-1)
$$

Under the usual assumption that $\epsilon_{ijk}$ is NID $(0,\sigma^2)$, each sum of squares on the right-hand side of Equation 4.28 is, upon division by $\sigma^2$, an independently distributed chi-square random variable. The appropriate statistic for testing for no differences in treatment means is

$$
F_0=\frac{MS_{\text{Treatments}}}{MS_E}
$$

which is distributed as $F_{p-1,(p-2)(p-1)}$ under the null hypothesis. We may also test for no row effect and no column effect by forming the ratio of $MS_{\text{Rows}}$ or $MS_{\text{Columns}}$ to $MS_E$. However, because the rows and columns represent restrictions on randomization, these tests may not be appropriate.

The computational procedure for the ANOVA in terms of treatment, row, and column totals is shown in Table 4.10. From the computational formulas for the sums of squares, we see that the analysis is a simple extension of the RCBD, with the sum of squares resulting from rows obtained from the row totals.

**TABLE 4.10** Analysis of Variance for the Latin Square Design

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments | $SS_{\text{Treatments}}=\dfrac1p\sum_{j=1}^{p}y_{.j.}^2-\dfrac{y_{...}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Treatments}}}{p-1}$ | $\dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Rows | $SS_{\text{Rows}}=\dfrac1p\sum_{i=1}^{p}y_{i..}^2-\dfrac{y_{...}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Rows}}}{p-1}$ | |
| Columns | $SS_{\text{Columns}}=\dfrac1p\sum_{k=1}^{p}y_{..k}^2-\dfrac{y_{...}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Columns}}}{p-1}$ | |
| Error | $SS_E$ (by subtraction) | $(p-2)(p-1)$ | $\dfrac{SS_E}{(p-2)(p-1)}$ | |
| Total | $SS_T=\sum_i\sum_j\sum_k y_{ijk}^2-\dfrac{y_{...}^2}{N}$ | $p^2-1$ | | |

### PDF page 177 (book page 161)

**EXAMPLE 4.3**

Consider the rocket propellant problem previously described, where both batches of raw material and operators represent randomization restrictions. The design for this experiment, shown in Table 4.8, is a $5\times5$ Latin square. After coding by subtracting 25 from each observation, we have the data in Table 4.11. The sums of squares for the total, batches (rows), and operators (columns) are computed as follows:

$$
\begin{aligned}
SS_T&=\sum_i\sum_j\sum_k y_{ijk}^2-\frac{y_{...}^2}{N}\\
&=680-\frac{(10)^2}{25}=676.00
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Batches}}&=\frac1p\sum_{i=1}^{p}y_{i..}^2-\frac{y_{...}^2}{N}\\
&=\frac15\big[(-14)^2+9^2+5^2+3^2+7^2\big]-\frac{(10)^2}{25}=68.00
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Operators}}&=\frac1p\sum_{k=1}^{p}y_{..k}^2-\frac{y_{...}^2}{N}\\
&=\frac15\big[(-18)^2+18^2+(-4)^2+5^2+9^2\big]-\frac{(10)^2}{25}=150.00
\end{aligned}
$$

The totals for the treatments (Latin letters) are

| Latin Letter | Treatment Total |
|---|---|
| $A$ | $y_{.1.}=18$ |
| $B$ | $y_{.2.}=-24$ |
| $C$ | $y_{.3.}=-13$ |
| $D$ | $y_{.4.}=24$ |
| $E$ | $y_{.5.}=5$ |

The sum of squares resulting from the formulations is computed from these totals as

$$
\begin{aligned}
SS_{\text{Formulations}}&=\frac1p\sum_{j=1}^{p}y_{.j.}^2-\frac{y_{...}^2}{N}\\
&=\frac{18^2+(-24)^2+(-13)^2+24^2+5^2}{5}-\frac{(10)^2}{25}=330.00
\end{aligned}
$$

The error sum of squares is found by subtraction

$$
\begin{aligned}
SS_E&=SS_T-SS_{\text{Batches}}-SS_{\text{Operators}}-SS_{\text{Formulations}}\\
&=676.00-68.00-150.00-330.00=128.00
\end{aligned}
$$

The analysis of variance is summarized in Table 4.12. We conclude that there is a significant difference in the mean burning rate generated by the different rocket propellant formulations. There is also an indication that differences between operators exist, so blocking on this factor was a good precaution. There is no strong evidence of a difference between batches of raw material, so it seems that in this particular experiment we were unnecessarily concerned about this source of variability. However, blocking on batches of raw material is usually a good idea.

**TABLE 4.11** Coded Data for the Rocket Propellant Problem

| Batches of Raw Material | Operators 1 | 2 | 3 | 4 | 5 | $y_{i..}$ |
|---|---|---|---|---|---|---|
| 1 | $A=-1$ | $B=-5$ | $C=-6$ | $D=-1$ | $E=-1$ | −14 |
| 2 | $B=-8$ | $C=-1$ | $D=5$ | $E=2$ | $A=11$ | 9 |
| 3 | $C=-7$ | $D=13$ | $E=1$ | $A=2$ | $B=-4$ | 5 |
| 4 | $D=1$ | $E=6$ | $A=1$ | $B=-2$ | $C=-3$ | 3 |
| 5 | $E=-3$ | $A=5$ | $B=-5$ | $C=4$ | $D=6$ | 7 |
| $y_{..k}$ | −18 | 18 | −4 | 5 | 9 | $10=y_{...}$ |

### PDF page 178 (book page 162)

**TABLE 4.12** Analysis of Variance for the Rocket Propellant Experiment

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Formulations | 330.00 | 4 | 82.50 | 7.73 | 0.0025 |
| Batches of raw material | 68.00 | 4 | 17.00 | | |
| Operators | 150.00 | 4 | 37.50 | | |
| Error | 128.00 | 12 | 10.67 | | |
| Total | 676.00 | 24 | | | |

As in any design problem, the experimenter should investigate the adequacy of the model by inspecting and plotting the residuals. For a Latin square, the residuals are given by

$$
\begin{aligned}
e_{ijk}&=y_{ijk}-\hat{y}_{ijk}\\
&=y_{ijk}-\bar{y}_{i..}-\bar{y}_{.j.}-\bar{y}_{..k}+2\bar{y}_{...}
\end{aligned}
$$

The reader should find the residuals for Example 4.3 and construct appropriate plots.

A Latin square in which the first row and column consists of the letters written in alphabetical order is called a **standard Latin square**, which is the design shown in Example 4.4. A standard Latin square can always be obtained by writing the first row in alphabetical order and then writing each successive row as the row of letters just above shifted one place to the left. Table 4.13 summarizes several important facts about Latin squares and standard Latin squares.

As with any experimental design, the observations in the Latin square should be taken in random order. The proper randomization procedure is to select the particular square employed at random. As we see in Table 4.13, there are a large number of Latin squares of a particular size, so it is impossible to enumerate all the squares and select one randomly. The usual procedure is

**TABLE 4.13** Standard Latin Squares and Number of Latin Squares of Various Sizes[^a]

| Size | $3\times3$ | $4\times4$ | $5\times5$ | $6\times6$ | $7\times7$ | $p\times p$ |
|---|---|---|---|---|---|---|
| Examples of standard squares | A B C<br>B C A<br>C A B | A B C D<br>B C D A<br>C D A B<br>D A B C | A B C D E<br>B A E C D<br>C D A E B<br>D E B A C<br>E C D B A | A B C D E F<br>B C F A D E<br>C F B E A D<br>D E A B F C<br>E A D F C B<br>F D E C B A | A B C D E F G<br>B C D E F G A<br>C D E F G A B<br>D E F G A B C<br>E F G A B C D<br>F G A B C D E<br>G A B C D E F | ABC … P<br>BCD … A<br>CDE … B<br>⋮<br>PAB … $(P-1)$ |
| Number of standard squares | 1 | 4 | 56 | 9408 | 16,942,080 | — |
| Total number of Latin squares | 12 | 576 | 161,280 | 818,851,200 | 61,479,419,904,000 | $p!(p-1)!\times$ (number of standard squares) |

[^a]: Some of the information in this table is found in Fisher and Yates (1953). Little is known about the properties of Latin squares larger than $7\times7$.

### PDF page 179 (book page 163)

to select an arbitrary Latin square from a table of such designs, as in Fisher and Yates (1953), or start with a standard square, and then arrange the order of the rows, columns, and letters at random. This is discussed more completely in Fisher and Yates (1953).

Occasionally, one observation in a Latin square is missing. For a $p\times p$ Latin square, the missing value may be estimated by

$$
y_{ijk}=\frac{p(y'_{i..}+y'_{.j.}+y'_{..k})-2y'_{...}}{(p-2)(p-1)} \tag{4.29}
$$

where the primes indicate totals for the row, column, and treatment with the missing value, and $y'_{...}$ is the grand total with the missing value.

Latin squares can be useful in situations where the rows and columns represent factors the experimenter actually wishes to study and where there are no randomization restrictions. Thus, three factors (rows, columns, and letters), each at $p$ levels, can be investigated in only $p^2$ runs. This design assumes that there is no interaction between the factors. More will be said later on the subject of interaction.

***Replication of Latin Squares.*** A disadvantage of small Latin squares is that they provide a relatively small number of error degrees of freedom. For example, a $3\times3$ Latin square has only two error degrees of freedom, a $4\times4$ Latin square has only six error degrees of freedom, and so forth. When small Latin squares are used, it is frequently desirable to replicate them to increase the error degrees of freedom.

A Latin square may be replicated in several ways. To illustrate, suppose that the $5\times5$ Latin square used in Example 4.4 is replicated $n$ times. This could have been done as follows:

1. Use the same batches and operators in each replicate.

2. Use the same batches but different operators in each replicate (or, equivalently, use the same operators but different batches).

3. Use different batches and different operators.

The analysis of variance depends on the method of replication.

Consider case 1, where the same levels of the row and column blocking factors are used in each replicate. Let $y_{ijkl}$ be the observation in row $i$, treatment $j$, column $k$, and replicate $l$. There are $N=np^2$ total observations. The ANOVA is summarized in Table 4.14.

**TABLE 4.14** Analysis of Variance for a Replicated Latin Square, Case 1

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments | $\dfrac1{np}\sum_{j=1}^{p}y_{.j..}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Treatments}}}{p-1}$ | $\dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Rows | $\dfrac1{np}\sum_{i=1}^{p}y_{i...}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Rows}}}{p-1}$ | |
| Columns | $\dfrac1{np}\sum_{k=1}^{p}y_{..k.}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Columns}}}{p-1}$ | |
| Replicates | $\dfrac1{p^2}\sum_{l=1}^{n}y_{...l}^2-\dfrac{y_{....}^2}{N}$ | $n-1$ | $\dfrac{SS_{\text{Replicates}}}{n-1}$ | |
| Error | Subtraction | $(p-1)[n(p+1)-3]$ | $\dfrac{SS_E}{(p-1)[n(p+1)-3]}$ | |
| Total | $\sum_i\sum_j\sum_k\sum_l y_{ijkl}^2-\dfrac{y_{....}^2}{N}$ | $np^2-1$ | | |

### PDF page 180 (book page 164)

**TABLE 4.15** Analysis of Variance for a Replicated Latin Square, Case 2

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments | $\dfrac1{np}\sum_{j=1}^{p}y_{.j..}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Treatments}}}{p-1}$ | $\dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Rows | $\dfrac1p\sum_{l=1}^{n}\sum_{i=1}^{p}y_{i..l}^2-\sum_{l=1}^{n}\dfrac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $\dfrac{SS_{\text{Rows}}}{n(p-1)}$ | |
| Columns | $\dfrac1{np}\sum_{k=1}^{p}y_{..k.}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Columns}}}{p-1}$ | |
| Replicates | $\dfrac1{p^2}\sum_{l=1}^{n}y_{...l}^2-\dfrac{y_{....}^2}{N}$ | $n-1$ | $\dfrac{SS_{\text{Replicates}}}{n-1}$ | |
| Error | Subtraction | $(p-1)(np-1)$ | $\dfrac{SS_E}{(p-1)(np-1)}$ | |
| Total | $\sum_i\sum_j\sum_k\sum_l y_{ijkl}^2-\dfrac{y_{....}^2}{N}$ | $np^2-1$ | | |

Now consider case 2 and assume that new batches of raw material but the same operators are used in each replicate. Thus, there are now five new rows (in general, $p$ new rows) within each replicate. The ANOVA is summarized in Table 4.15. Note that the source of variation for the rows really measures the variation between rows within the $n$ replicates.

Finally, consider case 3, where new batches of raw material and new operators are used in each replicate. Now the variation that results from both the rows and columns measures the variation resulting from these factors within the replicates. The ANOVA is summarized in Table 4.16.

There are other approaches to analyzing replicated Latin squares that allow some interactions between treatments and squares (refer to Problem 4.30).

***Crossover Designs and Designs Balanced for Residual Effects.*** Occasionally, one encounters a problem in which time periods are a factor in the experiment. In general, there are $p$ treatments to be tested in $p$ time periods using $np$ experimental units. For example, a human performance analyst is studying the effect of two replacement fluids on dehydration

**TABLE 4.16** Analysis of Variance for a Replicated Latin Square, Case 3

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments | $\dfrac1{np}\sum_{j=1}^{p}y_{.j..}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ | $\dfrac{SS_{\text{Treatments}}}{p-1}$ | $\dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Rows | $\dfrac1p\sum_{l=1}^{n}\sum_{i=1}^{p}y_{i..l}^2-\sum_{l=1}^{n}\dfrac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $\dfrac{SS_{\text{Rows}}}{n(p-1)}$ | |
| Columns | $\dfrac1p\sum_{l=1}^{n}\sum_{k=1}^{p}y_{..kl}^2-\sum_{l=1}^{n}\dfrac{y_{...l}^2}{p^2}$ | $n(p-1)$ | $\dfrac{SS_{\text{Columns}}}{n(p-1)}$ | |
| Replicates | $\dfrac1{p^2}\sum_{l=1}^{n}y_{...l}^2-\dfrac{y_{....}^2}{N}$ | $n-1$ | $\dfrac{SS_{\text{Replicates}}}{n-1}$ | |
| Error | Subtraction | $(p-1)[n(p-1)-1]$ | $\dfrac{SS_E}{(p-1)[n(p-1)-1]}$ | |
| Total | $\sum_i\sum_j\sum_k\sum_l y_{ijkl}^2-\dfrac{y_{....}^2}{N}$ | $np^2-1$ | | |

### PDF page 181 (book page 165)

**FIGURE 4.7** A crossover design

| Latin Square | I | | II | | III | | IV | | V | | VI | | VII | | VIII | | IX | | X | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Subject | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Period 1 | $A$ | $B$ | $B$ | $A$ | $B$ | $A$ | $A$ | $B$ | $A$ | $B$ | $B$ | $A$ | $A$ | $B$ | $A$ | $B$ | $A$ | $B$ | $A$ | $B$ |
| Period 2 | $B$ | $A$ | $A$ | $B$ | $A$ | $B$ | $B$ | $A$ | $B$ | $A$ | $A$ | $B$ | $B$ | $A$ | $B$ | $A$ | $B$ | $A$ | $B$ | $A$ |

*[Figure: ten two-period, two-treatment Latin squares pair the 20 subjects. Each subject receives fluids A and B in opposite orders across the two periods.]*

**TABLE 4.17** Analysis of Variance for the Crossover Design in Figure 4.7

| Source of Variation | Degrees of Freedom |
|---|---|
| Subjects (columns) | 19 |
| Periods (rows) | 1 |
| Fluids (letters) | 1 |
| Error | 18 |
| Total | 39 |

in 20 subjects. In the first period, half of the subjects (chosen at random) are given fluid $A$ and the other half fluid $B$. At the end of the period, the response is measured and a period of time is allowed to pass in which any physiological effect of the fluids is eliminated. Then the experimenter has the subjects who took fluid $A$ take fluid $B$ and those who took fluid $B$ take fluid $A$. This design is called a **crossover design**. It is analyzed as a set of 10 Latin squares with two rows (time periods) and two treatments (fluid types). The two columns in each of the 10 squares correspond to subjects.

The layout of this design is shown in Figure 4.7. Notice that the rows in the Latin square represent the time periods and the columns represent the subjects. The 10 subjects who received fluid $A$ first (1, 4, 6, 7, 9, 12, 13, 15, 17, and 19) are randomly determined.

An abbreviated analysis of variance is summarized in Table 4.17. The subject sum of squares is computed as the corrected sum of squares among the 20 subject totals, the period sum of squares is the corrected sum of squares among the rows, and the fluid sum of squares is computed as the corrected sum of squares among the letter totals. For further details of the statistical analysis of these designs see Cochran and Cox (1957), John (1971), and Anderson and McLean (1974).

It is also possible to employ Latin square type designs for experiments in which the treatments have a **residual effect**—that is, for example, if the data for fluid $B$ in period 2 still reflected some effect of fluid $A$ taken in period 1. Designs balanced for residual effects are discussed in detail by Cochran and Cox (1957) and John (1971).

**4.3 The Graeco-Latin Square Design**

Consider a $p\times p$ Latin square, and superimpose on it a second $p\times p$ Latin square in which the treatments are denoted by Greek letters. If the two squares when superimposed have the property that each Greek letter appears once and only once with each Latin letter, the two Latin squares are said to be **orthogonal**, and the design obtained is called a **Graeco-Latin square**. An example of a $4\times4$ Graeco-Latin square is shown in Table 4.18.

### PDF page 182 (book page 166)

**TABLE 4.18** $4\times4$ Graeco-Latin Square Design

| Row | Column 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | $A\alpha$ | $B\beta$ | $C\gamma$ | $D\delta$ |
| 2 | $B\delta$ | $A\gamma$ | $D\beta$ | $C\alpha$ |
| 3 | $C\beta$ | $D\alpha$ | $A\delta$ | $B\gamma$ |
| 4 | $D\gamma$ | $C\delta$ | $B\alpha$ | $A\beta$ |

The Graeco-Latin square design can be used to control systematically three sources of extraneous variability, that is, to block in three directions. The design allows investigation of four factors (rows, columns, Latin letters, and Greek letters), each at $p$ levels in only $p^2$ runs. Graeco-Latin squares exist for all $p\geq3$ except $p=6$.

The statistical model for the Graeco-Latin square design is

$$
y_{ijkl}=\mu+\theta_i+\tau_j+\omega_k+\Psi_l+\epsilon_{ijkl}
\begin{cases}
i=1,2,\ldots,p\\
j=1,2,\ldots,p\\
k=1,2,\ldots,p\\
l=1,2,\ldots,p
\end{cases}
\tag{4.30}
$$

where $y_{ijkl}$ is the observation in row $i$ and column $l$ for Latin letter $j$ and Greek letter $k$, $\theta_i$ is the effect of the $i$th row, $\tau_j$ is the effect of Latin letter treatment $j$, $\omega_k$ is the effect of Greek letter treatment $k$, $\Psi_l$ is the effect of column $l$, and $\epsilon_{ijkl}$ is an NID $(0,\sigma^2)$ random error component. Only two of the four subscripts are necessary to completely identify an observation.

The analysis of variance is very similar to that of a Latin square. Because the Greek letters appear exactly once in each row and column and exactly once with each Latin letter, the factor represented by the Greek letters is orthogonal to rows, columns, and Latin letter treatments. Therefore, a sum of squares due to the Greek letter factor may be computed from the Greek letter totals, and the experimental error is further reduced by this amount. The computational details are illustrated in Table 4.19. The null hypotheses of equal row, column, Latin letter, and Greek letter treatments would be tested by dividing the corresponding mean square by mean square error. The rejection region is the upper tail point of the $F_{p-1,(p-3)(p-1)}$ distribution.

**TABLE 4.19** Analysis of Variance for a Graeco-Latin Square Design

| Source of Variation | Sum of Squares | Degrees of Freedom |
|---|---|---|
| Latin letter treatments | $SS_L=\dfrac1p\sum_{j=1}^{p}y_{.j..}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ |
| Greek letter treatments | $SS_G=\dfrac1p\sum_{k=1}^{p}y_{..k.}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ |
| Rows | $SS_{\text{Rows}}=\dfrac1p\sum_{i=1}^{p}y_{i...}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ |
| Columns | $SS_{\text{Columns}}=\dfrac1p\sum_{l=1}^{p}y_{...l}^2-\dfrac{y_{....}^2}{N}$ | $p-1$ |
| Error | $SS_E$ (by subtraction) | $(p-3)(p-1)$ |
| Total | $SS_T=\sum_i\sum_j\sum_k\sum_l y_{ijkl}^2-\dfrac{y_{....}^2}{N}$ | $p^2-1$ |

### PDF page 183 (book page 167)

**EXAMPLE 4.4**

Suppose that in the rocket propellant experiment of Example 4.3 an additional factor, test assemblies, could be of importance. Let there be five test assemblies denoted by the Greek letters $\alpha$, $\beta$, $\gamma$, $\delta$, and $\epsilon$. The resulting $5\times5$ Graeco-Latin square design is shown in Table 4.20.

Notice that, because the totals for batches of raw material (rows), operators (columns), and formulations (Latin letters) are identical to those in Example 4.3, we have

$$
SS_{\text{Batches}}=68.00,\quad SS_{\text{Operators}}=150.00,\quad\text{and}\quad SS_{\text{Formulations}}=330.00
$$

The totals for the test assemblies (Greek letters) are

| Greek Letter | Test Assembly Total |
|---|---|
| $\alpha$ | $y_{..1.}=10$ |
| $\beta$ | $y_{..2.}=-6$ |
| $\gamma$ | $y_{..3.}=-3$ |
| $\delta$ | $y_{..4.}=-4$ |
| $\epsilon$ | $y_{..5.}=13$ |

Thus, the sum of squares due to the test assemblies is

$$
\begin{aligned}
SS_{\text{Assemblies}}&=\frac1p\sum_{k=1}^{p}y_{..k.}^2-\frac{y_{....}^2}{N}\\
&=\frac15\big[10^2+(-6)^2+(-3)^2+(-4)^2+13^2\big]-\frac{(10)^2}{25}=62.00
\end{aligned}
$$

The complete ANOVA is summarized in Table 4.21. Formulations are significantly different at 1 percent. In comparing Tables 4.21 and 4.12, we observe that removing the variability due to test assemblies has decreased the experimental error. However, in decreasing the experimental error, we have also reduced the error degrees of freedom from 12 (in the Latin square design of Example 4.3) to 8. Thus, our estimate of error has fewer degrees of freedom, and the test may be less sensitive.

**TABLE 4.20** Graeco-Latin Square Design for the Rocket Propellant Problem

| Batches of Raw Material | Operators 1 | 2 | 3 | 4 | 5 | $y_{i...}$ |
|---|---|---|---|---|---|---|
| 1 | $A\alpha=-1$ | $B\gamma=-5$ | $C\epsilon=-6$ | $D\beta=-1$ | $E\delta=-1$ | −14 |
| 2 | $B\beta=-8$ | $C\delta=-1$ | $D\alpha=5$ | $E\gamma=2$ | $A\epsilon=11$ | 9 |
| 3 | $C\gamma=-7$ | $D\epsilon=13$ | $E\beta=1$ | $A\delta=2$ | $B\alpha=-4$ | 5 |
| 4 | $D\delta=1$ | $E\alpha=6$ | $A\gamma=1$ | $B\epsilon=-2$ | $C\beta=-3$ | 3 |
| 5 | $E\epsilon=-3$ | $A\beta=5$ | $B\delta=-5$ | $C\alpha=4$ | $D\gamma=6$ | 7 |
| $y_{...l}$ | −18 | 18 | −4 | 5 | 9 | $10=y_{....}$ |

**TABLE 4.21** Analysis of Variance for the Rocket Propellant Problem

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Formulations | 330.00 | 4 | 82.50 | 10.00 | 0.0033 |
| Batches of raw material | 68.00 | 4 | 17.00 | | |
| Operators | 150.00 | 4 | 37.50 | | |
| Test assemblies | 62.00 | 4 | 15.50 | | |
| Error | 66.00 | 8 | 8.25 | | |
| Total | 676.00 | 24 | | | |

### PDF page 184 (book page 168)

The concept of orthogonal pairs of Latin squares forming a Graeco-Latin square can be extended somewhat. A $p\times p$ **hypersquare** is a design in which three or more orthogonal $p\times p$ Latin squares are superimposed. In general, up to $p+1$ factors could be studied if a complete set of $p-1$ orthogonal Latin squares is available. Such a design would utilize all $(p+1)(p-1)=p^2-1$ degrees of freedom, so an independent estimate of the error variance is necessary. Of course, there must be no interactions between the factors when using hypersquares.

**4.4 Balanced Incomplete Block Designs**

In certain experiments using randomized block designs, we may not be able to run all the treatment combinations in each block. Situations like this usually occur because of shortages of experimental apparatus or facilities or the physical size of the block. For example, in the vascular graft experiment (Example 4.1), suppose that each batch of material is only large enough to accommodate testing three extrusion pressures. Therefore, each pressure cannot be tested in each batch. For this type of problem it is possible to use randomized block designs in which every treatment is not present in every block. These designs are known as **randomized incomplete block designs**.

When all treatment comparisons are equally important, the treatment combinations used in each block should be selected in a balanced manner, so that any pair of treatments occur together the same number of times as any other pair. Thus, a **balanced incomplete block design (BIBD)** is an incomplete block design in which any two treatments appear together an equal number of times. Suppose that there are $a$ treatments and that each block can hold exactly $k$ $(k<a)$ treatments. A balanced incomplete block design may be constructed by taking $\binom{a}{k}$ blocks and assigning a different combination of treatments to each block. Frequently, however, balance can be obtained with fewer than $\binom{a}{k}$ blocks. Tables of BIBDs are given in Fisher and Yates (1953), Davies (1956), and Cochran and Cox (1957).

As an example, suppose that a chemical engineer thinks that the time of reaction for a chemical process is a function of the type of catalyst employed. Four catalysts are currently being investigated. The experimental procedure consists of selecting a batch of raw material, loading the pilot plant, applying each catalyst in a separate run of the pilot plant, and observing the reaction time. Because variations in the batches of raw material may affect the performance of the catalysts, the engineer decides to use batches of raw material as blocks. However, each batch is only large enough to permit three catalysts to be run. Therefore, a randomized incomplete block design must be used. The balanced incomplete block design for this experiment, along with the observations recorded, is shown in Table 4.22. The order in which the catalysts are run in each block is randomized.

**4.4.1 Statistical Analysis of the BIBD**

As usual, we assume that there are $a$ treatments and $b$ blocks. In addition, we assume that each block contains $k$ treatments, that each treatment occurs $r$ times in the design (or is replicated

**TABLE 4.22** Balanced Incomplete Block Design for Catalyst Experiment

| Treatment (Catalyst) | Block (Batch of Raw Material) 1 | 2 | 3 | 4 | $y_{i.}$ |
|---|---|---|---|---|---|
| 1 | 73 | 74 | — | 71 | 218 |
| 2 | — | 75 | 67 | 72 | 214 |
| 3 | 73 | 75 | 68 | — | 216 |
| 4 | 75 | — | 72 | 75 | 222 |
| $y_{.j}$ | 221 | 224 | 207 | 218 | $870=y_{..}$ |

### PDF page 185 (book page 169)

$r$ times), and that there are $N=ar=bk$ total observations. Furthermore, the number of times each pair of treatments appears in the same block is

$$
\lambda=\frac{r(k-1)}{a-1}
$$

If $a=b$, the design is said to be **symmetric**.

The parameter $\lambda$ must be an integer. To derive the relationship for $\lambda$, consider any treatment, say treatment 1. Because treatment 1 appears in $r$ blocks and there are $k-1$ other treatments in each of those blocks, there are $r(k-1)$ observations in a block containing treatment 1. These $r(k-1)$ observations also have to represent the remaining $a-1$ treatments $\lambda$ times. Therefore, $\lambda(a-1)=r(k-1)$.

The **statistical model** for the BIBD is

$$
y_{ij}=\mu+\tau_i+\beta_j+\epsilon_{ij} \tag{4.31}
$$

where $y_{ij}$ is the $i$th observation in the $j$th block, $\mu$ is the overall mean, $\tau_i$ is the effect of the $i$th treatment, $\beta_j$ is the effect of the $j$th block, and $\epsilon_{ij}$ is the NID $(0,\sigma^2)$ random error component. The total variability in the data is expressed by the total corrected sum of squares:

$$
SS_T=\sum_i\sum_j y_{ij}^2-\frac{y_{..}^2}{N} \tag{4.32}
$$

Total variability may be partitioned into

$$
SS_T=SS_{\text{Treatments(adjusted)}}+SS_{\text{Blocks}}+SS_E
$$

where the sum of squares for treatments is **adjusted** to separate the treatment and the block effects. This adjustment is necessary because each treatment is represented in a different set of $r$ blocks. Thus, differences between unadjusted treatment totals $y_{1.},y_{2.},\ldots,y_{a.}$ are also affected by differences between blocks.

The block sum of squares is

$$
SS_{\text{Blocks}}=\frac1k\sum_{j=1}^{b}y_{.j}^2-\frac{y_{..}^2}{N} \tag{4.33}
$$

where $y_{.j}$ is the total in the $j$th block. $SS_{\text{Blocks}}$ has $b-1$ degrees of freedom. The adjusted treatment sum of squares is

$$
SS_{\text{Treatments(adjusted)}}=\frac{k\sum_{i=1}^{a}Q_i^2}{\lambda a} \tag{4.34}
$$

where $Q_i$ is the adjusted total for the $i$th treatment, which is computed as

$$
Q_i=y_{i.}-\frac1k\sum_{j=1}^{b}n_{ij}y_{.j}\qquad i=1,2,\ldots,a \tag{4.35}
$$

with $n_{ij}=1$ if treatment $i$ appears in block $j$ and $n_{ij}=0$ otherwise. The adjusted treatment totals will always sum to zero. $SS_{\text{Treatments(adjusted)}}$ has $a-1$ degrees of freedom. The error sum of squares is computed by subtraction as

$$
SS_E=SS_T-SS_{\text{Treatments(adjusted)}}-SS_{\text{Blocks}} \tag{4.36}
$$

and has $N-a-b+1$ degrees of freedom.

The appropriate statistic for testing the equality of the treatment effects is

$$
F_0=\frac{MS_{\text{Treatments(adjusted)}}}{MS_E}
$$

The ANOVA is summarized in Table 4.23.

### PDF page 186 (book page 170)

**TABLE 4.23** Analysis of Variance for the Balanced Incomplete Block Design

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---|---|---|---|
| Treatments (adjusted) | $\dfrac{k\sum Q_i^2}{\lambda a}$ | $a-1$ | $\dfrac{SS_{\text{Treatments(adjusted)}}}{a-1}$ | $\dfrac{MS_{\text{Treatments(adjusted)}}}{MS_E}$ |
| Blocks | $\dfrac1k\sum y_{.j}^2-\dfrac{y_{..}^2}{N}$ | $b-1$ | $\dfrac{SS_{\text{Blocks}}}{b-1}$ | |
| Error | $SS_E$ (by subtraction) | $N-a-b+1$ | $\dfrac{SS_E}{N-a-b+1}$ | |
| Total | $\sum\sum y_{ij}^2-\dfrac{y_{..}^2}{N}$ | $N-1$ | | |

**EXAMPLE 4.5**

Consider the data in Table 4.22 for the catalyst experiment. This is a BIBD with $a=4$, $b=4$, $k=3$, $r=3$, $\lambda=2$, and $N=12$. The analysis of this data is as follows. The total sum of squares is

$$
\begin{aligned}
SS_T&=\sum_i\sum_j y_{ij}^2-\frac{y_{..}^2}{12}\\
&=63{,}156-\frac{(870)^2}{12}=81.00
\end{aligned}
$$

The block sum of squares is found from Equation 4.33 as

$$
\begin{aligned}
SS_{\text{Blocks}}&=\frac13\sum_{j=1}^{4}y_{.j}^2-\frac{y_{..}^2}{12}\\
&=\frac13\big[(221)^2+(207)^2+(224)^2+(218)^2\big]-\frac{(870)^2}{12}\\
&=55.00
\end{aligned}
$$

To compute the treatment sum of squares adjusted for blocks, we first determine the adjusted treatment totals using Equation 4.35 as

$$
\begin{aligned}
Q_1&=(218)-\tfrac13(221+224+218)=-9/3\\
Q_2&=(214)-\tfrac13(207+224+218)=-7/3\\
Q_3&=(216)-\tfrac13(221+207+224)=-4/3\\
Q_4&=(222)-\tfrac13(221+207+218)=20/3
\end{aligned}
$$

The adjusted sum of squares for treatments is computed from Equation 4.34 as

$$
\begin{aligned}
SS_{\text{Treatments(adjusted)}}&=\frac{k\sum_{i=1}^{4}Q_i^2}{\lambda a}\\
&=\frac{3[(-9/3)^2+(-7/3)^2+(-4/3)^2+(20/3)^2]}{(2)(4)}\\
&=22.75
\end{aligned}
$$

The error sum of squares is obtained by subtraction as

$$
\begin{aligned}
SS_E&=SS_T-SS_{\text{Treatments(adjusted)}}-SS_{\text{Blocks}}\\
&=81.00-22.75-55.00=3.25
\end{aligned}
$$

The analysis of variance is shown in Table 4.24. Because the $P$-value is small, we conclude that the catalyst employed has a significant effect on the time of reaction.

**TABLE 4.24** Analysis of Variance for Example 4.5

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| Treatments (adjusted for blocks) | 22.75 | 3 | 7.58 | 11.66 | 0.0107 |
| Blocks | 55.00 | 3 | — | | |
| Error | 3.25 | 5 | 0.65 | | |
| Total | 81.00 | 11 | | | |

### PDF page 187 (book page 171)

If the factor under study is fixed, tests on individual treatment means may be of interest. If orthogonal contrasts are employed, the contrasts must be made on the **adjusted treatment totals**, the $\{Q_i\}$ rather than the $\{y_{i.}\}$. The contrast sum of squares is

$$
SS_C=\frac{k\left(\sum_{i=1}^{a}c_iQ_i\right)^2}{\lambda a\sum_{i=1}^{a}c_i^2}
$$

where $\{c_i\}$ are the contrast coefficients. Other multiple comparison methods may be used to compare all the pairs of adjusted treatment effects, which we will find in Section 4.4.2, are estimated by $\hat{\tau}_i=kQ_i/(\lambda a)$. The standard error of an adjusted treatment effect is

$$
S=\sqrt{\frac{kMS_E}{\lambda a}} \tag{4.37}
$$

In the analysis that we have described, the total sum of squares has been partitioned into an adjusted sum of squares for treatments, an unadjusted sum of squares for blocks, and an error sum of squares. Sometimes we would like to assess the block effects. To do this, we require an alternate partitioning of $SS_T$, that is,

$$
SS_T=SS_{\text{Treatments}}+SS_{\text{Blocks(adjusted)}}+SS_E
$$

Here $SS_{\text{Treatments}}$ is unadjusted. If the design is symmetric, that is, if $a=b$, a simple formula may be obtained for $SS_{\text{Blocks(adjusted)}}$. The adjusted block totals are

$$
Q'_j=y_{.j}-\frac1r\sum_{i=1}^{a}n_{ij}y_{i.}\qquad j=1,2,\ldots,b \tag{4.38}
$$

and

$$
SS_{\text{Blocks(adjusted)}}=\frac{r\sum_{j=1}^{b}(Q'_j)^2}{\lambda b} \tag{4.39}
$$

The BIBD in Example 4.5 is symmetric because $a=b=4$. Therefore,

$$
\begin{aligned}
Q'_1&=(221)-\tfrac13(218+216+222)=7/3\\
Q'_2&=(224)-\tfrac13(218+214+216)=24/3\\
Q'_3&=(207)-\tfrac13(214+216+222)=-31/3\\
Q'_4&=(218)-\tfrac13(218+214+222)=0
\end{aligned}
$$

and

$$
SS_{\text{Blocks(adjusted)}}=\frac{3[(7/3)^2+(24/3)^2+(-31/3)^2+(0)^2]}{(2)(4)}=66.08
$$

Also,

$$
SS_{\text{Treatments}}=\frac{(218)^2+(214)^2+(216)^2+(222)^2}{3}-\frac{(870)^2}{12}=11.67
$$

A summary of the analysis of variance for the symmetric BIBD is given in Table 4.25. Notice that the sums of squares associated with the mean squares in Table 4.25 do not add to the total sum of squares, that is,

$$
SS_T\ne SS_{\text{Treatments(adjusted)}}+SS_{\text{Blocks(adjusted)}}+SS_E
$$

This is a consequence of the nonorthogonality of treatments and blocks.

### PDF page 188 (book page 172)

**TABLE 4.25** Analysis of Variance for Example 4.5, Including Both Treatments and Blocks

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|
| Treatments (adjusted) | 22.75 | 3 | 7.58 | 11.66 | 0.0107 |
| Treatments (unadjusted) | 11.67 | 3 | | | |
| Blocks (unadjusted) | 55.00 | 3 | | | |
| Blocks (adjusted) | 66.08 | 3 | 22.03 | 33.90 | 0.0010 |
| Error | 3.25 | 5 | 0.65 | | |
| Total | 81.00 | 11 | | | |

**Computer Output.** There are several computer packages that will perform the analysis for a balanced incomplete block design. The SAS General Linear Models procedure is one of these and Minitab and JMP are others. The upper portion of Table 4.26 is the Minitab General Linear Model output for Example 4.5. Comparing Tables 4.26 and 4.25, we see that Minitab has computed the adjusted treatment sum of squares and the adjusted block sum of squares (they are called “Adj SS” in the Minitab output).

The lower portion of Table 4.26 is a multiple comparison analysis, using the Tukey method. Confidence intervals on the differences in all pairs of means and the Tukey test are displayed. Notice that the Tukey method would lead us to conclude that catalyst 4 is different from the other three.

#### 4.4.2 Least Squares Estimation of the Parameters

Consider estimating the treatment effects for the BIBD model. The least squares normal equations are

$$
\begin{aligned}
\mu:\quad&N\hat\mu+r\sum_{i=1}^{a}\hat\tau_i+k\sum_{j=1}^{b}\hat\beta_j=y_{..}\\
\tau_i:\quad&r\hat\mu+r\hat\tau_i+\sum_{j=1}^{b}n_{ij}\hat\beta_j=y_{i.},
\qquad i=1,2,\ldots,a\\
\beta_j:\quad&k\hat\mu+\sum_{i=1}^{a}n_{ij}\hat\tau_i+k\hat\beta_j=y_{.j},
\qquad j=1,2,\ldots,b
\end{aligned}
\tag{4.40}
$$

Imposing $\sum\hat\tau_i=\sum\hat\beta_j=0$, we find that $\hat\mu=\bar y_{..}$. Furthermore, using the equations for $\{\beta_j\}$ to eliminate the block effects from the equations for $\{\tau_i\}$, we obtain

$$
rk\hat\tau_i-r\hat\tau_i-\sum_{j=1}^{b}\sum_{\substack{p=1\\p\ne i}}^{a}
n_{ij}n_{pj}\hat\tau_p
=ky_{i.}-\sum_{j=1}^{b}n_{ij}y_{.j}
\tag{4.41}
$$

Note that the right-hand side of Equation 4.36 is $kQ_i$, where $Q_i$ is the $i$th adjusted treatment total (see Equation 4.29). Now, because $\sum_{j=1}^{b}n_{ij}n_{pj}=\lambda$ if $p\ne i$ and $\sum_{j=1}^{b}n_{pj}^2=\sum_{j=1}^{b}n_{pj}=r$ (because $n_{pj}=0$ or 1), we may rewrite Equation 4.41 as

$$
r(k-1)\hat\tau_i-\lambda\sum_{\substack{p=1\\p\ne i}}^{a}\hat\tau_p
=kQ_i,\qquad i=1,2,\ldots,a
\tag{4.42}
$$

### PDF page 189 (book page 173)

**TABLE 4.26** Minitab (General Linear Model) Analysis for Example 4.5

```text
General Linear Model
Factor        Type       Levels      Values
Catalyst      fixed           4      1 2 3 4
Block         fixed           4      1 2 3 4

Analysis of Variance for Time, using Adjusted SS for Tests
Source       DF      Seq SS      Adj SS      Adj MS         F        P
Catalyst      3      11.667      22.750       7.583     11.67    0.011
Block         3      66.083      66.083      22.028     33.89    0.001
Error         5       3.250       3.250       0.650
Total        11      81.000

Tukey 95.0% Simultaneous Confidence Intervals
Response Variable Time
All Pairwise Comparisons among Levels of Catalyst

Catalyst = 1 subtracted from:

Catalyst     Lower    Center    Upper
2          -2.327    0.2500    2.827
3          -1.952    0.6250    3.202
4           1.048    3.6250    6.202

Catalyst = 2 subtracted from:

Catalyst     Lower    Center    Upper
3          -2.202    0.3750    2.952
4           0.798    3.3750    5.952

Catalyst = 3 subtracted from:

Catalyst     Lower    Center    Upper
4          0.4228     3.000    5.577

Tukey Simultaneous Tests
Response Variable Time
All Pairwise Comparisons among Levels of Catalyst

Catalyst = 1 subtracted from:

Level          Difference       SE of                 Adjusted
Catalyst         of Means       Difference    T-Value   P-Value
2                  0.2500          0.6982       0.3581    0.9825
3                  0.6250          0.6982       0.8951    0.8085
4                  3.6250          0.6982       5.1918    0.0130

Catalyst = 2 subtracted from:

Level          Difference       SE of                 Adjusted
Catalyst         of Means       Difference    T-Value   P-Value
3                  0.3750          0.6982       0.5371    0.9462
4                  3.3750          0.6982       4.8338    0.0175

Catalyst = 3 subtracted from:

Level          Difference       SE of                 Adjusted
Catalyst         of Means       Difference    T-Value   P-Value
4                   3.000          0.6982        4.297    0.0281
```

### PDF page 190 (book page 174)

Finally, note that the constraint $\sum_{i=1}^{a}\hat\tau_i=0$ implies that $\sum_{\substack{p=1\\p\ne i}}^{a}\hat\tau_p=-\hat\tau_i$ and recall that $r(k-1)=\lambda(a-1)$ to obtain

$$
\lambda a\hat\tau_i=kQ_i,\qquad i=1,2,\ldots,a
\tag{4.43}
$$

Therefore, the least squares estimators of the treatment effects in the balanced incomplete block model are

$$
\hat\tau_i=\frac{kQ_i}{\lambda a},\qquad i=1,2,\ldots,a
\tag{4.44}
$$

As an illustration, consider the BIBD in Example 4.5. Because $Q_1=-9/3$, $Q_2=-7/3$, $Q_3=-4/3$, and $Q_4=20/3$, we obtain

$$
\hat\tau_1=\frac{3(-9/3)}{(2)(4)}=-\frac98
\qquad
\hat\tau_2=\frac{3(-7/3)}{(2)(4)}=-\frac78
$$

$$
\hat\tau_3=\frac{3(-4/3)}{(2)(4)}=-\frac48
\qquad
\hat\tau_4=\frac{3(20/3)}{(2)(4)}=\frac{20}{8}
$$

as we found in Section 4.4.1.

#### 4.4.3 Recovery of Interblock Information in the BIBD

The analysis of the BIBD given in Section 4.4.1 is usually called the intrablock analysis because block differences are eliminated and all contrasts in the treatment effects can be expressed as comparisons between observations in the same block. This analysis is appropriate regardless of whether the blocks are fixed or random. Yates (1940) noted that, if the block effects are uncorrelated random variables with zero means and variance $\sigma_\beta^2$, one may obtain additional information about the treatment effects $\tau_i$. Yates called the method of obtaining this additional information the interblock analysis.

Consider the block totals $y_{.j}$ as a collection of $b$ observations. The model for these observations [following John (1971)] is

$$
y_{.j}=k\mu+\sum_{i=1}^{a}n_{ij}\tau_i+
\left(k\beta_j+\sum_{i=1}^{a}\epsilon_{ij}\right)
\tag{4.45}
$$

where the term in parentheses may be regarded as error. The interblock estimators of $\mu$ and $\tau_i$ are found by minimizing the least squares function

$$
L=\sum_{j=1}^{b}\left(y_{.j}-k\mu-\sum_{i=1}^{a}n_{ij}\tau_i\right)^2.
$$

This yields the following least squares normal equations:

$$
\begin{aligned}
\mu:\quad&N\tilde\mu+r\sum_{i=1}^{a}\tilde\tau_i=y_{..}\\
\tau_i:\quad&kr\tilde\mu+r\tilde\tau_i+
\lambda\sum_{\substack{p=1\\p\ne i}}^{a}\tilde\tau_p
=\sum_{j=1}^{b}n_{ij}y_{.j},
\qquad i=1,2,\ldots,a
\end{aligned}
\tag{4.46}
$$

where $\tilde\mu$ and $\tilde\tau_i$ denote the interblock estimators. Imposing the constraint $\sum_{i=1}^{a}\tilde\tau_i=0$, we obtain the solutions to Equations 4.46 as

$$
\tilde\mu=\bar y_{..}
\tag{4.47}
$$

$$
\tilde\tau_i=
\frac{\displaystyle\sum_{j=1}^{b}n_{ij}y_{.j}-kr\bar y_{..}}{r-\lambda},
\qquad i=1,2,\ldots,a
\tag{4.48}
$$

### PDF page 191 (book page 175)

It is possible to show that the interblock estimators $\{\tilde\tau_i\}$ and the intrablock estimators $\{\hat\tau_i\}$ are uncorrelated.

The interblock estimators $\{\tilde\tau_i\}$ can differ from the intrablock estimators $\{\hat\tau_i\}$. For example, the interblock estimators for the BIBD in Example 4.5 are computed as follows:

$$
\tilde\tau_1=\frac{663-(3)(3)(72.50)}{3-2}=10.50
$$

$$
\tilde\tau_2=\frac{649-(3)(3)(72.50)}{3-2}=-3.50
$$

$$
\tilde\tau_3=\frac{652-(3)(3)(72.50)}{3-2}=-0.50
$$

$$
\tilde\tau_4=\frac{646-(3)(3)(72.50)}{3-2}=-6.50
$$

Note that the values of $\sum_{j=1}^{b}n_{ij}y_{.j}$ were used previously on page 169 in computing the adjusted treatment totals in the intrablock analysis.

Now suppose we wish to combine the interblock and intrablock estimators to obtain a single, unbiased, minimum variance estimate of each $\tau_i$. It is possible to show that both $\hat\tau_i$ and $\tilde\tau_i$ are unbiased and also that

$$
V(\hat\tau_i)=\frac{k(a-1)}{\lambda a^2}\sigma^2
\qquad\text{(intrablock)}
$$

and

$$
V(\tilde\tau_i)=\frac{k(a-1)}{a(r-\lambda)}(\sigma^2+k\sigma_\beta^2)
\qquad\text{(interblock)}
$$

We use a linear combination of the two estimators, say

$$
\tau_i^*=\alpha_1\hat\tau_i+\alpha_2\tilde\tau_i
\tag{4.49}
$$

to estimate $\tau_i$. For this estimation method, the minimum variance unbiased combined estimator $\tau_i^*$ should have weights $\alpha_1=u_1/(u_1+u_2)$ and $\alpha_2=u_2/(u_1+u_2)$, where $u_1=1/V(\hat\tau_i)$ and $u_2=1/V(\tilde\tau_i)$. Thus, the optimal weights are inversely proportional to the variances of $\hat\tau_i$ and $\tilde\tau_i$. This implies that the best combined estimator is

$$
\tau_i^*=
\frac{
\hat\tau_i\dfrac{k(a-1)}{a(r-\lambda)}(\sigma^2+k\sigma_\beta^2)
+\tilde\tau_i\dfrac{k(a-1)}{\lambda a^2}\sigma^2
}{
\dfrac{k(a-1)}{\lambda a^2}\sigma^2+
\dfrac{k(a-1)}{a(r-\lambda)}(\sigma^2+k\sigma_\beta^2)
},
\qquad i=1,2,\ldots,a
$$

which can be simplified to

$$
\tau_i^*=
\frac{
kQ_i(\sigma^2+k\sigma_\beta^2)+
\left(\displaystyle\sum_{j=1}^{b}n_{ij}y_{.j}-kr\bar y_{..}\right)\sigma^2
}{
(r-\lambda)\sigma^2+\lambda a(\sigma^2+k\sigma_\beta^2)
},
\qquad i=1,2,\ldots,a
\tag{4.50}
$$

Unfortunately, Equation 4.50 cannot be used to estimate the $\tau_i$ because the variances $\sigma^2$ and $\sigma_\beta^2$ are unknown. The usual approach is to estimate $\sigma^2$ and $\sigma_\beta^2$ from the data and replace these parameters in Equation 4.50 by the estimates. The estimate usually taken for $\sigma^2$ is the error mean square from the intrablock analysis of variance, or the **intrablock error**. Thus,

$$
\hat\sigma^2=MS_E
$$

### PDF page 192 (book page 176)

The estimate of $\sigma_\beta^2$ is found from the mean square for blocks adjusted for treatments. In general, for a balanced incomplete block design, this mean square is

$$
MS_{\text{Blocks(adjusted)}}=
\frac{
\left(
\dfrac{k\displaystyle\sum_{i=1}^{a}Q_i^2}{\lambda a}
+\displaystyle\sum_{j=1}^{b}\frac{y_{.j}^2}{k}
-\displaystyle\sum_{i=1}^{a}\frac{y_{i.}^2}{r}
\right)
}{b-1}
\tag{4.51}
$$

and its expected value [which is derived in Graybill (1961)] is

$$
E[MS_{\text{Blocks(adjusted)}}]
=\sigma^2+\frac{a(r-1)}{b-1}\sigma_\beta^2.
$$

Thus, if $MS_{\text{Blocks(adjusted)}}>MS_E$, the estimate of $\sigma_\beta^2$ is

$$
\hat\sigma_\beta^2=
\frac{[MS_{\text{Blocks(adjusted)}}-MS_E](b-1)}{a(r-1)}
\tag{4.52}
$$

and if $MS_{\text{Blocks(adjusted)}}\leq MS_E$, we set $\hat\sigma_\beta^2=0$. This results in the combined estimator

$$
\tau_i^*=
\begin{cases}
\dfrac{
kQ_i(\hat\sigma^2+k\hat\sigma_\beta^2)
+\left(\displaystyle\sum_{j=1}^{b}n_{ij}y_{.j}-kr\bar y_{..}\right)\hat\sigma^2
}{
(r-\lambda)\hat\sigma^2+\lambda a(\hat\sigma^2+k\hat\sigma_\beta^2)
},
& \hat\sigma_\beta^2>0 \tag{4.53a}\\[1.2em]
\dfrac{y_{i.}-(1/a)y_{..}}{r},
& \hat\sigma_\beta^2=0 \tag{4.53b}
\end{cases}
$$

We now compute the combined estimates for the data in Example 4.5. From Table 4.25 we obtain $\hat\sigma^2=MS_E=0.65$ and $MS_{\text{Blocks(adjusted)}}=22.03$. (Note that in computing $MS_{\text{Blocks(adjusted)}}$ we make use of the fact that this is a symmetric design. In general, we must use Equation 4.51. Because $MS_{\text{Blocks(adjusted)}}>MS_E$, we use Equation 4.52 to estimate $\sigma_\beta^2$ as

$$
\hat\sigma_\beta^2=\frac{(22.03-0.65)(3)}{4(3-1)}=8.02
$$

Therefore, we may substitute $\hat\sigma^2=0.65$ and $\hat\sigma_\beta^2=8.02$ into Equation 4.53a to obtain the combined estimates listed below. For convenience, the intrablock and interblock estimates are also given. In this example, the combined estimates are close to the intrablock estimates because the variance of the interblock estimates is relatively large.

| Parameter | Intrablock Estimate | Interblock Estimate | Combined Estimate |
|---|---:|---:|---:|
| $\tau_1$ | $-1.12$ | $10.50$ | $-1.09$ |
| $\tau_2$ | $-0.88$ | $-3.50$ | $-0.88$ |
| $\tau_3$ | $-0.50$ | $-0.50$ | $-0.50$ |
| $\tau_4$ | $2.50$ | $-6.50$ | $2.47$ |

### PDF page 193 (book page 177)

## 4.5 Problems

**4.1.** The ANOVA from a randomized complete block experiment output is shown below.

| Source | DF | SS | MS | $F$ | $P$ |
|---|---:|---:|---:|---:|---:|
| Treatment | 4 | 1010.56 | ? | 29.84 | ? |
| Block | ? | ? | 64.765 | ? | ? |
| Error | 20 | 169.33 | ? | | |
| Total | 29 | 1503.71 | | | |

(a) Fill in the blanks. You may give bounds on the $P$-value.

(b) How many blocks were used in this experiment?

(c) What conclusions can you draw?

**4.2.** Consider the single-factor completely randomized single factor experiment shown in Problem 3.4. Suppose that this experiment had been conducted in a randomized complete block design, and that the sum of squares for blocks was 80.00. Modify the ANOVA for this experiment to show the correct analysis for the randomized complete block experiment.

**4.3.** A chemist wishes to test the effect of four chemical agents on the strength of a particular type of cloth. Because there might be variability from one bolt to another, the chemist decides to use a randomized block design, with the bolts of cloth considered as blocks. She selects five bolts and applies all four chemicals in random order to each bolt. The resulting tensile strengths follow. Analyze the data from this experiment (use $\alpha=0.05$) and draw appropriate conclusions.

| Chemical | Bolt 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| 1 | 73 | 68 | 74 | 71 | 67 |
| 2 | 73 | 67 | 75 | 72 | 70 |
| 3 | 75 | 68 | 78 | 73 | 68 |
| 4 | 73 | 71 | 75 | 75 | 69 |

**4.4.** Three different washing solutions are being compared to study their effectiveness in retarding bacteria growth in 5-gallon milk containers. The analysis is done in a laboratory, and only three trials can be run on any day. Because days could represent a potential source of variability, the experimenter decides to use a randomized block design. Observations are taken for four days, and the data are shown here. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

| Solution | Day 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| 1 | 13 | 22 | 18 | 39 |
| 2 | 16 | 24 | 17 | 44 |
| 3 | 5 | 4 | 1 | 22 |

**4.5.** Plot the mean tensile strengths observed for each chemical type in Problem 4.3 and compare them to an appropriately scaled $t$ distribution. What conclusions would you draw from this display?

**4.6.** Plot the average bacteria counts for each solution in Problem 4.4 and compare them to a scaled $t$ distribution. What conclusions can you draw?

**4.7.** Consider the hardness testing experiment described in Section 4.1. Suppose that the experiment was conducted as described and that the following Rockwell C-scale data (coded by subtracting 40 units) obtained:

| Tip | Coupon 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| 1 | 9.3 | 9.4 | 9.6 | 10.0 |
| 2 | 9.4 | 9.3 | 9.8 | 9.9 |
| 3 | 9.2 | 9.4 | 9.5 | 9.7 |
| 4 | 9.7 | 9.6 | 10.0 | 10.2 |

(a) Analyze the data from this experiment.

(b) Use the Fisher LSD method to make comparisons among the four tips to determine specifically which tips differ in mean hardness readings.

(c) Analyze the residuals from this experiment.

**4.8.** A consumer products company relies on direct mail marketing pieces as a major component of its advertising campaigns. The company has three different designs for a new brochure and wants to evaluate their effectiveness, as there are substantial differences in costs between the three designs. The company decides to test the three designs by mailing 5000 samples of each to potential customers in four different regions of the country. Since there are known regional differences in the customer base, regions are considered as blocks. The number of responses to each mailing is as follows.

| Design | NE | NW | SE | SW |
|---|---:|---:|---:|---:|
| 1 | 250 | 350 | 219 | 375 |
| 2 | 400 | 525 | 390 | 580 |
| 3 | 275 | 340 | 200 | 310 |

(a) Analyze the data from this experiment.

(b) Use the Fisher LSD method to make comparisons among the three designs to determine specifically which designs differ in the mean response rate.

(c) Analyze the residuals from this experiment.

### PDF page 194 (book page 178)

**4.9.** The effect of three different lubricating oils on fuel economy in diesel truck engines is being studied. Fuel economy is measured using brake-specific fuel consumption after the engine has been running for 15 minutes. Five different truck engines are available for the study, and the experimenters conduct the following randomized complete block design.

| Oil | Truck 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| 1 | 0.500 | 0.634 | 0.487 | 0.329 | 0.512 |
| 2 | 0.535 | 0.675 | 0.520 | 0.435 | 0.540 |
| 3 | 0.513 | 0.595 | 0.488 | 0.400 | 0.510 |

(a) Analyze the data from this experiment.

(b) Use the Fisher LSD method to make comparisons among the three lubricating oils to determine specifically which oils differ in brake-specific fuel consumption.

(c) Analyze the residuals from this experiment.

**4.10.** An article in the *Fire Safety Journal* (“The Effect of Nozzle Design on the Stability and Performance of Turbulent Water Jets,” Vol. 4, August 1981) describes an experiment in which a shape factor was determined for several different nozzle designs at six levels of jet efflux velocity. Interest focused on potential differences between nozzle designs, with velocity considered as a nuisance variable. The data are shown below:

| Nozzle Design | Jet Efflux Velocity (m/s): 11.73 | 14.37 | 16.59 | 20.43 | 23.46 | 28.74 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0.78 | 0.80 | 0.81 | 0.75 | 0.77 | 0.78 |
| 2 | 0.85 | 0.85 | 0.92 | 0.86 | 0.81 | 0.83 |
| 3 | 0.93 | 0.92 | 0.95 | 0.89 | 0.89 | 0.83 |
| 4 | 1.14 | 0.97 | 0.98 | 0.88 | 0.86 | 0.83 |
| 5 | 0.97 | 0.86 | 0.78 | 0.76 | 0.76 | 0.75 |

(a) Does nozzle design affect the shape factor? Compare the nozzles with a scatter plot and with an analysis of variance, using $\alpha=0.05$.

(b) Analyze the residuals from this experiment.

(c) Which nozzle designs are different with respect to shape factor? Draw a graph of the average shape factor for each nozzle type and compare this to a scaled $t$ distribution. Compare the conclusions that you draw from this plot to those from Duncan’s multiple range test.

**4.11.** An article in *Communications of the ACM* (Vol. 30, No. 5, 1987) studied different algorithms for estimating software development costs. Six algorithms were applied to several different software development projects and the percent error in estimating the development cost was observed. Some of the data from this experiment is shown in the table below.

(a) Do the algorithms differ in their mean cost estimation accuracy?

(b) Analyze the residuals from this experiment.

(c) Which algorithm would you recommend for use in practice?

| Algorithm | Project 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| 1(SLIM | 1244 | 21 | 82 | 2221 | 905 | 839 |
| 2(COCOMO-A) | 281 | 129 | 396 | 1306 | 336 | 910 |
| 3(COCOMO-R) | 220 | 84 | 458 | 543 | 300 | 794 |
| 4(COCONO-C) | 225 | 83 | 425 | 552 | 291 | 826 |
| 5(FUNCTION POINTS) | 19 | 11 | $-34$ | 121 | 15 | 103 |
| 6(ESTIMALS) | $-20$ | 35 | $-53$ | 170 | 104 | 199 |

**4.12.** An article in *Nature Genetics* (2003, Vol. 34, pp. 85–90) “Treatment-Specific Changes in Gene Expression Discriminate in vivo Drug Response in Human Leukemia Cells” studied gene expression as a function of different treatments for leukemia. Three treatment groups are: mercaptopurine (MP) only; low-dose methotrexate (LDMTX) and MP; and high-dose methotrexate (HDMTX) and MP. Each group contained ten subjects. The responses from a specific gene are shown in the table below.

(a) Is there evidence to support the claim that the treatment means differ?

(b) Check the normality assumption. Can we assume these samples are from normal populations?

(c) Take the logarithm of the raw data. Is there evidence to support the claim that the treatment means differ for the transformed data?

(d) Analyze the residuals from the transformed data and comment on model adequacy.

| Treatments | Observations |
|---|---|
| MP ONLY | 334.5, 31.6, 701, 41.2, 61.2, 69.6, 67.5, 66.6, 120.7, 881.9 |
| MP + HDMTX | 919.4, 404.2, 1024.8, 54.1, 62.8, 671.6, 882.1, 354.2, 321.9, 91.1 |
| MP + LDMTX | 108.4, 26.1, 240.8, 191.1, 69.7, 242.8, 62.7, 396.9, 23.6, 290.4 |

**4.13.** Consider the ratio control algorithm experiment described in Section 3.8. The experiment was actually conducted as a randomized block design, where six time periods were selected as the blocks, and all four ratio control algorithms were tested in each time period. The average cell voltage and the standard deviation of voltage (shown in parentheses) for each cell are as follows:

### PDF page 195 (book page 179)

| Ratio Control Algorithm | Time Period 1 | 2 | 3 |
|---|---:|---:|---:|
| 1 | 4.93 (0.05) | 4.86 (0.04) | 4.75 (0.05) |
| 2 | 4.85 (0.04) | 4.91 (0.02) | 4.79 (0.03) |
| 3 | 4.83 (0.09) | 4.88 (0.13) | 4.90 (0.11) |
| 4 | 4.89 (0.03) | 4.77 (0.04) | 4.94 (0.05) |

| Ratio Control Algorithm | Time Period 4 | 5 | 6 |
|---|---:|---:|---:|
| 1 | 4.95 (0.06) | 4.79 (0.03) | 4.88 (0.05) |
| 2 | 4.85 (0.05) | 4.75 (0.03) | 4.85 (0.02) |
| 3 | 4.75 (0.15) | 4.82 (0.08) | 4.90 (0.12) |
| 4 | 4.86 (0.05) | 4.79 (0.03) | 4.76 (0.02) |

(a) Analyze the average cell voltage data. (Use $\alpha=0.05$.) Does the choice of ratio control algorithm affect the average cell voltage?

(b) Perform an appropriate analysis on the standard deviation of voltage. (Recall that this is called “pot noise.”) Does the choice of ratio control algorithm affect the pot noise?

(c) Conduct any residual analyses that seem appropriate.

(d) Which ratio control algorithm would you select if your objective is to reduce both the average cell voltage and the pot noise?

**4.14.** An aluminum master alloy manufacturer produces grain refiners in ingot form. The company produces the product in four furnaces. Each furnace is known to have its own unique operating characteristics, so any experiment run in the foundry that involves more than one furnace will consider furnaces as a nuisance variable. The process engineers suspect that stirring rate affects the grain size of the product. Each furnace can be run at four different stirring rates. A randomized block design is run for a particular refiner, and the resulting grain size data is as follows.

| Stirring Rate (rpm) | Furnace 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| 5 | 8 | 4 | 5 | 6 |
| 10 | 14 | 5 | 6 | 9 |
| 15 | 14 | 6 | 9 | 2 |
| 20 | 17 | 9 | 3 | 6 |

(a) Is there any evidence that stirring rate affects grain size?

(b) Graph the residuals from this experiment on a normal probability plot. Interpret this plot.

(c) Plot the residuals versus furnace and stirring rate. Does this plot convey any useful information?

(d) What should the process engineers recommend concerning the choice of stirring rate and furnace for this particular grain refiner if small grain size is desirable?

**4.15.** Analyze the data in Problem 4.4 using the general regression significance test.

**4.16.** Assuming that chemical types and bolts are fixed, estimate the model parameters $\tau_i$ and $\beta_j$ in Problem 4.3.

**4.17.** Draw an operating characteristic curve for the design in Problem 4.4. Does the test seem to be sensitive to small differences in the treatment effects?

**4.18.** Suppose that the observation for chemical type 2 and bolt 3 is missing in Problem 4.3. Analyze the problem by estimating the missing value. Perform the exact analysis and compare the results.

**4.19.** Consider the hardness testing experiment in Problem 4.7. Suppose that the observation for tip 2 in coupon 3 is missing. Analyze the problem by estimating the missing value.

**4.20.** ***Two missing values in a randomized block.*** Suppose that in Problem 4.3 the observations for chemical type 2 and bolt 3 and chemical type 4 and bolt 4 are missing.

(a) Analyze the design by iteratively estimating the missing values, as described in Section 4.1.3.

(b) Differentiate $SS_E$ with respect to the two missing values, equate the results to zero, and solve for estimates of the missing values. Analyze the design using these two estimates of the missing values.

(c) Derive general formulas for estimating two missing values when the observations are in *different* blocks.

(d) Derive general formulas for estimating two missing values when the observations are in the *same* block.

**4.21.** An industrial engineer is conducting an experiment on eye focus time. He is interested in the effect of the distance of the object from the eye on the focus time. Four different distances are of interest. He has five subjects available for the experiment. Because there may be differences among individuals, he decides to conduct the experiment in a randomized block design. The data obtained follow. Analyze the data from this experiment (use $\alpha=0.05$) and draw appropriate conclusions.

| Distance (ft) | Subject 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| 4 | 10 | 6 | 6 | 6 | 6 |
| 6 | 7 | 6 | 6 | 1 | 6 |
| 8 | 5 | 3 | 3 | 2 | 5 |
| 10 | 6 | 4 | 4 | 2 | 3 |

### PDF page 196 (book page 180)

**4.22.** The effect of five different ingredients ($A$, $B$, $C$, $D$, $E$) on the reaction time of a chemical process is being studied. Each batch of new material is only large enough to permit five runs to be made. Furthermore, each run requires approximately $1\frac{1}{2}$ hours, so only five runs can be made in one day. The experimenter decides to run the experiment as a Latin square so that day and batch effects may be systematically controlled. She obtains the data that follow. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

| Batch | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---:|---:|---:|---:|---:|---:|
| 1 | $A=8$ | $B=7$ | $D=1$ | $C=7$ | $E=3$ |
| 2 | $C=11$ | $E=2$ | $A=7$ | $D=3$ | $B=8$ |
| 3 | $B=4$ | $A=9$ | $C=10$ | $E=1$ | $D=5$ |
| 4 | $D=6$ | $C=8$ | $E=6$ | $B=6$ | $A=10$ |
| 5 | $E=4$ | $D=2$ | $B=3$ | $A=8$ | $C=8$ |

**4.23.** An industrial engineer is investigating the effect of four assembly methods ($A$, $B$, $C$, $D$) on the assembly time for a color television component. Four operators are selected for the study. Furthermore, the engineer knows that each assembly method produces such fatigue that the time required for the last assembly may be greater than the time required for the first, regardless of the method. That is, a trend develops in the required assembly time. To account for this source of variability, the engineer uses the Latin square design shown below. Analyze the data from this experiment ($\alpha=0.05$) and draw appropriate conclusions.

| Order of Assembly | Operator 1 | Operator 2 | Operator 3 | Operator 4 |
|---:|---:|---:|---:|---:|
| 1 | $C=10$ | $D=14$ | $A=7$ | $B=8$ |
| 2 | $B=7$ | $C=18$ | $D=11$ | $A=8$ |
| 3 | $A=5$ | $B=10$ | $C=11$ | $D=9$ |
| 4 | $D=10$ | $A=10$ | $B=12$ | $C=14$ |

**4.24.** Consider the randomized complete block design in Problem 4.4. Assume that the days are random. Estimate the block variance component.

**4.25.** Consider the randomized complete block design in Problem 4.7. Assume that the coupons are random. Estimate the block variance component.

**4.26.** Consider the randomized complete block design in Problem 4.9. Assume that the trucks are random. Estimate the block variance component.

**4.27.** Consider the randomized complete block design in Problem 4.11. Assume that the software projects that were used as blocks are random. Estimate the block variance component.

**4.28.** Consider the gene expression experiment in Problem 4.12. Assume that the subjects used in this experiment are random. Estimate the block variance component.

**4.29.** Suppose that in Problem 4.20 the observation from batch 3 on day 4 is missing. Estimate the missing value and perform the analysis using the value.

**4.30.** Consider a $p\times p$ Latin square with rows ($\alpha_i$), columns ($\beta_k$), and treatments ($\tau_j$) fixed. Obtain least squares estimates of the model parameters $\alpha_i$, $\beta_k$, and $\tau_j$.

**4.31.** Derive the missing value formula (Equation 4.27) for the Latin square design.

**4.32.** ***Designs involving several Latin squares.*** [See Cochran and Cox (1957), John (1971).] The $p\times p$ Latin square contains only $p$ observations for each treatment. To obtain more replications the experimenter may use several squares, say $n$. It is immaterial whether the squares used are the same or different. The appropriate model is

$$
y_{ijkh}=\mu+\rho_h+\alpha_{i(h)}+\tau_j+\beta_{k(h)}
          +(\tau\rho)_{jh}+\epsilon_{ijkh}
\begin{cases}
i=1,2,\ldots,p\\
j=1,2,\ldots,p\\
k=1,2,\ldots,p\\
h=1,2,\ldots,n
\end{cases}
$$

where $y_{ijkh}$ is the observation on treatment $j$ in row $i$ and column $k$ of the $h$th square. Note that $\alpha_{i(h)}$ and $\beta_{k(h)}$ are the row and column effects in the $h$th square, $\rho_h$ is the effect of the $h$th square, and $(\tau\rho)_{jh}$ is the interaction between treatments and squares.

(a) Set up the normal equations for this model, and solve for estimates of the model parameters. Assume that appropriate side conditions on the parameters are $\sum_h\hat{\rho}_h=0$, $\sum_i\hat{\alpha}_{i(h)}=0$, and $\sum_k\hat{\beta}_{k(h)}=0$ for each $h$, $\sum_j\hat{\tau}_j=0$, $\sum_j(\widehat{\tau\rho})_{jh}=0$ for each $h$, and $\sum_h(\widehat{\tau\rho})_{jh}=0$ for each $j$.

(b) Write down the analysis of variance table for this design.

**4.33.** Discuss how the operating characteristics curves in the Appendix may be used with the Latin square design.

**4.34.** Suppose that in Problem 4.22 the data taken on day 5 were incorrectly analyzed and had to be discarded. Develop an appropriate analysis for the remaining data.

**4.35.** The yield of a chemical process was measured using five batches of raw material, five acid concentrations, five standing times ($A$, $B$, $C$, $D$, $E$), and five catalyst concentrations ($\alpha$, $\beta$, $\gamma$, $\delta$, $\epsilon$). The Graeco-Latin square that follows was used. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

### PDF page 197 (book page 181)

| Batch | Acid Concentration 1 | Acid Concentration 2 | Acid Concentration 3 |
|---:|---:|---:|---:|
| 1 | $A\alpha=26$ | $B\beta=16$ | $C\gamma=19$ |
| 2 | $B\gamma=18$ | $C\delta=21$ | $D\epsilon=18$ |
| 3 | $C\epsilon=20$ | $D\alpha=12$ | $E\beta=16$ |
| 4 | $D\beta=15$ | $E\gamma=15$ | $A\delta=22$ |
| 5 | $E\delta=10$ | $A\epsilon=24$ | $B\alpha=17$ |

| Batch | Acid Concentration 4 | Acid Concentration 5 |
|---:|---:|---:|
| 1 | $D\delta=16$ | $E\epsilon=13$ |
| 2 | $E\alpha=11$ | $A\beta=21$ |
| 3 | $A\gamma=25$ | $B\delta=13$ |
| 4 | $B\epsilon=14$ | $C\alpha=17$ |
| 5 | $C\beta=17$ | $D\gamma=14$ |

**4.36.** Suppose that in Problem 4.23 the engineer suspects that the workplaces used by the four operators may represent an additional source of variation. A fourth factor, workplace ($\alpha$, $\beta$, $\gamma$, $\delta$) may be introduced and another experiment conducted, yielding the Graeco-Latin square that follows. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

| Order of Assembly | Operator 1 | Operator 2 | Operator 3 | Operator 4 |
|---:|---:|---:|---:|---:|
| 1 | $C\beta=11$ | $B\gamma=10$ | $D\delta=14$ | $A\alpha=8$ |
| 2 | $B\alpha=8$ | $C\delta=12$ | $A\gamma=10$ | $D\beta=12$ |
| 3 | $A\delta=9$ | $D\alpha=11$ | $B\beta=7$ | $C\gamma=15$ |
| 4 | $D\gamma=9$ | $A\beta=8$ | $C\alpha=18$ | $B\delta=6$ |

**4.37.** Construct a $5\times5$ hypersquare for studying the effects of five factors. Exhibit the analysis of variance table for this design.

**4.38.** Consider the data in Problems 4.23 and 4.36. Suppressing the Greek letters in Problem 4.36, analyze the data using the method developed in Problem 4.32.

**4.39.** Consider the randomized block design with one missing value in Problem 4.19. Analyze this data by using the exact analysis of the missing value problem discussed in Section 4.1.4. Compare your results to the approximate analysis of these data given from Problem 4.19.

**4.40.** An engineer is studying the mileage performance characteristics of five types of gasoline additives. In the road test he wishes to use cars as blocks; however, because of a time constraint, he must use an incomplete block design. He runs the balanced design with the five blocks that follow. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

| Additive | Car 1 | Car 2 | Car 3 | Car 4 | Car 5 |
|---:|---:|---:|---:|---:|---:|
| 1 |  | 17 | 14 | 13 | 12 |
| 2 | 14 | 14 |  | 13 | 10 |
| 3 | 12 |  | 13 | 12 | 9 |
| 4 | 13 | 11 | 11 | 12 |  |
| 5 | 11 | 12 | 10 |  | 8 |

**4.41.** Construct a set of orthogonal contrasts for the data in Problem 4.33. Compute the sum of squares for each contrast.

**4.42.** Seven different hardwood concentrations are being studied to determine their effect on the strength of the paper produced. However, the pilot plant can only produce three runs each day. As days may differ, the analyst uses the balanced incomplete block design that follows. Analyze the data from this experiment (use $\alpha=0.05$) and draw conclusions.

| Hardwood Concentration (%) | Day 1 | Day 2 | Day 3 | Day 4 |
|---:|---:|---:|---:|---:|
| 2 |  | 114 |  |  |
| 4 |  | 126 | 120 |  |
| 6 |  | 137 |  | 117 |
| 8 | 141 |  | 129 | 149 |
| 10 | 145 |  |  | 150 |
| 12 |  | 120 |  |  |
| 14 |  |  |  | 136 |

| Hardwood Concentration (%) | Day 5 | Day 6 | Day 7 |
|---:|---:|---:|---:|
| 2 | 120 |  | 117 |
| 4 |  | 119 |  |
| 6 |  |  | 134 |
| 8 |  |  |  |
| 10 | 143 |  |  |
| 12 | 118 | 123 |  |
| 14 |  | 130 | 127 |

**4.43.** Analyze the data in Example 4.5 using the general regression significance test.

**4.44.** Prove that $k\left(\sum_{i=1}^{a}Q_i^2/(\lambda a)\right)$ is the adjusted sum of squares for treatments in a BIBD.

### PDF page 198 (book page 182)

**4.45.** An experimenter wishes to compare four treatments in blocks of two runs. Find a BIBD for this experiment with six blocks.

**4.46.** An experimenter wishes to compare eight treatments in blocks of four runs. Find a BIBD with 14 blocks and $\lambda=3$.

**4.47.** Perform the interblock analysis for the design in Problem 4.40.

**4.48.** Perform the interblock analysis for the design in Problem 4.42.

**4.49.** Verify that a BIBD with the parameters $a=8$, $r=8$, $k=4$, and $b=16$ does not exist.

**4.50.** Show that the variance of the intrablock estimators $\hat{\tau}_i$ is $k(a-1)\sigma^2/(\lambda a^2)$.

**4.51.** ***Extended incomplete block designs.*** Occasionally, the block size obeys the relationship $a<k<2a$. An extended incomplete block design consists of a single replicate of each treatment in each block along with an incomplete block design with $k^*=k-a$. In the balanced case, the incomplete block design will have parameters $k^*=k-a$, $r^*=r-b$, and $\lambda^*$. Write out the statistical analysis. (*Hint:* In the extended incomplete block design, we have $\lambda=2r-b+\lambda^*$.)

**4.52.** Suppose that a single-factor experiment with five levels of the factor has been conducted. There are three replicates and the experiment has been conducted as a complete randomized design. If the experiment had been conducted in blocks, the pure error degrees of freedom would be reduced by (choose the correct answer):

(a) 3  
(b) 5  
(c) 2  
(d) 4  
(e) None of the above

**4.53.** Physics graduate student Laura Van Ertia has conducted a complete randomized design with a single factor, hoping to solve the mystery of the unified theory and complete her dissertation. The results of this experiment are summarized in the following ANOVA display:

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Factor | — | — | 14.18 | — |
| Error | — | 37.75 | — | |
| Total | 23 | 108.63 | | |

Answer the following questions about this experiment.

(a) The sum of squares for the factor is ______.  
(b) The number of degrees of freedom for the single factor in the experiment is ______.  
(c) The number of degrees of freedom for error is ______.  
(d) The mean square for error is ______.  
(e) The value of the test statistic is ______.  
(f) If the significance level is 0.05, your conclusions are not to reject the null hypothesis. (Yes or No)  
(g) An upper bound on the $P$-value for the test statistic is ______.  
(h) A lower bound on the $P$-value for the test statistic is ______.  
(i) Laura used ______ levels of the factor in this experiment.  
(j) Laura replicated this experiment ______ times.  
(k) Suppose that Laura had actually conducted this experiment as a randomized complete block design and the sum of squares for blocks was 12. Reconstruct the ANOVA display above to reflect this new situation. How much has blocking reduced the estimate of experimental error?

**4.54.** Consider the direct mail marketing experiment in Problem 4.8. Suppose that this experiment had been run as a complete randomized design, ignoring potential regional differences, but that exactly the same data was obtained. Reanalyze the experiment under this new assumption. What difference would ignoring blocking have on the results and conclusions?
