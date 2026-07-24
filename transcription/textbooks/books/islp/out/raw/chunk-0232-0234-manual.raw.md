### PDF page 232 (book page 224)

```text
Out[25]: intercept                            2.067840
         poly(horsepower, 2, raw=True)[0]     0.033019
         poly(horsepower, 2, raw=True)[1]     0.000120
         dtype: float64
```

We compare the results to the standard errors computed using `sm.OLS()`.

```python
In [26]: M = sm.OLS(Auto['mpg'],
                    quad_model.fit_transform(Auto))
         summarize(M.fit())['std err']
```

```text
Out[26]: intercept                            1.800
         poly(horsepower, 2, raw=True)[0]     0.031
         poly(horsepower, 2, raw=True)[1]     0.000
         Name: std err, dtype: float64
```

**5.4  Exercises**

*Conceptual*

1. Using basic statistical properties of the variance, as well as single-variable calculus, derive (5.6). In other words, prove that $\alpha$ given by (5.6) does indeed minimize $\operatorname{Var}(\alpha X+(1-\alpha)Y)$.

2. We will now derive the probability that a given observation is part of a bootstrap sample. Suppose that we obtain a bootstrap sample from a set of $n$ observations.

   (a) What is the probability that the first bootstrap observation is *not* the $j$th observation from the original sample? Justify your answer.

   (b) What is the probability that the second bootstrap observation is *not* the $j$th observation from the original sample?

   (c) Argue that the probability that the $j$th observation is not in the bootstrap sample is $(1-1/n)^n$.

   (d) When $n=5$, what is the probability that the $j$th observation is in the bootstrap sample?

   (e) When $n=100$, what is the probability that the $j$th observation is in the bootstrap sample?

   (f) When $n=10{,}000$, what is the probability that the $j$th observation is in the bootstrap sample?

   (g) Create a plot that displays, for each integer value of $n$ from 1 to 100,000, the probability that the $j$th observation is in the bootstrap sample. Comment on what you observe.

   (h) We will now investigate numerically the probability that a bootstrap sample of size $n=100$ contains the $j$th observation. Here $j=4$. We first create an array `store` with values that will subsequently be overwritten using the function `np.empty()`. We then

### PDF page 233 (book page 225)

repeatedly create bootstrap samples, and each time we record whether or not the fifth observation is contained in the bootstrap sample.

```python
rng = np.random.default_rng(10)
store = np.empty(10000)
for i in range(10000):
    store[i] = np.sum(rng.choice(100, replace=True) == 4) \
               > 0
np.mean(store)
```

Comment on the results obtained.

3. We now review $k$-fold cross-validation.

   (a) Explain how $k$-fold cross-validation is implemented.

   (b) What are the advantages and disadvantages of $k$-fold cross-validation relative to:

      i. The validation set approach?

      ii. LOOCV?

4. Suppose that we use some statistical learning method to make a prediction for the response $Y$ for a particular value of the predictor $X$. Carefully describe how we might estimate the standard deviation of our prediction.

*Applied*

5. In Chapter 4, we used logistic regression to predict the probability of `default` using `income` and `balance` on the `Default` data set. We will now estimate the test error of this logistic regression model using the validation set approach. Do not forget to set a random seed before beginning your analysis.

   (a) Fit a logistic regression model that uses `income` and `balance` to predict `default`.

   (b) Using the validation set approach, estimate the test error of this model. In order to do this, you must perform the following steps:

      i. Split the sample set into a training set and a validation set.

      ii. Fit a multiple logistic regression model using only the training observations.

      iii. Obtain a prediction of default status for each individual in the validation set by computing the posterior probability of default for that individual, and classifying the individual to the `default` category if the posterior probability is greater than 0.5.

      iv. Compute the validation set error, which is the fraction of the observations in the validation set that are misclassified.

   (c) Repeat the process in (b) three times, using three different splits of the observations into a training set and a validation set. Comment on the results obtained.

### PDF page 234 (book page 226)

   (d) Now consider a logistic regression model that predicts the probability of `default` using `income`, `balance`, and a dummy variable for `student`. Estimate the test error for this model using the validation set approach. Comment on whether or not including a dummy variable for `student` leads to a reduction in the test error rate.

6. We continue to consider the use of a logistic regression model to predict the probability of `default` using `income` and `balance` on the `Default` data set. In particular, we will now compute estimates for the standard errors of the `income` and `balance` logistic regression coefficients in two different ways: (1) using the bootstrap, and (2) using the standard formula for computing the standard errors in the `sm.GLM()` function. Do not forget to set a random seed before beginning your analysis.

   (a) Using the `summarize()` and `sm.GLM()` functions, determine the estimated standard errors for the coefficients associated with `income` and `balance` in a multiple logistic regression model that uses both predictors.

   (b) Write a function, `boot_fn()`, that takes as input the `Default` data set as well as an index of the observations, and that outputs the coefficient estimates for `income` and `balance` in the multiple logistic regression model.

   (c) Following the bootstrap example in the lab, use your `boot_fn()` function to estimate the standard errors of the logistic regression coefficients for `income` and `balance`.

   (d) Comment on the estimated standard errors obtained using the `sm.GLM()` function and using the bootstrap.

7. In Sections 5.1.2 and 5.1.3, we saw that the `cross_validate()` function can be used in order to compute the LOOCV test error estimate. Alternatively, one could compute those quantities using just `sm.GLM()` and the `predict()` method of the fitted model within a for loop. You will now take this approach in order to compute the LOOCV error for a simple logistic regression model on the `Weekly` data set. Recall that in the context of classification problems, the LOOCV error is given in (5.4).

   (a) Fit a logistic regression model that predicts `Direction` using `Lag1` and `Lag2`.

   (b) Fit a logistic regression model that predicts `Direction` using `Lag1` and `Lag2` *using all but the first observation*.

   (c) Use the model from (b) to predict the direction of the first observation. You can do this by predicting that the first observation will go up if $\Pr(\texttt{Direction}=\texttt{"Up"}\mid\texttt{Lag1},\texttt{Lag2})>0.5$. Was this observation correctly classified?

   (d) Write a for loop from $i=1$ to $i=n$, where $n$ is the number of observations in the data set, that performs each of the following steps:
