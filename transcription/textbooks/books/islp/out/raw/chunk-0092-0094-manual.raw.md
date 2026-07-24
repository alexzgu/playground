Manual transcription from the rendered PDF pages, checked against the extracted text layer.

===PAGE 92===
### PDF page 92 (book page 83)

|  | Coefficient | Std. error | $t$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| Intercept | 2.939 | 0.3119 | 9.42 | $< 0.0001$ |
| `TV` | 0.046 | 0.0014 | 32.81 | $< 0.0001$ |
| `radio` | 0.189 | 0.0086 | 21.89 | $< 0.0001$ |
| `newspaper` | $-0.001$ | 0.0059 | $-0.18$ | 0.8599 |

**TABLE 3.4.** *For the `Advertising` data, least squares coefficient estimates of the multiple linear regression of number of units sold on `TV`, `radio`, and `newspaper` advertising budgets.*

|  | `TV` | `radio` | `newspaper` | `sales` |
|---|---:|---:|---:|---:|
| `TV` | 1.0000 | 0.0548 | 0.0567 | 0.7822 |
| `radio` |  | 1.0000 | 0.3541 | 0.5762 |
| `newspaper` |  |  | 1.0000 | 0.2283 |
| `sales` |  |  |  | 1.0000 |

**TABLE 3.5.** *Correlation matrix for `TV`, `radio`, `newspaper`, and `sales` for the `Advertising` data.*

opposite? In fact it does. Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5. Notice that the correlation between `radio` and `newspaper` is 0.35. This indicates that markets with high `newspaper` advertising tend to also have high `radio` advertising. Now suppose that the multiple regression is correct and `newspaper` advertising is not associated with `sales`, but `radio` advertising is associated with `sales`. Then in markets where we spend more on `radio` our `sales` will tend to be higher, and as our correlation matrix shows, we also tend to spend more on `newspaper` advertising in those same markets. Hence, in a simple linear regression which only examines `sales` versus `newspaper`, we will observe that higher values of `newspaper` tend to be associated with higher values of `sales`, even though `newspaper` advertising is not directly associated with `sales`. So `newspaper` advertising is a surrogate for `radio` advertising; `newspaper` gets “credit” for the association between `radio` on `sales`.

This slightly counterintuitive result is very common in many real life situations. Consider an absurd example to illustrate the point. Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between `sales` and `newspaper`. Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks. In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks. A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.

**3.2.2 Some Important Questions**

When we perform multiple linear regression, we usually are interested in answering a few important questions.

===PAGE 93===
### PDF page 93 (book page 84)

1. *Is at least one of the predictors $X_1, X_2, \ldots, X_p$ useful in predicting the response?*

2. *Do all the predictors help to explain $Y$, or is only a subset of the predictors useful?*

3. *How well does the model fit the data?*

4. *Given a set of predictor values, what response value should we predict, and how accurate is our prediction?*

We now address each of these questions in turn.

**One: Is There a Relationship Between the Response and Predictors?**

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_1 = 0$. In the multiple regression setting with $p$ predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_1 = \beta_2 = \cdots = \beta_p = 0$. As in the simple linear regression setting, we use a hypothesis test to answer this question. We test the null hypothesis,

$$
H_0:\ \beta_1 = \beta_2 = \cdots = \beta_p = 0
$$

versus the alternative

$$
H_a:\ \text{at least one } \beta_j \text{ is non-zero}.
$$

This hypothesis test is performed by computing the $F$-statistic,

$$
F = \frac{(\mathrm{TSS} - \mathrm{RSS})/p}{\mathrm{RSS}/(n-p-1)}, \tag{3.23}
$$

*[margin: F-statistic]*

where, as with simple linear regression, $\mathrm{TSS} = \sum (y_i-\bar{y})^2$ and $\mathrm{RSS} = \sum (y_i-\hat{y}_i)^2$. If the linear model assumptions are correct, one can show that

$$
\mathbb{E}\{\mathrm{RSS}/(n-p-1)\} = \sigma^2
$$

and that, provided $H_0$ is true,

$$
\mathbb{E}\{(\mathrm{TSS}-\mathrm{RSS})/p\} = \sigma^2.
$$

Hence, when there is no relationship between the response and predictors, one would expect the $F$-statistic to take on a value close to 1. On the other hand, if $H_a$ is true, then $\mathbb{E}\{(\mathrm{TSS}-\mathrm{RSS})/p\} > \sigma^2$, so we expect $F$ to be greater than 1.

The $F$-statistic for the multiple linear regression model obtained by regressing `sales` onto `radio`, `TV`, and `newspaper` is shown in Table 3.6. In this example the $F$-statistic is 570. Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_0$. In other words, the large $F$-statistic suggests that at least one of the advertising media must be related to `sales`. However, what if the $F$-statistic had been closer to 1? How large does the $F$-statistic need to be before we can reject $H_0$ and

===PAGE 94===
### PDF page 94 (book page 85)

| Quantity | Value |
|---|---:|
| Residual standard error | 1.69 |
| $R^2$ | 0.897 |
| $F$-statistic | 570 |

**TABLE 3.6.** *More information about the least squares model for the regression of number of units sold on `TV`, `newspaper`, and `radio` advertising budgets in the `Advertising` data. Other information about this model was displayed in Table 3.4.*

conclude that there is a relationship? It turns out that the answer depends on the values of $n$ and $p$. When $n$ is large, an $F$-statistic that is just a little larger than 1 might still provide evidence against $H_0$. In contrast, a larger $F$-statistic is needed to reject $H_0$ if $n$ is small. When $H_0$ is true and the errors $\epsilon_i$ have a normal distribution, the $F$-statistic follows an $F$-distribution.[^6] For any given value of $n$ and $p$, any statistical software package can be used to compute the $p$-value associated with the $F$-statistic using this distribution. Based on this $p$-value, we can determine whether or not to reject $H_0$. For the advertising data, the $p$-value associated with the $F$-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased `sales`.

In (3.23) we are testing $H_0$ that all the coefficients are zero. Sometimes we want to test that a particular subset of $q$ of the coefficients are zero. This corresponds to a null hypothesis

$$
H_0:\quad \beta_{p-q+1} = \beta_{p-q+2} = \cdots = \beta_p = 0,
$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables *except* those last $q$. Suppose that the residual sum of squares for that model is $\mathrm{RSS}_0$. Then the appropriate $F$-statistic is

$$
F = \frac{(\mathrm{RSS}_0-\mathrm{RSS})/q}{\mathrm{RSS}/(n-p-1)}. \tag{3.24}
$$

Notice that in Table 3.4, for each individual predictor a $t$-statistic and a $p$-value were reported. These provide information about whether each individual predictor is related to the response, after adjusting for the other predictors. It turns out that each of these is exactly equivalent[^7] to the $F$-test that omits that single variable from the model, leaving all the others in—i.e. $q=1$ in (3.24). So it reports the *partial effect* of adding that variable to the model. For instance, as we discussed earlier, these $p$-values indicate that `TV` and `radio` are related to `sales`, but that there is no evidence that `newspaper` is associated with `sales`, when `TV` and `radio` are held fixed.

Given these individual $p$-values for each variable, why do we need to look at the overall $F$-statistic? After all, it seems likely that if any one of the $p$-values for the individual variables is very small, then *at least one of the predictors is related to the response*. However, this logic is flawed, especially when the number of predictors $p$ is large.

[^6]: Even if the errors are not normally-distributed, the $F$-statistic approximately follows an $F$-distribution provided that the sample size $n$ is large.

[^7]: The square of each $t$-statistic is the corresponding $F$-statistic.
