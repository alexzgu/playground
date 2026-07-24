### PDF page 256 (book page 248)

**FIGURE 6.8.** *Left: Plots of squared bias (black), variance (green), and test MSE (purple) for the lasso on a simulated data set. Right: Comparison of squared bias, variance, and test MSE between lasso (solid) and ridge (dotted). Both are plotted against their $R^2$ on the training data, as a common form of indexing. The crosses in both plots indicate the lasso model for which the MSE is smallest.* *[Figure: The left panel plots mean squared error against $\lambda$ (log scale, about 0.02 to 50.00): squared bias rises, variance falls, and test MSE falls and then rises, with a cross at its minimum. The right panel plots the same three quantities against training $R^2$ from 0 to 1, comparing solid lasso curves with dotted ridge curves; the lasso minimum is marked by a cross.]*

panel of Figure 6.8, the dotted lines represent the ridge regression fits. Here we plot both against their $R^2$ on the training data. This is another useful way to index models, and can be used to compare models with different types of regularization, as is the case here. In this example, the lasso and ridge regression result in almost identical biases. However, the variance of ridge regression is slightly lower than the variance of the lasso. Consequently, the minimum MSE of ridge regression is slightly smaller than that of the lasso.

However, the data in Figure 6.8 were generated in such a way that all 45 predictors were related to the response—that is, none of the true coefficients $\beta_1,\ldots,\beta_{45}$ equaled zero. The lasso implicitly assumes that a number of the coefficients truly equal zero. Consequently, it is not surprising that ridge regression outperforms the lasso in terms of prediction error in this setting. Figure 6.9 illustrates a similar situation, except that now the response is a function of only 2 out of 45 predictors. Now the lasso tends to outperform ridge regression in terms of bias, variance, and MSE.

These two examples illustrate that neither ridge regression nor the lasso will universally dominate the other. In general, one might expect the lasso to perform better in a setting where a relatively small number of predictors have substantial coefficients, and the remaining predictors have coefficients that are very small or that equal zero. Ridge regression will perform better when the response is a function of many predictors, all with coefficients of roughly equal size. However, the number of predictors that is related to the response is never known *a priori* for real data sets. A technique such as cross-validation can be used in order to determine which approach is better on a particular data set.

As with ridge regression, when the least squares estimates have excessively high variance, the lasso solution can yield a reduction in variance at the expense of a small increase in bias, and consequently can generate more accurate predictions. Unlike ridge regression, the lasso performs variable selection, and hence results in models that are easier to interpret.

### PDF page 257 (book page 249)

**FIGURE 6.9.** *Left: Plots of squared bias (black), variance (green), and test MSE (purple) for the lasso. The simulated data is similar to that in Figure 6.8, except that now only two predictors are related to the response. Right: Comparison of squared bias, variance, and test MSE between lasso (solid) and ridge (dotted). Both are plotted against their $R^2$ on the training data, as a common form of indexing. The crosses in both plots indicate the lasso model for which the MSE is smallest.* *[Figure: The left panel plots mean squared error against $\lambda$ (log scale, about 0.02 to 50.00): variance falls, squared bias remains near zero before rising sharply, and test MSE falls and then rises, with a cross at its minimum. The right panel compares the three lasso and ridge curves against training $R^2$ from about 0.4 to 1.0; the lasso minimum is marked by a cross.]*

There are very efficient algorithms for fitting both ridge and lasso models; in both cases the entire coefficient paths can be computed with about the same amount of work as a single least squares fit. We will explore this further in the lab at the end of this chapter.

**A Simple Special Case for Ridge Regression and the Lasso**

In order to obtain a better intuition about the behavior of ridge regression and the lasso, consider a simple special case with $n=p$, and $\mathbf{X}$ a diagonal matrix with 1's on the diagonal and 0's in all off-diagonal elements. To simplify the problem further, assume also that we are performing regression without an intercept. With these assumptions, the usual least squares problem simplifies to finding $\beta_1,\ldots,\beta_p$ that minimize

$$
\sum_{j=1}^{p}(y_j-\beta_j)^2. \tag{6.11}
$$

In this case, the least squares solution is given by

$$
\hat{\beta}_j=y_j.
$$

And in this setting, ridge regression amounts to finding $\beta_1,\ldots,\beta_p$ such that

$$
\sum_{j=1}^{p}(y_j-\beta_j)^2+\lambda\sum_{j=1}^{p}\beta_j^2 \tag{6.12}
$$

is minimized, and the lasso amounts to finding the coefficients such that

$$
\sum_{j=1}^{p}(y_j-\beta_j)^2+\lambda\sum_{j=1}^{p}|\beta_j| \tag{6.13}
$$

### PDF page 258 (book page 250)

**FIGURE 6.10.** *The ridge regression and lasso coefficient estimates for a simple setting with $n=p$ and $\mathbf{X}$ a diagonal matrix with 1's on the diagonal. Left: The ridge regression coefficient estimates are shrunken proportionally towards zero, relative to the least squares estimates. Right: The lasso coefficient estimates are soft-thresholded towards zero.* *[Figure: Two coefficient-estimate plots against $y_j$, each with a dashed 45-degree least-squares line. The solid red ridge line in the left panel has a shallower positive slope. The solid red lasso line in the right panel is flat at zero between approximately $y_j=-0.5$ and $0.5$, then rises with unit slope outside that interval.]*

is minimized. One can show that in this setting, the ridge regression estimates take the form

$$
\hat{\beta}_j^R=\frac{y_j}{1+\lambda}, \tag{6.14}
$$

and the lasso estimates take the form

$$
\hat{\beta}_j^L=
\begin{cases}
y_j-\lambda/2 & \text{if } y_j>\lambda/2;\\
y_j+\lambda/2 & \text{if } y_j<-\lambda/2;\\
0 & \text{if } |y_j|\leq\lambda/2.
\end{cases} \tag{6.15}
$$

Figure 6.10 displays the situation. We can see that ridge regression and the lasso perform two very different types of shrinkage. In ridge regression, each least squares coefficient estimate is shrunken by the same proportion. In contrast, the lasso shrinks each least squares coefficient towards zero by a constant amount, $\lambda/2$; the least squares coefficients that are less than $\lambda/2$ in absolute value are shrunken entirely to zero. The type of shrinkage performed by the lasso in this simple setting (6.15) is known as *soft-thresholding*. *[margin: soft-thresholding]* The fact that some lasso coefficients are shrunken entirely to zero explains why the lasso performs feature selection.

In the case of a more general data matrix $\mathbf{X}$, the story is a little more complicated than what is depicted in Figure 6.10, but the main ideas still hold approximately: ridge regression more or less shrinks every dimension of the data by the same proportion, whereas the lasso more or less shrinks all coefficients toward zero by a similar amount, and sufficiently small coefficients are shrunken all the way to zero.

**Bayesian Interpretation of Ridge Regression and the Lasso**

We now show that one can view ridge regression and the lasso through a Bayesian lens. A Bayesian viewpoint for regression assumes that the coefficient vector $\beta$ has some prior distribution, say $p(\beta)$, where $\beta=(\beta_0,\beta_1,\ldots,\beta_p)^T$. The likelihood of the data can be written as $f(Y\mid X,\beta)$,
