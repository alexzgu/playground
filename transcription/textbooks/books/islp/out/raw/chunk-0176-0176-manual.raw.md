### PDF page 176 (book page 167)

| | Coefficient | Std. error | $t$-statistic | $p$-value |
|---|---:|---:|---:|---:|
| `Intercept` | 73.60 | 5.13 | 14.34 | 0.00 |
| `workingday` | 1.27 | 1.78 | 0.71 | 0.48 |
| `temp` | 157.21 | 10.26 | 15.32 | 0.00 |
| `weathersit[cloudy/misty]` | −12.89 | 1.96 | −6.56 | 0.00 |
| `weathersit[light rain/snow]` | −66.49 | 2.97 | −22.43 | 0.00 |
| `weathersit[heavy rain/snow]` | −109.75 | 76.67 | −1.43 | 0.15 |

**TABLE 4.10.** *Results for a least squares linear model fit to predict* `bikers` *in the* `Bikeshare` *data. The predictors* `mnth` *and* `hr` *are omitted from this table due to space constraints, and can be seen in Figure 4.13. For the qualitative variable* `weathersit`*, the baseline level corresponds to clear skies.*

create a more flexible version of logistic regression by including $X^2$, $X^3$, and even $X^4$ as predictors. This may or may not improve logistic regression's performance, depending on whether the increase in variance due to the added flexibility is offset by a sufficiently large reduction in bias. We could do the same for LDA. If we added all possible quadratic terms and cross-products to LDA, the form of the model would be the same as the QDA model, although the parameter estimates would be different. This device allows us to move somewhere between an LDA and a QDA model.

**4.6 Generalized Linear Models**

In Chapter 3, we assumed that the response $Y$ is quantitative, and explored the use of least squares linear regression to predict $Y$. Thus far in this chapter, we have instead assumed that $Y$ is qualitative. However, we may sometimes be faced with situations in which $Y$ is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable.

As a concrete example, we consider the `Bikeshare` data set. The response is `bikers`, the number of hourly users of a bike sharing program in Washington, DC. This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or *counts*. We will consider predicting `bikers` using the covariates `mnth` (month of the year), `hr` (hour of the day, from 0 to 23), `workingday` (an indicator variable that equals 1 if it is neither a weekend nor a holiday), `temp` (the normalized temperature, in Celsius), and `weathersit` (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.) *[margin: counts]*

In the analyses that follow, we will treat `mnth`, `hr`, and `weathersit` as qualitative variables.

**4.6.1 Linear Regression on the `Bikeshare` Data**

To begin, we consider predicting `bikers` using linear regression. The results are shown in Table 4.10.

We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour. Figure 4.13 displays the coefficients associated with `mnth`
