# Chapter 5 — Introduction to Factorial Designs
*(PDF pages 199–248; book pages 183–224)*

*⚠ In progress: 42 of 50 pages transcribed; missing PDF pages 241–248.*

### PDF page 199 (book page 183)

# Chapter 5 — Introduction to Factorial Designs

## Chapter Outline

- 5.1 Basic Definitions and Principles
- 5.2 The Advantage of Factorials
- 5.3 The Two-Factor Factorial Design
  - 5.3.1 An Example
  - 5.3.2 Statistical Analysis of the Fixed Effects Model
  - 5.3.3 Model Adequacy Checking
  - 5.3.4 Estimating the Model Parameters
  - 5.3.5 Choice of Sample Size
  - 5.3.6 The Assumption of No Interaction in a Two-Factor Model
  - 5.3.7 One Observation per Cell
- 5.4 The General Factorial Design
- 5.5 Fitting Response Curves and Surfaces
- 5.6 Blocking in a Factorial Design

**Supplemental Material for Chapter 5**

- S5.1 Expected Mean Squares in the Two-Factor Factorial
- S5.2 The Definition of Interaction
- S5.3 Estimable Functions in the Two-Factor Factorial Model
- S5.4 Regression Model Formulation of the Two-Factor Factorial
- S5.5 Model Hierarchy

The supplemental material is on the textbook website www.wiley.com/college/montgomery.

## 5.1 Basic Definitions and Principles

Many experiments involve the study of the effects of two or more factors. In general, **factorial designs** are most efficient for this type of experiment. By a factorial design, we mean that in each complete trial or replicate of the experiment all possible combinations of the levels of the factors are investigated. For example, if there are $a$ levels of factor $A$ and $b$ levels of factor $B$, each replicate contains all $ab$ treatment combinations. When factors are arranged in a factorial design, they are often said to be **crossed**.

The effect of a factor is defined to be the change in response produced by a change in the level of the factor. This is frequently called a **main effect** because it refers to the primary factors of interest in the experiment. For example, consider the simple experiment in Figure 5.1. This is a two-factor factorial experiment with both design factors at two levels. We have called these levels “low” and “high” and denoted them “$-$” and “$+$,” respectively. The main effect of factor $A$ in this two-level design can be thought of as the difference between the average response at the low level of $A$ and the average response at the high level of $A$. Numerically, this is

$$
A=\frac{40+52}{2}-\frac{20+30}{2}=21
$$

### PDF page 200 (book page 184)

**FIGURE 5.1** A two-factor factorial experiment, with the response ($y$) shown at the corners

*A square factor-space plot has factor $A$ on the horizontal axis and factor $B$ on the vertical axis. At $(A^-,B^-)$ the response is 20; at $(A^+,B^-)$, 40; at $(A^-,B^+)$, 30; and at $(A^+,B^+)$, 52.*

**FIGURE 5.2** A two-factor factorial experiment with interaction

*A square factor-space plot has factor $A$ on the horizontal axis and factor $B$ on the vertical axis. At $(A^-,B^-)$ the response is 20; at $(A^+,B^-)$, 50; at $(A^-,B^+)$, 40; and at $(A^+,B^+)$, 12.*

That is, increasing factor $A$ from the low level to the high level causes an **average response increase** of 21 units. Similarly, the main effect of $B$ is

$$
B=\frac{30+52}{2}-\frac{20+40}{2}=11
$$

If the factors appear at more than two levels, the above procedure must be modified because there are other ways to define the effect of a factor. This point is discussed more completely later.

In some experiments, we may find that the difference in response between the levels of one factor is not the same at all levels of the other factors. When this occurs, there is an **interaction** between the factors. For example, consider the two-factor factorial experiment shown in Figure 5.2. At the low level of factor $B$ (or $B^-$), the $A$ effect is

$$
A=50-20=30
$$

and at the high level of factor $B$ (or $B^+$), the $A$ effect is

$$
A=12-40=-28
$$

Because the effect of $A$ depends on the level chosen for factor $B$, we see that there is interaction between $A$ and $B$. The magnitude of the interaction effect is the average *difference* in these two $A$ effects, or $AB=(-28-30)/2=-29$. Clearly, the interaction is large in this experiment.

These ideas may be illustrated graphically. Figure 5.3 plots the response data in Figure 5.1 against factor $A$ for both levels of factor $B$. Note that the $B^-$ and $B^+$ lines are approximately parallel, indicating a lack of interaction between factors $A$ and $B$. Similarly, Figure 5.4

**FIGURE 5.3** A factorial experiment without interaction

*The response-versus-factor-$A$ lines for $B^-$ and $B^+$ rise from 20 to 40 and from 30 to 52, respectively, and are approximately parallel.*

**FIGURE 5.4** A factorial experiment with interaction

*The response-versus-factor-$A$ lines cross: the $B^-$ line rises from 20 to 50, while the $B^+$ line falls from 40 to 12.*

### PDF page 201 (book page 185)

plots the response data in Figure 5.2. Here we see that the $B^-$ and $B^+$ lines are not parallel. This indicates an interaction between factors $A$ and $B$. Two-factor interaction graphs such as these are frequently very useful in interpreting significant interactions and in reporting results to nonstatistically trained personnel. However, they should not be utilized as the sole technique of data analysis because their interpretation is subjective and their appearance is often misleading.

There is another way to illustrate the concept of interaction. Suppose that both of our design factors are **quantitative** (such as temperature, pressure, time, etc.). Then a **regression model representation** of the two-factor factorial experiment could be written as

$$
y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2+\epsilon
$$

where $y$ is the response, the $\beta$’s are parameters whose values are to be determined, $x_1$ is a variable that represents factor $A$, $x_2$ is a variable that represents factor $B$, and $\epsilon$ is a random error term. The variables $x_1$ and $x_2$ are defined on a **coded scale** from $-1$ to $+1$ (the low and high levels of $A$ and $B$), and $x_1x_2$ represents the interaction between $x_1$ and $x_2$.

The parameter estimates in this regression model turn out to be related to the effect estimates. For the experiment shown in Figure 5.1 we found the main effects of $A$ and $B$ to be $A=21$ and $B=11$. The estimates of $\beta_1$ and $\beta_2$ are one-half the value of the corresponding main effect; therefore, $\hat{\beta}_1=21/2=10.5$ and $\hat{\beta}_2=11/2=5.5$. The interaction effect in Figure 5.1 is $AB=1$, so the value of interaction coefficient in the regression model is $\hat{\beta}_{12}=1/2=0.5$. The parameter $\beta_0$ is estimated by the average of all four responses, or $\hat{\beta}_0=(20+40+30+52)/4=35.5$. Therefore, the fitted regression model is

$$
\hat{y}=35.5+10.5x_1+5.5x_2+0.5x_1x_2
$$

The parameter estimates obtained in the manner for the factorial design with all factors at two levels ($-$ and $+$) turn out to be **least squares estimates** (more on this later).

The interaction coefficient ($\hat{\beta}_{12}=0.5$) is small relative to the main effect coefficients $\hat{\beta}_1$ and $\hat{\beta}_2$. We will take this to mean that interaction is small and can be ignored. Therefore, dropping the term $0.5x_1x_2$ gives us the model

$$
\hat{y}=35.5+10.5x_1+5.5x_2
$$

Figure 5.5 presents graphical representations of this model. In Figure 5.5a we have a plot of the plane of $y$-values generated by the various combinations of $x_1$ and $x_2$. This three-dimensional graph is called a **response surface plot**. Figure 5.5b shows the contour lines of constant response $y$ in the $x_1$, $x_2$ plane. Notice that because the response surface is a plane, the contour plot contains parallel straight lines.

**FIGURE 5.5** Response surface and contour plot for the model $\hat{y}=35.5+10.5x_1+5.5x_2$

*Panel (a) is a planar response surface over $-1\leq x_1,x_2\leq1$, rising from approximately 19 to 59. Panel (b) shows parallel straight contour lines labeled 22 through 49.*

### PDF page 202 (book page 186)

**FIGURE 5.6** Response surface and contour plot for the model $\hat{y}=35.5+10.5x_1+5.5x_2+8x_1x_2$

*Panel (a) is a twisted response surface over $-1\leq x_1,x_2\leq1$, with response values from approximately 22 to 62. Panel (b) shows curved contour lines labeled 25 through 49.*

Now suppose that the interaction contribution to this experiment was not negligible; that is, the coefficient $\beta_{12}$ was not small. Figure 5.6 presents the response surface and contour plot for the model

$$
\hat{y}=35.5+10.5x_1+5.5x_2+8x_1x_2
$$

(We have let the interaction effect be the average of the two main effects.) Notice that the significant interaction effect “twists” the plane in Figure 5.6a. This twisting of the response surface results in curved contour lines of constant response in the $x_1$, $x_2$ plane, as shown in Figure 5.6b. Thus, **interaction is a form of curvature** in the underlying response surface model for the experiment.

The response surface model for an experiment is extremely important and useful. We will say more about it in Section 5.5 and in subsequent chapters.

Generally, when an interaction is large, the corresponding main effects have little practical meaning. For the experiment in Figure 5.2, we would estimate the main effect of $A$ to be

$$
A=\frac{50+12}{2}-\frac{20+40}{2}=1
$$

which is very small, and we are tempted to conclude that there is no effect due to $A$. However, when we examine the effects of $A$ at *different levels of factor $B$*, we see that this is not the case. Factor $A$ has an effect, but it *depends on the level of factor $B$*. That is, knowledge of the $AB$ interaction is more useful than knowledge of the main effect. A significant interaction will often **mask** the significance of main effects. These points are clearly indicated by the interaction plot in Figure 5.4. In the presence of significant interaction, the experimenter must usually examine the levels of one factor, say $A$, with levels of the other factors fixed to draw conclusions about the main effect of $A$.

## 5.2 The Advantage of Factorials

The advantage of factorial designs can be easily illustrated. Suppose we have two factors $A$ and $B$, each at two levels. We denote the levels of the factors by $A^-$, $A^+$, $B^-$, and $B^+$. Information on both factors could be obtained by varying the factors one at a time, as shown in Figure 5.7. The effect of changing factor $A$ is given by $A^+B^- - A^-B^-$, and the effect of changing factor $B$ is given by $A^-B^+ - A^-B^-$. Because experimental error is present, it is desirable to take two observations, say, at each treatment combination and estimate the effects of the factors using average responses. Thus, a total of six observations are required.

### PDF page 203 (book page 187)

**FIGURE 5.7** A one-factor-at-a-time experiment

*An L-shaped path in the two-factor space connects $A^-B^-$ to $A^-B^+$ and to $A^+B^-$. The $A^+B^+$ combination is absent.*

**FIGURE 5.8** Relative efficiency of a factorial design to a one-factor-at-a-time experiment (two factor levels)

*Relative efficiency rises linearly with the number of factors: 1.5, 2.0, 2.5, 3.0, and 3.5 for two through six factors.*

If a factorial experiment had been performed, an additional treatment combination, $A^+B^+$, would have been taken. Now, using just four observations, two estimates of the $A$ effect can be made: $A^+B^- - A^-B^-$ and $A^+B^+ - A^-B^+$. Similarly, two estimates of the $B$ effect can be made. These two estimates of each main effect could be averaged to produce average main effects that are *just as precise* as those from the single-factor experiment, but only four total observations are required and we would say that the relative efficiency of the factorial design to the one-factor-at-a-time experiment is $(6/4)=1.5$. Generally, this relative efficiency will increase as the number of factors increases, as shown in Figure 5.8.

Now suppose interaction is present. If the one-factor-at-a-time design indicated that $A^-B^+$ and $A^+B^-$ gave better responses than $A^-B^-$, a logical conclusion would be that $A^+B^+$ would be even better. However, if interaction is present, this conclusion may be *seriously in error*. For an example, refer to the experiment in Figure 5.2.

In summary, note that factorial designs have several advantages. They are more efficient than one-factor-at-a-time experiments. Furthermore, a factorial design is necessary when interactions may be present to avoid misleading conclusions. Finally, factorial designs allow the effects of a factor to be estimated at several levels of the other factors, yielding conclusions that are valid over a range of experimental conditions.

## 5.3 The Two-Factor Factorial Design

### 5.3.1 An Example

The simplest types of factorial designs involve only two factors or sets of treatments. There are $a$ levels of factor $A$ and $b$ levels of factor $B$, and these are arranged in a factorial design; that is, each replicate of the experiment contains all $ab$ treatment combinations. In general, there are $n$ replicates.

As an example of a factorial design involving two factors, an engineer is designing a battery for use in a device that will be subjected to some extreme variations in temperature. The only design parameter that he can select at this point is the plate material for the battery, and he has three possible choices. When the device is manufactured and is shipped to the field, the engineer has no control over the temperature extremes that the device will encounter, and he knows from experience that temperature will probably affect the effective battery life. However, temperature can be controlled in the product development laboratory for the purposes of a test.

### PDF page 204 (book page 188)

**TABLE 5.1** Life (in hours) Data for the Battery Design Example

| Material Type | Temperature 15°F | Temperature 70°F | Temperature 125°F |
|---:|---|---|---|
| 1 | 130, 155, 74, 180 | 34, 40, 80, 75 | 20, 70, 82, 58 |
| 2 | 150, 188, 159, 126 | 136, 122, 106, 115 | 25, 70, 58, 45 |
| 3 | 138, 110, 168, 160 | 174, 120, 150, 139 | 96, 104, 82, 60 |

The engineer decides to test all three plate materials at three temperature levels—15, 70, and 125°F—because these temperature levels are consistent with the product end-use environment. Because there are two factors at three levels, this design is sometimes called a $3^2$ **factorial design**. Four batteries are tested at each combination of plate material and temperature, and all 36 tests are run in random order. The experiment and the resulting observed battery life data are given in Table 5.1.

In this problem the engineer wants to answer the following questions:

1. What effects do material type and temperature have on the life of the battery?
2. Is there a choice of material that would give *uniformly long life regardless of temperature*?

This last question is particularly important. It may be possible to find a material alternative that is not greatly affected by temperature. If this is so, the engineer can make the battery **robust** to temperature variation in the field. This is an example of using statistical experimental design for **robust product design**, a very important engineering problem.

This design is a specific example of the general case of a two-factor factorial. To pass to the general case, let $y_{ijk}$ be the observed response when factor $A$ is at the $i$th level ($i=1,2,\ldots,a$) and factor $B$ is at the $j$th level ($j=1,2,\ldots,b$) for the $k$th replicate ($k=1,2,\ldots,n$). In general, a two-factor factorial experiment will appear as in Table 5.2. The order in which the $abn$ observations are taken is selected at random so that this design is a **completely randomized design**.

The observations in a factorial experiment can be described by a model. There are several ways to write the model for a factorial experiment. The **effects model** is

$$
y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,n
\end{cases}
\tag{5.1}
$$

where $\mu$ is the overall mean effect, $\tau_i$ is the effect of the $i$th level of the row factor $A$, $\beta_j$ is the effect of the $j$th level of column factor $B$, $(\tau\beta)_{ij}$ is the effect of the interaction between $\tau_i$ and $\beta_j$, and $\epsilon_{ijk}$ is a random error component. Both factors are assumed to be **fixed**, and the treatment effects are defined as deviations from the overall mean, so $\sum_{i=1}^{a}\tau_i=0$ and $\sum_{j=1}^{b}\beta_j=0$. Similarly, the interaction effects are fixed and are defined such that $\sum_{i=1}^{a}(\tau\beta)_{ij}=\sum_{j=1}^{b}(\tau\beta)_{ij}=0$. Because there are $n$ replicates of the experiment, there are $abn$ total observations.

### PDF page 205 (book page 189)

**TABLE 5.2** General Arrangement for a Two-Factor Factorial Design

| Factor $A$ | Factor $B=1$ | Factor $B=2$ | $\cdots$ | Factor $B=b$ |
|---:|---|---|---|---|
| 1 | $y_{111},y_{112},\ldots,y_{11n}$ | $y_{121},y_{122},\ldots,y_{12n}$ | | $y_{1b1},y_{1b2},\ldots,y_{1bn}$ |
| 2 | $y_{211},y_{212},\ldots,y_{21n}$ | $y_{221},y_{222},\ldots,y_{22n}$ | | $y_{2b1},y_{2b2},\ldots,y_{2bn}$ |
| $\vdots$ | | | | |
| $a$ | $y_{a11},y_{a12},\ldots,y_{a1n}$ | $y_{a21},y_{a22},\ldots,y_{a2n}$ | | $y_{ab1},y_{ab2},\ldots,y_{abn}$ |

Another possible model for a factorial experiment is the **means model**

$$
y_{ijk}=\mu_{ij}+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,n
\end{cases}
$$

where the mean of the $ij$th cell is

$$
\mu_{ij}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}
$$

We could also use a **regression model** as in Section 5.1. Regression models are particularly useful when one or more of the factors in the experiment are quantitative. Throughout most of this chapter we will use the effects model (Equation 5.1) with an illustration of the regression model in Section 5.5.

In the two-factor factorial, both row and column factors (or treatments), $A$ and $B$, are of equal interest. Specifically, we are interested in testing hypotheses about the equality of row treatment effects, say

$$
\begin{aligned}
H_0&:\tau_1=\tau_2=\cdots=\tau_a=0\\
H_1&:\text{at least one }\tau_i\ne0
\end{aligned}
\tag{5.2a}
$$

and the equality of column treatment effects, say

$$
\begin{aligned}
H_0&:\beta_1=\beta_2=\cdots=\beta_b=0\\
H_1&:\text{at least one }\beta_j\ne0
\end{aligned}
\tag{5.2b}
$$

We are also interested in determining whether row and column treatments *interact*. Thus, we also wish to test

$$
\begin{aligned}
H_0&:(\tau\beta)_{ij}=0 && \text{for all }i,j\\
H_1&:\text{at least one }(\tau\beta)_{ij}\ne0
\end{aligned}
\tag{5.2c}
$$

We now discuss how these hypotheses are tested using a **two-factor analysis of variance**.

### 5.3.2 Statistical Analysis of the Fixed Effects Model

Let $y_{i..}$ denote the total of all observations under the $i$th level of factor $A$, $y_{.j.}$ denote the total of all observations under the $j$th level of factor $B$, $y_{ij.}$ denote the total of all observations in the

### PDF page 206 (book page 190)

$ij$th cell, and $y_{...}$ denote the grand total of all the observations. Define $\bar{y}_{i..}$, $\bar{y}_{.j.}$, $\bar{y}_{ij.}$, and $\bar{y}_{...}$ as the corresponding row, column, cell, and grand averages. Expressed mathematically,

$$
\begin{aligned}
y_{i..}&=\sum_{j=1}^{b}\sum_{k=1}^{n}y_{ijk},
&\bar{y}_{i..}&=\frac{y_{i..}}{bn},
&i&=1,2,\ldots,a\\
y_{.j.}&=\sum_{i=1}^{a}\sum_{k=1}^{n}y_{ijk},
&\bar{y}_{.j.}&=\frac{y_{.j.}}{an},
&j&=1,2,\ldots,b\\
y_{ij.}&=\sum_{k=1}^{n}y_{ijk},
&\bar{y}_{ij.}&=\frac{y_{ij.}}{n},
&i&=1,2,\ldots,a;\quad j=1,2,\ldots,b\\
y_{...}&=\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}y_{ijk},
&\bar{y}_{...}&=\frac{y_{...}}{abn}
\end{aligned}
\tag{5.3}
$$

The **total corrected sum of squares** may be written as

$$
\begin{aligned}
\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}(y_{ijk}-\bar{y}_{...})^2
={}&\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}
\big[(\bar{y}_{i..}-\bar{y}_{...})+(\bar{y}_{.j.}-\bar{y}_{...})\\
&\quad+(\bar{y}_{ij.}-\bar{y}_{i..}-\bar{y}_{.j.}+\bar{y}_{...})
+(y_{ijk}-\bar{y}_{ij.})\big]^2\\
={}&bn\sum_{i=1}^{a}(\bar{y}_{i..}-\bar{y}_{...})^2
+an\sum_{j=1}^{b}(\bar{y}_{.j.}-\bar{y}_{...})^2\\
&+n\sum_{i=1}^{a}\sum_{j=1}^{b}
(\bar{y}_{ij.}-\bar{y}_{i..}-\bar{y}_{.j.}+\bar{y}_{...})^2\\
&+\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}
(y_{ijk}-\bar{y}_{ij.})^2
\end{aligned}
\tag{5.4}
$$

because the six cross products on the right-hand side are zero. Notice that the total sum of squares has been partitioned into a sum of squares due to “rows,” or factor $A$, ($SS_A$); a sum of squares due to “columns,” or factor $B$, ($SS_B$); a sum of squares due to the interaction between $A$ and $B$, ($SS_{AB}$); and a sum of squares due to error, ($SS_E$). This is the fundamental ANOVA equation for the two-factor factorial. From the last component on the right-hand side of Equation 5.4, we see that there must be at least two replicates ($n\geq2$) to obtain an error sum of squares.

We may write Equation 5.4 symbolically as

$$
SS_T=SS_A+SS_B+SS_{AB}+SS_E
\tag{5.5}
$$

The number of degrees of freedom associated with each sum of squares is

| Effect | Degrees of Freedom |
|---|---:|
| $A$ | $a-1$ |
| $B$ | $b-1$ |
| $AB$ interaction | $(a-1)(b-1)$ |
| Error | $ab(n-1)$ |
| Total | $abn-1$ |

We may justify this allocation of the $abn-1$ total degrees of freedom to the sums of squares as follows: The main effects $A$ and $B$ have $a$ and $b$ levels, respectively; therefore they have $a-1$ and $b-1$ degrees of freedom as shown. The interaction degrees of freedom are simply the number of degrees of freedom for cells (which is $ab-1$) minus the number of degrees of freedom for the two main effects $A$ and $B$; that is, $ab-1-(a-1)-(b-1)=$

### PDF page 207 (book page 191)

$(a-1)(b-1)$. Within each of the $ab$ cells, there are $n-1$ degrees of freedom between the $n$ replicates; thus there are $ab(n-1)$ degrees of freedom for error. Note that the number of degrees of freedom on the right-hand side of Equation 5.5 adds to the total number of degrees of freedom.

Each sum of squares divided by its degrees of freedom is a **mean square**. The expected values of the mean squares are

$$
E(MS_A)=E\left(\frac{SS_A}{a-1}\right)
=\sigma^2+\frac{bn\sum_{i=1}^{a}\tau_i^2}{a-1}
$$

$$
E(MS_B)=E\left(\frac{SS_B}{b-1}\right)
=\sigma^2+\frac{an\sum_{j=1}^{b}\beta_j^2}{b-1}
$$

$$
E(MS_{AB})=E\left(\frac{SS_{AB}}{(a-1)(b-1)}\right)
=\sigma^2+\frac{n\sum_{i=1}^{a}\sum_{j=1}^{b}(\tau\beta)_{ij}^2}
{(a-1)(b-1)}
$$

and

$$
E(MS_E)=E\left(\frac{SS_E}{ab(n-1)}\right)=\sigma^2
$$

Notice that if the null hypotheses of no row treatment effects, no column treatment effects, and no interaction are true, then $MS_A$, $MS_B$, $MS_{AB}$, and $MS_E$ all estimate $\sigma^2$. However, if there are differences between row treatment effects, say, then $MS_A$ will be larger than $MS_E$. Similarly, if there are column treatment effects or interaction present, then the corresponding mean squares will be larger than $MS_E$. Therefore, to test the significance of both main effects and their interaction, simply divide the corresponding mean square by the error mean square. Large values of this ratio imply that the data do not support the null hypothesis.

If we assume that the model (Equation 5.1) is adequate and that the error terms $\epsilon_{ijk}$ are normally and independently distributed with constant variance $\sigma^2$, then each of the ratios of mean squares $MS_A/MS_E$, $MS_B/MS_E$, and $MS_{AB}/MS_E$ is distributed as $F$ with $a-1$, $b-1$, and $(a-1)(b-1)$ numerator degrees of freedom, respectively, and $ab(n-1)$ denominator degrees of freedom,^1 and the critical region would be the upper tail of the $F$ distribution. The test procedure is usually summarized in an **analysis of variance table**, as shown in Table 5.3.

Computationally, we almost always employ a statistical software package to conduct an ANOVA. However, manual computing of the sums of squares in Equation 5.5 is straightforward. One could write out the individual elements of the ANOVA identity

$$
\begin{aligned}
y_{ijk}-\bar{y}_{...}
={}&(\bar{y}_{i..}-\bar{y}_{...})+(\bar{y}_{.j.}-\bar{y}_{...})\\
&+(\bar{y}_{ij.}-\bar{y}_{i..}-\bar{y}_{.j.}+\bar{y}_{...})
+(y_{ijk}-\bar{y}_{ij.})
\end{aligned}
$$

and calculate them in the columns of a spreadsheet. Then each column could be squared and summed to produce the ANOVA sums of squares. Computing formulas in terms of row, column, and cell totals can also be used. The total sum of squares is computed as usual by

$$
SS_T=\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}y_{ijk}^2-\frac{y_{...}^2}{abn}
\tag{5.6}
$$

---

^1 The $F$ test may be viewed as an approximation to a randomization test, as noted previously.

### PDF page 208 (book page 192)

**TABLE 5.3** The Analysis of Variance Table for the Two-Factor Factorial, Fixed Effects Model

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---:|---:|---:|---:|
| $A$ treatments | $SS_A$ | $a-1$ | $MS_A=SS_A/(a-1)$ | $F_0=MS_A/MS_E$ |
| $B$ treatments | $SS_B$ | $b-1$ | $MS_B=SS_B/(b-1)$ | $F_0=MS_B/MS_E$ |
| Interaction | $SS_{AB}$ | $(a-1)(b-1)$ | $MS_{AB}=SS_{AB}/[(a-1)(b-1)]$ | $F_0=MS_{AB}/MS_E$ |
| Error | $SS_E$ | $ab(n-1)$ | $MS_E=SS_E/[ab(n-1)]$ | |
| Total | $SS_T$ | $abn-1$ | | |

The sums of squares for the main effects are

$$
SS_A=\frac{1}{bn}\sum_{i=1}^{a}y_{i..}^2-\frac{y_{...}^2}{abn}
\tag{5.7}
$$

and

$$
SS_B=\frac{1}{an}\sum_{j=1}^{b}y_{.j.}^2-\frac{y_{...}^2}{abn}
\tag{5.8}
$$

It is convenient to obtain the $SS_{AB}$ in two stages. First we compute the sum of squares between the $ab$ cell totals, which is called the sum of squares due to “subtotals”:

$$
SS_{\text{Subtotals}}=\frac{1}{n}\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij.}^2-\frac{y_{...}^2}{abn}
$$

This sum of squares also contains $SS_A$ and $SS_B$. Therefore, the second step is to compute $SS_{AB}$ as

$$
SS_{AB}=SS_{\text{Subtotals}}-SS_A-SS_B
\tag{5.9}
$$

We may compute $SS_E$ by subtraction as

$$
SS_E=SS_T-SS_{AB}-SS_A-SS_B
\tag{5.10}
$$

or

$$
SS_E=SS_T-SS_{\text{Subtotals}}
$$

### EXAMPLE 5.1 — The Battery Design Experiment

Table 5.4 presents the effective life (in hours) observed in the battery design example described in Section 5.3.1. The row and column totals are shown in the margins of the table, and the circled numbers are the cell totals.

### PDF page 209 (book page 193)

**TABLE 5.4** Life Data (in hours) for the Battery Design Experiment

| Material Type | Temperature 15°F (observations; cell total) | Temperature 70°F (observations; cell total) | Temperature 125°F (observations; cell total) | $y_{i..}$ |
|---:|---|---|---|---:|
| 1 | 130, 155, 74, 180; 539 | 34, 40, 80, 75; 229 | 20, 70, 82, 58; 230 | 998 |
| 2 | 150, 188, 159, 126; 623 | 136, 122, 106, 115; 479 | 25, 70, 58, 45; 198 | 1300 |
| 3 | 138, 110, 168, 160; 576 | 174, 120, 150, 139; 583 | 96, 104, 82, 60; 342 | 1501 |
| $y_{.j.}$ | 1738 | 1291 | 770 | $3799=y_{...}$ |

Using Equations 5.6 through 5.10, the sums of squares are computed as follows:

$$
\begin{aligned}
SS_T
&=\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{n}y_{ijk}^2-\frac{y_{...}^2}{abn}\\
&=(130)^2+(155)^2+(74)^2+\cdots+(60)^2-\frac{(3799)^2}{36}\\
&=77{,}646.97
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Material}}
&=\frac{1}{bn}\sum_{i=1}^{a}y_{i..}^2-\frac{y_{...}^2}{abn}\\
&=\frac{1}{(3)(4)}[(998)^2+(1300)^2+(1501)^2]-\frac{(3799)^2}{36}\\
&=10{,}683.72
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Temperature}}
&=\frac{1}{an}\sum_{j=1}^{b}y_{.j.}^2-\frac{y_{...}^2}{abn}\\
&=\frac{1}{(3)(4)}[(1738)^2+(1291)^2+(770)^2]-\frac{(3799)^2}{36}\\
&=39{,}118.72
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Interaction}}
&=\frac{1}{n}\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij.}^2-\frac{y_{...}^2}{abn}
-SS_{\text{Material}}-SS_{\text{Temperature}}\\
&=\frac{1}{4}[(539)^2+(229)^2+\cdots+(342)^2]
-\frac{(3799)^2}{36}-10{,}683.72-39{,}118.72\\
&=9613.78
\end{aligned}
$$

and

$$
\begin{aligned}
SS_E
&=SS_T-SS_{\text{Material}}-SS_{\text{Temperature}}-SS_{\text{Interaction}}\\
&=77{,}646.97-10{,}683.72-39{,}118.72-9613.78\\
&=18{,}230.75
\end{aligned}
$$

The ANOVA is shown in Table 5.5. Because $F_{0.05,4,27}=2.73$, we conclude that there is a significant interaction between material types and temperature. Furthermore, $F_{0.05,2,27}=3.35$, so the main effects of material type and temperature are also significant. Table 5.5 also shows the $P$-values for the test statistics.

To assist in interpreting the results of this experiment, it is helpful to construct a graph of the average responses at

### PDF page 210 (book page 194)

**TABLE 5.5** Analysis of Variance for Battery Life Data

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|
| Material types | 10,683.72 | 2 | 5,341.86 | 7.91 | 0.0020 |
| Temperature | 39,118.72 | 2 | 19,559.36 | 28.97 | $<0.0001$ |
| Interaction | 9,613.78 | 4 | 2,403.44 | 3.56 | 0.0186 |
| Error | 18,230.75 | 27 | 675.21 | | |
| Total | 77,646.97 | 35 | | | |

each treatment combination. This graph is shown in Figure 5.9. The significant interaction is indicated by the lack of parallelism of the lines. In general, longer life is attained at low temperature, regardless of material type. Changing from low to intermediate temperature, battery life with material type 3 may actually increase, whereas it decreases for types 1 and 2. From intermediate to high temperature, battery life decreases for material types 2 and 3 and is essentially unchanged for type 1. Material type 3 seems to give the best results if we want less loss of effective life as the temperature changes.

**FIGURE 5.9** Material type–temperature plot for Example 5.1

*Average battery life is plotted at 15, 70, and 125°F. Material type 1 falls from about 135 to about 57 and then stays near 58; type 2 falls from about 156 to 120 to 50; type 3 changes from about 144 to 146 to 86.*

***Multiple Comparisons.*** When the ANOVA indicates that row or column means differ, it is usually of interest to make comparisons between the individual row or column means to discover the specific differences. The multiple comparison methods discussed in Chapter 3 are useful in this regard.

We now illustrate the use of Tukey’s test on the battery life data in Example 5.1. Note that in this experiment, interaction is significant. When interaction is significant, comparisons between the means of one factor (e.g., $A$) may be obscured by the $AB$ interaction. One approach to this situation is to fix factor $B$ at a specific level and apply Tukey’s test to the means of factor $A$ at that level. To illustrate, suppose that in Example 5.1 we are interested in detecting differences among the means of the three material types. Because interaction is significant, we make this comparison at just one level of temperature, say level 2 (70°F). We assume that the best estimate of the error variance is the $MS_E$ from the ANOVA table,

### PDF page 211 (book page 195)

utilizing the assumption that the experimental error variance is the same over all treatment combinations.

The three material type averages at 70°F arranged in ascending order are

$$
\begin{aligned}
\bar{y}_{12.}&=57.25 &&\text{(material type 1)}\\
\bar{y}_{22.}&=119.75 &&\text{(material type 2)}\\
\bar{y}_{32.}&=145.75 &&\text{(material type 3)}
\end{aligned}
$$

and

$$
\begin{aligned}
T_{0.05}
&=q_{0.05}(3,27)\sqrt{\frac{MS_E}{n}}\\
&=3.50\sqrt{\frac{675.21}{4}}\\
&=45.47
\end{aligned}
$$

where we obtained $q_{0.05}(3,27)\simeq3.50$ by interpolation in Appendix Table VII. The pairwise comparisons yield

$$
\begin{aligned}
3\text{ vs. }1:\quad&145.75-57.25=88.50>T_{0.05}=45.47\\
3\text{ vs. }2:\quad&145.75-119.75=26.00<T_{0.05}=45.47\\
2\text{ vs. }1:\quad&119.75-57.25=62.50>T_{0.05}=45.47
\end{aligned}
$$

This analysis indicates that at the temperature level 70°F, the mean battery life is the same for material types 2 and 3, and that the mean battery life for material type 1 is significantly lower in comparison to both types 2 and 3.

If interaction is significant, the experimenter could compare all $ab$ cell means to determine which ones differ significantly. In this analysis, differences between cell means include interaction effects as well as both main effects. In Example 5.1, this would give 36 comparisons between all possible pairs of the nine cell means.

***Computer Output.*** Figure 5.10 presents condensed computer output for the battery life data in Example 5.1. Figure 5.10a contains Design-Expert output and Figure 5.10b contains JMP output. Note that

$$
\begin{aligned}
SS_{\text{Model}}
&=SS_{\text{Material}}+SS_{\text{Temperature}}+SS_{\text{Interaction}}\\
&=10{,}683.72+39{,}118.72+9613.78\\
&=59{,}416.22
\end{aligned}
$$

with 8 degrees of freedom. An $F$ test is displayed for the model source of variation. The $P$-value is small ($<0.0001$), so the interpretation of this test is that at least one of the three terms in the model is significant. The tests on the individual model terms ($A$, $B$, $AB$) follow. Also,

$$
R^2=\frac{SS_{\text{Model}}}{SS_{\text{Total}}}
=\frac{59{,}416.22}{77{,}646.97}=0.7652
$$

That is, about 77 percent of the variability in the battery life is explained by the plate material in the battery, the temperature, and the material type–temperature interaction. The residuals from the fitted model are displayed on the Design-Expert computer output and the JMP output contains a plot of the residuals versus the predicted response. We now discuss the use of these residuals and residual plots in model adequacy checking.

### PDF page 212 (book page 196)

**FIGURE 5.10** Computer output for Example 5.1. (a) Design-Expert output; (b) JMP output

**(a) Design-Expert output**

**Response: Life in Hours — ANOVA for Selected Factorial Model — Analysis of Variance Table [Partial Sum of Squares]**

| Source | Sum of Squares | DF | Mean Square | $F$ Value | Prob $>F$ | |
|---|---:|---:|---:|---:|---:|---|
| Model | 59416.22 | 8 | 7427.03 | 11.00 | $<0.0001$ | significant |
| $A$ | 10683.72 | 2 | 5341.86 | 7.91 | 0.0020 | |
| $B$ | 39118.72 | 2 | 19559.36 | 28.97 | $<0.0001$ | |
| $AB$ | 9613.78 | 4 | 2403.44 | 3.56 | 0.0186 | |
| Residual | 18230.75 | 27 | 675.21 | | | |
| Lack of Fit | 0.000 | 0 | | | | |
| Pure Error | 18230.75 | 27 | 675.21 | | | |
| Cor Total | 77646.97 | 35 | | | | |

| Statistic | Value | Statistic | Value |
|---|---:|---|---:|
| Std. Dev. | 25.98 | R-Squared | 0.7652 |
| Mean | 105.53 | Adj R-Squared | 0.6956 |
| C.V. | 24.62 | Pred R-Squared | 0.5826 |
| PRESS | 32410.22 | Adeq Precision | 8.178 |

**Diagnostics Case Statistics**

| Standard Order | Actual Value | Predicted Value | Residual | Leverage | Student Residual | Cook’s Distance | Outlier $t$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 130.00 | 134.75 | −4.75 | 0.250 | −0.211 | 0.002 | −0.207 |
| 2 | 74.00 | 134.75 | −60.75 | 0.250 | −2.700 | 0.270 | −3.100 |
| 3 | 155.00 | 134.75 | 20.25 | 0.250 | 0.900 | 0.030 | 0.897 |
| 4 | 180.00 | 134.75 | 45.25 | 0.250 | 2.011 | 0.150 | 2.140 |
| 5 | 150.00 | 155.75 | −5.75 | 0.250 | −0.256 | 0.002 | −0.251 |
| 6 | 159.00 | 155.75 | 3.25 | 0.250 | 0.144 | 0.001 | 0.142 |
| 7 | 188.00 | 155.75 | 32.25 | 0.250 | 1.433 | 0.076 | 1.463 |
| 8 | 126.00 | 155.75 | −29.75 | 0.250 | −1.322 | 0.065 | −1.341 |
| 9 | 138.00 | 144.00 | −6.00 | 0.250 | −0.267 | 0.003 | −0.262 |
| 10 | 168.00 | 144.00 | 24.00 | 0.250 | 1.066 | 0.042 | 1.069 |
| 11 | 110.00 | 144.00 | −34.00 | 0.250 | −1.511 | 0.085 | −1.550 |
| 12 | 160.00 | 144.00 | 16.00 | 0.250 | 0.711 | 0.019 | 0.704 |
| 13 | 34.00 | 57.25 | −23.25 | 0.250 | −1.033 | 0.040 | −1.035 |
| 14 | 80.00 | 57.25 | 22.75 | 0.250 | 1.011 | 0.038 | 1.011 |
| 15 | 40.00 | 57.25 | −17.25 | 0.250 | −0.767 | 0.022 | −0.761 |
| 16 | 75.00 | 57.25 | 17.75 | 0.250 | 0.789 | 0.023 | 0.783 |
| 17 | 136.00 | 119.75 | 16.25 | 0.250 | 0.722 | 0.019 | 0.716 |
| 18 | 106.00 | 119.75 | −13.75 | 0.250 | −0.611 | 0.014 | −0.604 |
| 19 | 122.00 | 119.75 | 2.25 | 0.250 | 0.100 | 0.000 | 0.098 |
| 20 | 115.00 | 119.75 | −4.75 | 0.250 | −0.211 | 0.002 | −0.207 |
| 21 | 174.00 | 145.75 | 28.25 | 0.250 | 1.255 | 0.058 | 1.269 |
| 22 | 150.00 | 145.75 | 4.25 | 0.250 | 0.189 | 0.001 | 0.185 |
| 23 | 120.00 | 145.75 | −25.75 | 0.250 | −1.144 | 0.048 | −1.151 |
| 24 | 139.00 | 145.75 | −6.75 | 0.250 | −0.300 | 0.003 | −0.295 |
| 25 | 20.00 | 57.50 | −37.50 | 0.250 | −1.666 | 0.103 | −1.726 |
| 26 | 82.00 | 57.50 | 24.50 | 0.250 | 1.089 | 0.044 | 1.093 |
| 27 | 70.00 | 57.50 | 12.50 | 0.250 | 0.555 | 0.011 | 0.548 |
| 28 | 58.00 | 57.50 | 0.50 | 0.250 | 0.022 | 0.000 | 0.022 |
| 29 | 25.00 | 49.50 | −24.50 | 0.250 | −1.089 | 0.044 | −1.093 |
| 30 | 58.00 | 49.50 | 8.50 | 0.250 | 0.378 | 0.005 | 0.372 |
| 31 | 70.00 | 49.50 | 20.50 | 0.250 | 0.911 | 0.031 | 0.908 |
| 32 | 45.00 | 49.50 | −4.50 | 0.250 | −0.200 | 0.001 | −0.196 |
| 33 | 96.00 | 85.50 | 10.50 | 0.250 | 0.467 | 0.008 | 0.460 |
| 34 | 82.00 | 85.50 | −3.50 | 0.250 | −0.156 | 0.001 | −0.153 |
| 35 | 104.00 | 85.50 | 18.50 | 0.250 | 0.822 | 0.025 | 0.817 |
| 36 | 60.00 | 85.50 | −25.50 | 0.250 | −1.133 | 0.048 | −1.139 |

### PDF page 213 (book page 197)

**FIGURE 5.10 (Continued)**

**(b) JMP output**

**Response Life — Whole Model — Actual by Predicted Plot**

*Actual life is plotted against predicted life from 0 to 200, with the fitted line and confidence bands. The display reports “Life predicted $P<.0001$; RSq = 0.77; RMSE = 25.985.”*

**Summary of Fit**

| Statistic | Value |
|---|---:|
| RSquare | 0.76521 |
| RSquare Adj | 0.695642 |
| Root Mean Square Error | 25.98486 |
| Mean of Response | 105.5278 |
| Observations (or Sum Wgts) | 36 |

**Analysis of Variance**

| Source | DF | Sum of Squares | Mean Square | $F$ Ratio |
|---|---:|---:|---:|---:|
| Model | 8 | 59416.222 | 7427.03 | 10.9995 |
| Error | 27 | 18230.750 | 675.21 | Prob $>F$ |
| C. Total | 35 | 77646.972 | | $<.001$ |

**Effect Tests**

| Source | Nparm | DF | Sum of Squares | $F$ Ratio | Prob $>F$ |
|---|---:|---:|---:|---:|---:|
| Material Type | 2 | 2 | 10683.722 | 7.9114 | 0.0020 |
| Temperature | 2 | 2 | 39118.722 | 28.9677 | $<.0001$ |
| Material Type Temperature | 4 | 4 | 9613.778 | 3.5595 | 0.0186 |

**Residual by Predicted Plot**

*Residuals are plotted against predicted life. They range approximately from −60 to 48 and are scattered around the zero line, with predicted values between about 50 and 155.*

### PDF page 214 (book page 198)

**TABLE 5.6** Residuals for Example 5.1

| Material Type | Temperature 15°F | Temperature 70°F | Temperature 125°F |
|---:|---|---|---|
| 1 | −4.75, 20.25, −60.75, 45.25 | −23.25, −17.25, 22.75, 17.75 | −37.50, 12.50, 24.50, 0.50 |
| 2 | −5.75, 32.25, 3.25, −29.75 | 16.25, 2.25, −13.75, −4.75 | −24.50, 20.50, 8.50, −4.50 |
| 3 | −6.00, −34.00, 24.00, 16.00 | 28.25, −25.75, 4.25, −6.75 | 10.50, 18.50, −3.50, −25.50 |

### 5.3.3 Model Adequacy Checking

Before the conclusions from the ANOVA are adopted, the adequacy of the underlying model should be checked. As before, the primary diagnostic tool is **residual analysis**. The residuals for the two-factor factorial model with interaction are

$$
e_{ijk}=y_{ijk}-\hat{y}_{ijk}
\tag{5.11}
$$

and because the fitted value $\hat{y}_{ijk}=\bar{y}_{ij.}$ (the average of the observations in the $ij$th cell), Equation 5.11 becomes

$$
e_{ijk}=y_{ijk}-\bar{y}_{ij.}
\tag{5.12}
$$

The residuals from the battery life data in Example 5.1 are shown in the Design-Expert computer output (Figure 5.10a) and in Table 5.6. The normal probability plot of these residuals (Figure 5.11) does not reveal anything particularly troublesome, although the largest negative residual (−60.75 at 15°F for material type 1) does stand out somewhat from the others. The standardized value of this residual is $-60.75/\sqrt{675.21}=-2.34$, and this is the only residual whose absolute value is larger than 2.

Figure 5.12 plots the residuals versus the fitted values $\hat{y}_{ijk}$. This plot was also shown in the JMP computer output in Figure 5.10b. There is some mild tendency for the variance of the residuals to increase as the battery life increases. Figures 5.13 and 5.14 plot the residuals versus material types and temperature, respectively. Both plots indicate mild inequality of variance, with the treatment combination of 15°F and material type 1 possibly having larger variance than the others.

From Table 5.6 we see that the 15°F-material type 1 cell contains both extreme residuals (−60.75 and 45.25). These two residuals are primarily responsible for the inequality of variance detected in Figures 5.12, 5.13, and 5.14. Reexamination of the data does not reveal any obvious problem, such as an error in recording, so we accept these responses as legitimate. It is possible that this particular treatment combination produces slightly more erratic battery life than the others. The problem, however, is not severe enough to have a dramatic impact on the analysis and conclusions.

### 5.3.4 Estimating the Model Parameters

The parameters in the effects model for two-factor factorial

$$
y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\epsilon_{ijk}
\tag{5.13}
$$

### PDF page 215 (book page 199)

**FIGURE 5.11** Normal probability plot of residuals for Example 5.1

*The 36 residuals, spanning −60.75 to 45.25, lie approximately along the normal-probability reference line. The −60.75 residual is the most conspicuous departure.*

**FIGURE 5.12** Plot of residuals versus $\hat{y}_{ijk}$ for Example 5.1

*Residuals range from about −61 to 45 over fitted values from about 50 to 156. Their spread is somewhat larger at the higher fitted values.*

**FIGURE 5.13** Plot of residuals versus material type for Example 5.1

*Four residuals from each of three temperatures are plotted at each material type. Material type 1 has the widest range, approximately −61 to 45.*

**FIGURE 5.14** Plot of residuals versus temperature for Example 5.1

*Twelve residuals are plotted at each of 15, 70, and 125°F. The 15°F group has the widest range, approximately −61 to 45.*

may be estimated by least squares. Because the model has $1+a+b+ab$ parameters to be estimated, there are $1+a+b+ab$ normal equations. Using the method of Section 3.9, we find that it is not difficult to show that the normal equations are

$$
\mu:\quad
abn\hat{\mu}+bn\sum_{i=1}^{a}\hat{\tau}_i
+an\sum_{j=1}^{b}\hat{\beta}_j
+n\sum_{i=1}^{a}\sum_{j=1}^{b}(\widehat{\tau\beta})_{ij}
=y_{...}
\tag{5.14a}
$$

$$
\tau_i:\quad
bn\hat{\mu}+bn\hat{\tau}_i
+n\sum_{j=1}^{b}\hat{\beta}_j
+n\sum_{j=1}^{b}(\widehat{\tau\beta})_{ij}
=y_{i..},
\qquad i=1,2,\ldots,a
\tag{5.14b}
$$

### PDF page 216 (book page 200)

$$
\beta_j:\quad
an\hat{\mu}+n\sum_{i=1}^{a}\hat{\tau}_i
+an\hat{\beta}_j
+n\sum_{i=1}^{a}(\widehat{\tau\beta})_{ij}
=y_{.j.},
\qquad j=1,2,\ldots,b
\tag{5.14c}
$$

$$
(\tau\beta)_{ij}:\quad
n\hat{\mu}+n\hat{\tau}_i+n\hat{\beta}_j
+n(\widehat{\tau\beta})_{ij}
=y_{ij.}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b
\end{cases}
\tag{5.14d}
$$

For convenience, we have shown the parameter corresponding to each normal equation on the left in Equations 5.14.

The effects model (Equation 5.13) is an overparameterized model. Notice that the $a$ equations in Equation 5.14b sum to Equation 5.14a and that the $b$ equations of Equation 5.14c sum to Equation 5.14a. Also summing Equation 5.14d over $j$ for a particular $i$ will give Equation 5.14b, and summing Equation 5.14d over $i$ for a particular $j$ will give Equation 5.14c. Therefore, there are $a+b+1$ **linear dependencies** in this system of equations, and no unique solution will exist. In order to obtain a solution, we impose the constraints

$$
\sum_{i=1}^{a}\hat{\tau}_i=0
\tag{5.15a}
$$

$$
\sum_{j=1}^{b}\hat{\beta}_j=0
\tag{5.15b}
$$

$$
\sum_{i=1}^{a}(\widehat{\tau\beta})_{ij}=0,
\qquad j=1,2,\ldots,b
\tag{5.15c}
$$

and

$$
\sum_{j=1}^{b}(\widehat{\tau\beta})_{ij}=0,
\qquad i=1,2,\ldots,a
\tag{5.15d}
$$

Equations 5.15a and 5.15b constitute two constraints, whereas Equations 5.15c and 5.15d form $a+b-1$ independent constraints. Therefore, we have $a+b+1$ total constraints, the number needed.

Applying these constraints, the normal equations (Equations 5.14) simplify considerably, and we obtain the solution

$$
\begin{aligned}
\hat{\mu}&=\bar{y}_{...}\\
\hat{\tau}_i&=\bar{y}_{i..}-\bar{y}_{...},
&&i=1,2,\ldots,a\\
\hat{\beta}_j&=\bar{y}_{.j.}-\bar{y}_{...},
&&j=1,2,\ldots,b\\
(\widehat{\tau\beta})_{ij}
&=\bar{y}_{ij.}-\bar{y}_{i..}-\bar{y}_{.j.}+\bar{y}_{...},
&&\begin{cases}i=1,2,\ldots,a\\j=1,2,\ldots,b\end{cases}
\end{aligned}
\tag{5.16}
$$

Notice the considerable intuitive appeal of this solution to the normal equations. Row treatment effects are estimated by the row average minus the grand average; column treatments are estimated by the column average minus the grand average; and the $ij$th interaction is estimated by the $ij$th cell average minus the grand average, the $i$th row effect, and the $j$th column effect.

Using Equation 5.16, we may find the **fitted value** $\hat{y}_{ijk}$ as

$$
\begin{aligned}
\hat{y}_{ijk}
&=\hat{\mu}+\hat{\tau}_i+\hat{\beta}_j+(\widehat{\tau\beta})_{ij}\\
&=\bar{y}_{...}+(\bar{y}_{i..}-\bar{y}_{...})
+(\bar{y}_{.j.}-\bar{y}_{...})\\
&\quad+(\bar{y}_{ij.}-\bar{y}_{i..}-\bar{y}_{.j.}+\bar{y}_{...})\\
&=\bar{y}_{ij.}
\end{aligned}
$$

### PDF page 217 (book page 201)

That is, the $k$th observation in the $ij$th cell is estimated by the average of the $n$ observations in that cell. This result was used in Equation 5.12 to obtain the residuals for the two-factor factorial model.

Because constraints (Equations 5.15) have been used to solve the normal equations, the model parameters are not uniquely estimated. However, certain important functions of the model parameters *are estimable*, that is, uniquely estimated regardless of the constraint chosen. An example is $\tau_i-\tau_u+\overline{(\tau\beta)}_{i.}-\overline{(\tau\beta)}_{u.}$, which might be thought of as the “true” difference between the $i$th and the $u$th levels of factor $A$. Notice that the true difference between the levels of any main effect includes an “average” interaction effect. It is this result that disturbs the tests on main effects in the presence of interaction, as noted earlier. In general, any function of the model parameters that is a linear combination of the left-hand side of the normal equations is estimable. This property was also noted in Chapter 3 when we were discussing the single-factor model. For more information, see the supplemental text material for this chapter.

### 5.3.5 Choice of Sample Size

The operating characteristic curves in Appendix Chart V can be used to assist the experimenter in determining an appropriate sample size (number of replicates, $n$) for a two-factor factorial design. The appropriate value of the parameter $\Phi^2$ and the numerator and denominator degrees of freedom are shown in Table 5.7.

A very effective way to use these curves is to find the smallest value of $\Phi^2$ corresponding to a specified difference between any two treatment means. For example, if the difference in any two row means is $D$, then the minimum value of $\Phi^2$ is

$$
\Phi^2=\frac{nbD^2}{2a\sigma^2}
\tag{5.17}
$$

whereas if the difference in any two column means is $D$, then the minimum value of $\Phi^2$ is

$$
\Phi^2=\frac{naD^2}{2b\sigma^2}
\tag{5.18}
$$

**TABLE 5.7** Operating Characteristic Curve Parameters for Chart V of the Appendix for the Two-Factor Factorial, Fixed Effects Model

| Factor | $\Phi^2$ | Numerator Degrees of Freedom | Denominator Degrees of Freedom |
|---|---|---:|---:|
| $A$ | $\dfrac{bn\sum_{i=1}^{a}\tau_i^2}{a\sigma^2}$ | $a-1$ | $ab(n-1)$ |
| $B$ | $\dfrac{an\sum_{j=1}^{b}\beta_j^2}{b\sigma^2}$ | $b-1$ | $ab(n-1)$ |
| $AB$ | $\dfrac{n\sum_{i=1}^{a}\sum_{j=1}^{b}(\tau\beta)_{ij}^2}{\sigma^2[(a-1)(b-1)+1]}$ | $(a-1)(b-1)$ | $ab(n-1)$ |

### PDF page 218 (book page 202)

Finally, the minimum value of $\Phi^2$ corresponding to a difference of $D$ between any two interaction effects is

$$
\Phi^2=\frac{nD^2}{2\sigma^2[(a-1)(b-1)+1]}
\tag{5.19}
$$

To illustrate the use of these equations, consider the battery life data in Example 5.1. Suppose that before running the experiment we decide that the null hypothesis should be rejected with a high probability if the difference in mean battery life between any two temperatures is as great as 40 hours. Thus a difference of $D=40$ has engineering significance, and if we assume that the standard deviation of battery life is approximately 25, then Equation 5.18 gives

$$
\begin{aligned}
\Phi^2&=\frac{naD^2}{2b\sigma^2}\\
&=\frac{n(3)(40)^2}{2(3)(25)^2}\\
&=1.28n
\end{aligned}
$$

as the minimum value of $\Phi^2$. Assuming that $\alpha=0.05$, we can now use Appendix Table V to construct the following display:

| $n$ | $\Phi^2$ | $\Phi$ | $\nu_1=$ Numerator Degrees of Freedom | $\nu_2=$ Error Degrees of Freedom | $\beta$ |
|---:|---:|---:|---:|---:|---:|
| 2 | 2.56 | 1.60 | 2 | 9 | 0.45 |
| 3 | 3.84 | 1.96 | 2 | 18 | 0.18 |
| 4 | 5.12 | 2.26 | 2 | 27 | 0.06 |

Note that $n=4$ replicates give a $\beta$ risk of about 0.06, or approximately a 94 percent chance of rejecting the null hypothesis if the difference in mean battery life at any two temperature levels is as large as 40 hours. Thus, we conclude that four replicates are enough to provide the desired sensitivity as long as our estimate of the standard deviation of battery life is not seriously in error. If in doubt, the experimenter could repeat the above procedure with other values of $\sigma$ to determine the effect of misestimating this parameter on the sensitivity of the design.

### 5.3.6 The Assumption of No Interaction in a Two-Factor Model

Occasionally, an experimenter feels that a **two-factor model without interaction** is appropriate, say

$$
y_{ijk}=\mu+\tau_i+\beta_j+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,n
\end{cases}
\tag{5.20}
$$

We should be very careful in dispensing with the interaction terms, however, because the presence of significant interaction can have a dramatic impact on the interpretation of the data.

The statistical analysis of a two-factor factorial model without interaction is straightforward. Table 5.8 presents the analysis of the battery life data from Example 5.1, assuming that

### PDF page 219 (book page 203)

**TABLE 5.8** Analysis of Variance for Battery Life Data Assuming No Interaction

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ |
|---|---:|---:|---:|---:|
| Material types | 10,683.72 | 2 | 5,341.86 | 5.95 |
| Temperature | 39,118.72 | 2 | 19,559.36 | 21.78 |
| Error | 27,844.52 | 31 | 898.21 | |
| Total | 77,646.96 | 35 | | |

the no-interaction model (Equation 5.20) applies. As noted previously, both main effects are significant. However, as soon as a residual analysis is performed for these data, it becomes clear that the no-interaction model is inadequate. For the two-factor model without interaction, the fitted values are $\hat{y}_{ijk}=\bar{y}_{i..}+\bar{y}_{.j.}-\bar{y}_{...}$. A plot of $\bar{y}_{ij.}-\hat{y}_{ijk}$ (the cell averages minus the fitted value for that cell) versus the fitted value $\hat{y}_{ijk}$ is shown in Figure 5.15. Now the quantities $\bar{y}_{ij.}-\hat{y}_{ijk}$ may be viewed as the differences between the observed cell means and the estimated cell means assuming no interaction. Any pattern in these quantities is suggestive of the presence of interaction. Figure 5.15 shows a distinct pattern as the quantities $\bar{y}_{ij.}-\hat{y}_{ijk}$ move from positive to negative to positive to negative again. This structure is the result of interaction between material types and temperature.

**FIGURE 5.15** Plot of $\bar{y}_{ij.}-\hat{y}_{ijk}$ versus $\hat{y}_{ijk}$, battery life data

*Nine cell-mean residuals alternate from positive to negative as the no-interaction fitted values increase from about 35 to 155, showing a pronounced structured pattern.*

### 5.3.7 One Observation per Cell

Occasionally, one encounters a two-factor experiment with only a **single replicate**, that is, only one observation per cell. If there are two factors and only one observation per cell, the effects model is

$$
y_{ij}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\epsilon_{ij}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b
\end{cases}
\tag{5.21}
$$

The analysis of variance for this situation is shown in Table 5.9, assuming that both factors are fixed.

From examining the expected mean squares, we see that the error variance $\sigma^2$ is *not estimable*; that is, the two-factor interaction effect $(\tau\beta)_{ij}$ and the experimental error cannot be separated in any obvious manner. Consequently, there are no tests on main effects unless the

### PDF page 220 (book page 204)

**TABLE 5.9** Analysis of Variance for a Two-Factor Model, One Observation per Cell

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | Expected Mean Square |
|---|---|---:|---|---|
| Rows ($A$) | $\displaystyle\sum_{i=1}^{a}\frac{y_{i.}^2}{b}-\frac{y_{..}^2}{ab}$ | $a-1$ | $MS_A$ | $\displaystyle\sigma^2+\frac{b\sum\tau_i^2}{a-1}$ |
| Columns ($B$) | $\displaystyle\sum_{j=1}^{b}\frac{y_{.j}^2}{a}-\frac{y_{..}^2}{ab}$ | $b-1$ | $MS_B$ | $\displaystyle\sigma^2+\frac{a\sum\beta_j^2}{b-1}$ |
| Residual or $AB$ | Subtraction | $(a-1)(b-1)$ | $MS_{\text{Residual}}$ | $\displaystyle\sigma^2+\frac{\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ |
| Total | $\displaystyle\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2-\frac{y_{..}^2}{ab}$ | $ab-1$ | | |

interaction effect is zero. If there is no interaction present, then $(\tau\beta)_{ij}=0$ for all $i$ and $j$, and a plausible model is

$$
y_{ij}=\mu+\tau_i+\beta_j+\epsilon_{ij}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b
\end{cases}
\tag{5.22}
$$

If the model (Equation 5.22) is appropriate, then the residual mean square in Table 5.9 is an unbiased estimator of $\sigma^2$, and the main effects may be tested by comparing $MS_A$ and $MS_B$ to $MS_{\text{Residual}}$.

A test developed by Tukey (1949a) is helpful in determining whether interaction is present. The procedure assumes that the interaction term is of a particularly simple form, namely,

$$
(\tau\beta)_{ij}=\gamma\tau_i\beta_j
$$

where $\gamma$ is an unknown constant. By defining the interaction term this way, we may use a regression approach to test the significance of the interaction term. The test partitions the residual sum of squares into a single-degree-of-freedom component due to nonadditivity (interaction) and a component for error with $(a-1)(b-1)-1$ degrees of freedom. Computationally, we have

$$
SS_N=
\frac{
\left[
\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}y_{i.}y_{.j}
-y_{..}\left(SS_A+SS_B+\dfrac{y_{..}^2}{ab}\right)
\right]^2}
{abSS_ASS_B}
\tag{5.23}
$$

with one degree of freedom, and

$$
SS_{\text{Error}}=SS_{\text{Residual}}-SS_N
\tag{5.24}
$$

with $(a-1)(b-1)-1$ degrees of freedom. To test for the presence of interaction, we compute

$$
F_0=\frac{SS_N}{SS_{\text{Error}}/[(a-1)(b-1)-1]}
\tag{5.25}
$$

If $F_0>F_{\alpha,1,(a-1)(b-1)-1}$, the hypothesis of no interaction must be rejected.

### PDF page 221 (book page 205)

### EXAMPLE 5.2

The impurity present in a chemical product is affected by two factors—pressure and temperature. The data from a single replicate of a factorial experiment are shown in Table 5.10. The sums of squares are

$$
\begin{aligned}
SS_A&=\frac{1}{b}\sum_{i=1}^{a}y_{i.}^2-\frac{y_{..}^2}{ab}\\
&=\frac{1}{5}[23^2+13^2+8^2]-\frac{44^2}{(3)(5)}=23.33
\end{aligned}
$$

$$
\begin{aligned}
SS_B&=\frac{1}{a}\sum_{j=1}^{b}y_{.j}^2-\frac{y_{..}^2}{ab}\\
&=\frac{1}{3}[9^2+6^2+13^2+6^2+10^2]-\frac{44^2}{(3)(5)}=11.60
\end{aligned}
$$

$$
\begin{aligned}
SS_T&=\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}^2-\frac{y_{..}^2}{ab}\\
&=166-129.07=36.93
\end{aligned}
$$

and

$$
\begin{aligned}
SS_{\text{Residual}}&=SS_T-SS_A-SS_B\\
&=36.93-23.33-11.60=2.00
\end{aligned}
$$

**TABLE 5.10** Impurity Data for Example 5.2

| Temperature (°F) | Pressure 25 | Pressure 30 | Pressure 35 | Pressure 40 | Pressure 45 | $y_{i.}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 5 | 4 | 6 | 3 | 5 | 23 |
| 125 | 3 | 1 | 4 | 2 | 3 | 13 |
| 150 | 1 | 1 | 3 | 1 | 2 | 8 |
| $y_{.j}$ | 9 | 6 | 13 | 6 | 10 | $44=y_{..}$ |

The sum of squares for nonadditivity is computed from Equation 5.23 as follows:

$$
\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}y_{i.}y_{.j}
=(5)(23)(9)+(4)(23)(6)+\cdots+(2)(8)(10)=7236
$$

$$
\begin{aligned}
SS_N&=
\frac{\left[
\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij}y_{i.}y_{.j}
-y_{..}\left(SS_A+SS_B+\dfrac{y_{..}^2}{ab}\right)
\right]^2}{abSS_ASS_B}\\
&=\frac{[7236-(44)(23.33+11.60+129.07)]^2}{(3)(5)(23.33)(11.60)}\\
&=\frac{[20.00]^2}{4059.42}=0.0985
\end{aligned}
$$

and the error sum of squares is, from Equation 5.24,

$$
\begin{aligned}
SS_{\text{Error}}&=SS_{\text{Residual}}-SS_N\\
&=2.00-0.0985=1.9015
\end{aligned}
$$

The complete ANOVA is summarized in Table 5.11. The test statistic for nonadditivity is $F_0=0.0985/0.2716=0.36$, so we conclude that there is no evidence of interaction in these data. The main effects of temperature and pressure are significant.

**TABLE 5.11** Analysis of Variance for Example 5.2

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|
| Temperature | 23.33 | 2 | 11.67 | 42.97 | 0.0001 |
| Pressure | 11.60 | 4 | 2.90 | 10.68 | 0.0042 |
| Nonadditivity | 0.0985 | 1 | 0.0985 | 0.36 | 0.5674 |
| Error | 1.9015 | 7 | 0.2716 | | |
| Total | 36.93 | 14 | | | |

### PDF page 222 (book page 206)

In concluding this section, we note that the two-factor factorial model with one observation per cell (Equation 5.22) looks exactly like the randomized complete block model (Equation 4.1). In fact, the Tukey single-degree-of-freedom test for nonadditivity can be directly applied to test for interaction in the randomized block model. However, remember that the **experimental situations** that lead to the randomized block and factorial models are very different. In the factorial model, all $ab$ runs have been made in random order, whereas in the randomized block model, randomization occurs only *within the block*. The blocks are a randomization restriction. Hence, the manner in which the experiments are run and the interpretation of the two models are quite different.

## 5.4 The General Factorial Design

The results for the two-factor factorial design may be extended to the general case where there are $a$ levels of factor $A$, $b$ levels of factor $B$, $c$ levels of factor $C$, and so on, arranged in a factorial experiment. In general, there will be $abc\cdots n$ total observations if there are $n$ replicates of the complete experiment. Once again, note that we must have at least two replicates ($n\geq2$) to determine a sum of squares due to error if all possible interactions are included in the model.

If all factors in the experiment are fixed, we may easily formulate and test hypotheses about the main effects and interactions using the ANOVA. For a fixed effects model, test statistics for each main effect and interaction may be constructed by dividing the corresponding mean square for the effect or interaction by the mean square error. All of these $F$ tests will be upper-tail, one-tail tests. The number of degrees of freedom for any main effect is the number of levels of the factor minus one, and the number of degrees of freedom for an interaction is the product of the number of degrees of freedom associated with the individual components of the interaction.

For example, consider the **three-factor analysis of variance model**:

$$
\begin{aligned}
y_{ijkl}={}&\mu+\tau_i+\beta_j+\gamma_k+(\tau\beta)_{ij}
+(\tau\gamma)_{ik}+(\beta\gamma)_{jk}\\
&+(\tau\beta\gamma)_{ijk}+\epsilon_{ijkl}
\end{aligned}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,c\\
l=1,2,\ldots,n
\end{cases}
\tag{5.26}
$$

Assuming that $A$, $B$, and $C$ are fixed, the **analysis of variance table** is shown in Table 5.12. The $F$ tests on main effects and interactions follow directly from the expected mean squares.

Usually, the analysis of variance computations would be done using a statistics software package. However, manual computing formulas for the sums of squares in Table 5.12 are occasionally useful. The total sum of squares is found in the usual way as

$$
SS_T=\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}\sum_{l=1}^{n}
y_{ijkl}^2-\frac{y_{....}^2}{abcn}
\tag{5.27}
$$

The sums of squares for the main effects are found from the totals for factors $A$ ($y_{i...}$), $B$ ($y_{.j..}$), and $C$ ($y_{..k.}$) as follows:

$$
SS_A=\frac{1}{bcn}\sum_{i=1}^{a}y_{i...}^2-\frac{y_{....}^2}{abcn}
\tag{5.28}
$$

$$
SS_B=\frac{1}{acn}\sum_{j=1}^{b}y_{.j..}^2-\frac{y_{....}^2}{abcn}
\tag{5.29}
$$

$$
SS_C=\frac{1}{abn}\sum_{k=1}^{c}y_{..k.}^2-\frac{y_{....}^2}{abcn}
\tag{5.30}
$$

### PDF page 223 (book page 207)

**TABLE 5.12** The Analysis of Variance Table for the Three-Factor Fixed Effects Model

| Source | Sum of Squares | Degrees of Freedom | Mean Square | Expected Mean Square | $F_0$ |
|---|---:|---:|---:|---|---:|
| $A$ | $SS_A$ | $a-1$ | $MS_A$ | $\displaystyle\sigma^2+\frac{bcn\sum\tau_i^2}{a-1}$ | $MS_A/MS_E$ |
| $B$ | $SS_B$ | $b-1$ | $MS_B$ | $\displaystyle\sigma^2+\frac{acn\sum\beta_j^2}{b-1}$ | $MS_B/MS_E$ |
| $C$ | $SS_C$ | $c-1$ | $MS_C$ | $\displaystyle\sigma^2+\frac{abn\sum\gamma_k^2}{c-1}$ | $MS_C/MS_E$ |
| $AB$ | $SS_{AB}$ | $(a-1)(b-1)$ | $MS_{AB}$ | $\displaystyle\sigma^2+\frac{cn\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ | $MS_{AB}/MS_E$ |
| $AC$ | $SS_{AC}$ | $(a-1)(c-1)$ | $MS_{AC}$ | $\displaystyle\sigma^2+\frac{bn\sum\sum(\tau\gamma)_{ik}^2}{(a-1)(c-1)}$ | $MS_{AC}/MS_E$ |
| $BC$ | $SS_{BC}$ | $(b-1)(c-1)$ | $MS_{BC}$ | $\displaystyle\sigma^2+\frac{an\sum\sum(\beta\gamma)_{jk}^2}{(b-1)(c-1)}$ | $MS_{BC}/MS_E$ |
| $ABC$ | $SS_{ABC}$ | $(a-1)(b-1)(c-1)$ | $MS_{ABC}$ | $\displaystyle\sigma^2+\frac{n\sum\sum\sum(\tau\beta\gamma)_{ijk}^2}{(a-1)(b-1)(c-1)}$ | $MS_{ABC}/MS_E$ |
| Error | $SS_E$ | $abc(n-1)$ | $MS_E$ | $\sigma^2$ | |
| Total | $SS_T$ | $abcn-1$ | | | |

To compute the two-factor interaction sums of squares, the totals for the $A\times B$, $A\times C$, and $B\times C$ cells are needed. It is frequently helpful to collapse the original data table into three two-way tables to compute these quantities. The sums of squares are found from

$$
\begin{aligned}
SS_{AB}
&=\frac{1}{cn}\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij..}^2
-\frac{y_{....}^2}{abcn}-SS_A-SS_B\\
&=SS_{\text{Subtotals}(AB)}-SS_A-SS_B
\end{aligned}
\tag{5.31}
$$

$$
\begin{aligned}
SS_{AC}
&=\frac{1}{bn}\sum_{i=1}^{a}\sum_{k=1}^{c}y_{i.k.}^2
-\frac{y_{....}^2}{abcn}-SS_A-SS_C\\
&=SS_{\text{Subtotals}(AC)}-SS_A-SS_C
\end{aligned}
\tag{5.32}
$$

and

$$
\begin{aligned}
SS_{BC}
&=\frac{1}{an}\sum_{j=1}^{b}\sum_{k=1}^{c}y_{.jk.}^2
-\frac{y_{....}^2}{abcn}-SS_B-SS_C\\
&=SS_{\text{Subtotals}(BC)}-SS_B-SS_C
\end{aligned}
\tag{5.33}
$$

Note that the sums of squares for the two-factor subtotals are found from the totals in each two-way table. The three-factor interaction sum of squares is computed from the three-way cell totals $\{y_{ijk.}\}$ as

$$
\begin{aligned}
SS_{ABC}
={}&\frac{1}{n}\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}y_{ijk.}^2
-\frac{y_{....}^2}{abcn}\\
&-SS_A-SS_B-SS_C-SS_{AB}-SS_{AC}-SS_{BC}
\end{aligned}
\tag{5.34a}
$$

$$
SS_{ABC}=SS_{\text{Subtotals}(ABC)}-SS_A-SS_B-SS_C-SS_{AB}-SS_{AC}-SS_{BC}
\tag{5.34b}
$$

### PDF page 224 (book page 208)

The error sum of squares may be found by subtracting the sum of squares for each main effect and interaction from the total sum of squares or by

$$
SS_E=SS_T-SS_{\text{Subtotals}(ABC)}
\tag{5.35}
$$

### EXAMPLE 5.3 — The Soft Drink Bottling Problem

A soft drink bottler is interested in obtaining more uniform fill heights in the bottles produced by his manufacturing process. The filling machine theoretically fills each bottle to the correct target height, but in practice, there is variation around this target, and the bottler would like to understand the sources of this variability better and eventually reduce it.

The process engineer can control three variables during the filling process: the percent carbonation ($A$), the operating pressure in the filler ($B$), and the bottles produced per minute or the line speed ($C$). The pressure and speed are easy to control, but the percent carbonation is more difficult to control during actual manufacturing because it varies with product temperature. However, for purposes of an experiment, the engineer can control carbonation at three levels: 10, 12, and 14 percent. She chooses two levels for pressure (25 and 30 psi) and two levels for line speed (200 and 250 bpm). She decides to run two replicates of a factorial design in these three factors, with all 24 runs taken in random order. The response variable observed is the average deviation from the target fill height observed in a production run of bottles at each set of conditions. The data that resulted from this experiment are shown in Table 5.13. Positive deviations are fill heights above the target, whereas negative deviations are fill heights below the target. The circled numbers in Table 5.13 are the three-way cell totals $y_{ijk.}$.

The total corrected sum of squares is found from Equation 5.27 as

$$
\begin{aligned}
SS_T&=\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}\sum_{l=1}^{n}
y_{ijkl}^2-\frac{y_{....}^2}{abcn}\\
&=571-\frac{(75)^2}{24}=336.625
\end{aligned}
$$

**TABLE 5.13** Fill Height Deviation Data for Example 5.3

| Percent Carbonation ($A$) | Pressure 25 psi, Speed 200 (observations; total) | Pressure 25 psi, Speed 250 (observations; total) | Pressure 30 psi, Speed 200 (observations; total) | Pressure 30 psi, Speed 250 (observations; total) | $y_{i...}$ |
|---:|---|---|---|---|---:|
| 10 | −3, −1; −4 | −1, 0; −1 | −1, 0; −1 | 1, 1; 2 | −4 |
| 12 | 0, 1; 1 | 2, 1; 3 | 2, 3; 5 | 6, 5; 11 | 20 |
| 14 | 5, 4; 9 | 7, 6; 13 | 7, 9; 16 | 10, 11; 21 | 59 |
| $B\times C$ totals $y_{.jk.}$ | 6 | 15 | 20 | 34 | $75=y_{....}$ |

Pressure totals $y_{.j..}$: 25 psi = 21; 30 psi = 54.

**$A\times B$ Totals $y_{ij..}$**

| $A$ | $B=25$ | $B=30$ |
|---:|---:|---:|
| 10 | −5 | 1 |
| 12 | 4 | 16 |
| 14 | 22 | 37 |

**$A\times C$ Totals $y_{i.k.}$**

| $A$ | $C=200$ | $C=250$ |
|---:|---:|---:|
| 10 | −5 | 1 |
| 12 | 6 | 14 |
| 14 | 25 | 34 |

### PDF page 225 (book page 209)

and the sums of squares for the main effects are calculated from Equations 5.28, 5.29, and 5.30 as

$$
\begin{aligned}
SS_{\text{Carbonation}}
&=\frac{1}{bcn}\sum_{i=1}^{a}y_{i...}^2-\frac{y_{....}^2}{abcn}\\
&=\frac{1}{8}[(-4)^2+(20)^2+(59)^2]-\frac{(75)^2}{24}\\
&=252.750
\end{aligned}
$$

$$
\begin{aligned}
SS_{\text{Pressure}}
&=\frac{1}{acn}\sum_{j=1}^{b}y_{.j..}^2-\frac{y_{....}^2}{abcn}\\
&=\frac{1}{12}[(21)^2+(54)^2]-\frac{(75)^2}{24}=45.375
\end{aligned}
$$

and

$$
\begin{aligned}
SS_{\text{Speed}}
&=\frac{1}{abn}\sum_{k=1}^{c}y_{..k.}^2-\frac{y_{....}^2}{abcn}\\
&=\frac{1}{12}[(26)^2+(49)^2]-\frac{(75)^2}{24}=22.042
\end{aligned}
$$

To calculate the sums of squares for the two-factor interactions, we must find the two-way cell totals. For example, to find the carbonation–pressure or $AB$ interaction, we need the totals for the $A\times B$ cells $\{y_{ij..}\}$ shown in Table 5.13. Using Equation 5.31, we find the sums of squares as

$$
\begin{aligned}
SS_{AB}
&=\frac{1}{cn}\sum_{i=1}^{a}\sum_{j=1}^{b}y_{ij..}^2
-\frac{y_{....}^2}{abcn}-SS_A-SS_B\\
&=\frac{1}{4}[(-5)^2+(1)^2+(4)^2+(16)^2+(22)^2+(37)^2]\\
&\quad-\frac{(75)^2}{24}-252.750-45.375\\
&=5.250
\end{aligned}
$$

The carbonation–speed or $AC$ interaction uses the $A\times C$ cell totals $\{y_{i.k.}\}$ shown in Table 5.13 and Equation 5.32:

$$
\begin{aligned}
SS_{AC}
&=\frac{1}{bn}\sum_{i=1}^{a}\sum_{k=1}^{c}y_{i.k.}^2
-\frac{y_{....}^2}{abcn}-SS_A-SS_C\\
&=\frac{1}{4}[(-5)^2+(1)^2+(6)^2+(14)^2+(25)^2+(34)^2]\\
&\quad-\frac{(75)^2}{24}-252.750-22.042\\
&=0.583
\end{aligned}
$$

The pressure–speed or $BC$ interaction is found from the $B\times C$ cell totals $\{y_{.jk.}\}$ shown in Table 5.13 and Equation 5.33:

$$
\begin{aligned}
SS_{BC}
&=\frac{1}{an}\sum_{j=1}^{b}\sum_{k=1}^{c}y_{.jk.}^2
-\frac{y_{....}^2}{abcn}-SS_B-SS_C\\
&=\frac{1}{6}[(6)^2+(15)^2+(20)^2+(34)^2]-\frac{(75)^2}{24}\\
&\quad-45.375-22.042\\
&=1.042
\end{aligned}
$$

The three-factor interaction sum of squares is found from the $A\times B\times C$ cell totals $\{y_{ijk.}\}$, which are circled in Table 5.13. From Equation 5.34a, we find

$$
\begin{aligned}
SS_{ABC}
&=\frac{1}{n}\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}y_{ijk.}^2
-\frac{y_{....}^2}{abcn}-SS_A-SS_B-SS_C\\
&\quad-SS_{AB}-SS_{AC}-SS_{BC}\\
&=\frac{1}{2}[(-4)^2+(-1)^2+(-1)^2+\cdots+(16)^2+(21)^2]\\
&\quad-\frac{(75)^2}{24}-252.750-45.375-22.042-5.250-0.583-1.042\\
&=1.083
\end{aligned}
$$

Finally, noting that

$$
SS_{\text{Subtotals}(ABC)}
=\frac{1}{n}\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}y_{ijk.}^2
-\frac{y_{....}^2}{abcn}=328.125
$$

we have

$$
\begin{aligned}
SS_E&=SS_T-SS_{\text{Subtotals}(ABC)}\\
&=336.625-328.125\\
&=8.500
\end{aligned}
$$

The ANOVA is summarized in Table 5.14. We see that the percentage of carbonation, operating pressure, and line speed significantly affect the fill volume. The carbonation-pressure interaction $F$ ratio has a $P$-value of 0.0558, indicating some interaction between these factors.

The next step should be an analysis of the residuals from this experiment. We leave this as an exercise for the reader but point out that a normal probability plot of the residuals and the other usual diagnostics do not indicate any major concerns.

To assist in the practical interpretation of this experiment, Figure 5.16 presents plots of the three main effects and the $AB$ (carbonation–pressure) interaction. The main effect plots are just graphs of the marginal response averages at the levels of the three factors. Notice that all three variables have *positive* main effects; that is, increasing the variable moves the average deviation from the fill target upward. The interaction between carbonation and pressure is fairly small, as shown by the similar shape of the two curves in Figure 5.16d.

Because the company wants the average deviation from the fill target to be close to zero, the engineer decides to recommend the low level of operating pressure (25 psi) and the high level of line speed (250 bpm, which will maximize the production rate). Figure 5.17 plots the average observed deviation from the target fill height at the three different carbonation levels for this set of operating conditions. Now the carbonation level cannot presently be perfectly controlled in the manufacturing process, and the normal distribution shown with the solid curve in Figure 5.17 approximates

### PDF page 226 (book page 210)

**TABLE 5.14** Analysis of Variance for Example 5.3

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|
| Percentage of carbonation ($A$) | 252.750 | 2 | 126.375 | 178.412 | $<0.0001$ |
| Operating pressure ($B$) | 45.375 | 1 | 45.375 | 64.059 | $<0.0001$ |
| Line speed ($C$) | 22.042 | 1 | 22.042 | 31.118 | 0.0001 |
| $AB$ | 5.250 | 2 | 2.625 | 3.706 | 0.0558 |
| $AC$ | 0.583 | 2 | 0.292 | 0.412 | 0.6713 |
| $BC$ | 1.042 | 1 | 1.042 | 1.471 | 0.2485 |
| $ABC$ | 1.083 | 2 | 0.542 | 0.765 | 0.4867 |
| Error | 8.500 | 12 | 0.708 | | |
| Total | 336.625 | 23 | | | |

the variability in the carbonation levels presently experienced. As the process is impacted by the values of the carbonation level drawn from this distribution, the fill heights will fluctuate considerably. This variability in the fill heights could be reduced if the distribution of the carbonation level values followed the normal distribution shown with the dashed line in Figure 5.17. Reducing the standard deviation of the carbonation level distribution was ultimately achieved by improving temperature control during manufacturing.

**FIGURE 5.16** Main effects and interaction plots for Example 5.3. (a) Percentage of carbonation ($A$). (b) Pressure ($B$). (c) Line speed ($C$). (d) Carbonation–pressure interaction

*Panel (a) shows average fill deviation increasing steeply as carbonation rises from 10 to 14 percent. Panel (b) shows an increase from about 1.8 to 4.5 as pressure rises from 25 to 30 psi. Panel (c) shows an increase from about 2.2 to 4.1 as line speed rises from 200 to 250. Panel (d) shows similar increasing curves over carbonation for both pressures, with the 30-psi curve consistently higher.*

### PDF page 227 (book page 211)

**FIGURE 5.17** Average fill height deviation at high speed and low pressure for different carbonation levels

*At 250 bpm and 25 psi, average fill deviation rises from about −0.5 at 10 percent carbonation to 1.5 at 12 percent and 7.5 at 14 percent. A broad solid normal curve illustrates the present carbonation distribution, while a narrow dashed curve centered near 11 percent illustrates an improved distribution.*

We have indicated that if all the factors in a factorial experiment are fixed, test statistic construction is straightforward. The statistic for testing any main effect or interaction is always formed by dividing the mean square for the main effect or interaction by the mean square error. However, if the factorial experiment involves one or more random factors, the test statistic construction is not always done this way. We must examine the expected mean squares to determine the correct tests. We defer a complete discussion of experiments with random factors until Chapter 13.

## 5.5 Fitting Response Curves and Surfaces

The ANOVA always treats all of the factors in the experiment as if they were qualitative or categorical. However, many experiments involve at least one quantitative factor. It can be useful to fit a **response curve** to the levels of a quantitative factor so that the experimenter has an equation that relates the response to the factor. This equation might be used for interpolation, that is, for predicting the response at factor levels between those actually used in the experiment. When at least two factors are quantitative, we can fit a **response surface** for predicting $y$ at various combinations of the design factors. In general, **linear regression methods** are used to fit these models to the experimental data. We illustrated this procedure in Section 3.5.1 for an experiment with a single factor. We now present two examples involving factorial experiments. In both examples, we will use a computer software package to generate the regression models. For more information about regression analysis, refer to Chapter 10 and the supplemental text material for this chapter.

### EXAMPLE 5.4

Consider the battery life experiment described in Example 5.1. The factor temperature is quantitative, and the material type is qualitative. Furthermore, there are three levels of temperature. Consequently, we can compute a linear and a quadratic temperature effect to study how temperature affects the battery life. Table 5.15 presents condensed output from Design-Expert for this experiment and assumes that temperature is quantitative and material type is qualitative.

The ANOVA in Table 5.15 shows that the “model” source of variability has been subdivided into several components. The components “$A$” and “$A^2$” represent the

### PDF page 228 (book page 212)

**TABLE 5.15** Design-Expert Output for Example 5.4

**Response: Life — In Hours — ANOVA for Response Surface Reduced Cubic Model — Analysis of Variance Table [Partial Sum of Squares]**

| Source | Sum of Squares | DF | Mean Square | $F$ Value | Prob $>F$ | |
|---|---:|---:|---:|---:|---:|---|
| Model | 59416.22 | 8 | 7427.03 | 11.00 | $<0.0001$ | significant |
| $A$ | 39042.67 | 1 | 39042.67 | 57.82 | $<0.0001$ | |
| $B$ | 10683.72 | 2 | 5341.86 | 7.91 | 0.0020 | |
| $A^2$ | 76.06 | 1 | 76.06 | 0.11 | 0.7398 | |
| $AB$ | 2315.08 | 2 | 1157.54 | 1.71 | 0.1991 | |
| $A^2B$ | 7298.69 | 2 | 3649.35 | 5.40 | 0.0106 | |
| Residual | 18230.75 | 27 | 675.21 | | | |
| Lack of Fit | 0.000 | 0 | | | | |
| Pure Error | 18230.75 | 27 | 675.21 | | | |
| Cor Total | 77646.97 | 35 | | | | |

| Statistic | Value | Statistic | Value |
|---|---:|---|---:|
| Std. Dev. | 25.98 | R-Squared | 0.7652 |
| Mean | 105.53 | Adj R-Squared | 0.6956 |
| C.V. | 24.62 | Pred R-Squared | 0.5826 |
| PRESS | 32410.22 | Adeq Precision | 8.178 |

| Term | Coefficient Estimate | DF | Standard Error | 95% CI Low | 95% CI High | VIF |
|---|---:|---:|---:|---:|---:|---:|
| Intercept | 107.58 | 1 | 7.50 | 92.19 | 122.97 | |
| $A$-Temp | −40.33 | 1 | 5.30 | −51.22 | −29.45 | 1.00 |
| $B[1]$ | −50.33 | 1 | 10.61 | −72.10 | −28.57 | |
| $B[2]$ | 12.17 | 1 | 10.61 | −9.60 | 33.93 | |
| $A^2$ | −3.08 | 1 | 9.19 | −21.93 | 15.77 | 1.00 |
| $AB[1]$ | 1.71 | 1 | 7.50 | −13.68 | 17.10 | |
| $AB[2]$ | −12.79 | 1 | 7.50 | −28.18 | 2.60 | |
| $A^2B[1]$ | 41.96 | 1 | 12.99 | 15.30 | 68.62 | |
| $A^2B[2]$ | −14.04 | 1 | 12.99 | −40.70 | 12.62 | |

**Final Equation in Terms of Coded Factors:**

$$
\begin{aligned}
\text{Life}={}&+107.58-40.33A-50.33B[1]+12.17B[2]\\
&-3.08A^2+1.71AB[1]-12.79AB[2]\\
&+41.96A^2B[1]-14.04A^2[2]
\end{aligned}
$$

### PDF page 229 (book page 213)

**TABLE 5.15 (Continued)**

**Final Equation in Terms of Actual Factors:**

For material type 1:

$$
\text{Life}=+169.38017-2.48860(\text{Temp})+0.012851(\text{Temp}^2)
$$

For material type 2:

$$
\text{Life}=+159.62397-0.17901(\text{Temp})+0.41627(\text{Temp}^2)
$$

For material type 3:

$$
\text{Life}=+132.76240+0.89264(\text{Temp})-0.43218(\text{Temp}^2)
$$

linear and quadratic effects of temperature, and “$B$” represents the main effect of the material type factor. Recall that material type is a qualitative factor with three levels. The terms “$AB$” and “$A^2B$” are the interactions of the linear and quadratic temperature factor with material type.

The $P$-values indicate that $A^2$ and $AB$ are not significant, whereas the $A^2B$ term is significant. Often we think about removing nonsignificant terms or factors from a model, but in this case, removing $A^2$ and $AB$ and retaining $A^2B$ will result in a model that is not **hierarchical**. The **hierarchy principle** indicates that if a model contains a high-order term (such as $A^2B$), it should also contain all of the lower order terms that compose it (in this case $A^2$ and $AB$). Hierarchy promotes a type of internal

**FIGURE 5.18** Predicted life as a function of temperature for the three material types, Example 5.4

*Observed battery lives at 15, 70, and 125 are overlaid with three fitted quadratic curves. Material type 1 falls sharply and then turns upward slightly; material type 2 declines steadily; material type 3 rises slightly near intermediate temperature and then declines. Vertical error bars are shown at 15 and 125.*

### PDF page 230 (book page 214)

consistency in a model, and many statistical model builders rigorously follow the principle. However, hierarchy is not always a good idea, and many models actually work better as prediction equations without including the nonsignificant terms that promote hierarchy. For more information, see the supplemental text material for this chapter.

The computer output also gives model coefficient estimates and a final prediction equation for battery life in coded factors. In this equation, the levels of temperature are $A=-1,0,+1$, respectively, when temperature is at the low, middle, and high levels (15, 70, and 125°C). The variables $B[1]$ and $B[2]$ are coded **indicator variables** that are defined as follows:

| | Material Type 1 | Material Type 2 | Material Type 3 |
|---|---:|---:|---:|
| $B[1]$ | 1 | 0 | −1 |
| $B[2]$ | 0 | 1 | −1 |

There are also prediction equations for battery life in terms of the actual factor levels. Notice that because material type is a qualitative factor there is an equation for predicted life as a function of temperature for each material type. Figure 5.18 shows the response curves generated by these three prediction equations. Compare them to the two-factor interaction graph for this experiment in Figure 5.9.

If several factors in a factorial experiment are quantitative a response surface may be used to model the relationship between $y$ and the design factors. Furthermore, the quantitative factor effects may be represented by single-degree-of-freedom polynomial effects. Similarly, the interactions of quantitative factors can be partitioned into single-degree-of-freedom components of interaction. This is illustrated in the following example.

### EXAMPLE 5.5

The effective life of a cutting tool installed in a numerically controlled machine is thought to be affected by the cutting speed and the tool angle. Three speeds and three angles are selected, and a $3^2$ factorial experiment with two replicates is performed. The coded data are shown in Table 5.16. The circled numbers in the cells are the cell totals $\{y_{ij.}\}$.

Table 5.17 shows the JMP output for this experiment. This is a classical ANOVA, treating both factors as categorical. Notice that both design factors tool angle and speed as well as the angle–speed interaction are significant. Since the factors are quantitative, and both factors have three levels, a **second-order model** such as

$$
y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2
+\beta_{11}x_1^2+\beta_{22}x_2^2+\epsilon
$$

where $x_1=$ angle and $x_2=$ speed could also be fit to the data. The JMP output for this model is shown in Table 5.18. Notice that JMP “centers” the predictors when forming the interaction and quadratic model terms. The second-order model

**TABLE 5.16** Data for Tool Life Experiment

| Tool Angle (degrees) | Speed 125 (observations; total) | Speed 150 (observations; total) | Speed 175 (observations; total) | $y_{i..}$ |
|---:|---|---|---|---:|
| 15 | −2, −1; −3 | −3, 0; −3 | 2, 3; 5 | −1 |
| 20 | 0, 2; 2 | 1, 3; 4 | 4, 6; 10 | 16 |
| 25 | −1, 0; −1 | 5, 6; 11 | 0, −1; −1 | 9 |
| $y_{.j.}$ | −2 | 12 | 14 | $24=y_{...}$ |

### PDF page 231 (book page 215)

**TABLE 5.17** JMP ANOVA for the Tool Life Experiment in Example 5.5

**Response Tool Life — Whole Model — Actual by Predicted Plot**

*Actual tool life is plotted against predicted tool life from approximately −3 to 6. The fitted line and confidence bands are shown. The display reports $P=0.0013$, RSq = 0.90, and RMSE = 1.2019.*

**Summary of Fit**

| Statistic | Value |
|---|---:|
| RSquare | 0.895161 |
| RSquare Adj | 0.801971 |
| Root Mean Square Error | 1.20185 |
| Mean of Response | 1.333333 |
| Observations (or Sum Wgts) | 18 |

**Analysis of Variance**

| Source | DF | Sum of Squares | Mean Square | $F$ Ratio |
|---|---:|---:|---:|---:|
| Model | 8 | 111.00000 | 13.8750 | 9.6058 |
| Error | 9 | 13.00000 | 1.4444 | Prob $>F$ |
| C. Total | 17 | 124.00000 | | 0.0013 |

**Effect Tests**

| Source | Nparm | DF | Sum of Squares | $F$ Ratio | Prob $>F$ |
|---|---:|---:|---:|---:|---:|
| Angle | 2 | 2 | 24.333333 | 8.4231 | 0.0087 |
| Speed | 2 | 2 | 25.333333 | 8.7692 | 0.0077 |
| Angle*Speed | 4 | 4 | 61.333333 | 10.6154 | 0.0018 |

**Residual by Predicted Plot**

*Residuals are scattered between about −1.5 and 1.8 over predicted tool-life values from about −2.5 to 5.7, with no strong pattern.*

### PDF page 232 (book page 216)

doesn’t look like a very good fit to the data; the value of $R^2$ is only 0.465 (compared to $R^2=0.895$ in the categorical variable ANOVA) and the only significant factor is the linear term in speed for which the $P$-value is 0.0731. Notice that the mean square for error in the second-order model fit is 5.5278, considerably larger than it was in the classical categorical variable ANOVA of Table 5.17. The JMP output in Table 5.18 shows the **prediction profiler**, a graphical display showing the response variable life as a function of each design factor, angle and speed. The prediction profiler is very useful for optimization. Here it has been set to the levels of angle and speed that result in maximum predicted life.

Part of the reason for the relatively poor fit of the second-order model is that only one of the four degrees of freedom for interaction are accounted for in this model. In addition to the term $\beta_{12}x_1x_2$, there are three other terms that could be fit to completely account for the four degrees of freedom for interaction, namely $\beta_{112}x_1^2x_2$, $\beta_{122}x_1x_2^2$, and $\beta_{1122}x_1^2x_2^2$.

**TABLE 5.18** JMP Output for the Second-Order Model, Example 5.5

**Response Tool Life — Actual by Predicted Plot**

*Actual tool life is plotted against predicted tool life from approximately −3 to 6, with the fitted line and broad confidence bands. The display reports $P=0.1377$, RSq = 0.47, and RMSE = 2.3511.*

**Summary of Fit**

| Statistic | Value |
|---|---:|
| RSquare | 0.465054 |
| RSquare Adj | 0.242159 |
| Root Mean Square Error | 2.351123 |
| Mean of Response | 1.333333 |
| Observations (or Sum Wgts) | 18 |

**Analysis of Variance**

| Source | DF | Sum of Squares | Mean Square | $F$ Ratio |
|---|---:|---:|---:|---:|
| Model | 5 | 57.66667 | 11.5333 | 2.0864 |
| Error | 12 | 66.33333 | 5.5278 | Prob $>F$ |
| C. Total | 17 | 124.00000 | | 0.1377 |

**Parameter Estimates**

| Term | Estimate | Std. Error | $t$ Ratio | Prob $>|t|$ |
|---|---:|---:|---:|---:|
| Intercept | −8 | 5.048683 | −1.58 | 0.1390 |
| Angle | 0.1666667 | 0.135742 | 1.23 | 0.2431 |
| Speed | 0.0533333 | 0.027148 | 1.96 | 0.0731 |

### PDF page 233 (book page 217)

**TABLE 5.18 (Continued)**

| Term | Estimate | Std. Error | $t$ Ratio | Prob $>|t|$ |
|---|---:|---:|---:|---:|
| (Angle−20)*(Speed−150) | −0.008 | 0.00665 | −1.20 | 0.2522 |
| (Angle−20)*(Angle−20) | −0.08 | 0.047022 | −1.70 | 0.1146 |
| (Speed−150)*(Speed−150) | −0.0016 | 0.001881 | −0.85 | 0.4116 |

**Prediction Profiler**

*The profiler is set to angle 20.2381 and speed 166.0714. Predicted tool life is 3.781746 with an uncertainty of ±2.384705, and desirability is 0.696343. Curves show predicted life and desirability against angle and speed, alongside the combined desirability ramp.*

JMP output for the second-order model with the additional higher-order terms is shown in Table 5.19. While these higher-order terms are components of the two-factor interaction, the final model is a reduced quartic. Although there are some large $P$-values, all model terms have been retained to ensure hierarchy. The prediction profiler indicates that maximum tool life is achieved around an angle of 25 degrees and speed of 150 in/min.

**FIGURE 5.19** Two-dimensional contour plot of the tool life response surface for Example 5.5

*Contours over tool angle 15–25 degrees and speed 125–175 in/min are labeled −0.75, 0.5, 1.75, 3, and 4.25. The response is highest near angle 25 and speed 150.*

**FIGURE 5.20** Three-dimensional tool life response surface for Example 5.5

*A curved mesh surface plots life against tool angle and speed, with the corresponding contour projection on the base. The surface peaks near tool angle 25 degrees and speed 150 in/min.*

### PDF page 234 (book page 218)

Figure 5.19 is the contour plot of tool life for this model and Figure 5.20 is a three-dimensional response surface plot. These plots confirm the estimate of the optimum operating conditions found from the JMP prediction profiler. Exploration of response surfaces is an important use of designed experiments, which we will discuss in more detail in Chapter 11.

**TABLE 5.19** JMP Output for the Expanded Model in Example 5.5

**Response Y — Actual by Predicted Plot**

*Actual $Y$ is plotted against predicted $Y$ from approximately −4 to 7, along with the fitted diagonal. The display reports $P=0.0013$, RSq = 0.90, and RMSE = 1.2019.*

**Summary of Fit**

| Statistic | Value |
|---|---:|
| RSquare | 0.895161 |
| RSquare Adj | 0.801971 |
| Root Mean Square Error | 1.20185 |
| Mean of Response | 1.333333 |
| Observations (or Sum Wgts) | 18 |

**Analysis of Variance**

| Source | DF | Sum of Squares | Mean Square | $F$ Ratio |
|---|---:|---:|---:|---:|
| Model | 8 | 111.00000 | 13.8750 | 9.6058 |
| Error | 9 | 13.00000 | 1.4444 | Prob $>F$ |
| C. Total | 17 | 124.00000 | | 0.0013* |

**Parameter Estimates**

| Term | Estimate | Std Error | $t$ Ratio | Prob$>|t|$ |
|---|---:|---:|---:|---:|
| Intercept | −24 | 4.41588 | −5.43 | 0.0004* |
| Angle | 0.7 | 0.120185 | 5.82 | 0.0003* |
| Speed | 0.08 | 0.024037 | 3.33 | 0.0088* |
| (Angle−20)*(Speed−150) | −0.008 | 0.003399 | −2.35 | 0.0431* |
| (Angle−20)*(Angle−20) | $2.776\mathrm{e}{-17}$ | 0.041633 | 0.00 | 1.0000 |
| (Speed−150)*(Speed−150) | 0.0016 | 0.001665 | 0.96 | 0.3618 |
| (Angle−20)*(Speed−150)*(Angle−20) | −0.0016 | 0.001178 | −1.36 | 0.2073 |
| (Speed−150)*(Speed−150)*(Angle−20) | −0.00128 | 0.000236 | −5.43 | 0.0004* |
| (Angle−20)*(Speed−150)*(Angle−20)*(Speed−150) | −0.000192 | $8.158\mathrm{e}{-5}$ | −2.35 | 0.0431* |

### PDF page 235 (book page 219)

**TABLE 5.19 (Continued)**

**Effect Tests**

| Source | Nparm | DF | Sum of Squares | $F$ Ratio | Prob $>F$ |
|---|---:|---:|---:|---:|---:|
| Angle | 1 | 1 | 49.000000 | 33.9231 | 0.0003* |
| Speed | 1 | 1 | 16.000000 | 11.0769 | 0.0088* |
| Angle*Speed | 1 | 1 | 8.000000 | 5.5385 | 0.0431* |
| Angle*Angle | 1 | 1 | $6.4198\mathrm{e}{-31}$ | 0.0000 | 1.0000 |
| Speed*Speed | 1 | 1 | 1.333333 | 0.9231 | 0.3618 |
| Angle*Speed*Angle | 1 | 1 | 2.666667 | 1.8462 | 0.2073 |
| Speed*Speed*Angle | 1 | 1 | 42.666667 | 29.5385 | 0.0004* |
| Angle*Speed*Angle*Speed | 1 | 1 | 8.000000 | 5.5385 | 0.0431* |

**Sorted Parameter Estimates**

| Term | Estimate | Std Error | $t$ Ratio | Prob$>|t|$ |
|---|---:|---:|---:|---:|
| Angle | 0.7 | 0.120185 | 5.82 | 0.0003* |
| (Speed−150)*(Speed−150)*(Angle−20) | −0.00128 | 0.000236 | −5.43 | 0.0004* |
| Speed | 0.08 | 0.024037 | 3.33 | 0.0088* |
| (Angle−20)*(Speed−150)*(Angle−20)*(Speed−150) | −0.000192 | $8.158\mathrm{e}{-5}$ | −2.35 | 0.0431* |
| (Angle−20)*(Speed−150) | −0.008 | 0.003399 | −2.35 | 0.0431* |
| (Angle−20)*(Speed−150)*(Angle−20) | −0.0016 | 0.001178 | −1.36 | 0.2073 |
| (Speed−150)*(Speed−150) | 0.0016 | 0.001665 | 0.96 | 0.3618 |
| (Angle−20)*(Angle−20) | $2.776\mathrm{e}{-17}$ | 0.041633 | 0.00 | 1.0000 |

**Prediction Profiler**

*The profiler is set to angle 25 and speed 149.99901. Predicted $Y$ is 5.5 with an uncertainty of ±1.922464, and desirability is 0.849109.*

## 5.6 Blocking in a Factorial Design

We have discussed factorial designs in the context of a completely randomized experiment. Sometimes, it is not feasible or practical to completely randomize all of the runs in a factorial. For example, the presence of a nuisance factor may require that the experiment be run in blocks. We discussed the basic concepts of blocking in the context of a single-factor experiment in Chapter 4. We now show how blocking can be incorporated in a factorial. Some other aspects of blocking in factorial designs are presented in Chapters 7, 8, 9, and 13.

### PDF page 236 (book page 220)

Consider a factorial experiment with two factors ($A$ and $B$) and $n$ replicates. The linear statistical model for this design is

$$
y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,n
\end{cases}
\tag{5.36}
$$

where $\tau_i$, $\beta_j$, and $(\tau\beta)_{ij}$ represent the effects of factors $A$, $B$, and the $AB$ interaction, respectively. Now suppose that to run this experiment a particular raw material is required. This raw material is available in batches that are not large enough to allow all $abn$ treatment combinations to be run from the *same* batch. However, if a batch contains enough material for $ab$ observations, then an alternative design is to run each of the $n$ replicates using a separate batch of raw material. Consequently, the batches of raw material represent a randomization restriction or a **block**, and a single replicate of a complete factorial experiment is run within each block. The effects model for this new design is

$$
y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\delta_k+\epsilon_{ijk}
\begin{cases}
i=1,2,\ldots,a\\
j=1,2,\ldots,b\\
k=1,2,\ldots,n
\end{cases}
\tag{5.37}
$$

where $\delta_k$ is the effect of the $k$th block. Of course, within a block the order in which the treatment combinations are run is completely randomized.

The model (Equation 5.37) assumes that interaction between blocks and treatments is negligible. This was assumed previously in the analysis of randomized block designs. If these interactions do exist, they cannot be separated from the error component. In fact, the error term in this model really consists of the $(\tau\delta)_{ik}$, $(\beta\delta)_{jk}$, and $(\tau\beta\delta)_{ijk}$ interactions. The analysis of variance is outlined in Table 5.20. The layout closely resembles that of a factorial design, with the error sum of squares reduced by the sum of squares for blocks. Computationally, we find the sum of squares for blocks as the sum of squares between the $n$

**TABLE 5.20** Analysis of Variance for a Two-Factor Factorial in a Randomized Complete Block

| Source of Variation | Sum of Squares | Degrees of Freedom | Expected Mean Square | $F_0$ |
|---|---|---:|---|---:|
| Blocks | $\displaystyle\frac{1}{ab}\sum_k y_{..k}^2-\frac{y_{...}^2}{abn}$ | $n-1$ | $\sigma^2+ab\sigma_\delta^2$ | |
| $A$ | $\displaystyle\frac{1}{bn}\sum_i y_{i..}^2-\frac{y_{...}^2}{abn}$ | $a-1$ | $\displaystyle\sigma^2+\frac{bn\sum\tau_i^2}{a-1}$ | $MS_A/MS_E$ |
| $B$ | $\displaystyle\frac{1}{an}\sum_j y_{.j.}^2-\frac{y_{...}^2}{abn}$ | $b-1$ | $\displaystyle\sigma^2+\frac{an\sum\beta_j^2}{b-1}$ | $MS_B/MS_E$ |
| $AB$ | $\displaystyle\frac{1}{n}\sum_i\sum_j y_{ij.}^2-\frac{y_{...}^2}{abn}-SS_A-SS_B$ | $(a-1)(b-1)$ | $\displaystyle\sigma^2+\frac{n\sum\sum(\tau\beta)_{ij}^2}{(a-1)(b-1)}$ | $MS_{AB}/MS_E$ |
| Error | Subtraction | $(ab-1)(n-1)$ | $\sigma^2$ | |
| Total | $\displaystyle\sum_i\sum_j\sum_k y_{ijk}^2-\frac{y_{...}^2}{abn}$ | $abn-1$ | | |

### PDF page 237 (book page 221)

block totals $\{y_{..k}\}$. The ANOVA in Table 5.20 assumes that both factors are fixed and that blocks are random. The ANOVA estimator of the variance component for blocks $\sigma_\delta^2$, is

$$
\hat{\sigma}_\delta^2=\frac{MS_{\text{Blocks}}-MS_E}{ab}
$$

In the previous example, the randomization was restricted to within a batch of raw material. In practice, a variety of phenomena may cause randomization restrictions, such as time and operators. For example, if we could not run the entire factorial experiment on one day, then the experimenter could run a complete replicate on day 1, a second replicate on day 2, and so on. Consequently, each day would be a block.

### EXAMPLE 5.6

An engineer is studying methods for improving the ability to detect targets on a radar scope. Two factors she considers to be important are the amount of background noise, or “ground clutter,” on the scope and the type of filter placed over the screen. An experiment is designed using three levels of ground clutter and two filter types. We will consider these as fixed-type factors. The experiment is performed by randomly selecting a treatment combination (ground clutter level and filter type) and then introducing a signal representing the target into the scope. The intensity of this target is increased until the operator observes it. The intensity level at detection is then measured as the response variable. Because of operator availability, it is convenient to select an operator and keep him or her at the scope until all the necessary runs have been made. Furthermore, operators differ in their skill and ability to use the scope. Consequently, it seems logical to use the operators as blocks. Four operators are randomly selected. Once an operator is chosen, the order in which the six treatment combinations are run is randomly determined. Thus, we have a $3\times2$ factorial experiment run in a randomized complete block. The data are shown in Table 5.21.

The linear model for this experiment is

$$
y_{ijk}=\mu+\tau_i+\beta_j+(\tau\beta)_{ij}+\delta_k+\epsilon_{ijk}
\begin{cases}
i=1,2,3\\
j=1,2\\
k=1,2,3,4
\end{cases}
$$

where $\tau_i$ represents the ground clutter effect, $\beta_j$ represents the filter type effect, $(\tau\beta)_{ij}$ is the interaction, $\delta_k$ is the block effect, and $\epsilon_{ijk}$ is the NID$(0,\sigma^2)$ error component. The sums of squares for ground clutter, filter type, and their interaction are computed in the usual manner. The sum of squares due to blocks is found from the operator totals $\{y_{..k}\}$ as follows:

$$
\begin{aligned}
SS_{\text{Blocks}}
&=\frac{1}{ab}\sum_{k=1}^{n}y_{..k}^2-\frac{y_{...}^2}{abn}\\
&=\frac{1}{(3)(2)}[(572)^2+(579)^2+(597)^2+(530)^2]
-\frac{(2278)^2}{(3)(2)(4)}\\
&=402.17
\end{aligned}
$$

**TABLE 5.21** Intensity Level at Target Detection

| Ground Clutter | Operator 1, Filter 1 | Operator 1, Filter 2 | Operator 2, Filter 1 | Operator 2, Filter 2 | Operator 3, Filter 1 | Operator 3, Filter 2 | Operator 4, Filter 1 | Operator 4, Filter 2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Low | 90 | 86 | 96 | 84 | 100 | 92 | 92 | 81 |
| Medium | 102 | 87 | 106 | 90 | 105 | 97 | 96 | 80 |
| High | 114 | 93 | 112 | 91 | 108 | 95 | 98 | 83 |

The complete ANOVA for this experiment is summarized in Table 5.22. The presentation in Table 5.22 indicates that all effects are tested by dividing their mean squares by the mean square error. Both ground clutter level and filter type are significant at the 1 percent level, whereas their interaction is significant only at the 10 percent level. Thus, we conclude that both ground clutter level and the type of scope filter used affect the operator’s ability to detect the target, and there is

### PDF page 238 (book page 222)

some evidence of mild interaction between these factors. The ANOVA estimate of the variance component for blocks is

$$
\hat{\sigma}_\delta^2
=\frac{MS_{\text{Blocks}}-MS_E}{ab}
=\frac{134.06-11.09}{(3)(2)}
=20.50
$$

**TABLE 5.22** Analysis of Variance for Example 5.6

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|
| Ground clutter ($G$) | 335.58 | 2 | 167.79 | 15.13 | 0.0003 |
| Filter type ($F$) | 1066.67 | 1 | 1066.67 | 96.19 | $<0.0001$ |
| $GF$ | 77.08 | 2 | 38.54 | 3.48 | 0.0573 |
| Blocks | 402.17 | 3 | 134.06 | | |
| Error | 166.33 | 15 | 11.09 | | |
| Total | 2047.83 | 23 | | | |

The JMP output for this experiment is shown in Table 5.23. The REML estimate of the variance component for blocks is shown in this output, and because this is a balanced design, the REML and ANOVA estimates agree. JMP also provides the confidence intervals on both variance components $\sigma^2$ and $\sigma_\delta^2$.

**TABLE 5.23** JMP Output for Example 5.6

**Whole Model — Actual by Predicted Plot**

*Actual $Y$ is plotted against predicted $Y$ from 75 to 115, along with the fitted diagonal. The display reports $P<.0001$, RSq = 0.92, and RMSE = 3.33.*

**Summary of Fit**

| Statistic | Value |
|---|---:|
| RSquare | 0.917432 |
| RSquare Adj | 0.894497 |
| Root Mean Square Error | 3.329998 |
| Mean of Response | 94.91667 |
| Observations (or Sum Wgts) | 24 |

**REML Variance Component Estimates**

| Random Effect | Var Ratio | Var Component | Std Error | 95% Lower | 95% Upper | Pct of Total |
|---|---:|---:|---:|---:|---:|---:|
| Operators (Blocks) | 1.8481964 | 20.494444 | 18.255128 | −15.28495 | 56.273839 | 64.890 |
| Residual | | 11.088889 | 4.0490897 | 6.0510389 | 26.561749 | 35.110 |
| Total | | 31.583333 | | | | 100.000 |

−2 LogLikelihood = 118.73680261

### PDF page 239 (book page 223)

**Covariance Matrix of Variance Component Estimates**

| Random Effect | Operators (Blocks) | Residual |
|---|---:|---:|
| Operators (Blocks) | 333.24972 | −2.732521 |
| Residual | −2.732521 | 16.395128 |

**Fixed Effect Tests**

| Source | Nparm | DF | DFDen | $F$ Ratio | Prob $>F$ |
|---|---:|---:|---:|---:|---:|
| Clutter | 2 | 2 | 15 | 15.1315 | 0.0003* |
| Filter Type | 1 | 1 | 15 | 96.1924 | $<.0001$* |
| Clutter*Filter Type | 2 | 2 | 15 | 3.4757 | 0.0575 |

**Residual by Predicted Plot**

*Residuals range from about −10 to 8 over predicted values from approximately 85 to 109. They are scattered around the zero line without a pronounced pattern.*

In the case of two randomization restrictions, each with $p$ levels, if the number of treatment combinations in a $k$-factor factorial design exactly equals the number of restriction levels, that is, if $p=ab\cdots m$, then the factorial design may be run in a $p\times p$ Latin square. For example, consider a modification of the radar target detection experiment of Example 5.6. The factors in this experiment are filter type (two levels) and ground clutter (three levels), and operators are considered as blocks. Suppose now that because of the setup time required, only six runs can be made per day. Thus, days become a second randomization restriction, resulting in the $6\times6$ Latin square design, as shown in Table 5.24. In this table we have used the lowercase letters $f_i$ and $g_j$ to represent the $i$th and $j$th levels of filter type and ground clutter, respectively. That is, $f_1g_2$ represents filter type 1 and medium ground clutter. Note that now six operators are required, rather than four as in the original experiment, so the number of treatment combinations in the $3\times2$ factorial design exactly equals the number of restriction levels. Furthermore, in this design, each operator would be used only once on each day. The Latin letters $A$, $B$, $C$, $D$, $E$, and $F$ represent the $3\times2=6$ factorial treatment combinations as follows: $A=f_1g_1$, $B=f_1g_2$, $C=f_1g_3$, $D=f_2g_1$, $E=f_2g_2$, and $F=f_2g_3$.

The five degrees of freedom between the six Latin letters correspond to the main effects of filter type (one degree of freedom), ground clutter (two degrees of freedom), and their interaction (two degrees of freedom). The linear statistical model for this design is

$$
y_{ijkl}=\mu+\alpha_i+\tau_j+\beta_k+(\tau\beta)_{jk}
+\theta_l+\epsilon_{ijkl}
\begin{cases}
i=1,2,\ldots,6\\
j=1,2,3\\
k=1,2\\
l=1,2,\ldots,6
\end{cases}
\tag{5.38}
$$

### PDF page 240 (book page 224)

**TABLE 5.24** Radar Detection Experiment Run in a $6\times6$ Latin Square

| Day | Operator 1 | Operator 2 | Operator 3 | Operator 4 | Operator 5 | Operator 6 |
|---:|---|---|---|---|---|---|
| 1 | $A(f_1g_1=90)$ | $B(f_1g_2=106)$ | $C(f_1g_3=108)$ | $D(f_2g_1=81)$ | $F(f_2g_3=90)$ | $E(f_2g_2=88)$ |
| 2 | $C(f_1g_3=114)$ | $A(f_1g_1=96)$ | $B(f_1g_2=105)$ | $F(f_2g_3=83)$ | $E(f_2g_2=86)$ | $D(f_2g_1=84)$ |
| 3 | $B(f_1g_2=102)$ | $E(f_2g_2=90)$ | $G(f_2g_3=95)$ | $A(f_1g_1=92)$ | $D(f_2g_1=85)$ | $C(f_1g_3=104)$ |
| 4 | $E(f_2g_2=87)$ | $D(f_2g_1=84)$ | $A(f_1g_1=100)$ | $B(f_1g_2=96)$ | $C(f_1g_3=110)$ | $F(f_2g_3=91)$ |
| 5 | $F(f_2g_3=93)$ | $C(f_1g_3=112)$ | $D(f_2g_1=92)$ | $E(f_2g_2=80)$ | $A(f_1g_1=90)$ | $B(f_1g_2=98)$ |
| 6 | $D(f_2g_1=86)$ | $F(f_2g_3=91)$ | $E(f_2g_2=97)$ | $C(f_1g_3=98)$ | $B(f_1g_2=100)$ | $A(f_1g_1=92)$ |

where $\tau_j$ and $\beta_k$ are effects of ground clutter and filter type, respectively, and $\alpha_i$ and $\theta_l$ represent the randomization restrictions of days and operators, respectively. To compute the sums of squares, the following two-way table of treatment totals is helpful:

| Ground Clutter | Filter Type 1 | Filter Type 2 | $y_{.j..}$ |
|---|---:|---:|---:|
| Low | 560 | 512 | 1072 |
| Medium | 607 | 528 | 1135 |
| High | 646 | 543 | 1189 |
| $y_{..k.}$ | 1813 | 1583 | $3396=y_{....}$ |

Furthermore, the row and column totals are

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Rows ($y_{i.jkl}$) | 563 | 568 | 568 | 568 | 565 | 564 |
| Columns ($y_{ijk.}$) | 572 | 579 | 597 | 530 | 561 | 557 |

The ANOVA is summarized in Table 5.25. We have added a column to this table indicating how the number of degrees of freedom for each sum of squares is determined.

**TABLE 5.25** Analysis of Variance for the Radar Detection Experiment Run as a $3\times2$ Factorial in a Latin Square

| Source of Variation | Sum of Squares | Degrees of Freedom | General Formula for Degrees of Freedom | Mean Square | $F_0$ | $P$-Value |
|---|---:|---:|---:|---:|---:|---:|
| Ground clutter, $G$ | 571.50 | 2 | $a-1$ | 285.75 | 28.86 | $<0.0001$ |
| Filter type, $F$ | 1469.44 | 1 | $b-1$ | 1469.44 | 148.43 | $<0.0001$ |
| $GF$ | 126.73 | 2 | $(a-1)(b-1)$ | 63.37 | 6.40 | 0.0071 |
| Days (rows) | 4.33 | 5 | $ab-1$ | 0.87 | | |
| Operators (columns) | 428.00 | 5 | $ab-1$ | 85.60 | | |
| Error | 198.00 | 20 | $(ab-1)(ab-2)$ | 9.90 | | |
| Total | 2798.00 | 35 | $(ab)^2-1$ | | | |
