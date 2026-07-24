### PDF page 247 (book page 239)

**FIGURE 6.3.** For the `Credit` data set, three quantities are displayed for the best model containing $d$ predictors, for $d$ ranging from 1 to 11. The overall best model, based on each of these quantities, is shown as a blue cross. Left: Square root of BIC. Center: Validation set errors. Right: Cross-validation errors.

the model for which the resulting estimated test error is smallest. This procedure has an advantage relative to AIC, BIC, $C_p$, and adjusted $R^2$, in that it provides a direct estimate of the test error, and makes fewer assumptions about the true underlying model. It can also be used in a wider range of model selection tasks, even in cases where it is hard to pinpoint the model degrees of freedom (e.g. the number of predictors in the model) or hard to estimate the error variance $\sigma^2$. Note that when cross-validation is used, the sequence of models $\mathcal{M}_k$ in Algorithms 6.1–6.3 is determined separately for each training fold, and the validation errors are averaged over all folds for each model size $k$. This means, for example with best-subset regression, that $\mathcal{M}_k$, the best subset of size $k$, can differ across the folds. Once the best size $k$ is chosen, we find the best model of that size on the full data set.

In the past, performing cross-validation was computationally prohibitive for many problems with large $p$ and/or large $n$, and so AIC, BIC, $C_p$, and adjusted $R^2$ were more attractive approaches for choosing among a set of models. However, nowadays with fast computers, the computations required to perform cross-validation are hardly ever an issue. Thus, cross-validation is a very attractive approach for selecting from among a number of models under consideration.

Figure 6.3 displays, as a function of $d$, the BIC, validation set errors, and cross-validation errors on the `Credit` data, for the best $d$-variable model. The validation errors were calculated by randomly selecting three-quarters of the observations as the training set, and the remainder as the validation set. The cross-validation errors were computed using $k=10$ folds. In this case, the validation and cross-validation methods both result in a six-variable model. However, all three approaches suggest that the four-, five-, and six-variable models are roughly equivalent in terms of their test errors.

In fact, the estimated test error curves displayed in the center and right-hand panels of Figure 6.3 are quite flat. While a three-variable model clearly has lower estimated test error than a two-variable model, the estimated test errors of the 3- to 11-variable models are quite similar. Furthermore, if we

### PDF page 248 (book page 240)

repeated the validation set approach using a different split of the data into a training set and a validation set, or if we repeated cross-validation using a different set of cross-validation folds, then the precise model with the lowest estimated test error would surely change. In this setting, we can select a model using the *one-standard-error rule*. *[margin: one-standard-error rule]* We first calculate the standard error of the estimated test MSE for each model size, and then select the smallest model for which the estimated test error is within one standard error of the lowest point on the curve. The rationale here is that if a set of models appear to be more or less equally good, then we might as well choose the simplest model—that is, the model with the smallest number of predictors. In this case, applying the one-standard-error rule to the validation set or cross-validation approach leads to selection of the three-variable model.

**6.2  Shrinkage Methods**

The subset selection methods described in Section 6.1 involve using least squares to fit a linear model that contains a subset of the predictors. As an alternative, we can fit a model containing all $p$ predictors using a technique that *constrains* or *regularizes* the coefficient estimates, or equivalently, that *shrinks* the coefficient estimates towards zero. It may not be immediately obvious why such a constraint should improve the fit, but it turns out that shrinking the coefficient estimates can significantly reduce their variance. The two best-known techniques for shrinking the regression coefficients towards zero are *ridge regression* and *the lasso*.

**6.2.1  Ridge Regression**

Recall from Chapter 3 that the least squares fitting procedure estimates $\beta_0,\beta_1,\ldots,\beta_p$ using the values that minimize

$$
\operatorname{RSS}=\sum_{i=1}^{n}\left(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\right)^2.
$$

*Ridge regression* is very similar to least squares, except that the coefficients are estimated by minimizing a slightly different quantity. *[margin: ridge regression]* In particular, the ridge regression coefficient estimates $\hat{\beta}^{R}$ are the values that minimize

$$
\sum_{i=1}^{n}\left(y_i-\beta_0-\sum_{j=1}^{p}\beta_jx_{ij}\right)^2
+\lambda\sum_{j=1}^{p}\beta_j^2
=\operatorname{RSS}+\lambda\sum_{j=1}^{p}\beta_j^2, \tag{6.5}
$$

where $\lambda\geq 0$ is a *tuning parameter*, to be determined separately. *[margin: tuning parameter]* Equation 6.5 trades off two different criteria. As with least squares, ridge regression seeks coefficient estimates that fit the data well, by making the RSS small. However, the second term, $\lambda\sum_j\beta_j^2$, called a *shrinkage penalty*, is small when $\beta_1,\ldots,\beta_p$ are close to zero, and so it has the effect of *shrinking* the estimates of $\beta_j$ towards zero. *[margin: shrinkage penalty]* The tuning parameter $\lambda$ serves to control

### PDF page 249 (book page 241)

**FIGURE 6.4.** The standardized ridge regression coefficients are displayed for the `Credit` data set, as a function of $\lambda$ and $\lVert\hat{\beta}^{R}_{\lambda}\rVert_2/\lVert\hat{\beta}\rVert_2$.

the relative impact of these two terms on the regression coefficient estimates. When $\lambda=0$, the penalty term has no effect, and ridge regression will produce the least squares estimates. However, as $\lambda\to\infty$, the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates will approach zero. Unlike least squares, which generates only one set of coefficient estimates, ridge regression will produce a different set of coefficient estimates, $\hat{\beta}^{R}_{\lambda}$, for each value of $\lambda$. Selecting a good value for $\lambda$ is critical; we defer this discussion to Section 6.2.3, where we use cross-validation.

Note that in (6.5), the shrinkage penalty is applied to $\beta_1,\ldots,\beta_p$, but not to the intercept $\beta_0$. We want to shrink the estimated association of each variable with the response; however, we do not want to shrink the intercept, which is simply a measure of the mean value of the response when $x_{i1}=x_{i2}=\cdots=x_{ip}=0$. If we assume that the variables—that is, the columns of the data matrix $\mathbf{X}$—have been centered to have mean zero before ridge regression is performed, then the estimated intercept will take the form $\hat{\beta}_0=\bar{y}=\sum_{i=1}^{n}y_i/n$.

**An Application to the Credit Data**

In Figure 6.4, the ridge regression coefficient estimates for the `Credit` data set are displayed. In the left-hand panel, each curve corresponds to the ridge regression coefficient estimate for one of the ten variables, plotted as a function of $\lambda$. For example, the black solid line represents the ridge regression estimate for the `income` coefficient, as $\lambda$ is varied. At the extreme left-hand side of the plot, $\lambda$ is essentially zero, and so the corresponding ridge coefficient estimates are the same as the usual least squares estimates. But as $\lambda$ increases, the ridge coefficient estimates shrink towards zero. When $\lambda$ is extremely large, then all of the ridge coefficient estimates are basically zero; this corresponds to the *null model* that contains no predictors. In this plot, the `income`, `limit`, `rating`, and `student` variables are displayed in distinct colors, since these variables tend to have by far the largest coefficient estimates. While the ridge coefficient estimates tend to decrease in aggregate as $\lambda$ increases, individual coefficients, such as `rating` and `income`, may occasionally increase as $\lambda$ increases.
