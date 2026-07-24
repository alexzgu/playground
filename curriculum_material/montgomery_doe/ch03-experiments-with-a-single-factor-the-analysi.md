# Chapter 3 — Experiments with a Single Factor: The Analysis of Variance
*(PDF pages 81–154; book pages 65–78)*

*⚠ In progress: 14 of 74 pages transcribed; missing PDF pages 95–154.*

### PDF page 81 (book page 65)

# Chapter 3 — Experiments with a Single Factor: The Analysis of Variance

**CHAPTER OUTLINE**

- 3.1 AN EXAMPLE
- 3.2 THE ANALYSIS OF VARIANCE
- 3.3 ANALYSIS OF THE FIXED EFFECTS MODEL
  - 3.3.1 Decomposition of the Total Sum of Squares
  - 3.3.2 Statistical Analysis
  - 3.3.3 Estimation of the Model Parameters
  - 3.3.4 Unbalanced Data
- 3.4 MODEL ADEQUACY CHECKING
  - 3.4.1 The Normality Assumption
  - 3.4.2 Plot of Residuals in Time Sequence
  - 3.4.3 Plot of Residuals Versus Fitted Values
  - 3.4.4 Plots of Residuals Versus Other Variables
- 3.5 PRACTICAL INTERPRETATION OF RESULTS
  - 3.5.1 A Regression Model
  - 3.5.2 Comparisons Among Treatment Means
  - 3.5.3 Graphical Comparisons of Means
  - 3.5.4 Contrasts
  - 3.5.5 Orthogonal Contrasts
  - 3.5.6 Scheffé’s Method for Comparing All Contrasts
  - 3.5.7 Comparing Pairs of Treatment Means
  - 3.5.8 Comparing Treatment Means with a Control
- 3.6 SAMPLE COMPUTER OUTPUT
- 3.7 DETERMINING SAMPLE SIZE
  - 3.7.1 Operating Characteristic Curves
  - 3.7.2 Specifying a Standard Deviation Increase
  - 3.7.3 Confidence Interval Estimation Method
- 3.8 OTHER EXAMPLES OF SINGLE-FACTOR EXPERIMENTS
  - 3.8.1 Chocolate and Cardiovascular Health
  - 3.8.2 A Real Economy Application of a Designed Experiment
  - 3.8.3 Analyzing Dispersion Effects
- 3.9 THE RANDOM EFFECTS MODEL
  - 3.9.1 A Single Random Factor
  - 3.9.2 Analysis of Variance for the Random Model
  - 3.9.3 Estimating the Model Parameters
- 3.10 THE REGRESSION APPROACH TO THE ANALYSIS OF VARIANCE
  - 3.10.1 Least Squares Estimation of the Model Parameters
  - 3.10.2 The General Regression Significance Test
- 3.11 NONPARAMETRIC METHODS IN THE ANALYSIS OF VARIANCE
  - 3.11.1 The Kruskal–Wallis Test
  - 3.11.2 General Comments on the Rank Transformation
- SUPPLEMENTAL MATERIAL FOR CHAPTER 3
  - S3.1 The Definition of Factor Effects
  - S3.2 Expected Mean Squares
  - S3.3 Confidence Interval for $\sigma^2$
  - S3.4 Simultaneous Confidence Intervals on Treatment Means
  - S3.5 Regression Models for a Quantitative Factor
  - S3.6 More about Estimable Functions
  - S3.7 Relationship Between Regression and Analysis of Variance

The supplemental material is on the textbook website www.wiley.com/college/montgomery.

### PDF page 82 (book page 66)

In Chapter 2, we discussed methods for comparing two conditions or treatments. For example, the Portland cement tension bond experiment involved two different mortar formulations. Another way to describe this experiment is as a single-factor experiment with two levels of the factor, where the factor is mortar formulation and the two levels are the two different formulation methods. Many experiments of this type involve more than two levels of the factor. This chapter focuses on methods for the design and analysis of single-factor experiments with an arbitrary number $a$ levels of the factor (or $a$ treatments). We will assume that the experiment has been completely randomized.

**3.1 An Example**

In many integrated circuit manufacturing steps, wafers are completely coated with a layer of material such as silicon dioxide or a metal. The unwanted material is then selectively removed by etching through a mask, thereby creating circuit patterns, electrical interconnects, and areas in which diffusions or metal depositions are to be made. A plasma etching process is widely used for this operation, particularly in small geometry applications. Figure 3.1 shows the important features of a typical single-wafer etching tool. Energy is supplied by a radio-frequency (RF) generator causing plasma to be generated in the gap between the electrodes. The chemical species in the plasma are determined by the particular gases used. Fluorocarbons, such as $\mathrm{CF_4}$ (tetrafluoromethane) or $\mathrm{C_2F_6}$ (hexafluoroethane), are often used in plasma etching, but other gases and mixtures of gases are relatively common, depending on the application.

An engineer is interested in investigating the relationship between the RF power setting and the etch rate for this tool. The objective of an experiment like this is to model the relationship between etch rate and RF power, and to specify the power setting that will give a desired target etch rate. She is interested in a particular gas ($\mathrm{C_2F_6}$) and gap (0.80 cm) and wants to test four levels of RF power: 160, 180, 200, and 220 W. She decided to test five wafers at each level of RF power.

This is an example of a single-factor experiment with $a = 4$ **levels** of the factor and $n = 5$ **replicates**. The 20 runs should be made in random order. A very efficient way to generate the run order is to enter the 20 runs in a spreadsheet (Excel), generate a column of random numbers using the RAND ( ) function, and then sort by that column.

**FIGURE 3.1** A single-wafer plasma etching tool *[Figure: schematic diagram of the etching tool. At upper left, three cylinders labeled "Gas supply" feed lines up into a box labeled "Gas control panel," from which a line runs down (arrow) into the top of a rectangular process chamber. Inside the chamber, a horizontal upper plate labeled "Anode" sits above a shaded rectangle labeled "Wafer" resting on a lower plate labeled "Cathode." A box at upper right labeled "RF generator" is connected by a line to the chamber's electrode. From the bottom of the chamber a line passes through a small box labeled "Valve" to a box labeled "Vacuum pump," which exhausts to the right (arrow).]*

### PDF page 83 (book page 67)

Suppose that the test sequence obtained from this process is given as below:

| Test Sequence | Excel Random Number (Sorted) | Power |
|---:|---:|---:|
| 1 | 12417 | 200 |
| 2 | 18369 | 220 |
| 3 | 21238 | 220 |
| 4 | 24621 | 160 |
| 5 | 29337 | 160 |
| 6 | 32318 | 180 |
| 7 | 36481 | 200 |
| 8 | 40062 | 160 |
| 9 | 43289 | 180 |
| 10 | 49271 | 200 |
| 11 | 49813 | 220 |
| 12 | 52286 | 220 |
| 13 | 57102 | 160 |
| 14 | 63548 | 160 |
| 15 | 67710 | 220 |
| 16 | 71834 | 180 |
| 17 | 77216 | 180 |
| 18 | 84675 | 180 |
| 19 | 89323 | 200 |
| 20 | 94037 | 200 |

This randomized test sequence is necessary to prevent the effects of unknown nuisance variables, perhaps varying out of control during the experiment, from contaminating the results. To illustrate this, suppose that we were to run the 20 test wafers in the original nonrandomized order (that is, all five 160 W power runs are made first, all five 180 W power runs are made next, and so on). If the etching tool exhibits a warm-up effect such that the longer it is on, the lower the observed etch rate readings will be, the warm-up effect will potentially contaminate the data and destroy the validity of the experiment.

Suppose that the engineer runs the experiment that we have designed in the random order. The observations that she obtains on etch rate are shown in Table 3.1.

It is always a good idea to examine experimental data **graphically**. Figure 3.2*a* presents **box plots** for etch rate at each level of RF power, and Figure 3.2*b* a **scatter diagram** of etch rate versus RF power. Both graphs indicate that etch rate increases as the power setting increases. There

**TABLE 3.1**
**Etch Rate Data (in Å/min) from the Plasma Etching Experiment**

*(Columns 1–5 fall under the spanning header "Observations.")*

| Power (W) | 1 | 2 | 3 | 4 | 5 | Totals | Averages |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 160 | 575 | 542 | 530 | 539 | 570 | 2756 | 551.2 |
| 180 | 565 | 593 | 590 | 579 | 610 | 2937 | 587.4 |
| 200 | 600 | 651 | 610 | 637 | 629 | 3127 | 625.4 |
| 220 | 725 | 700 | 715 | 685 | 710 | 3535 | 707.0 |

### PDF page 84 (book page 68)

**FIGURE 3.2** Box plots and scatter diagram of the etch rate data
*[Figure: two side-by-side panels, each with vertical axis "Etch rate (Å/min)" scaled 550 to 750 and horizontal axis "Power (w)" at 160, 180, 200, and 220. Panel (a), labeled "Comparative box plot," shows four box plots that rise steadily with power — medians near roughly 545, 590, 625, and 705 Å/min. Panel (b), labeled "Scatter diagram," plots the five individual etch rate observations at each power level, showing the same increasing trend.]*

is no strong evidence to suggest that the variability in etch rate around the average depends on the power setting. On the basis of this simple graphical analysis, we strongly suspect that (1) RF power setting affects the etch rate and (2) higher power settings result in increased etch rate.

Suppose that we wish to be more **objective** in our analysis of the data. Specifically, suppose that we wish to test for differences between the mean etch rates at all $a = 4$ levels of RF power. Thus, we are interested in testing the equality of all four means. It might seem that this problem could be solved by performing a $t$-test for all six possible pairs of means. However, this is not the best solution to this problem. First of all, performing all six pairwise $t$-tests is inefficient. It takes a lot of effort. Second, conducting all these pairwise comparisons inflates the type I error. Suppose that all four means are equal, so if we select $\alpha = 0.05$, the probability of reaching the correct decision on any single comparison is 0.95. However, the probability of reaching the correct conclusion on all six comparisons is considerably less than 0.95, so the type I error is inflated.

The appropriate procedure for testing the equality of several means is the **analysis of variance**. However, the analysis of variance has a much wider application than the problem above. It is probably the most useful technique in the field of statistical inference.

**3.2 The Analysis of Variance**

Suppose we have $a$ **treatments** or different **levels** of a **single factor** that we wish to compare. The observed response from each of the $a$ treatments is a random variable. The data would appear as in Table 3.2. An entry in Table 3.2 (e.g., $y_{ij}$) represents the $j$th observation taken under factor level or treatment $i$. There will be, in general, $n$ observations under the $i$th treatment. Notice that Table 3.2 is the general case of the data from the plasma etching experiment in Table 3.1.

**TABLE 3.2**
**Typical Data for a Single-Factor Experiment**

*(Columns 2–5 fall under the spanning header "Observations." The last row, printed beneath a rule in the Totals and Averages columns, gives the grand total and grand average.)*

| Treatment (Level) | | | | | Totals | Averages |
|---|---|---|---|---|---|---|
| 1 | $y_{11}$ | $y_{12}$ | $\cdots$ | $y_{1n}$ | $y_{1.}$ | $\bar{y}_{1.}$ |
| 2 | $y_{21}$ | $y_{22}$ | $\cdots$ | $y_{2n}$ | $y_{2.}$ | $\bar{y}_{2.}$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\cdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $a$ | $y_{a1}$ | $y_{a2}$ | $\cdots$ | $y_{an}$ | $y_{a.}$ | $\bar{y}_{a.}$ |
| | | | | | $y_{..}$ | $\bar{y}_{..}$ |

### PDF page 85 (book page 69)

***Models for the Data.*** We will find it useful to describe the observations from an experiment with a **model**. One way to write this model is

$$
y_{ij} = \mu_i + \epsilon_{ij} \begin{cases} i = 1, 2, \ldots, a \\ j = 1, 2, \ldots, n \end{cases} \tag{3.1}
$$

where $y_{ij}$ is the $ij$th observation, $\mu_i$ is the mean of the $i$th factor level or treatment, and $\epsilon_{ij}$ is a **random error** component that incorporates all other sources of variability in the experiment including measurement, variability arising from uncontrolled factors, differences between the experimental units (such as test material, etc.) to which the treatments are applied, and the general background noise in the process (such as variability over time, effects of environmental variables, and so forth). It is convenient to think of the errors as having mean zero, so that $E(y_{ij}) = \mu_i$.

Equation 3.1 is called the **means model**. An alternative way to write a model for the data is to define

$$
\mu_i = \mu + \tau_i, \qquad i = 1, 2, \ldots, a
$$

so that Equation 3.1 becomes

$$
y_{ij} = \mu + \tau_i + \epsilon_{ij} \begin{cases} i = 1, 2, \ldots, a \\ j = 1, 2, \ldots, n \end{cases} \tag{3.2}
$$

In this form of the model, $\mu$ is a parameter common to all treatments called the **overall mean**, and $\tau_i$ is a parameter unique to the $i$th treatment called the **$i$th treatment effect.** Equation 3.2 is usually called the **effects model**.

Both the means model and the effects model are **linear statistical models**; that is, the response variable $y_{ij}$ is a linear function of the model parameters. Although both forms of the model are useful, the effects model is more widely encountered in the experimental design literature. It has some intuitive appeal in that $\mu$ is a constant and the treatment effects $\tau_i$ represent deviations from this constant when the specific treatments are applied.

Equation 3.2 (or 3.1) is also called the **one-way** or **single-factor analysis of variance** (**ANOVA**) model because only one factor is investigated. Furthermore, we will require that the experiment be performed in random order so that the environment in which the treatments are applied (often called the **experimental units**) is as uniform as possible. Thus, the experimental design is a **completely randomized design**. Our objectives will be to test appropriate hypotheses about the treatment means and to estimate them. For hypothesis testing, the model errors are assumed to be normally and independently distributed random variables with mean zero and variance $\sigma^2$. The variance $\sigma^2$ is assumed to be constant for all levels of the factor. This implies that the observations

$$
y_{ij} \sim N(\mu + \tau_i, \sigma^2)
$$

and that the observations are mutually independent.

***Fixed or Random Factor?*** The statistical model, Equation 3.2, describes two different situations with respect to the treatment effects. First, the $a$ treatments could have been specifically chosen by the experimenter. In this situation, we wish to test hypotheses about the treatment means, and our conclusions will apply only to the factor levels considered in the analysis. The conclusions cannot be extended to similar treatments that were not explicitly considered. We may also wish to estimate the model parameters ($\mu$, $\tau_i$, $\sigma^2$). This is called the **fixed effects model**. Alternatively, the $a$ treatments could be a **random sample** from a larger population of treatments. In this situation, we should like to be able to extend the conclusions (which are based on the sample of treatments) to all treatments in the population,

### PDF page 86 (book page 70)

whether or not they were explicitly considered in the analysis. Here, the $\tau_i$ are random variables, and knowledge about the particular ones investigated is relatively useless. Instead, we test hypotheses about the variability of the $\tau_i$ and try to estimate this variability. This is called the **random effects model** or **components of variance model**. We discuss the single-factor random effects model in Section 3.9. However, we will defer a more complete discussion of experiments with random factors to Chapter 13.

**3.3 Analysis of the Fixed Effects Model**

In this section, we develop the single-factor analysis of variance for the fixed effects model. Recall that $y_{i.}$ represents the total of the observations under the $i$th treatment. Let $\bar{y}_{i.}$ represent the average of the observations under the $i$th treatment. Similarly, let $y_{..}$ represent the grand total of all the observations and $\bar{y}_{..}$ represent the grand average of all the observations. Expressed symbolically,

$$
\begin{aligned}
y_{i.} &= \sum_{j=1}^{n} y_{ij} \qquad \bar{y}_{i.} = y_{i.}/n \qquad i = 1, 2, \ldots, a \\
y_{..} &= \sum_{i=1}^{a} \sum_{j=1}^{n} y_{ij} \qquad \bar{y}_{..} = y_{..}/N
\end{aligned}
\tag{3.3}
$$

where $N = an$ is the total number of observations. We see that the "dot" subscript notation implies summation over the subscript that it replaces.

We are interested in testing the equality of the $a$ treatment means; that is, $E(y_{ij}) = \mu + \tau_i = \mu_i$, $i = 1, 2, \ldots, a$. The appropriate hypotheses are

$$
\begin{aligned}
H_0 &: \mu_1 = \mu_2 = \cdots = \mu_a \\
H_1 &: \mu_i \neq \mu_j \qquad \text{for at least one pair } (i, j)
\end{aligned}
\tag{3.4}
$$

In the effects model, we break the $i$th treatment mean $\mu_i$ into two components such that $\mu_i = \mu + \tau_i$. We usually think of $\mu$ as an overall mean so that

$$
\frac{\displaystyle\sum_{i=1}^{a} \mu_i}{a} = \mu
$$

This definition implies that

$$
\sum_{i=1}^{a} \tau_i = 0
$$

That is, the treatment or factor effects can be thought of as deviations from the overall mean.[^1] Consequently, an equivalent way to write the above hypotheses is in terms of the treatment effects $\tau_i$, say

$$
\begin{aligned}
H_0 &: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \\
H_1 &: \tau_i \neq 0 \qquad \text{for at least one } i
\end{aligned}
$$

Thus, we speak of testing the equality of treatment means or testing that the treatment effects (the $\tau_i$) are zero. The appropriate procedure for testing the equality of $a$ treatment means is the analysis of variance.

[^1]: For more information on this subject, refer to the supplemental text material for Chapter 3.

### PDF page 87 (book page 71)

**3.3.1 Decomposition of the Total Sum of Squares**

The name **analysis of variance** is derived from a partitioning of total variability into its component parts. The total corrected sum of squares

$$
SS_T = \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{..})^2
$$

is used as a measure of overall variability in the data. Intuitively, this is reasonable because if we were to divide $SS_T$ by the appropriate number of degrees of freedom (in this case, $an - 1 = N - 1$), we would have the **sample variance** of the $y$'s. The sample variance is, of course, a standard measure of variability.

Note that the total corrected sum of squares $SS_T$ may be written as

$$
\sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{..})^2 = \sum_{i=1}^{a} \sum_{j=1}^{n} [(\bar{y}_{i.} - \bar{y}_{..}) + (y_{ij} - \bar{y}_{i.})]^2
\tag{3.5}
$$

or

$$
\begin{aligned}
\sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{..})^2 = n \sum_{i=1}^{a} (\bar{y}_{i.} - \bar{y}_{..})^2 &+ \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2 \\
&+ 2 \sum_{i=1}^{a} \sum_{j=1}^{n} (\bar{y}_{i.} - \bar{y}_{..})(y_{ij} - \bar{y}_{i.})
\end{aligned}
$$

However, the cross-product term in this last equation is zero, because

$$
\sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.}) = y_{i.} - n\bar{y}_{i.} = y_{i.} - n(y_{i.}/n) = 0
$$

Therefore, we have

$$
\sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{..})^2 = n \sum_{i=1}^{a} (\bar{y}_{i.} - \bar{y}_{..})^2 + \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2
\tag{3.6}
$$

Equation 3.6 is the fundamental ANOVA identity. It states that the total variability in the data, as measured by the total corrected sum of squares, can be partitioned into a sum of squares of the differences **between** the treatment averages and the grand average plus a sum of squares of the differences of observations **within** treatments from the treatment average. Now, the difference between the observed treatment averages and the grand average is a measure of the differences between treatment means, whereas the differences of observations within a treatment from the treatment average can be due to only random error. Thus, we may write Equation 3.6 symbolically as

$$
SS_T = SS_{\text{Treatments}} + SS_E
$$

where $SS_{\text{Treatments}}$ is called the sum of squares due to treatments (i.e., between treatments), and $SS_E$ is called the sum of squares due to error (i.e., within treatments). There are $an = N$ total observations; thus, $SS_T$ has $N - 1$ degrees of freedom. There are $a$ levels of the factor (and $a$ treatment means), so $SS_{\text{Treatments}}$ has $a - 1$ degrees of freedom. Finally, there are $n$ replicates within any treatment providing $n - 1$ degrees of freedom with which to estimate the experimental error. Because there are $a$ treatments, we have $a(n - 1) = an - a = N - a$ degrees of freedom for error.

It is instructive to examine explicitly the two terms on the right-hand side of the fundamental ANOVA identity. Consider the error sum of squares

$$
SS_E = \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2 = \sum_{i=1}^{a} \left[ \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2 \right]
$$

### PDF page 88 (book page 72)

In this form, it is easy to see that the term within square brackets, if divided by $n - 1$, is the sample variance in the $i$th treatment, or

$$
S_i^2 = \frac{\displaystyle\sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2}{n - 1} \qquad i = 1, 2, \ldots, a
$$

Now $a$ sample variances may be combined to give a single estimate of the common population variance as follows:

$$
\begin{aligned}
\frac{(n - 1)S_1^2 + (n - 1)S_2^2 + \cdots + (n - 1)S_a^2}{(n - 1) + (n - 1) + \cdots + (n - 1)} &= \frac{\displaystyle\sum_{i=1}^{a} \left[ \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2 \right]}{\displaystyle\sum_{i=1}^{a} (n - 1)} \\
&= \frac{SS_E}{(N - a)}
\end{aligned}
$$

Thus, $SS_E/(N - a)$ is a **pooled estimate** of the common variance within each of the $a$ treatments.

Similarly, if there were no differences between the $a$ treatment means, we could use the variation of the treatment averages from the grand average to estimate $\sigma^2$. Specifically,

$$
\frac{SS_{\text{Treatments}}}{a - 1} = \frac{n \displaystyle\sum_{i=1}^{a} (\bar{y}_{i.} - \bar{y}_{..})^2}{a - 1}
$$

is an estimate of $\sigma^2$ if the treatment means are equal. The reason for this may be intuitively seen as follows: The quantity $\sum_{i=1}^{a}(\bar{y}_{i.} - \bar{y}_{..})^2/(a - 1)$ estimates $\sigma^2/n$, the variance of the treatment averages, so $n\sum_{i=1}^{a}(\bar{y}_{i.} - \bar{y}_{..})^2/(a - 1)$ must estimate $\sigma^2$ if there are no differences in treatment means.

We see that the ANOVA identity (Equation 3.6) provides us with two estimates of $\sigma^2$—one based on the inherent variability within treatments and the other based on the variability between treatments. If there are no differences in the treatment means, these two estimates should be very similar, and if they are not, we suspect that the observed difference must be caused by differences in the treatment means. Although we have used an intuitive argument to develop this result, a somewhat more formal approach can be taken.

The quantities

$$
MS_{\text{Treatments}} = \frac{SS_{\text{Treatments}}}{a - 1}
$$

and

$$
MS_E = \frac{SS_E}{N - a}
$$

are called **mean squares**. We now examine the **expected values** of these mean squares. Consider

$$
\begin{aligned}
E(MS_E) &= E\left(\frac{SS_E}{N - a}\right) = \frac{1}{N - a} E\left[ \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{i.})^2 \right] \\
&= \frac{1}{N - a} E\left[ \sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij}^2 - 2y_{ij}\bar{y}_{i.} + \bar{y}_{i.}^2) \right]
\end{aligned}
$$

### PDF page 89 (book page 73)

$$
\begin{aligned}
&= \frac{1}{N - a} E\left[ \sum_{i=1}^{a} \sum_{j=1}^{n} y_{ij}^2 - 2n \sum_{i=1}^{a} \bar{y}_{i.}^2 + n \sum_{i=1}^{a} \bar{y}_{i.}^2 \right] \\
&= \frac{1}{N - a} E\left[ \sum_{i=1}^{a} \sum_{j=1}^{n} y_{ij}^2 - \frac{1}{n} \sum_{i=1}^{a} y_{i.}^2 \right]
\end{aligned}
$$

Substituting the model (Equation 3.1) into this equation, we obtain

$$
E(MS_E) = \frac{1}{N - a} E\left[ \sum_{i=1}^{a} \sum_{j=1}^{n} (\mu + \tau_i + \epsilon_{ij})^2 - \frac{1}{n} \sum_{i=1}^{a} \left( \sum_{j=1}^{n} \mu + \tau_i + \epsilon_{ij} \right)^2 \right]
$$

Now when squaring and taking expectation of the quantity within the brackets, we see that terms involving $\epsilon_{ij}^2$ and $\epsilon_{i.}^2$ are replaced by $\sigma^2$ and $n\sigma^2$, respectively, because $E(\epsilon_{ij}) = 0$. Furthermore, all cross products involving $\epsilon_{ij}$ have zero expectation. Therefore, after squaring and taking expectation, the last equation becomes

$$
E(MS_E) = \frac{1}{N - a} \left[ N\mu^2 + n \sum_{i=1}^{a} \tau_i^2 + N\sigma^2 - N\mu^2 - n \sum_{i=1}^{a} \tau_i^2 - a\sigma^2 \right]
$$

or

$$
E(MS_E) = \sigma^2
$$

By a similar approach, we may also show that[^2]

$$
E(MS_{\text{Treatments}}) = \sigma^2 + \frac{n \displaystyle\sum_{i=1}^{a} \tau_i^2}{a - 1}
$$

Thus, as we argued heuristically, $MS_E = SS_E/(N - a)$ estimates $\sigma^2$, and, if there are no differences in treatment means (which implies that $\tau_i = 0$), $MS_{\text{Treatments}} = SS_{\text{Treatments}}/(a - 1)$ also estimates $\sigma^2$. However, note that if treatment means do differ, the expected value of the treatment mean square is greater than $\sigma^2$.

It seems clear that a test of the hypothesis of no difference in treatment means can be performed by comparing $MS_{\text{Treatments}}$ and $MS_E$. We now consider how this comparison may be made.

**3.3.2 Statistical Analysis**

We now investigate how a formal test of the hypothesis of no differences in treatment means ($H_0\colon \mu_1 = \mu_2 = \cdots = \mu_a$, or equivalently, $H_0\colon \tau_1 = \tau_2 = \cdots = \tau_a = 0$) can be performed. Because we have assumed that the errors $\epsilon_{ij}$ are normally and independently distributed with mean zero and variance $\sigma^2$, the observations $y_{ij}$ are normally and independently distributed with mean $\mu + \tau_i$ and variance $\sigma^2$. Thus, $SS_T$ is a sum of squares in normally distributed random variables; consequently, it can be shown that $SS_T/\sigma^2$ is distributed as chi-square with $N - 1$ degrees of freedom. Furthermore, we can show that $SS_E/\sigma^2$ is chi-square with $N - a$ degrees of freedom and that $SS_{\text{Treatments}}/\sigma^2$ is chi-square with $a - 1$ degrees of freedom if the null hypothesis $H_0\colon \tau_i = 0$ is true. However, all three sums of squares are not necessarily independent because $SS_{\text{Treatments}}$ and $SS_E$ add to $SS_T$. The following theorem, which is a special form of one attributed to William G. Cochran, is useful in establishing the independence of $SS_E$ and $SS_{\text{Treatments}}$.

[^2]: Refer to the supplemental text material for Chapter 3.

### PDF page 90 (book page 74)

**THEOREM 3-1**
**Cochran’s Theorem**

Let $Z_i$ be NID(0, 1) for $i = 1, 2, \ldots, \nu$ and

$$
\sum_{i=1}^{\nu} Z_i^2 = Q_1 + Q_2 + \cdots + Q_s
$$

where $s \le \nu$, and $Q_i$ has $\nu_i$ degrees of freedom ($i = 1, 2, \ldots, s$). Then $Q_1, Q_2, \ldots, Q_s$ are independent chi-square random variables with $\nu_1, \nu_2, \ldots, \nu_s$ degrees of freedom, respectively, if and only if

$$
\nu = \nu_1 + \nu_2 + \cdots + \nu_s
$$

Because the degrees of freedom for $SS_{\text{Treatments}}$ and $SS_E$ add to $N - 1$, the total number of degrees of freedom, Cochran's theorem implies that $SS_{\text{Treatments}}/\sigma^2$ and $SS_E/\sigma^2$ are independently distributed chi-square random variables. Therefore, if the null hypothesis of no difference in treatment means is true, the ratio

$$
F_0 = \frac{SS_{\text{Treatments}}/(a - 1)}{SS_E/(N - a)} = \frac{MS_{\text{Treatments}}}{MS_E} \tag{3.7}
$$

is distributed as $F$ with $a - 1$ and $N - a$ degrees of freedom. Equation 3.7 is the **test statistic** for the hypothesis of no differences in treatment means.

From the expected mean squares we see that, in general, $MS_E$ is an unbiased estimator of $\sigma^2$. Also, under the null hypothesis, $MS_{\text{Treatments}}$ is an unbiased estimator of $\sigma^2$. However, if the null hypothesis is false, the expected value of $MS_{\text{Treatments}}$ is greater than $\sigma^2$. Therefore, under the alternative hypothesis, the expected value of the numerator of the test statistic (Equation 3.7) is greater than the expected value of the denominator, and we should reject $H_0$ on values of the test statistic that are too large. This implies an upper-tail, one-tail critical region. Therefore, we should reject $H_0$ and conclude that there are differences in the treatment means if

$$
F_0 > F_{\alpha, a-1, N-a}
$$

where $F_0$ is computed from Equation 3.7. Alternatively, we could use the $P$-value approach for decision making. The table of $F$ percentages in the Appendix (Table IV) can be used to find bounds on the $P$-value.

The sums of squares may be computed in several ways. One direct approach is to make use of the definition

$$
y_{ij} - \bar{y}_{..} = (\bar{y}_{i.} - \bar{y}_{..}) + (y_{ij} - \bar{y}_{i.})
$$

Use a spreadsheet to compute these three terms for each observation. Then, sum up the squares to obtain $SS_T$, $SS_{\text{Treatments}}$, and $SS_E$. Another approach is to rewrite and simplify the definitions of $SS_{\text{Treatments}}$ and $SS_T$ in Equation 3.6, which results in

$$
SS_T = \sum_{i=1}^{a} \sum_{j=1}^{n} y_{ij}^2 - \frac{y_{..}^2}{N} \tag{3.8}
$$

$$
SS_{\text{Treatments}} = \frac{1}{n} \sum_{i=1}^{a} y_{i.}^2 - \frac{y_{..}^2}{N} \tag{3.9}
$$

and

$$
SS_E = SS_T - SS_{\text{Treatments}} \tag{3.10}
$$

### PDF page 91 (book page 75)

**TABLE 3.3**
**The Analysis of Variance Table for the Single-Factor, Fixed Effects Model**

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|:---|:---|:---|:---|:---|
| Between treatments | $SS_{\text{Treatments}} = n \displaystyle\sum_{i=1}^{a} (\bar{y}_{i.} - \bar{y}_{..})^2$ | $a - 1$ | $MS_{\text{Treatments}}$ | $F_0 = \dfrac{MS_{\text{Treatments}}}{MS_E}$ |
| Error (within treatments) | $SS_E = SS_T - SS_{\text{Treatments}}$ | $N - a$ | $MS_E$ | |
| Total | $SS_T = \displaystyle\sum_{i=1}^{a} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{..})^2$ | $N - 1$ | | |

This approach is nice because some calculators are designed to accumulate the sum of entered numbers in one register and the sum of the squares of those numbers in another, so each number only has to be entered once. In practice, we use computer software to do this.

The test procedure is summarized in Table 3.3. This is called an **analysis of variance** (or **ANOVA**) table.

**EXAMPLE 3.1 — The Plasma Etching Experiment**

To illustrate the analysis of variance, return to the first example discussed in Section 3.1. Recall that the engineer is interested in determining if the RF power setting affects the etch rate, and she has run a completely randomized experiment with four levels of RF power and five replicates. For convenience, we repeat here the data from Table 3.1:

We will use the analysis of variance to test $H_0\colon \mu_1 = \mu_2 = \mu_3 = \mu_4$ against the alternative $H_1$: some means are different. The sums of squares required are computed using Equations 3.8, 3.9, and 3.10 as follows:

*(Columns 1–5 fall under the spanning header "Observed Etch Rate (Å/min)".)*

| RF Power (W) | 1 | 2 | 3 | 4 | 5 | Totals $y_{i.}$ | Averages $\bar{y}_{i.}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 160 | 575 | 542 | 530 | 539 | 570 | 2756 | 551.2 |
| 180 | 565 | 593 | 590 | 579 | 610 | 2937 | 587.4 |
| 200 | 600 | 651 | 610 | 637 | 629 | 3127 | 625.4 |
| 220 | 725 | 700 | 715 | 685 | 710 | 3535 | 707.0 |
| | | | | | | $y_{..} = 12{,}355$ | $\bar{y}_{..} = 617.75$ |

$$
\begin{aligned}
SS_T &= \sum_{i=1}^{4} \sum_{j=1}^{5} y_{ij}^2 - \frac{y_{..}^2}{N} \\
&= (575)^2 + (542)^2 + \cdots + (710)^2 - \frac{(12{,}355)^2}{20} \\
&= 72{,}209.75
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Treatments}} &= \frac{1}{n} \sum_{i=1}^{4} y_{i.}^2 - \frac{y_{..}^2}{N} \\
&= \frac{1}{5}\left[(2756)^2 + \cdots + (3535)^2\right] - \frac{(12{,}355)^2}{20} \\
&= 66{,}870.55
\end{aligned}
$$

$$
\begin{aligned}
SS_E &= SS_T - SS_{\text{Treatments}} \\
&= 72{,}209.75 - 66{,}870.55 = 5339.20
\end{aligned}
$$

Usually, these calculations would be performed on a computer, using a software package with the capability to analyze data from designed experiments.

The ANOVA is summarized in Table 3.4. Note that the RF power or between-treatment mean square (22,290.18) is many times larger than the within-treatment or error mean square (333.70). This indicates that it is unlikely that the treatment means are equal. More formally, we

### PDF page 92 (book page 76)

**TABLE 3.4**
**ANOVA for the Plasma Etching Experiment**

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---|---|---|---|---|
| RF Power | 66,870.55 | 3 | 22,290.18 | $F_0 = 66.80$ | <0.01 |
| Error | 5339.20 | 16 | 333.70 | | |
| Total | 72,209.75 | 19 | | | |

can compute the $F$ ratio $F_0 = 22,290.18/333.70 = 66.80$ and compare this to an appropriate upper-tail percentage point of the $F_{3,16}$ distribution. To use a fixed significance level approach, suppose that the experimenter has selected $\alpha = 0.05$. From Appendix Table IV we find that $F_{0.05,3,16} = 3.24$. Because $F_0 = 66.80 > 3.24$, we reject $H_0$ and conclude that the treatment means differ; that is, the RF power setting significantly affects the mean etch rate. We could also compute a $P$-value for this test statistic. Figure 3.3 shows the reference distribution $(F_{3,16})$ for the test statistic $F_0$. Clearly, the $P$-value is very small in this case. From Appendix Table A-4, we find that $F_{0.01,3,16} = 5.29$ and because $F_0 > 5.29$, we can conclude that an upper bound for the $P$-value is 0.01; that is, $P < 0.01$ (the exact $P$-value is $P = 2.88 \times 10^{-9}$).

**FIGURE 3.3** The reference distribution $(F_{3,16})$ for the test statistic $F_0$ in Example 3.1 *[Figure: a right-skewed $F$ probability density curve; the vertical axis is labeled "Probability density" from 0 to 0.8 in steps of 0.2, and the horizontal axis (labeled $F_0$) runs 0, 4, 8, 12, then has a break, resuming at 66 and 70. Arrows below the axis mark $F_{0.05,3,16}$ (≈3.24) and $F_{0.01,3,16}$ (≈5.29) near the peak region, and $F_0 = 66.80$ far out in the right tail beyond the axis break.]*

***Coding the Data.*** Generally, we need not be too concerned with computing because there are many widely available computer programs for performing the calculations. These computer programs are also helpful in performing many other analyses associated with experimental design (such as residual analysis and model adequacy checking). In many cases, these programs will also assist the experimenter in setting up the design.

However, when hand calculations are necessary, it is sometimes helpful to code the observations. This is illustrated in the next example.

### PDF page 93 (book page 77)

**EXAMPLE 3.2 — Coding the Observations**

The ANOVA calculations may often be made more easily or accurately by **coding** the observations. For example, consider the plasma etching data in Example 3.1. Suppose we subtract 600 from each observation. The coded data are shown in Table 3.5. It is easy to verify that

$$
\begin{aligned}
SS_T &= (-25)^2 + (-58)^2 + \cdots \\
&\quad + (110)^2 - \frac{(355)^2}{20} = 72,209.75
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Treatments}} &= \frac{(-244)^2 + (-63)^2 + (127)^2 + (535)^2}{5} \\
&\quad - \frac{(355)^2}{20} = 66,870.55
\end{aligned}
$$

and

$$SS_E = 5339.20$$

Comparing these sums of squares to those obtained in Example 3.1, we see that subtracting a constant from the original data does not change the sums of squares.

Now suppose that we multiply each observation in Example 3.1 by 2. It is easy to verify that the sums of squares for the transformed data are $SS_T = 288,839.00$, $SS_{\text{Treatments}} = 267,482.20$, and $SS_E = 21,356.80$. These sums of squares appear to differ considerably from those obtained in Example 3.1. However, if they are divided by 4 (i.e., $2^2$), the results are identical. For example, for the treatment sum of squares $267,482.20/4 = 66,870.55$. Also, for the coded data, the $F$ ratio is $F = (267,482.20/3)/(21,356.80/16) = 66.80$, which is identical to the $F$ ratio for the original data. Thus, the ANOVAs are equivalent.

**TABLE 3.5**
**Coded Etch Rate Data for Example 3.2**

*[Columns 1–5 are grouped under the spanning header "Observations."]*

| RF Power (W) | 1 | 2 | 3 | 4 | 5 | Totals $y_{i.}$ |
|---|---|---|---|---|---|---|
| 160 | -25 | -58 | -70 | -61 | -30 | -244 |
| 180 | -35 | -7 | -10 | -21 | 10 | -63 |
| 200 | 0 | 51 | 10 | 37 | 29 | 127 |
| 220 | 125 | 100 | 115 | 85 | 110 | 535 |

***Randomization Tests and Analysis of Variance.*** In our development of the ANOVA $F$ test, we have used the assumption that the random errors $\epsilon_{ij}$ are normally and independently distributed random variables. The $F$ test can also be justified as an approximation to a **randomization test**. To illustrate this, suppose that we have five observations on each of two treatments and that we wish to test the equality of treatment means. The data would look like this:

| Treatment 1 | Treatment 2 |
|---|---|
| $y_{11}$ | $y_{21}$ |
| $y_{12}$ | $y_{22}$ |
| $y_{13}$ | $y_{23}$ |
| $y_{14}$ | $y_{24}$ |
| $y_{15}$ | $y_{25}$ |

### PDF page 94 (book page 78)

We could use the ANOVA $F$ test to test $H_0: \mu_1 = \mu_2$. Alternatively, we could use a somewhat different approach. Suppose we consider all the possible ways of allocating the 10 numbers in the above sample to the two treatments. There are $10!/5!5! = 252$ possible arrangements of the 10 observations. If there is no difference in treatment means, all 252 arrangements are equally likely. For each of the 252 arrangements, we calculate the value of the $F$ statistic using Equation 3.7. The distribution of these $F$ values is called a **randomization distribution**, and a large value of $F$ indicates that the data are not consistent with the hypothesis $H_0: \mu_1 = \mu_2$. For example, if the value of $F$ actually observed was exceeded by only five of the values of the randomization distribution, this would correspond to rejection of $H_0: \mu_1 = \mu_2$ at a significance level of $\alpha = 5/252 = 0.0198$ (or 1.98 percent). Notice that no normality assumption is required in this approach.

The difficulty with this approach is that, even for relatively small problems, it is computationally prohibitive to enumerate the exact randomization distribution. However, numerous studies have shown that the exact randomization distribution is well approximated by the usual normal-theory $F$ distribution. Thus, even without the normality assumption, the ANOVA $F$ test can be viewed as an approximation to the randomization test. For further reading on randomization tests in the analysis of variance, see Box, Hunter, and Hunter (2005).

**3.3.3 Estimation of the Model Parameters**

We now present estimators for the parameters in the single-factor model

$$y_{ij} = \mu + \tau_i + \epsilon_{ij}$$

and confidence intervals on the treatment means. We will prove later that reasonable estimates of the overall mean and the treatment effects are given by

$$
\begin{aligned}
\hat{\mu} &= \bar{y}_{..} \\
\hat{\tau}_i &= \bar{y}_{i.} - \bar{y}_{..}, \qquad i = 1, 2, \ldots, a
\end{aligned}
\tag{3.11}
$$

These estimators have considerable intuitive appeal; note that the overall mean is estimated by the grand average of the observations and that any treatment effect is just the difference between the treatment average and the grand average.

A **confidence interval** estimate of the $i$th treatment mean may be easily determined. The mean of the $i$th treatment is

$$\mu_i = \mu + \tau_i$$

A point estimator of $\mu_i$ would be $\hat{\mu}_i = \hat{\mu} + \hat{\tau}_i = \bar{y}_{i.}$. Now, if we assume that the errors are normally distributed, each treatment average $\bar{y}_{i.}$ is distributed $\text{NID}(\mu_i, \sigma^2/n)$. Thus, if $\sigma^2$ were known, we could use the normal distribution to define the confidence interval. Using the $MS_E$ as an estimator of $\sigma^2$, we would base the confidence interval on the $t$ distribution. Therefore, a $100(1 - \alpha)$ percent confidence interval on the $i$th treatment mean $\mu_i$ is

$$\bar{y}_{i.} - t_{\alpha/2,N-a}\sqrt{\frac{MS_E}{n}} \leq \mu_i \leq \bar{y}_{i.} + t_{\alpha/2,N-a}\sqrt{\frac{MS_E}{n}} \tag{3.12}$$

Differences in treatments are frequently of great practical interest. A $100(1 - \alpha)$ percent confidence interval on the difference in any two treatments means [sic], say $\mu_i - \mu_j$, would be

$$\bar{y}_{i.} - \bar{y}_{j.} - t_{\alpha/2,N-a}\sqrt{\frac{2MS_E}{n}} \leq \mu_i - \mu_j \leq \bar{y}_{i.} - \bar{y}_{j.} + t_{\alpha/2,N-a}\sqrt{\frac{2MS_E}{n}} \tag{3.13}$$
