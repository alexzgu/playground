Manual transcription from the rendered PDF pages, checked against the extracted text layer.

===PAGE 95===
### PDF page 95 (book page 86)

For instance, consider an example in which $p = 100$ and $H_0:\beta_1=\beta_2=\cdots=\beta_p=0$ is true, so no variable is truly associated with the response. In this situation, about 5 % of the $p$-values associated with each variable (of the type shown in Table 3.4) will be below 0.05 by chance. In other words, we expect to see approximately five small $p$-values even in the absence of any true association between the predictors and the response.[^8] In fact, it is likely that we will observe at least one $p$-value below 0.05 by chance! Hence, if we use the individual $t$-statistics and associated $p$-values in order to decide whether or not there is any association between the variables and the response, there is a very high chance that we will incorrectly conclude that there is a relationship. However, the $F$-statistic does not suffer from this problem because it adjusts for the number of predictors. Hence, if $H_0$ is true, there is only a 5 % chance that the $F$-statistic will result in a $p$-value below 0.05, regardless of the number of predictors or the number of observations.

The approach of using an $F$-statistic to test for any association between the predictors and the response works when $p$ is relatively small, and certainly small compared to $n$. However, sometimes we have a very large number of variables. If $p > n$ then there are more coefficients $\beta_j$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the $F$-statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When $p$ is large, some of the approaches discussed in the next section, such as forward selection, can be used. This *high-dimensional* setting is discussed in greater detail in Chapter 6.

*[margin: high-dimensional]*

**Two: Deciding on Important Variables**

As discussed in the previous section, the first step in a multiple regression analysis is to compute the $F$-statistic and to examine the associated $p$-value. If we conclude on the basis of that $p$-value that at least one of the predictors is related to the response, then it is natural to wonder *which* are the guilty ones! We could look at the individual $p$-values as in Table 3.4, but as discussed (and as further explored in Chapter 13), if $p$ is large we are likely to make some false discoveries.

It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors. The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as *variable selection*. The variable selection problem is studied extensively in Chapter 6, and so here we will provide only a brief outline of some classical approaches.

*[margin: variable selection]*

Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors. For instance, if $p=2$, then we can consider four models: (1) a model containing no variables, (2) a model containing $X_1$ only, (3) a model containing

[^8]: This is related to the important concept of *multiple testing*, which is the focus of Chapter 13.

===PAGE 96===
### PDF page 96 (book page 87)

$X_2$ only, and (4) a model containing both $X_1$ and $X_2$. We can then select the best model out of all of the models that we have considered. How do we determine which model is best? Various statistics can be used to judge the quality of a model. These include Mallow's $C_p$, Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^2$. These are discussed in more detail in Chapter 6. We can also determine which model is best by plotting various model outputs, such as the residuals, in order to search for patterns.

*[margin: Mallow's $C_p$]*

*[margin: Akaike information criterion]*

*[margin: Bayesian information criterion]*

*[margin: adjusted $R^2$]*

Unfortunately, there are a total of $2^p$ models that contain subsets of $p$ variables. This means that even for moderate $p$, trying out every possible subset of the predictors is infeasible. For instance, we saw that if $p=2$, then there are $2^2=4$ models to consider. But if $p=30$, then we must consider $2^{30}=1{,}073{,}741{,}824$ models! This is not practical. Therefore, unless $p$ is very small, we cannot consider all $2^p$ models, and instead we need an automated and efficient approach to choose a smaller set of models to consider. There are three classical approaches for this task:

- *Forward selection.* We begin with the *null model*—a model that contains an intercept but no predictors. We then fit $p$ simple linear regressions and add to the null model the variable that results in the lowest RSS. We then add to that model the variable that results in the lowest RSS for the new two-variable model. This approach is continued until some stopping rule is satisfied.

  *[margin: forward selection]*

  *[margin: null model]*

- *Backward selection.* We start with all variables in the model, and remove the variable with the largest $p$-value—that is, the variable that is the least statistically significant. The new $(p-1)$-variable model is fit, and the variable with the largest $p$-value is removed. This procedure continues until a stopping rule is reached. For instance, we may stop when all remaining variables have a $p$-value below some threshold.

  *[margin: backward selection]*

- *Mixed selection.* This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add variables one-by-one. Of course, as we noted with the `Advertising` example, the $p$-values for variables can become larger as new predictors are added to the model. Hence, if at any point the $p$-value for one of the variables in the model rises above a certain threshold, then we remove that variable from the model. We continue to perform these forward and backward steps until all variables in the model have a sufficiently low $p$-value, and all variables outside the model would have a large $p$-value if added to the model.

  *[margin: mixed selection]*

Backward selection cannot be used if $p>n$, while forward selection can always be used. Forward selection is a greedy approach, and might include variables early that later become redundant. Mixed selection can remedy this.

===PAGE 97===
### PDF page 97 (book page 88)

**Three: Model Fit**

Two of the most common numerical measures of model fit are the RSE and $R^2$, the fraction of variance explained. These quantities are computed and interpreted in the same fashion as for simple linear regression.

Recall that in simple regression, $R^2$ is the square of the correlation of the response and the variable. In multiple linear regression, it turns out that it equals $\operatorname{Cor}(Y,\hat{Y})^2$, the square of the correlation between the response and the fitted linear model; in fact one property of the fitted linear model is that it maximizes this correlation among all possible linear models.

An $R^2$ value close to 1 indicates that the model explains a large portion of the variance in the response variable. As an example, we saw in Table 3.6 that for the `Advertising` data, the model that uses all three advertising media to predict `sales` has an $R^2$ of 0.8972. On the other hand, the model that uses only `TV` and `radio` to predict `sales` has an $R^2$ value of 0.89719. In other words, there is a small increase in $R^2$ if we include `newspaper` advertising in the model that already contains `TV` and `radio` advertising, even though we saw earlier that the $p$-value for `newspaper` advertising in Table 3.4 is not significant. It turns out that $R^2$ will always increase when more variables are added to the model, even if those variables are only weakly associated with the response. This is due to the fact that adding another variable always results in a decrease in the residual sum of squares on the training data (though not necessarily the testing data). Thus, the $R^2$ statistic, which is also computed on the training data, must increase. The fact that adding `newspaper` advertising to the model containing only `TV` and `radio` advertising leads to just a tiny increase in $R^2$ provides additional evidence that `newspaper` can be dropped from the model. Essentially, `newspaper` provides no real improvement in the model fit to the training samples, and its inclusion will likely lead to poor results on independent test samples due to overfitting.

By contrast, the model containing only `TV` as a predictor had an $R^2$ of 0.61 (Table 3.2). Adding `radio` to the model leads to a substantial improvement in $R^2$. This implies that a model that uses `TV` and `radio` expenditures to predict `sales` is substantially better than one that uses only `TV` advertising. We could further quantify this improvement by looking at the $p$-value for the `radio` coefficient in a model that contains only `TV` and `radio` as predictors.

The model that contains only `TV` and `radio` as predictors has an RSE of 1.681, and the model that also contains `newspaper` as a predictor has an RSE of 1.686 (Table 3.6). In contrast, the model that contains only `TV` has an RSE of 3.26 (Table 3.2). This corroborates our previous conclusion that a model that uses `TV` and `radio` expenditures to predict `sales` is much more accurate (on the training data) than one that only uses `TV` spending. Furthermore, given that `TV` and `radio` expenditures are used as predictors, there is no point in also using `newspaper` spending as a predictor in the model. The observant reader may wonder how RSE can increase when `newspaper` is added to the model given that RSS must decrease. In general RSE is defined as

$$
\mathrm{RSE} = \sqrt{\frac{1}{n-p-1}\mathrm{RSS}}, \tag{3.25}
$$
