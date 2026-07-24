### PDF page 172 (book page 163)

Inspection of (4.32), (4.33), and (4.34) yields the following observations about LDA, QDA, and naive Bayes:

- LDA is a special case of QDA with $c_{kjl}=0$ for all $j=1,\ldots,p$, $l=1,\ldots,p$, and $k=1,\ldots,K$. (Of course, this is not surprising, since LDA is simply a restricted version of QDA with $\boldsymbol{\Sigma}_1=\cdots=\boldsymbol{\Sigma}_K=\boldsymbol{\Sigma}$.)

- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j)=b_{kj}x_j$. In particular, this means that LDA is a special case of naive Bayes! This is not at all obvious from the descriptions of LDA and naive Bayes earlier in this chapter, since each method makes very different assumptions: LDA assumes that the features are normally distributed with a common within-class covariance matrix, and naive Bayes instead assumes independence of the features.

- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj},\sigma_j^2)$, then we end up with $g_{kj}(x_j)=b_{kj}x_j$ where $b_{kj}=(\mu_{kj}-\mu_{Kj})/\sigma_j^2$. In this case, naive Bayes is actually a special case of LDA with $\boldsymbol{\Sigma}$ restricted to be a diagonal matrix with $j$th diagonal element equal to $\sigma_j^2$.

- Neither QDA nor naive Bayes is a special case of the other. Naive Bayes can produce a more flexible fit, since any choice can be made for $g_{kj}(x_j)$. However, it is restricted to a purely *additive* fit, in the sense that in (4.34), a function of $x_j$ is added to a function of $x_l$, for $j\neq l$; however, these terms are never multiplied. By contrast, QDA includes multiplicative terms of the form $c_{kjl}x_jx_l$. Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important in discriminating between classes.

None of these methods uniformly dominates the others: in any setting, the choice of method will depend on the true distribution of the predictors in each of the $K$ classes, as well as other considerations, such as the values of $n$ and $p$. The latter ties into the bias-variance trade-off.

How does logistic regression tie into this story? Recall from (4.12) that multinomial logistic regression takes the form

$$
\log\left(\frac{\Pr(Y=k\mid X=x)}{\Pr(Y=K\mid X=x)}\right)
=\beta_{k0}+\sum_{j=1}^{p}\beta_{kj}x_j.
$$

This is identical to the linear form of LDA (4.32): in both cases, $\log\left(\frac{\Pr(Y=k\mid X=x)}{\Pr(Y=K\mid X=x)}\right)$ is a linear function of the predictors. In LDA, the coefficients in this linear function are functions of estimates for $\pi_k$, $\pi_K$, $\mu_k$, $\mu_K$, and $\boldsymbol{\Sigma}$ obtained by assuming that $X_1,\ldots,X_p$ follow a normal distribution within each class. By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.
