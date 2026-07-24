### PDF page 268 (book page 260)

**FIGURE 6.20.** *Left: PCR standardized coefficient estimates on the* `Credit` *data set for different values of $M$. Right: The ten-fold cross-validation MSE obtained using PCR, as a function of $M$.* *[Figure: Two panels against Number of Components, from 1 to 11. The left panel shows standardized coefficient paths from about $-300$ to $450$; `Income`, `Limit`, `Rating`, and `Student` are distinguished from the gray paths for the remaining variables. The right panel shows cross-validation MSE, which stays near 70,000–90,000 for one through nine components and drops sharply to about 10,000 at ten components.]*

development of a model that relies upon a small set of the original features. In this sense, PCR is more closely related to ridge regression than to the lasso. In fact, one can show that PCR and ridge regression are very closely related. One can even think of ridge regression as a continuous version of PCR![^8]

In PCR, the number of principal components, $M$, is typically chosen by cross-validation. The results of applying PCR to the `Credit` data set are shown in Figure 6.20; the right-hand panel displays the cross-validation errors obtained, as a function of $M$. On these data, the lowest cross-validation error occurs when there are $M=10$ components; this corresponds to almost no dimension reduction at all, since PCR with $M=11$ is equivalent to simply performing least squares.

When performing PCR, we generally recommend standardizing each predictor, using (6.6), prior to generating the principal components. This standardization ensures that all variables are on the same scale. In the absence of standardization, the high-variance variables will tend to play a larger role in the principal components obtained, and the scale on which the variables are measured will ultimately have an effect on the final PCR model. However, if the variables are all measured in the same units (say, kilograms, or inches), then one might choose not to standardize them.

**6.3.2 Partial Least Squares**

The PCR approach that we just described involves identifying linear combinations, or *directions*, that best represent the predictors $X_1,\ldots,X_p$. These directions are identified in an *unsupervised* way, since the response $Y$ is not used to help determine the principal component directions. That is, the response does not *supervise* the identification of the principal components. Consequently, PCR suffers from a drawback: there is no guarantee

[^8]: More details can be found in Section 3.5 of *The Elements of Statistical Learning* by Hastie, Tibshirani, and Friedman.

### PDF page 269 (book page 261)

**FIGURE 6.21.** *For the advertising data, the first PLS direction (solid line) and first PCR direction (dotted line) are shown.* *[Figure: Scatterplot of Ad Spending (vertical axis, about 5–30) against Population (horizontal axis, about 20–60) for 100 regions, shown as purple points. The green solid PLS line and green dotted PCR line both slope upward; the PLS line is slightly flatter.]*

that the directions that best explain the predictors will also be the best directions to use for predicting the response. Unsupervised methods are discussed further in Chapter 12.

We now present *partial least squares* (PLS), a *supervised* alternative to PCR. *[margin: partial least squares]* Like PCR, PLS is a dimension reduction method, which first identifies a new set of features $Z_1,\ldots,Z_M$ that are linear combinations of the original features, and then fits a linear model via least squares using these $M$ new features. But unlike PCR, PLS identifies these new features in a supervised way—that is, it makes use of the response $Y$ in order to identify new features that not only approximate the old features well, but also that are *related to the response*. Roughly speaking, the PLS approach attempts to find directions that help explain both the response and the predictors.

We now describe how the first PLS direction is computed. After standardizing the $p$ predictors, PLS computes the first direction $Z_1$ by setting each $\phi_{j1}$ in (6.16) equal to the coefficient from the simple linear regression of $Y$ onto $X_j$. One can show that this coefficient is proportional to the correlation between $Y$ and $X_j$. Hence, in computing $Z_1=\sum_{j=1}^{p}\phi_{j1}X_j$, PLS places the highest weight on the variables that are most strongly related to the response.

Figure 6.21 displays an example of PLS on a synthetic dataset with Sales in each of 100 regions as the response, and two predictors; Population Size and Advertising Spending. The solid green line indicates the first PLS direction, while the dotted line shows the first principal component direction. PLS has chosen a direction that has less change in the `ad` dimension per unit change in the `pop` dimension, relative to PCA. This suggests that `pop` is more highly correlated with the response than is `ad`. The PLS direction does not fit the predictors as closely as does PCA, but it does a better job explaining the response.

To identify the second PLS direction we first *adjust* each of the variables for $Z_1$, by regressing each variable on $Z_1$ and taking *residuals*. These residuals can be interpreted as the remaining information that has not been explained by the first PLS direction. We then compute $Z_2$ using this *or-*

### PDF page 270 (book page 262)

*thogonalized* data in exactly the same fashion as $Z_1$ was computed based on the original data. This iterative approach can be repeated $M$ times to identify multiple PLS components $Z_1,\ldots,Z_M$. Finally, at the end of this procedure, we use least squares to fit a linear model to predict $Y$ using $Z_1,\ldots,Z_M$ in exactly the same fashion as for PCR.

As with PCR, the number $M$ of partial least squares directions used in PLS is a tuning parameter that is typically chosen by cross-validation. We generally standardize the predictors and response before performing PLS.

PLS is popular in the field of chemometrics, where many variables arise from digitized spectrometry signals. In practice it often performs no better than ridge regression or PCR. While the supervised dimension reduction of PLS can reduce bias, it also has the potential to increase variance, so that the overall benefit of PLS relative to PCR is a wash.

**6.4 Considerations in High Dimensions**

**6.4.1 High-Dimensional Data**

Most traditional statistical techniques for regression and classification are intended for the *low-dimensional* setting in which $n$, the number of observations, is much greater than $p$, the number of features. *[margin: low-dimensional]* This is due in part to the fact that throughout most of the field's history, the bulk of scientific problems requiring the use of statistics have been low-dimensional. For instance, consider the task of developing a model to predict a patient's blood pressure on the basis of his or her age, sex, and body mass index (BMI). There are three predictors, or four if an intercept is included in the model, and perhaps several thousand patients for whom blood pressure and age, sex, and BMI are available. Hence $n\gg p$, and so the problem is low-dimensional. (By dimension here we are referring to the size of $p$.)

In the past 20 years, new technologies have changed the way that data are collected in fields as diverse as finance, marketing, and medicine. It is now commonplace to collect an almost unlimited number of feature measurements ($p$ very large). While $p$ can be extremely large, the number of observations $n$ is often limited due to cost, sample availability, or other considerations. Two examples are as follows:

1. Rather than predicting blood pressure on the basis of just age, sex, and BMI, one might also collect measurements for half a million *single nucleotide polymorphisms* (SNPs; these are individual DNA mutations that are relatively common in the population) for inclusion in the predictive model. Then $n\approx 200$ and $p\approx 500{,}000$.

2. A marketing analyst interested in understanding people's online shopping patterns could treat as features all of the search terms entered by users of a search engine. This is sometimes known as the “bag-of-words” model. The same researcher might have access to the search histories of only a few hundred or a few thousand search engine users who have consented to share their information with the researcher. For a given user, each of the $p$ search terms is scored present (0) or

### PDF page 271 (book page 263)

absent (1), creating a large binary feature vector. Then $n\approx 1{,}000$ and $p$ is much larger.

Data sets containing more features than observations are often referred to as *high-dimensional*. *[margin: high-dimensional]* Classical approaches such as least squares linear regression are not appropriate in this setting. Many of the issues that arise in the analysis of high-dimensional data were discussed earlier in this book, since they apply also when $n>p$: these include the role of the bias-variance trade-off and the danger of overfitting. Though these issues are always relevant, they can become particularly important when the number of features is very large relative to the number of observations.

We have defined the *high-dimensional setting* as the case where the number of features $p$ is larger than the number of observations $n$. But the considerations that we will now discuss certainly also apply if $p$ is slightly smaller than $n$, and are best always kept in mind when performing supervised learning.

**6.4.2 What Goes Wrong in High Dimensions?**

In order to illustrate the need for extra care and specialized techniques for regression and classification when $p>n$, we begin by examining what can go wrong if we apply a statistical technique not intended for the high-dimensional setting. For this purpose, we examine least squares regression. But the same concepts apply to logistic regression, linear discriminant analysis, and other classical statistical approaches.

When the number of features $p$ is as large as, or larger than, the number of observations $n$, least squares as described in Chapter 3 cannot (or rather, *should not*) be performed. The reason is simple: regardless of whether or not there truly is a relationship between the features and the response, least squares will yield a set of coefficient estimates that result in a perfect fit to the data, such that the residuals are zero.

An example is shown in Figure 6.22 with $p=1$ feature (plus an intercept) in two cases: when there are 20 observations, and when there are only two observations. When there are 20 observations, $n>p$ and the least squares regression line does not perfectly fit the data; instead, the regression line seeks to approximate the 20 observations as well as possible. On the other hand, when there are only two observations, then regardless of the values of those observations, the regression line will fit the data exactly.

This is problematic because this perfect fit will almost certainly lead to overfitting of the data. In other words, though it is possible to perfectly fit the training data in the high-dimensional setting, the resulting linear model will perform extremely poorly on an independent test set, and therefore does not constitute a useful model. In fact, we can see that this happened in Figure 6.22: the least squares line obtained in the right-hand panel will perform very poorly on a test set comprised of the observations in the left-hand panel. The problem is simple: when $p>n$ or $p\approx n$, a simple least squares regression line is too *flexible* and hence overfits the data.

Figure 6.23 further illustrates the risk of carelessly applying least squares when the number of features $p$ is large. Data were simulated with $n=20$ observations, and regression was performed with between 1 and 20 features,

### PDF page 272 (book page 264)

**FIGURE 6.22.** *Left: Least squares regression in the low-dimensional setting. Right: Least squares regression with $n=2$ observations and two parameters to be estimated (an intercept and a coefficient).* *[Figure: Two scatterplots of $Y$ against $X$, both with the same fitted black line. The left panel has 20 red observations scattered around the line; the right panel has two red observations lying exactly on it.]*

**FIGURE 6.23.** *On a simulated example with $n=20$ training observations, features that are completely unrelated to the outcome are added to the model. Left: The $R^2$ increases to 1 as more features are included. Center: The training set MSE decreases to 0 as more features are included. Right: The test set MSE increases as more features are included.* *[Figure: Three line plots against Number of Variables, from 1 to about 19. The left panel's $R^2$ climbs from near 0 to 1. The center panel's Training MSE falls from near 1 to 0. The right panel's Test MSE, on a logarithmic vertical scale, rises from about 1 to more than 500.]*

each of which was completely unrelated to the response. As shown in the figure, the model $R^2$ increases to 1 as the number of features included in the model increases, and correspondingly the training set MSE decreases to 0 as the number of features increases, *even though the features are completely unrelated to the response*. On the other hand, the MSE on an independent test set becomes extremely large as the number of features included in the model increases, because including the additional predictors leads to a vast increase in the variance of the coefficient estimates. Looking at the test set MSE, it is clear that the best model contains at most a few variables. However, someone who carelessly examines only the $R^2$ or the training set MSE might erroneously conclude that the model with the greatest number of variables is best. This indicates the importance of applying extra care when analyzing data sets with a large number of variables, and of always evaluating model performance on an independent test set.

### PDF page 273 (book page 265)

**FIGURE 6.24.** *The lasso was performed with $n=100$ observations and three values of $p$, the number of features. Of the $p$ features, 20 were associated with the response. The boxplots show the test MSEs that result using three different values of the tuning parameter $\lambda$ in (6.7). For ease of interpretation, rather than reporting $\lambda$, the degrees of freedom are reported; for the lasso this turns out to be simply the number of estimated non-zero coefficients. When $p=20$, the lowest test MSE was obtained with the smallest amount of regularization. When $p=50$, the lowest test MSE was achieved when there is a substantial amount of regularization. When $p=2{,}000$ the lasso performed poorly regardless of the amount of regularization, due to the fact that only 20 of the 2,000 features truly are associated with the outcome.* *[Figure: Three panels of cyan boxplots of test MSE, on a 0–5 scale, against degrees of freedom. For $p=20$, the boxplots at 1, 16, and 21 degrees of freedom fall as freedom increases. For $p=50$, the center boxplot at 28 has the lowest error. For $p=2{,}000$, all three boxplots at 1, 70, and 111 have similarly high errors.]*

In Section 6.1.3, we saw a number of approaches for adjusting the training set RSS or $R^2$ in order to account for the number of variables used to fit a least squares model. Unfortunately, the $C_p$, AIC, and BIC approaches are not appropriate in the high-dimensional setting, because estimating $\hat{\sigma}^2$ is problematic. (For instance, the formula for $\hat{\sigma}^2$ from Chapter 3 yields an estimate $\hat{\sigma}^2=0$ in this setting.) Similarly, problems arise in the application of adjusted $R^2$ in the high-dimensional setting, since one can easily obtain a model with an adjusted $R^2$ value of 1. Clearly, alternative approaches that are better-suited to the high-dimensional setting are required.

**6.4.3 Regression in High Dimensions**

It turns out that many of the methods seen in this chapter for fitting *less flexible* least squares models, such as forward stepwise selection, ridge regression, the lasso, and principal components regression, are particularly useful for performing regression in the high-dimensional setting. Essentially, these approaches avoid overfitting by using a less flexible fitting approach than least squares.

Figure 6.24 illustrates the performance of the lasso in a simple simulated example. There are $p=20$, 50, or 2,000 features, of which 20 are truly associated with the outcome. The lasso was performed on $n=100$ training observations, and the mean squared error was evaluated on an independent test set. As the number of features increases, the test set error increases. When $p=20$, the lowest validation set error was achieved when $\lambda$ in
