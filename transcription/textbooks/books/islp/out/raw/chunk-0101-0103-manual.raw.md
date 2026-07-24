Manual transcription from the rendered PDF pages, checked against the extracted text layer.

===PAGE 101===
### PDF page 101 (book page 92)

*[Figure: a 7-by-7 scatterplot matrix for the `Credit` variables `Balance`, `Age`, `Cards`, `Education`, `Income`, `Limit`, and `Rating`. Variable names appear on the diagonal. The off-diagonal panels show blue points for each pair of variables; the strongest relationships are between `Balance`, `Income`, `Limit`, and `Rating`, with `Limit` and `Rating` nearly perfectly linear.]*

**FIGURE 3.6.** *The `Credit` data set contains information about `balance`, `age`, `cards`, `education`, `income`, `limit`, and `rating` for a number of potential customers.*

notice that the $p$-value for the dummy variable is very high. This indicates that there is no statistical evidence of a difference in average credit card balance based on house ownership.

The decision to code owners as 1 and non-owners as 0 in (3.27) is arbitrary, and has no effect on the regression fit, but does alter the interpretation of the coefficients. If we had coded non-owners as 1 and owners as 0, then the estimates for $\beta_0$ and $\beta_1$ would have been 529.53 and $-19.73$, respectively, leading once again to a prediction of credit card debt of \$529.53 $-$ \$19.73 $=$ \$509.80 for non-owners and a prediction of \$529.53 for owners. Alternatively, instead of a 0/1 coding scheme, we could create a dummy variable

$$
x_i =
\begin{cases}
1 & \text{if } i\text{th person owns a house},\\
-1 & \text{if } i\text{th person does not own a house}
\end{cases}
$$

and use this variable in the regression equation. This results in the model

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i =
\begin{cases}
\beta_0 + \beta_1 + \epsilon_i & \text{if } i\text{th person owns a house},\\
\beta_0 - \beta_1 + \epsilon_i & \text{if } i\text{th person does not own a house}.
\end{cases}
$$

===PAGE 102===
### PDF page 102 (book page 93)

|  | Coefficient | Std. error | $t$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| Intercept | 509.80 | 33.13 | 15.389 | $< 0.0001$ |
| `own[Yes]` | 19.73 | 46.05 | 0.429 | 0.6690 |

**TABLE 3.7.** *Least squares coefficient estimates associated with the regression of `balance` onto `own` in the `Credit` data set. The linear model is given in (3.27). That is, ownership is encoded as a dummy variable, as in (3.26).*

Now $\beta_0$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_1$ is the amount by which house owners and non-owners have credit card balances that are above and below the average, respectively.[^11] In this example, the estimate for $\beta_0$ is \$519.665, halfway between the non-owner and owner averages of \$509.80 and \$529.53. The estimate for $\beta_1$ is \$9.865, which is half of \$19.73, the average difference between owners and non-owners. It is important to note that the final predictions for the credit balances of owners and non-owners will be identical regardless of the coding scheme used. The only difference is in the way that the coefficients are interpreted.

**Qualitative Predictors with More than Two Levels**

When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values. In this situation, we can create additional dummy variables. For example, for the `region` variable we create two dummy variables. The first could be

$$
x_{i1} =
\begin{cases}
1 & \text{if } i\text{th person is from the South},\\
0 & \text{if } i\text{th person is not from the South},
\end{cases} \tag{3.28}
$$

and the second could be

$$
x_{i2} =
\begin{cases}
1 & \text{if } i\text{th person is from the West},\\
0 & \text{if } i\text{th person is not from the West}.
\end{cases} \tag{3.29}
$$

Then both of these variables can be used in the regression equation, in order to obtain the model

$$
y_i = \beta_0+\beta_1x_{i1}+\beta_2x_{i2}+\epsilon_i =
\begin{cases}
\beta_0+\beta_1+\epsilon_i & \text{if } i\text{th person is from the South},\\
\beta_0+\beta_2+\epsilon_i & \text{if } i\text{th person is from the West},\\
\beta_0+\epsilon_i & \text{if } i\text{th person is from the East}.
\end{cases} \tag{3.30}
$$

Now $\beta_0$ can be interpreted as the average credit card balance for individuals from the East, $\beta_1$ can be interpreted as the difference in the average balance between people from the South versus the East, and $\beta_2$ can be interpreted as the difference in the average balance between those from the West versus the East. There will always be one fewer dummy variable than the number of levels. The level with no dummy variable—East in this example—is known as the *baseline*.

*[margin: baseline]*

[^11]: Technically $\beta_0$ is half the sum of the average debt for house owners and the average debt for non-house owners. Hence, $\beta_0$ is exactly equal to the overall average only if the two groups have an equal number of members.

===PAGE 103===
### PDF page 103 (book page 94)

|  | Coefficient | Std. error | $t$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| Intercept | 531.00 | 46.32 | 11.464 | $< 0.0001$ |
| `region[South]` | $-12.50$ | 56.68 | $-0.221$ | 0.8260 |
| `region[West]` | $-18.69$ | 65.02 | $-0.287$ | 0.7740 |

**TABLE 3.8.** *Least squares coefficient estimates associated with the regression of `balance` onto `region` in the `Credit` data set. The linear model is given in (3.30). That is, `region` is encoded via two dummy variables (3.28) and (3.29).*

From Table 3.8, we see that the estimated `balance` for the baseline, East, is \$531.00. It is estimated that those in the South will have \$18.69 less debt than those in the East, and that those in the West will have \$12.50 less debt than those in the East. However, the $p$-values associated with the coefficient estimates for the two dummy variables are very large, suggesting no statistical evidence of a real difference in average credit card balance between South and East or between West and East.[^12] Once again, the level selected as the baseline category is arbitrary, and the final predictions for each group will be the same regardless of this choice. However, the coefficients and their $p$-values do depend on the choice of dummy variable coding. Rather than rely on the individual coefficients, we can use an $F$-test to test $H_0:\beta_1=\beta_2=0$; this does not depend on the coding. This $F$-test has a $p$-value of 0.96, indicating that we cannot reject the null hypothesis that there is no relationship between `balance` and `region`.

Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors. For example, to regress `balance` on both a quantitative variable such as `income` and a qualitative variable such as `student`, we must simply create a dummy variable for `student` and then fit a multiple regression model using `income` and the dummy variable as predictors for credit card balance.

There are many different ways of coding qualitative variables besides the dummy variable approach taken here. All of these approaches lead to equivalent model fits, but the coefficients are different and have different interpretations, and are designed to measure particular *contrasts*. This topic is beyond the scope of the book.

*[margin: contrast]*

**3.3.2 Extensions of the Linear Model**

The standard linear regression model (3.19) provides interpretable results and works quite well on many real-world problems. However, it makes several highly restrictive assumptions that are often violated in practice. Two of the most important assumptions state that the relationship between the predictors and response are *additive* and *linear*. The additivity assumption means that the association between a predictor $X_j$ and the response $Y$ does not depend on the values of the other predictors. The linearity assumption states that the change in the response $Y$ associated with a one-unit change in $X_j$ is constant, regardless of the value of $X_j$. In later chapters of this book, we examine a number of sophisticated methods that relax these two

*[margin: additive]*

*[margin: linear]*

[^12]: There could still in theory be a difference between South and West, although the data here does not suggest any difference.
