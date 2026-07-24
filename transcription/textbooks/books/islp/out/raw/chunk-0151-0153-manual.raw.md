===PAGE 151===

### PDF page 151 (book page 142)

| | Coefficient | Std. error | $z$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| `Intercept` | −10.6513 | 0.3612 | −29.5 | <0.0001 |
| `balance` | 0.0055 | 0.0002 | 24.9 | <0.0001 |

**TABLE 4.1.** *For the* `Default` *data, estimated coefficients of the logistic regression model that predicts the probability of* `default` *using* `balance`*. A one-unit increase in* `balance` *is associated with an increase in the log odds of* `default` *by 0.0055 units.*

| | Coefficient | Std. error | $z$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| `Intercept` | −3.5041 | 0.0707 | −49.55 | <0.0001 |
| `student[Yes]` | 0.4049 | 0.1150 | 3.52 | 0.0004 |

**TABLE 4.2.** *For the* `Default` *data, estimated coefficients of the logistic regression model that predicts the probability of* `default` *using student status. Student status is encoded as a dummy variable, with a value of 1 for a student and a value of 0 for a non-student, and represented by the variable* `student[Yes]` *in the table.*

for an individual with a `balance` of \$1,000 is

$$
\hat{p}(X)
= \frac{e^{\hat{\beta}_0+\hat{\beta}_1 X}}{1+e^{\hat{\beta}_0+\hat{\beta}_1 X}}
= \frac{e^{-10.6513+0.0055\times 1{,}000}}{1+e^{-10.6513+0.0055\times 1{,}000}}
= 0.00576,
$$

which is below 1 %. In contrast, the predicted probability of default for an individual with a `balance` of \$2,000 is much higher, and equals 0.586 or 58.6 %.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the `Default` data set contains the qualitative variable `student`. To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students. The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated $p$-value is statistically significant. This indicates that students tend to have higher default probabilities than non-students:

$$
\widehat{\Pr}(\texttt{default}=\texttt{Yes}\mid\texttt{student}=\texttt{Yes})
= \frac{e^{-3.5041+0.4049\times 1}}{1+e^{-3.5041+0.4049\times 1}}
= 0.0431,
$$

$$
\widehat{\Pr}(\texttt{default}=\texttt{Yes}\mid\texttt{student}=\texttt{No})
= \frac{e^{-3.5041+0.4049\times 0}}{1+e^{-3.5041+0.4049\times 0}}
= 0.0292.
$$

**4.3.4 Multiple Logistic Regression**

We now consider the problem of predicting a binary response using multiple predictors. By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:

$$
\log\left(\frac{p(X)}{1-p(X)}\right)
= \beta_0+\beta_1 X_1+\cdots+\beta_p X_p,
\tag{4.6}
$$

where $X=(X_1,\ldots,X_p)$ are $p$ predictors. Equation 4.6 can be rewritten as

$$
p(X)=\frac{e^{\beta_0+\beta_1 X_1+\cdots+\beta_p X_p}}
{1+e^{\beta_0+\beta_1 X_1+\cdots+\beta_p X_p}}.
\tag{4.7}
$$

===PAGE 152===

### PDF page 152 (book page 143)

| | Coefficient | Std. error | $z$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| `Intercept` | −10.8690 | 0.4923 | −22.08 | <0.0001 |
| `balance` | 0.0057 | 0.0002 | 24.74 | <0.0001 |
| `income` | 0.0030 | 0.0082 | 0.37 | 0.7115 |
| `student[Yes]` | −0.6468 | 0.2362 | −2.74 | 0.0062 |

**TABLE 4.3.** *For the* `Default` *data, estimated coefficients of the logistic regression model that predicts the probability of* `default` *using* `balance`*,* `income`*, and student status. Student status is encoded as a dummy variable* `student[Yes]`*, with a value of 1 for a student and a value of 0 for a non-student. In fitting this model,* `income` *was measured in thousands of dollars.*

Just as in Section 4.3.2, we use the maximum likelihood method to estimate $\beta_0,\beta_1,\ldots,\beta_p$.

Table 4.3 shows the coefficient estimates for a logistic regression model that uses `balance`, `income` (in thousands of dollars), and `student` status to predict probability of `default`. There is a surprising result here. The $p$-values associated with `balance` and the dummy variable for `student` status are very small, indicating that each of these variables is associated with the probability of `default`. However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than non-students. In contrast, the coefficient for the dummy variable is positive in Table 4.2. How is it possible for student status to be associated with an *increase* in probability of default in Table 4.2 and a *decrease* in probability of default in Table 4.3? The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox. The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance. The negative coefficient for `student` in the multiple logistic regression indicates that *for a fixed value of* `balance` *and* `income`*,* a student is less likely to default than a non-student. Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of `balance`. But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of `balance` and `income`, suggest the opposite effect: the overall student default rate is higher than the non-student default rate. Consequently, there is a positive coefficient for `student` in the single variable logistic regression output shown in Table 4.2.

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy. The variables `student` and `balance` are correlated. Students tend to hold higher levels of debt, which is in turn associated with higher probability of default. In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates. Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students. This is an important distinction for a credit card company that is trying to determine to whom they should offer credit. A student is riskier than a non-student if no information about the student's credit card

===PAGE 153===

### PDF page 153 (book page 144)

**FIGURE 4.3.** *Confounding in the* `Default` *data. Left: Default rates are shown for students (orange) and non-students (blue). The solid lines display default rate as a function of* `balance`*, while the horizontal broken lines display the overall default rates. Right: Boxplots of* `balance` *for students (orange) and non-students (blue) are shown.* *[Figure: two side-by-side plots. Left — Default Rate against Credit Card Balance, with orange and blue solid curves rising sharply at high balances and corresponding horizontal broken lines near the bottom of the plot. Right — blue “No” and orange “Yes” boxplots of Credit Card Balance by Student Status; the student distribution is shifted upward, though the two distributions overlap.]*

balance is available. However, that student is less risky than a non-student *with the same credit card balance!*

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant. As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors. In general, the phenomenon seen in Figure 4.3 is known as *confounding*. *[margin: confounding]*

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions. For example, a student with a credit card balance of \$1,500 and an income of \$40,000 has an estimated probability of default of

$$
\hat{p}(X)
= \frac{e^{-10.869+0.00574\times 1{,}500+0.003\times 40-0.6468\times 1}}
{1+e^{-10.869+0.00574\times 1{,}500+0.003\times 40-0.6468\times 1}}
= 0.058.
\tag{4.8}
$$

A non-student with the same balance and income has an estimated probability of default of

$$
\hat{p}(X)
= \frac{e^{-10.869+0.00574\times 1{,}500+0.003\times 40-0.6468\times 0}}
{1+e^{-10.869+0.00574\times 1{,}500+0.003\times 40-0.6468\times 0}}
= 0.105.
\tag{4.9}
$$

(Here we multiply the `income` coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with `income` measured in units of \$1,000.)

**4.3.5 Multinomial Logistic Regression**

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: `stroke`, `drug overdose`, `epileptic seizure`. However, the logistic regression approach that we have seen in this section only allows for $K=2$ classes for the response variable.
