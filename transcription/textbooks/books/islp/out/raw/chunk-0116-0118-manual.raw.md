Manual transcription from the rendered PDF pages, checked against the extracted text layer.

===PAGE 116===
### PDF page 116 (book page 107)

*[Figure: two contour plots of RSS for regressions using the `Credit` data. Left: nearly circular contours labeled 21.25, 21.5, and 21.8, with $\beta_{\mathrm{Limit}}$ on the horizontal axis from about 0.16 to 0.19 and $\beta_{\mathrm{Age}}$ on the vertical axis from about $-5$ to 0; a black dot and dashed guides mark the sharply defined minimum near $(0.174,-2.3)$. Right: a long narrow diagonal valley of contours labeled 21.5 and 21.8, with $\beta_{\mathrm{Limit}}$ from about $-0.1$ to 0.2 and $\beta_{\mathrm{Rating}}$ from 0 to 5; a black dot and dashed guides mark the minimum near $(0.025,2.2)$.]*

**FIGURE 3.15.** *Contour plots for the RSS values as a function of the parameters $\beta$ for various regressions involving the `Credit` data set. In each plot, the black dots represent the coefficient values corresponding to the minimum RSS.* Left: *A contour plot of RSS for the regression of `balance` onto `age` and `limit`. The minimum value is well defined.* Right: *A contour plot of RSS for the regression of `balance` onto `rating` and `limit`. Because of the collinearity, there are many pairs $(\beta_{\mathrm{Limit}},\beta_{\mathrm{Rating}})$ with a similar value for RSS.*

that correspond to the same RSS, with ellipses nearest to the center taking on the lowest values of RSS. The black dots and associated dashed lines represent the coefficient estimates that result in the smallest possible RSS—in other words, these are the least squares estimates. The axes for `limit` and `age` have been scaled so that the plot includes possible coefficient estimates that are up to four standard errors on either side of the least squares estimates. Thus the plot includes all plausible values for the coefficients. For example, we see that the true `limit` coefficient is almost certainly somewhere between 0.15 and 0.20.

In contrast, the right-hand panel of Figure 3.15 displays contour plots of the RSS associated with possible coefficient estimates for the regression of `balance` onto `limit` and `rating`, which we know to be highly collinear. Now the contours run along a narrow valley; there is a broad range of values for the coefficient estimates that result in equal values for RSS. Hence a small change in the data could cause the pair of coefficient values that yield the smallest RSS—that is, the least squares estimates—to move anywhere along this valley. This results in a great deal of uncertainty in the coefficient estimates. Notice that the scale for the `limit` coefficient now runs from roughly $-0.2$ to 0.2; this is an eight-fold increase over the plausible range of the `limit` coefficient in the regression with `age`. Interestingly, even though the `limit` and `rating` coefficients now have much more individual uncertainty, they will almost certainly lie somewhere in this contour valley. For example, we would not expect the true value of the `limit` and `rating` coefficients to be $-0.1$ and 1 respectively, even though such a value is plausible for each coefficient individually.

Since collinearity reduces the accuracy of the estimates of the regression coefficients, it causes the standard error for $\hat{\beta}_j$ to grow. Recall that the $t$-statistic for each predictor is calculated by dividing $\hat{\beta}_j$ by its standard

===PAGE 117===
### PDF page 117 (book page 108)

|  |  | Coefficient | Std. error | $t$-statistic | $p$-value |
|---|---|---:|---:|---:|---:|
| Model 1 | Intercept | $-173.411$ | 43.828 | $-3.957$ | $< 0.0001$ |
|  | `age` | $-2.292$ | 0.672 | $-3.407$ | 0.0007 |
|  | `limit` | 0.173 | 0.005 | 34.496 | $< 0.0001$ |
| Model 2 | Intercept | $-377.537$ | 45.254 | $-8.343$ | $< 0.0001$ |
|  | `rating` | 2.202 | 0.952 | 2.312 | 0.0213 |
|  | `limit` | 0.025 | 0.064 | 0.384 | 0.7012 |

**TABLE 3.11.** *The results for two multiple regression models involving the `Credit` data set are shown. Model 1 is a regression of `balance` on `age` and `limit`, and Model 2 a regression of `balance` on `rating` and `limit`. The standard error of $\hat{\beta}_{\mathrm{limit}}$ increases 12-fold in the second regression, due to collinearity.*

error. Consequently, collinearity results in a decline in the $t$-statistic. As a result, in the presence of collinearity, we may fail to reject $H_0:\beta_j=0$. This means that the *power* of the hypothesis test—the probability of correctly detecting a non-zero coefficient—is reduced by collinearity.

*[margin: power]*

Table 3.11 compares the coefficient estimates obtained from two separate multiple regression models. The first is a regression of `balance` on `age` and `limit`, and the second is a regression of `balance` on `rating` and `limit`. In the first regression, both `age` and `limit` are highly significant with very small $p$-values. In the second, the collinearity between `limit` and `rating` has caused the standard error for the `limit` coefficient estimate to increase by a factor of 12 and the $p$-value to increase to 0.701. In other words, the importance of the `limit` variable has been masked due to the presence of collinearity. To avoid such a situation, it is desirable to identify and address potential collinearity problems while fitting the model.

A simple way to detect collinearity is to look at the correlation matrix of the predictors. An element of this matrix that is large in absolute value indicates a pair of highly correlated variables, and therefore a collinearity problem in the data. Unfortunately, not all collinearity problems can be detected by inspection of the correlation matrix: it is possible for collinearity to exist between three or more variables even if no pair of variables has a particularly high correlation. We call this situation *multicollinearity*. Instead of inspecting the correlation matrix, a better way to assess multicollinearity is to compute the *variance inflation factor* (VIF). The VIF is the ratio of the variance of $\hat{\beta}_j$ when fitting the full model divided by the variance of $\hat{\beta}_j$ if fit on its own. The smallest possible value for VIF is 1, which indicates the complete absence of collinearity. Typically in practice there is a small amount of collinearity among the predictors. As a rule of thumb, a VIF value that exceeds 5 or 10 indicates a problematic amount of collinearity. The VIF for each variable can be computed using the formula

*[margin: multicollinearity]*

*[margin: variance inflation factor]*

$$
\mathrm{VIF}(\hat{\beta}_j) = \frac{1}{1-R^2_{X_j\mid X_{-j}}},
$$

where $R^2_{X_j\mid X_{-j}}$ is the $R^2$ from a regression of $X_j$ onto all of the other predictors. If $R^2_{X_j\mid X_{-j}}$ is close to one, then collinearity is present, and so the VIF will be large.

===PAGE 118===
### PDF page 118 (book page 109)

In the `Credit` data, a regression of `balance` on `age`, `rating`, and `limit` indicates that the predictors have VIF values of 1.01, 160.67, and 160.59. As we suspected, there is considerable collinearity in the data!

When faced with the problem of collinearity, there are two simple solutions. The first is to drop one of the problematic variables from the regression. This can usually be done without much compromise to the regression fit, since the presence of collinearity implies that the information that this variable provides about the response is redundant in the presence of the other variables. For instance, if we regress `balance` onto `age` and `limit`, without the `rating` predictor, then the resulting VIF values are close to the minimum possible value of 1, and the $R^2$ drops from 0.754 to 0.75. So dropping `rating` from the set of predictors has effectively solved the collinearity problem without compromising the fit. The second solution is to combine the collinear variables together into a single predictor. For instance, we might take the average of standardized versions of `limit` and `rating` in order to create a new variable that measures *credit worthiness*.

**3.4 The Marketing Plan**

We now briefly return to the seven questions about the `Advertising` data that we set out to answer at the beginning of this chapter.

1. *Is there a relationship between sales and advertising budget?*

   This question can be answered by fitting a multiple regression model of `sales` onto `TV`, `radio`, and `newspaper`, as in (3.20), and testing the hypothesis $H_0:\beta_{\mathrm{TV}}=\beta_{\mathrm{radio}}=\beta_{\mathrm{newspaper}}=0$. In Section 3.2.2, we showed that the $F$-statistic can be used to determine whether or not we should reject this null hypothesis. In this case the $p$-value corresponding to the $F$-statistic in Table 3.6 is very low, indicating clear evidence of a relationship between advertising and sales.

2. *How strong is the relationship?*

   We discussed two measures of model accuracy in Section 3.1.3. First, the RSE estimates the standard deviation of the response from the population regression line. For the `Advertising` data, the RSE is 1.69 units while the mean value for the response is 14.022, indicating a percentage error of roughly 12 %. Second, the $R^2$ statistic records the percentage of variability in the response that is explained by the predictors. The predictors explain almost 90 % of the variance in `sales`. The RSE and $R^2$ statistics are displayed in Table 3.6.

3. *Which media are associated with sales?*

   To answer this question, we can examine the $p$-values associated with each predictor's $t$-statistic (Section 3.1.2). In the multiple linear regression displayed in Table 3.4, the $p$-values for `TV` and `radio` are low, but the $p$-value for `newspaper` is not. This suggests that only `TV` and `radio` are related to `sales`. In Chapter 6 we explore this question in greater detail.
