# Chapter 5 — The Many Variables & The Spurious Waffles
*(PDF pages 143–180; book pages 127–164)*

### PDF page 143 (book page 127)

# Chapter 5 — The Many Variables & The Spurious Waffles

One of the most reliable sources of waffles in North America, if not the entire world, is a Waffle House diner. Waffle House is nearly always open, even just after a hurricane. Most diners invest in disaster preparedness, including having their own electrical generators. As a consequence, the United States' disaster relief agency (FEMA) informally uses Waffle House as an index of disaster severity.<sup>77</sup> If the Waffle House is closed, that's a serious event.

It is ironic then that steadfast Waffle House is associated with the nation's highest divorce rates (Figure 5.1). States with many Waffle Houses per person, like Georgia and Alabama, also have some of the highest divorce rates in the United States. The lowest divorce rates are found where there are zero Waffle Houses. Could always-available waffles and hash brown potatoes put marriage at risk?

Probably not. This is an example of a misleading correlation. No one thinks there is any plausible mechanism by which Waffle House diners make divorce more likely. Instead, when we see a correlation of this kind, we immediately start asking about other variables that are really driving the relationship between waffles and divorce. In this case, Waffle House began in Georgia in the year 1955. Over time, the diners spread across the Southern United States, remaining largely within it. So Waffle House is associated with the South. Divorce is not a uniquely Southern institution, but the Southern United States has some of the highest divorce rates in the nation. So it's probably just an accident of history that Waffle House and high divorce rates both occur in the South.

Such accidents are commonplace. It is not surprising that Waffle House is correlated with divorce, because correlation in general is not surprising. In large data sets, every pair of variables has a statistically discernible non-zero correlation.<sup>78</sup> But since most correlations do not indicate causal relationships, we need tools for distinguishing mere association from evidence of causation. This is why so much effort is devoted to **multiple regression**, using more than one predictor variable to simultaneously model an outcome. Reasons given for multiple regression models include:

1. Statistical "control" for confounds. A *confound* is something that misleads us about a causal influence—there will be a more precise definition in the next chapter. The spurious waffles and divorce correlation is one possible type of confound, where the confound (southernness) makes a variable with no real importance (Waffle House density) appear to be important. But confounds are diverse. They can hide real important variables just as easily as they can produce false ones.

2. Multiple causation. A phenomenon may arise from multiple causes. Measurement of each cause is useful, so when we can use the same data to estimate more than one

### PDF page 144 (book page 128)

**FIGURE 5.1.** The number of Waffle House diners per million people is associated with divorce rate (in the year 2009) within the United States. Each point is a State. “Southern” (former Confederate) States shown in blue. Shaded region is 89% percentile interval of the mean. These data are in `data(WaffleDivorce)` in the `rethinking` package. *[Figure: scatter plot of divorce rate against Waffle Houses per million, with a rising fitted line and gray 89% interval. Southern States are blue; labeled points include ME, OK, NJ, AR, AL, GA, and SC.]*

type of influence, we should. Furthermore, when causation is multiple, one cause can hide another.

3. **Interactions.** The importance of one variable may depend upon another. For example, plants benefit from both light and water. But in the absence of either, the other is no benefit at all. Such **interactions** occur very often. Effective inference about one variable will often depend upon consideration of others.

In this chapter, we begin to deal with the first of these two, using multiple regression to deal with simple confounds and to take multiple measurements of association. You’ll see how to include any arbitrary number of *main effects* in your linear model of the Gaussian mean. These main effects are additive combinations of variables, the simplest type of multiple variable model. We’ll focus on two valuable things these models can help us with: (1) revealing *spurious* correlations like the Waffle House correlation with divorce and (2) revealing important correlations that may be *masked* by unrevealed correlations with other variables. Along the way, you’ll meet **categorical variables**, which require special handling compared to continuous variables.

However, multiple regression can be worse than useless, if we don’t know how to use it. Just adding variables to a model can do a lot of damage. So in this chapter, we’ll begin to think formally about **causal inference** and introduce graphical causal models as a way to design and interpret regression models. The next chapter continues on this theme, describing some serious and common dangers of adding predictor variables, ending with a unifying framework for understanding the examples in both this chapter and the next.

---

**Rethinking: Causal inference.** Despite its central importance, there is no unified approach to causal inference yet in the sciences or in statistics. There are even people who argue that cause does not really exist; it’s just a psychological illusion.<sup>79</sup> And in complex dynamical systems, everything seems to cause everything else. “Cause” loses intuitive value. About one thing, however, there is general agreement: Causal inference always depends upon unverifiable assumptions. Another way to say this is that it’s always possible to imagine some way in which your inference about cause is mistaken, no matter how careful the design or analysis. A lot can be accomplished, despite this barrier.<sup>80</sup>

---

### PDF page 145 (book page 129)

**FIGURE 5.2.** Divorce rate is associated with both marriage rate (left) and median age at marriage (right). Both predictor variables are standardized in this example. The average marriage rate across States is 20 per 1000 adults, and the average median age at marriage is 26 years. *[Figure: two scatter plots of State divorce rates. At left, divorce rate rises with marriage rate; at right, divorce rate falls with median age at marriage. Each plot has a fitted line and gray uncertainty interval.]*

**5.1. Spurious association**

Let’s leave waffles behind, at least for the moment. An example that is easier to understand is the correlation between divorce rate and marriage rate (Figure 5.2). The rate at which adults marry is a great predictor of divorce rate, as seen in the left-hand plot in the figure. But does marriage *cause* divorce? In a trivial sense it obviously does: One cannot get a divorce without first getting married. But there’s no reason high marriage rate must be correlated with divorce. It’s easy to imagine high marriage rate indicating high cultural valuation of marriage and therefore being associated with *low* divorce rate. So something is suspicious here.

Another predictor associated with divorce is the median age at marriage, displayed in the right-hand plot in Figure 5.2. Age at marriage is also a good predictor of divorce rate—higher age at marriage predicts less divorce. Let’s load these data and standardize the variables of interest:

*[margin: R code 5.1]*

```r
# load data and copy
library(rethinking)
data(WaffleDivorce)
d <- WaffleDivorce

# standardize variables
d$A <- scale( d$MedianAgeMarriage )
d$D <- scale( d$Divorce )
```

### PDF page 146 (book page 130)

You can replicate the right-hand plot in the figure using a linear regression model:

$$
\begin{aligned}
D_i &\sim \operatorname{Normal}(\mu_i,\sigma) \\
\mu_i &= \alpha + \beta_A A_i \\
\alpha &\sim \operatorname{Normal}(0,0.2) \\
\beta_A &\sim \operatorname{Normal}(0,0.5) \\
\sigma &\sim \operatorname{Exponential}(1)
\end{aligned}
$$

$D_i$ is the standardized (zero centered, standard deviation one) divorce rate for State $i$, and $A_i$ is State $i$’s standardized median age at marriage. The linear model structure should be familiar from the previous chapter.

What about those priors? Since the outcome and the predictor are both standardized, the intercept $\alpha$ should end up very close to zero. What does the prior slope $\beta_A$ imply? If $\beta_A = 1$, that would imply that a change of one standard deviation in age at marriage is associated likewise with a change of one standard deviation in divorce. To know whether or not that is a strong relationship, you need to know how big a standard deviation of age at marriage is:

*[margin: R code 5.2]*

```r
sd( d$MedianAgeMarriage )
```

```text
[1] 1.24363
```

So when $\beta_A = 1$, a change of 1.2 years in median age at marriage is associated with a full standard deviation change in the outcome variable. That seems like an insanely strong relationship. The prior above thinks that only 5% of plausible slopes more extreme than 1. We’ll simulate from these priors in a moment, so you can see how they look in the outcome space.

To compute the approximate posterior, there are no new code tricks or techniques here. But I’ll add comments to help explain the mass of code to follow.

*[margin: R code 5.3]*

```r
m5.1 <- quap(
    alist(
        D ~ dnorm( mu , sigma ) ,
        mu <- a + bA * A ,
        a ~ dnorm( 0 , 0.2 ) ,
        bA ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data = d )
```

To simulate from the priors, we can use `extract.prior` and `link` as in the previous chapter. I’ll plot the lines over the range of 2 standard deviations for both the outcome and predictor. That’ll cover most of the possible range of both variables.

*[margin: R code 5.4]*

```r
set.seed(10)
prior <- extract.prior( m5.1 )
mu <- link( m5.1 , post=prior , data=list( A=c(-2,2) ) )
plot( NULL , xlim=c(-2,2) , ylim=c(-2,2) )
for ( i in 1:50 ) lines( c(-2,2) , mu[i,] , col=col.alpha("black",0.4) )
```

Figure 5.3 displays the result. You may wish to try some vaguer, flatter priors and see how quickly the prior regression lines become ridiculous.

### PDF page 147 (book page 131)

**FIGURE 5.3.** Plausible regression lines implied by the priors in `m5.1`. These are weakly informative priors in that they allow some implusibly strong relationships but generally bound the lines to possible ranges of the variables. *[Figure: a plot with x-axis "Median age marriage (std)" ranging −2 to 2 and y-axis "Divorce rate (std)" ranging −2 to 2, showing many straight regression lines of varying slopes — both positive and negative — fanning out and crossing near the origin, with most lines bounded within the plotting region.]*

Now for the posterior predictions. The procedure is exactly like the examples from the previous chapter: `link`, then summarize with `mean` and `PI`, and then plot.

*[margin: R code 5.5]*

```r
# compute percentile interval of mean
A_seq <- seq( from=-3 , to=3.2 , length.out=30 )
mu <- link( m5.1 , data=list(A=A_seq) )
mu.mean <- apply( mu , 2, mean )
mu.PI <- apply( mu , 2 , PI )

# plot it all
plot( D ~ A , data=d , col=rangi2 )
lines( A_seq , mu.mean , lwd=2 )
shade( mu.PI , A_seq )
```

If you inspect the `precis` output, you'll see that posterior for $\beta_A$ is reliably negative, as seen in Figure 5.2.

You can fit a similar regression for the relationship in the left-hand plot:

*[margin: R code 5.6]*

```r
d$M <- scale( d$Marriage )
m5.2 <- quap(
    alist(
        D ~ dnorm( mu , sigma ) ,
        mu <- a + bM * M ,
        a ~ dnorm( 0 , 0.2 ) ,
        bM ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data = d )
```

As you can see in the figure, this relationship isn't as strong as the previous one.

But merely comparing parameter means between different bivariate regressions is no way to decide which predictor is better. Both of these predictors could provide independent value, or they could be redundant, or one could eliminate the value of the other.

### PDF page 148 (book page 132)

To make sense of this, we're going to have to think causally. And then, only after we've done some thinking, a bigger regression model that includes both age at marriage and marriage rate will help us.

**5.1.1. Think before you regress.** There are three observed variables in play: divorce rate (D), marriage rate (M), and the median age at marriage (A) in each State. The pattern we see in the previous two models and illustrated in Figure 5.2 is symptomatic of a situation in which only one of the predictor variables, $A$ in this case, has a *causal* impact on the outcome, $D$, even though both predictor variables are strongly associated with the outcome.

To understand this better, it is helpful to introduce a particular type of causal graph known as a **DAG**, short for **directed acyclic graph**. *Graph* means it is nodes and connections. *Directed* means the connections have arrows that indicate directions of causal influence. And *acyclic* means that causes do not eventually flow back on themselves. A DAG is a way of describing qualitative causal relationships among variables. It isn't as detailed as a full model description, but it contains information that a purely statistical model does not. Unlike a statistical model, a DAG, if it is correct, will tell you the consequences of intervening to change a variable.

Here is a DAG for our divorce rate example:

*[Diagram: a directed acyclic graph with node $A$ at the upper left, node $M$ at the upper right, and node $D$ at the bottom center. Arrows: $A \to M$, $A \to D$, and $M \to D$.]*

If you want to see the code to draw this, see the Overthinking box at the end of this section. It may not look like much, but this type of diagram does a lot of work. It represents a heuristic causal model. Like other models, it is an analytical assumption. The symbols $A$, $M$, and $D$ are our observed variables. The arrows show directions of influence. What this DAG says is:

1. $A$ directly influences $D$
2. $M$ directly influences $D$
3. $A$ directly influences $M$

These statements can then have further implications. In this case, because $A \to M$ and $M \to D$, age of marriage influences divorce in two ways. First it can have a direct effect, perhaps because younger people change faster than older people and are therefore more likely to grow incompatible with a partner. Second, it can have an indirect effect by influencing the marriage rate. If people get married earlier, then the marriage rate may rise, because there are more young people. Consider for example if an evil dictator forced everyone to marry at age 65. Since a smaller fraction of the population lives to 65 than to 25, forcing delayed marriage will also reduce the marriage rate. If marriage rate itself has any direct effect on divorce, maybe by making marriage more or less normative, then some of that direct effect could be the indirect effect of age at marriage.

To infer the strength of these different arrows, we need more than one statistical model. Model `m5.1`, the regression of $D$ on $A$, tells us only that the *total* influence of age at marriage is strongly negative with divorce rate. The "total" here means we have to account for every path from $A$ to $D$. There are two such paths in this graph: $A \to D$, a direct path, and $A \to M \to D$, an indirect path. In general, it is possible that a variable like $A$ has no direct effect at all on an

### PDF page 149 (book page 133)

outcome like $D$. It could still be associated with $D$ entirely through the indirect path. That type of relationship is known as **mediation**, and we'll have another example later.

In this example however, the indirect path does almost no work. How can we show that? We know from `m5.2` that marriage rate is positively associated with divorce rate. But that isn't enough to tell us that the path $M \to D$ is positive. It could be that the association between $M$ and $D$ arises entirely from $A$'s influence on both $M$ and $D$. Like this:

*[Diagram: a directed acyclic graph with node $A$ at the upper left, node $M$ at the upper right, and node $D$ at the bottom center. Arrows: $A \to M$ and $A \to D$.]*

This DAG is also consistent with the posterior distributions of models `m5.1` and `m5.2`. So which is it? Is there a direct effect of marriage rate, or rather is age at marriage just driving both, creating a spurious correlation between marriage rate and divorce rate?

To find out, we need to slow down and consider carefully what each DAG implies. That's what we'll do next.

---

**Overthinking: Drawing a DAG.** There are several packages, whether for R or Python or another environment, that aid with drawing and analyzing directed acyclic graphs. The one I use for examples in this book is `dagitty`. It has the advantage of being both an R package and something you can use in your internet browser or on your computer desktop. Visit `http://www.dagitty.net/`. To draw the simple DAG you saw earlier in this section:

*[margin: R code 5.7]*

```r
library(dagitty)
dag5.1 <- dagitty( "dag {
    A -> D
    A -> M
    M -> D
}")
coordinates(dag5.1) <- list( x=c(A=0,D=1,M=2) , y=c(A=0,D=1,M=0) )
drawdag( dag5.1 )
```

The `->` arrows in the DAG definition indicate directions of influence. The `coordinates` function let's you layout the plot as you like. You can also let `dagitty` do the layout, using `plot(graphLayout(dag5.1))`. The `rethinking` package has a DAG plotting function that allows a bit more visual control. See `?drawdag`.

---

**5.1.2. Testable implications.** How do we use data to compare multiple, plausible causal models? The first thing to consider are the **testable implications** of each model. Consider the two DAGs we have so far considered:

*[Diagram: two directed acyclic graphs side by side. Left: nodes $A$ (upper left), $M$ (upper right), $D$ (bottom center), with arrows $A \to M$, $A \to D$, and $M \to D$. Right: the same three nodes with arrows $A \to M$ and $A \to D$ only.]*

### PDF page 150 (book page 134)

Any DAG may imply that some variables are independent of others under certain conditions. These are the model’s testable implications, it’s **conditional independencies**. Conditional independencies come in two forms. First, they are statements of which variables should be associated with one another (or not) in the data. Second, they are statements of which variables become dis-associated when we condition on some other set of variables. In more formal notation, the implication that some variable $Y$ is not associated with some variable $X$, after conditioning on some other variable $Z$ is written: $Y \perp\!\!\!\perp X \mid Z$. This is very weird notation and any feelings of annoyance on your part are justified. So let’s consider this in the context of the divorce example.

What are the conditional independencies of the DAGs at the top of the page? How do we derive these conditional independencies? Finding conditional independencies is not hard, but also not at all obvious. With a little practice, it becomes very easy. The more general rules can wait until the next chapter. For now, let’s consider each DAG in turn and inspect the possibilities.

For the DAG on the left above, the one with three arrows, first note that every pair of variables is correlated. This is because there is a causal arrow between every pair. These arrows create correlations. So before we condition on anything, everything is associated with everything else. This is already a testable implication. We could write it:

$$
D \not\!\perp\!\!\!\perp A,\; D \not\!\perp\!\!\!\perp M,\; A \not\!\perp\!\!\!\perp M
$$

That $\not\!\perp\!\!\!\perp$ thing means “not independent of.” If we now look in the data and find that any pair of variables are not associated, then something is wrong with the DAG (assuming the data are correct). In these data, all three pairs are in fact strongly associated. Check for yourself. You can use `cor()` to measure simple correlations. Correlations are very simple and sometimes terrible measures of association—mamy different patterns of association with different implications can produce the same correlation. But they do honest work in this case.

Are there any other testable implications for the first DAG above? No. It will be easier to see why, if we slide over to consider the second DAG, the one in which $M$ has no influence on $D$. In this DAG, it is still true that all three variable are associated with one another. $A$ is associated with $D$ and $M$ because it influences them both. And $D$ and $M$ are associated with one another, because $M$ influences them both. They share a cause, and this leads them to be correlated with one another through that cause. But suppose we condition on $A$. All of the information in $M$ that is relevant to predicting $D$ is in $A$. So once we’ve conditioned on $A$, $M$ tells us nothing more about $D$. So in the second DAG, a testable implication is that $D$ is independent of $M$, conditional on $A$. In other words, $D \perp\!\!\!\perp M \mid A$. The same thing does not happen with the first DAG. Conditioning on $A$ does not make $D$ independent of $M$, because $M$ really influences $D$ all by itself in this model.

If you are having trouble seeing these implications, the conditional independencies, the `dagitty` package can find them for you. Here’s the code to define the second DAG and display the implied conditional independencies.

*[margin: R code 5.8]*

```r
DMA_dag2 <- dagitty('dag{ D <- A -> M }')
impliedConditionalIndependencies( DMA_dag2 )
```

```text
D _||_ M | A
```

The first DAG has no conditional independencies. You can define it and check with this:

### PDF page 151 (book page 135)

*[margin: R code 5.9]*

```r
DMA_dag1 <- dagitty('dag{ D <- A -> M -> D }')
impliedConditionalIndependencies( DMA_dag1 )
```

There are no conditional independencies, so there is no output to display.

Let’s try to summarize. The testable implications of the first DAG are that all pairs of variables should be associated, whatever we condition on. The testable implications of the second DAG are that all pairs of variables should be associated, before conditioning on anything, but that $D$ and $M$ should be independent after conditioning on $A$. So the only implication that differs between these DAGs is the last one: $D \perp\!\!\!\perp M \mid A$.

To test this implication, we need a statistical model that conditions on $A$, so we can see whether that renders $D$ independent of $M$. And that is what multiple regression helps with. It can address a useful *descriptive* question:

> *Is there any additional value in knowing a variable, once I already know all of the other predictor variables?*

So for example once you fit a multiple regression to predict divorce using both marriage rate and age at marriage, the model addresses the questions:

1. After I already know marriage rate, what additional value is there in also knowing age at marriage?
2. After I already know age at marriage, what additional value is there in also knowing marriage rate?

The parameter estimates corresponding to each predictor are the (often opaque) answers to these questions. The questions above are descriptive, and the answers are also descriptive. It is only the derivation of the testable implications above that give these descriptive results a causal meaning.

---

**Rethinking: “Control” is out of control.** Very often, the question just above is spoken of as “statistical control,” as in *controlling for* the effect of one variable while estimating the effect of another. But this is sloppy language, as it implies too much. Statistical control is quite different from experimental control, as we’ll explore more in the next chapter. The point here isn’t to police language. Instead, the point is to observe the distinction between small world and large world interpretations. Since most people who use statistics are not statisticians, sloppy language like “control” can promote a sloppy culture of interpretation. Such cultures tend to overestimate the power of statistical methods, so resisting them can be difficult. Disciplining your own language may be enough. Disciplining another’s language is hard to do, without seeming like a fastidious scold, as this very box must seem.

---

**5.1.3. Multiple regression notation.** Multiple regression formulas look a lot like the polynomial models at the end of the previous chapter—they add more parameters and variables to the definition of $\mu_i$. The strategy is straightforward:

1. Nominate the predictor variables you want in the linear model of the mean.
2. For each predictor, make a parameter that will measure its association with the outcome.
3. Multiply the parameter by the variable and add that term to the linear model.

### PDF page 152 (book page 136)

Examples are always necessary, so here is the model that predicts divorce rate, using both marriage rate and age at marriage.

$$
\begin{aligned}
D_i &\sim \operatorname{Normal}(\mu_i,\sigma) && \text{[probability of data]} \\
\mu_i &= \alpha + \beta_M M_i + \beta_A A_i && \text{[linear model]} \\
\alpha &\sim \operatorname{Normal}(0,0.2) && \text{[prior for }\alpha\text{]} \\
\beta_M &\sim \operatorname{Normal}(0,0.5) && \text{[prior for }\beta_M\text{]} \\
\beta_A &\sim \operatorname{Normal}(0,0.5) && \text{[prior for }\beta_A\text{]} \\
\sigma &\sim \operatorname{Exponential}(1) && \text{[prior for }\sigma\text{]}
\end{aligned}
$$

You can use whatever symbols you like for the parameters and variables, but here I’ve chosen $R$ for marriage rate and $A$ for age at marriage, reusing these symbols as subscripts for the corresponding parameters. But feel free to use whichever symbols reduce the load on your own memory.

So what does it mean to assume $\mu_i = \alpha + \beta_M M_i + \beta_A A_i$? It means that the expected outcome for any State with marriage rate $M_i$ and median age at marriage $A_i$ is the sum of three independent terms. The first term is a constant, $\alpha$. Every State gets this. The second term is the product of the marriage rate, $M_i$, and the coefficient, $\beta_M$, that measures the association between marriage rate and divorce rate. The third term is similar, but for the association with median age at marriage instead.

If you are like most people, this is still pretty mysterious. So it might help to read the $+$ symbols as “or” and then say: *A State’s divorce rate can be a function of its marriage rate or its median age at marriage.* The “or” indicates independent associations, which may be purely statistical or rather causal.

---

**Overthinking: Compact notation and the design matrix.** Often, linear models are written using a compact form like:

$$
\mu_i = \alpha + \sum_{j=1}^{n} \beta_j x_{ji}
$$

where $j$ is an index over predictor variables and $n$ is the number of predictor variables. The same model may also be abbreviated:

$$
\mu_i = \alpha + \beta_1 x_{1i} + \beta_2 x_{2i} + \cdots + \beta_n x_{ni}
$$

Both of these forms may be read as *the mean is a modeled as the sum of an intercept and an additive combination of the products of parameters and predictors.* Even more compactly, using matrix notation:

$$
\mathbf{m} = \mathbf{Xb}
$$

where $\mathbf{m}$ is a vector of predicted means, one for each row in the data, $\mathbf{b}$ is a (column) vector of parameters, one for each predictor variable, and $\mathbf{X}$ is a matrix. This matrix is called a *design matrix*. It has as many rows as the data, and as many columns as there are predictors plus one. So $\mathbf{X}$ is basically a data frame, but with an extra first column. The extra column is filled with 1s. These 1s are multiplied by the first parameter, which is the intercept, and so return the unmodified intercept. When $\mathbf{X}$ is matrix-multiplied by $\mathbf{b}$, you get the predicted means. In R notation, this operation is `X %*% b`.

We’re not going to use the design matrix approach in this book. And in general you don’t need to. But it’s good to recognize it, and sometimes it can save you a lot of work. For example, for linear regressions, there is a nice matrix formula for the maximum likelihood (or *least squares*) estimates. Most statistical software exploits that formula, which requires using a design matrix.

---

### PDF page 153 (book page 137)

**5.1.4. Approximating the posterior.** To fit this model to the divorce data, we just expand the linear model. Here's the model definition again, with the code on the right-hand side:

|  |  |
|---|---|
| $D_i \sim \text{Normal}(\mu_i, \sigma)$ | `D ~ dnorm(mu,sigma)` |
| $\mu_i = \alpha + \beta_M M_i + \beta_A A_i$ | `mu <- a + bM*M + bA*A` |
| $\alpha \sim \text{Normal}(0, 0.2)$ | `a ~ dnorm(0,0.2)` |
| $\beta_M \sim \text{Normal}(0, 0.5)$ | `bM ~ dnorm(0,0.5)` |
| $\beta_A \sim \text{Normal}(0, 0.5)$ | `bA ~ dnorm(0,0.5)` |
| $\sigma \sim \text{Exponential}(1)$ | `sigma ~ dexp(1)` |

And here is the `quap` code to approximate the posterior distribution:

*[margin: R code 5.10]*

```r
m5.3 <- quap(
    alist(
        D ~ dnorm( mu , sigma ) ,
        mu <- a + bM*M + bA*A ,
        a ~ dnorm( 0 , 0.2 ) ,
        bM ~ dnorm( 0 , 0.5 ) ,
        bA ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data = d )
precis( m5.3 )
```

```
        mean   sd  5.5% 94.5%
a       0.00 0.10 -0.16  0.16
bM     -0.07 0.15 -0.31  0.18
bA     -0.61 0.15 -0.85 -0.37
sigma   0.79 0.08  0.66  0.91
```

The posterior mean for marriage rate, `bM`, is now close to zero, with plenty of probability of both sides of zero. The posterior mean for age at marriage, `bA`, is essentially unchanged. It will help to visualize the posterior distributions for all three models, focusing just on the slope parameters $\beta_A$ and $\beta_M$:

*[margin: R code 5.11]*

```r
plot( coeftab(m5.1,m5.2,m5.3), par=c("bA","bM") )
```

*[Figure: a coeftab dot-and-interval plot. The vertical axis is split into two groups. Under the label `bA`, rows `m5.3`, `m5.2`, `m5.1` (top to bottom): `m5.3` and `m5.1` each show a point near −0.6 with a horizontal interval line, while the `m5.2` row is empty. Under the label `bM`, rows `m5.3`, `m5.2`, `m5.1`: `m5.3` shows a point near 0 (slightly negative), `m5.2` a point near +0.35, and the `m5.1` row is empty. The horizontal axis is labeled "Estimate" with ticks at −0.5, 0.0, 0.5, and a vertical dashed reference line at 0.]*

posterior means shown by the points and the 89% compatibility intervals by the solid horizontal lines. Notice how `bA` doesn't move, only grows a bit more uncertain, while `bM` is only

### PDF page 154 (book page 138)

associated with divorce when age at marriage is missing from the model. You can interpret these distributions as saying:

> *Once we know median age at marriage for a State, there is little or no additional predictive power in also knowing the rate of marriage in that State.*

In that weird notation, $D \perp\!\!\!\perp M \mid A$. This tests the implication of the second DAG from earlier. Since the first DAG did not imply this result, it is out.

Note that this does not mean that there is no value in knowing marriage rate. Consistent with the earlier DAG, if you didn't have access to age-at-marriage data, then you'd definitely find value in knowing the marriage rate. This implies there is no, or almost no, direct causal path from marriage rate to divorce rate. The association between marriage rate and divorce rate is spurious, caused by the influence of age of marriage on both marriage rate and divorce rate. I'll leave it to the reader to investigate the relationship between age at marriage, A, and marriage rate, M, to complete the picture.

But how did model `m5.3` achieve the inference that marriage rate adds no additional information, once we know age at marriage? Let's draw some pictures.

---

**Overthinking: Simulating the divorce example.** The divorce data are real data. See the sources in `?WaffleDivorce`. But it is useful to simulate the kind of causal relationships shown in the previous DAG: $M \leftarrow A \rightarrow D$. Every DAG implies a simulation, and such simulations can help us design models to correctly infer relationships among variables. In this case, you just need to simulate each of the three variables:

*[margin: R code 5.12]*

```r
N <- 50 # number of simulated States
age <- rnorm( N )         # sim A
mar <- rnorm( N , -age )  # sim A -> M
div <- rnorm( N , age )   # sim A -> D
```

Now if you use these variables in models `m5.1`, `m5.2`, and `m5.3`, you'll see the same pattern of posterior inferences. It is also possible to simulate that both $A$ and $M$ influence $D$: `div <- rnorm(N, age + mar )`. In that case, a naive regression of $D$ on $A$ will overestimate the the influence of $A$, just like a naive regression of $D$ on $M$ will overestimate the importance of $M$. The multiple regression will help sort things out for you in this situation as well. But interpreting the parameter estimates will always depend upon what you believe about the causal model, because typically several (or very many) causal models are consistent with any one set of parameter estimates. We'll discuss this later under the name of Markov equivalence.

---

**5.1.5. Plotting multivariate posteriors.** Let's pause for a moment, before moving on. There are a lot of moving parts here: three variables, some strange DAGs, and three models. If you feel at all confused, it is only because you are paying attention.

It will help to visualize the model's inferences. Visualizing the posterior distribution in simple bivariate regressions, like those in the previous chapter, is easy. There's only one predictor variable, so a single scatterplot can convey a lot of information. And so in the previous chapter we used scatters of the data. Then we overlaid regression lines and intervals to both (1) visualize the size of the association between the predictor and outcome and (2) to get a crude sense of the ability of the model to predict the individual observations.

With multivariate regression, you'll need more plots. There is a huge literature detailing a variety of plotting techniques that all attempt to help one understand multiple linear

### PDF page 155 (book page 139)

regression. None of these techniques is suitable for all jobs, and most do not generalize beyond linear regression. So the approach I take here is to instead help you compute whatever you need from the model. I offer three examples of interpretive plots:

1. *Predictor residual plots.* These plots show the outcome against *residual* predictor values. They are useful for understanding the statistical model, but not much else.
2. *Posterior prediction plots.* These show model-based predictions against raw data, or otherwise display the error in prediction. They are tools for checking fit and assessing predictions. They are not causal tools.
3. *Counterfactual plots.* These show the implied predictions for imaginary experiments. These plots allow you to explore the causal implications of manipulating one or more variables.

Each of these plot types has its advantages and deficiencies, depending upon the context and the question of interest. In the rest of this section, I show you how to manufacture each of these in the context of the divorce data.

**5.1.5.1. *Predictor residual plots.*** A predictor variable residual is the average prediction error when we use all of the other predictor variables to model a predictor of interest. That's a complicated concept, so we'll go straight to the example, where it will make sense. The benefit of computing these things is that, once plotted against the outcome, we have a bivariate regression of sorts that has already "controlled" for all of the other predictor variables. It just leaves in the variation that is not expected by the model of the mean, $\mu$, as a function of the other predictors.

In our multivariate model of divorce rate, we have two predictors: (1) marriage rate (M) and (2) median age at marriage (A). To compute predictor residuals for either, we just use the other predictor to model it. So for marriage rate, this is the model we need:

$$
\begin{aligned}
M_i &\sim \text{Normal}(\mu_i, \sigma) \\
\mu_i &= \alpha + \beta A_i \\
\alpha &\sim \text{Normal}(0, 0.2) \\
\beta &\sim \text{Normal}(0, 0.5) \\
\sigma &\sim \text{Exponential}(1)
\end{aligned}
$$

As before, $M$ is marriage rate and $A$ is median age at marriage. Note that since we standardized both variables, we already expect the mean $\alpha$ to be around zero, as before. So I'm reusing the same priors as earlier. This code will approximate the posterior:

*[margin: R code 5.13]*

```r
m5.4 <- quap(
    alist(
        M ~ dnorm( mu , sigma ) ,
        mu <- a + bAM * A ,
        a ~ dnorm( 0 , 0.2 ) ,
        bAM ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data = d )
```

And then we compute the *residuals* by subtracting the observed marriage rate in each State from the predicted rate, based upon the model above:

### PDF page 156 (book page 140)

**FIGURE 5.4** Understanding multiple regression through residuals. The top row shows each predictor regressed on the other predictor. The lengths of the line segments connecting the model's expected value of the outcome, the regression line, and the actual value are the *residuals*. In the bottom row, divorce rate is regressed on the residuals from the top row. Bottom left: The residual variation in marriage rate shows no association with divorce rate. Bottom right: Divorce rate on age at marriage residuals, showing remaining variation among the residuals, and this variation is associated with divorce rate.

*[Figure: Four scatterplots arranged in two rows. Top left: Marriage rate (std) on the y-axis (−1 to 2) versus Age at marriage (std) on the x-axis (−2 to 3), with a downward-sloping regression line and vertical line segments from each point to the line marking residuals; labeled points WY, ND, HI, DC, ME. Top right: Age at marriage (std) on the y-axis (−2 to 3) versus Marriage rate (std) on the x-axis (−1 to 2), with a downward-sloping regression line and residual segments; labeled points DC, HI, ID. Bottom left: Divorce rate (std) on the y-axis (−2 to 2) versus Marriage rate residuals on the x-axis (−1.5 to 1.5), with a nearly flat regression line, a shaded confidence band, and a vertical dashed line at 0; labeled points ME, WY, HI, ND, DC. Bottom right: Divorce rate (std) on the y-axis (−2 to 2) versus Age at marriage residuals on the x-axis (−1 to 2), with a downward-sloping regression line, a shaded confidence band, and a vertical dashed line at 0; labeled points ID, HI, DC.]*

*[margin: R code 5.14]*

```r
mu <- link(m5.4)
mu_mean <- apply( mu , 2 , mean )
mu_resid <- d$M - mu_mean
```

When a residual is positive, that means that the observed rate was in excess of what the model expects, given the median age at marriage in that State. When a residual is negative, that

### PDF page 157 (book page 141)

means the observed rate was below what the model expects. In simpler terms, States with positive residuals have high marriage rates for their median age of marriage, while States with negative residuals have low rates for their median age of marriage. It'll help to plot the relationship between these two variables, and show the residuals as well. In Figure 5.4, upper left, I show m5.4 along with line segments for each residual. Notice that the residuals are variation in marriage rate that is left over, after taking out the purely linear relationship between the two variables.

Now to use these residuals, let's put them on a horizontal axis and plot them against the actual outcome of interest, divorce rate. In Figure 5.4 also (lower left), I plot these residuals against divorce rate, overlaying the linear regression of the two variables. You can think of this plot as displaying the linear relationship between divorce and marriage rates, having statistically "controlled" for median age of marriage. The vertical dashed line indicates marriage rate that exactly matches the expectation from median age at marriage. So States to the right of the line have higher marriage rates than expected. States to the left of the line have lower rates. Average divorce rate on both sides of the line is about the same, and so the regression line demonstrates little relationship between divorce and marriage rates.

The same procedure works for the other predictor. The top right plot in Figure 5.4 shows the regression of A on M and the residuals. In the lower right, these residuals are used to predict divorce rate. States to the right of the vertical dashed line have older-than-expected median age at marriage, while those to the left have younger-than-expected median age at marriage. Now we find that the average divorce rate on the right is lower than the rate on the left, as indicated by the regression line. States in which people marry older than expected for a given rate of marriage tend to have less divorce.

So what's the point of all of this? There's conceptual value in seeing the model-based predictions displayed against the outcome, after subtracting out the influence of other predictors. The plots in Figure 5.4 do this. But this procedure also brings home the message that regression models measure the remaining association of each predictor with the outcome, after already knowing the other predictors. In computing the predictor residual plots, you had to perform those calculations yourself. In the unified multivariate model, it all happens automatically. Nevertheless, it is useful to keep this fact in mind, because regressions can behave in surprising ways as a result. We'll have an example soon.

Linear regression models do all of this simultaneous measurement with a very specific additive model of how the variables relate to one another. But predictor variables can be related to one another in non-additive ways. The basic logic of statistical control does not change in those cases, but the details definitely do, and these residual plots cease to be useful. Luckily there are other ways to understand a model. That's where we turn next.

**Rethinking: Never use residuals as data.** There is a tradition, especially in parts of biology, of using residuals from one model as data in another model. For example, a biologist might regress brain size on body size and then use the brain size residuals as data in another model. This procedure is always a mistake. Residuals are not known. They are parameters, variables with unobserved values. Treating them as known values throws away uncertainty. The right way to control for body size is to include it in the same model, preferably a model designed with an explicit causal identification strategy.<sup>81</sup>

**5.1.5.2. *Posterior prediction plots.*** It's important to check the model's implied predictions against the observed data. This is what you did in Chapter 3, when you simulated

### PDF page 158 (book page 142)

globe tosses, averaging over the posterior, and comparing the simulated results to the observed. These kinds of checks are useful in many ways. For now, we'll focus on two uses for them.

1. Did the model correctly approximate the posterior distribution? Golems do make mistakes, as do golem engineers. Errors can be more easily diagnosed by comparing implied predictions to the raw data. Some caution is required, because not all models try to exactly match the sample. But even then, you'll know what to expect from a successful approximation. You'll see some examples later (Chapter 13).

2. How does the model fail? All models are useful fictions, so they always fail in some way. Sometimes, the model fits correctly but is still so poor for our purposes that it must be discarded. More often, a model predicts well in some respects, but not in others. By inspecting the individual cases where the model makes poor predictions, you might get an idea of how to improve the model. The difficulty is that this process is essentially creative and relies upon the analysts domain expertise. No robot can (yet) do it for you. It also risks chasing noise, a topic we'll focus on in later chapters.

How could we produce a simple posterior predictive check in the divorce example? Let's begin by simulating predictions, averaging over the posterior.

*[margin: R code 5.15]*

```r
# call link without specifying new data
# so it uses original data
mu <- link( m5.3 )

# summarize samples across cases
mu_mean <- apply( mu , 2 , mean )
mu_PI <- apply( mu , 2 , PI )

# simulate observations
# again no new data, so uses original data
D_sim <- sim( m5.3 , n=1e4 )
D_PI <- apply( D_sim , 2 , PI )
```

This code is similar to what you've seen before, but now using the original observed data.

For multivariate models, there are many different ways to display these simulations. The simplest is to just plot predictions against observed. This code will do that, and then add a line to show perfect prediction and line segments for the confidence interval of each prediction:

*[margin: R code 5.16]*

```r
plot( mu_mean ~ d$D , col=rangi2 , ylim=range(mu_PI) ,
    xlab="Observed divorce" , ylab="Predicted divorce" )
abline( a=0 , b=1 , lty=2 )
for ( i in 1:nrow(d) ) lines( rep(d$D[i],2) , mu_PI[,i] , col=rangi2 )
```

The resulting plot appears in Figure 5.5. It's easy to see from this arrangement of the simulations that the model under-predicts for States with very high divorce rates while it over-predicts for States with very low divorce rates. That's normal. This is what regression does—it is skeptical of extreme values, so it expects regression towards the mean. But beyond this general regression to the mean, some States are very frustrating to the model, lying very far from the diagonal. I've labeled some points like this, including Idaho (ID) and Utah (UT), both of

### PDF page 159 (book page 143)

**FIGURE 5.5.** Posterior predictive plot for the multivariate divorce model, `m5.3`. The horizontal axis is the observed divorce rate in each State. The vertical axis is the model's posterior predicted divorce rate, given each State's median age at marriage and marriage rate. The blue line segments are 89% compatibility intervals. The diagonal line shows where posterior predictions exactly match the sample. *[Figure: scatterplot with "Observed divorce" on the horizontal axis (ticks −2, −1, 0, 1, 2) and "Predicted divorce" on the vertical axis (ticks −2, −1, 0, 1). Each State is an open blue point with a vertical blue line segment (89% interval); a dashed diagonal line runs from lower-left to upper-right marking exact agreement. Four points are labeled: ID and UT sit above the diagonal at upper left/center, RI sits below the diagonal at lower center, and ME sits to the right at mid-height.]*

which have much lower divorce rates than the model expects them to have. The easiest way to label a few select points is to use `identify`:

*[margin: R code 5.17]*

```r
identify( x=d$D , y=mu_mean , labels=d$Loc )
```

After executing the line of code above, R will wait for you to click near a point in the active plot window. It'll then place a label near that point, on the side you choose. When you are done labeling points, press your right mouse button (or press ESC, on some platforms).

What is unusual about Idaho and Utah? Both of these States have large proportions of members of the Church of Jesus Christ of Latter-day Saints. Members of this church have low rates of divorce, wherever they live. This suggests that having a finer view on the demographic composition of each State, beyond just median age at marriage, would help a lot to refine our understanding.

**Rethinking: Stats, huh, yeah what is it good for?** Often people want statistical modeling to do things that statistical modeling cannot do. For example, we'd like to know whether an effect is "real" or rather spurious. Unfortunately, modeling merely quantifies uncertainty in the precise way that the model understands the problem. Usually answers to large world questions about truth and causation depend upon information not included in the model. For example, any observed correlation between an outcome and predictor could be eliminated or reversed once another predictor is added to the model. But if we cannot think of the right variable, we might never notice. Therefore all statistical models are vulnerable to and demand critique, regardless of the precision of their estimates and apparent accuracy of their predictions. Rounds of model criticism and revision embody the real tests of scientific hypotheses. A true hypothesis will pass and fail many statistical "tests" on its way to acceptance.

**Overthinking: Simulating spurious association.** One way that spurious associations between a predictor and outcome can arise is when a truly causal predictor, call it $x_{\text{real}}$, influences both the outcome, $y$, and a spurious predictor, $x_{\text{spur}}$. This can be confusing, however, so it may help to simulate this scenario and see both how the spurious data arise and prove to yourself that multiple regression can reliably indicate the right predictor, $x_{\text{real}}$. So here's a very basic simulation:

### PDF page 160 (book page 144)

*[margin: R code 5.18]*

```r
N <- 100                         # number of cases
x_real <- rnorm( N )             # x_real as Gaussian with mean 0 and stddev 1
x_spur <- rnorm( N , x_real )    # x_spur as Gaussian with mean=x_real
y <- rnorm( N , x_real )         # y as Gaussian with mean=x_real
d <- data.frame(y,x_real,x_spur) # bind all together in data frame
```

Now the data frame `d` has 100 simulated cases. Because `x_real` influences both `y` and `x_spur`, you can think of `x_spur` as another outcome of `x_real`, but one which we mistake as a potential predictor of `y`. As a result, both $x_{\text{real}}$ and $x_{\text{spur}}$ are correlated with $y$. You can see this in the scatterplots from `pairs(d)`. But when you include both $x$ variables in a linear regression predicting $y$, the posterior mean for the association between $y$ and $x_{\text{spur}}$ will be close to zero, while the comparable mean for $x_{\text{real}}$ will be closer to 1.

**5.1.5.3.** *Counterfactual plots.* A second sort of inferential plot displays the implied predictions of the model. I call these plots COUNTERFACTUAL, because they can be produced for any values of the predictor variables you like, even unobserved or impossible combinations like very high median age of marriage and very high marriage rate. There are no States with this combination, but in a counterfactual plot, you can ask the model for a prediction for such a State. This means you have take care not to plot nonsense. But used with clarity of purpose, counterfactual plots help you understand the model and generate predictions for imaginary interventions.

The simplest use of a counterfactual plot is to see how the predictions change as you change only one predictor at a time. This means holding the values of all predictors constant, except for a single predictor of interest. A tension with such plots, however, is that they ignore the assumed causal structure. In the small world of the model, it is possible to change median age of marriage without also changing the marriage rate. But is this also possible in the large world of reality? Probably not. Suppose for example that you pay young couples to postpone marriage until they are 35 years old. Surely this will also decrease the number of couples who ever get married—some people will die before turning 35, among other reasons—decreasing the overall marriage rate. An extraordinary and evil degree of control over people would be necessary to really hold marriage rate constant while forcing everyone to marry at a later age.

So let's see how to generate plots of model predictions that take the causal structure into account. The basic recipe is:

(1) Pick a variable to manipulate, the intervention variable.
(2) Define the range of values to set the intervention variable to.
(3) For each value of the intervention variable, and for each sample in posterior, use the causal model to simulate the values of other variables, including the outcome.

In the end, you end up with a posterior distribution of counterfactual outcomes that you can plot and summarize in various ways, depending upon your goal.

Let's see how to do this for the divorce model. Again we take this DAG as given:

*[DAG: three nodes — A (top left) and M (top right), with D (bottom center). Directed edges: A → M (across the top), A → D (down to the left), and M → D (down to the right).]*

### PDF page 161 (book page 145)

To simulate from this, we need more than the DAG. We also need a set of functions that tell us how each variable is generated. For simplicity, we'll use Gaussian distributions for each variable, just like in model `m5.3`. But model `m5.3` ignored the assumption that $A$ influences $M$. We didn't need that to estimate $A \to D$. But we do need it to predict the consequences of manipulating $A$, because some of the effect of $A$ acts through $M$.

To estimate the influence of $A$ on $M$, all we need is to regress $A$ on $M$, there are no other variables in the DAG creating an association between $A$ and $M$. We can just add this regression to the `quap()` model, running two regressions at the same time:

*[margin: R code 5.19]*

```r
data(WaffleDivorce)
d <- list()
d$A <- standardize( WaffleDivorce$MedianAgeMarriage )
d$D <- standardize( WaffleDivorce$Divorce )
d$M <- standardize( WaffleDivorce$Marriage )

m5.3_A <- quap(
    alist(
      ## A -> D <- M
        D ~ dnorm( mu , sigma ) ,
        mu <- a + bM*M + bA*A ,
        a ~ dnorm( 0 , 0.2 ) ,
        bM ~ dnorm( 0 , 0.5 ) ,
        bA ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 ),
      ## A -> M
        M ~ dnorm( mu_M , sigma_M ),
        mu_M <- aM + bAM*A,
        aM ~ dnorm( 0 , 0.2 ),
        bAM ~ dnorm( 0 , 0.5 ),
        sigma_M ~ dexp( 1 )
    ) , data = d )
```

Look at the `precis(5.3_A)` summary. You'll see that $M$ and $A$ are strongly negatively associated. If we interpret this causally, it indicates that manipulating $A$ reduces $M$.

The goal is to simulate what would happen, if we manipulate $A$. So next we define a range of values for $A$.

*[margin: R code 5.20]*

```r
A_seq <- seq( from=-2 , to=2 , length.out=30 )
```

This defines a list of 30 imaginary interventions, ranging from 2 standard deviations below and 2 above the mean. Now we can use `sim()`, which you met in the previous chapter, to simulate observations from model `m5.3_A`. But this time we'll tell it to simulate both $M$ and $D$, in that order. Why in that order? Because we have to simulate the influence of $A$ on $M$ before we simulate the joint influence of $A$ and $M$ on $D$. The `vars` argument to `sim()` tells it both which observables to simulate and in which order.

*[margin: R code 5.21]*

```r
# prep data
sim_dat <- data.frame( A=A_seq )
```

### PDF page 162 (book page 146)

**FIGURE 5.6.** Counterfactual plots for the multivariate divorce model, `m5.3`. These plots visualize the predicted effect of manipulating age at marriage $A$ on divorce rate $D$. Left: Total causal effect of manipulating $A$ (horizontal) on $D$. The model allows some of the total causal effect of $A$ to act through $M$, although the posterior distribution finds little support for an effect of $M$ on $D$. This plot nevertheless contains both paths, $A \to D$ and $A \to M \to D$. Right: Simulated values of $M$ show the estimated influence $A \to M$. *[Figure: two side-by-side line plots with gray shaded uncertainty bands. Left panel titled "Total counterfactual effect of A on D", x-axis "manipulated A" (−2 to 2), y-axis "counterfactual D" (−2 to 2), showing a downward-sloping line from about +1 to about −1. Right panel titled "Counterfactual effect A -> M", x-axis "manipulated A" (−2 to 2), y-axis "counterfactual M" (−2 to 2), showing a similar downward-sloping line.]*

```r
# simulate M and then D, using A_seq
s <- sim( m5.3_A , data=sim_dat , vars=c("M","D") )
```

That's all there is to it. But do at least glance at the Overthinking box at the end of this section, where I show you the individual steps, so you can perform this kind of counterfactual simulation for any model fit with any software. Now to plot the predictions:

*[R code 5.22]*

```r
# display counterfactual predictions
plot( sim_dat$A , colMeans(s$D) , ylim=c(-2,2) , type="l" ,
    xlab="manipulated A" , ylab="counterfactual D"  )
shade( apply(s$D,2,PI) , sim_dat$A )
mtext( "Total counterfactual effect of A on D" )
```

The resulting plot is shown in FIGURE 5.6 (left side). This predicted trend in $D$ include both paths: $A \to D$ and $A \to M \to D$. We found previously that $M \to D$ is very small, so the second path doesn't contribute much to the trend. But if $M$ were to strongly influence $D$, the code above would include the effect. The counterfactual simulation also generated values for $M$. These are show on the right in FIGURE 5.6. The object `s` from the code above includes these simulated $M$ values. Try to reproduce the figure yourself, by modifying the plotting code.

The trick with simulating counterfactuals is to realize that when we manipulate some variable $X$, we break the causal influence of other variables on $X$. This is the same as saying

### PDF page 163 (book page 147)

**FIGURE 5.7.** The counterfactual effect of manipulating marriage rate $M$ on divorce rate $D$. Since $M \to D$ was estimated to be very small, there is almost no trend here. By manipulating $M$, we break the influence of $A$ on $M$, and this removes the association between $M$ and $D$. *[Figure: a single line plot with a wide gray shaded uncertainty band, titled "Total counterfactual effect of M on D", x-axis "manipulated M" (−2 to 2), y-axis "counterfactual D" (−2 to 2), showing an almost flat line near 0.]*

we modify the DAG so that no arrows enter $X$. Suppose for example that we now simulate the effect of manipulating $M$. This implies the DAG:

```
A           M
 ↘         ↙
     D
```

The arrow $A \to M$ is deleted, because if we control the values of $M$, then $A$ no longer influences it. It's like a perfectly controlled experiment. Now we can modify the code above to simulate the counterfactual result of manipulating $M$. We'll simulate a counterfactual for an average state, with $A = 0$, and see what changing $M$ does.

*[R code 5.23]*

```r
sim_dat <- data.frame( M=seq(from=-2,to=2,length.out=30) , A=0 )
s <- sim( m5.3_A , data=sim_dat , vars="D" )

plot( sim_dat$M , colMeans(s) , ylim=c(-2,2) , type="l" ,
    xlab="manipulated M" , ylab="counterfactual D"  )
shade( apply(s,2,PI) , sim_dat$M )
mtext( "Total counterfactual effect of M on D" )
```

We only simulate $D$ now—note the `vars` argument to `sim()` in the code above. We don't simulate $A$, because $M$ doesn't influence it. I show this plot in FIGURE 5.7. This trend is naturally less strong, because we already found that there is no evidence for a strong influence of $M$ on $D$.

In more complex models with many potential paths, the same strategy will compute counterfactuals for an exposure of interest. But as you'll see in later examples, often it is simply not possible to estimate a plausible, un-confounded causal effect of some exposure $X$ on some outcome $Y$. But even in those cases, there are still important counterfactuals to consider. So we'll return to this theme in future chapters.

### PDF page 164 (book page 148)

**Overthinking: Simulating counterfactuals.** The example in this section used `sim()` to hide the details. But simulating counterfactuals on your own is not hard. It just uses the model definition. Assume we've already fit model `m5.3_A`, the model that includes both causal paths $A \to D$ and $A \to M \to D$. We define a range of values that we want to assign to $A$:

*[R code 5.24]*

```r
A_seq <- seq( from=-2 , to=2 , length.out=30 )
```

Next we need to extract the posterior samples, because we'll simulate observations for each set of samples. Then it really is just a matter of using the model definition with the samples, as in previous examples. The model defines the distribution of $M$. We just convert that definition to the corresponding simulation function, which is `rnorm` in this case:

*[R code 5.25]*

```r
post <- extract.samples( m5.3_A )
M_sim <- with( post , sapply( 1:30 ,
    function(i) rnorm( 1e3 , aM + bAM*A_seq[i] , sigma_M ) ) )
```

I used the `with()` function, which saves us having to type `post$` in front of every parameter name. The linear model inside `rnorm` comes right out of the model definition. This produces a matrix of values, with samples in rows and cases corresponding to the values in `A_seq` in the columns. Now that we have simulated values for $M$, we can simulate $D$ too:

*[R code 5.26]*

```r
D_sim <- with( post , sapply( 1:30 ,
    function(i) rnorm( 1e3 , a + bA*A_seq[i] + bM*M_sim[,i] , sigma ) ) )
```

If you plot `A_seq` against the column means of `D_sim`, you'll see the same result as before. In complex models, there might be many more variables to simulate. But the basic procedure is the same.

**5.2. Masked relationship**

The divorce rate example demonstrates that multiple predictor variables are useful for knocking out spurious association. A second reason to use more than one predictor variable is to measure the direct influences of multiple factors on an outcome, when none of those influences is apparent from bivariate relationships. This kind of problem tends to arise when there are two predictor variables that are correlated with one another. However, one of these is positively correlated with the outcome and the other is negatively correlated with it.

You'll consider this kind of problem in a new data context, information about the composition of milk across primate species, as well as some facts about those species, like body mass and brain size.[^82] Milk is a huge investment, being much more expensive than gestation. Such an expensive resource is likely adjusted in subtle ways, depending upon the physiological and development details of each mammal species. Let's load the data into R first:

*[R code 5.27]*

```r
library(rethinking)
data(milk)
d <- milk
str(d)
```

You should see in the structure of the data frame that you have 29 rows (cases) for 8 variables (columns).

[^82]: (Endnote reference 82; note text appears in the book's collected endnotes, not on this page.)

### PDF page 165 (book page 149)

A popular hypothesis has it that primates with larger brains produce more energetic milk, so that brains can grow quickly. Answering questions of this sort consumes a lot of effort in evolutionary biology, because there are many subtle statistical issues that arise when comparing species. We'll start simple, but by the end of the book we'll include some more of these subtle issues. The variables we'll consider for now are:

- `kcal.per.g` : Kilocalories of energy per gram of milk.
- `mass` : Average female body mass, in kilograms.
- `neocortex.perc` : The percent of total brain mass that is neocortex mass.

The question here is to what extent energy content of milk, measured here by kilocalories, is related to the percent of the brain mass that is neocortex. Neocortex is the gray, outer part of the brain that is particularly elaborated in mammals and especially primates. We'll end up needing female body mass as well, to see the masking that hides the relationships among the variables. Let's standardize these three variables. As in previous examples, standardizing helps us both get a reliable approximation of the posterior as well as build reasonable priors.

*[R code 5.28]*
```r
d$K <- scale( d$kcal.per.g )
d$N <- scale( d$neocortex.perc )
d$M <- scale( log(d$mass) )
```

The first model to consider is the simple bivariate regression between kilocalories and neocortex percent. You already know how to set up this regression. In mathematical form:

$$K_i \sim \text{Normal}(\mu_i, \sigma)$$
$$\mu_i = \alpha + \beta_N N_i$$

where $K$ is standardized kilocalories and $N$ is standardized neocortex percent. We still need to consider the priors. But first let's just try to run this as a `quap` model with some vague priors, because there is another key modeling issue to address first.

*[R code 5.29]*
```r
m5.5_draft <- quap(
    alist(
        K ~ dnorm( mu , sigma ) ,
        mu <- a + bN*N ,
        a ~ dnorm( 0 , 1 ) ,
        bN ~ dnorm( 0 , 1 ) ,
        sigma ~ dexp( 1 )
    ) , data=d )
```

When you execute this code, you'll get a confusing error message:

```
Error in quap(alist(K ~ dnorm(mu, sigma), mu <- a + bN * N, a ~ dnorm(0,  :
  initial value in 'vmmin' is not finite
The start values for the parameters were invalid. This could be caused by
missing values (NA) in the data or by start values outside the parameter
constraints. If there are no NA values in the data, try using explicit start
values.
```

What has gone wrong here? This particular error message means that the model didn't return a valid probability for even the starting parameter values. In this case, the culprit is the

### PDF page 166 (book page 150)

missing values in the `N` variable. Take a look inside the original variable and see for yourself:

*[R code 5.30]*
```r
d$neocortex.perc
```

```
 [1] 55.16    NA    NA    NA    NA 64.54 64.54 67.64    NA 68.85 58.85 61.69
[13] 60.32    NA    NA 69.97    NA 70.41    NA 73.40    NA 67.53    NA 71.26
[25] 72.60    NA 70.24 76.30 75.49
```

Each `NA` in the output is a missing value. If you pass a vector like this to a likelihood function like `dnorm`, it doesn't know what to do. After all, what's the probability of a missing value? Whatever the answer, it isn't a number, and so `dnorm` returns a `NaN`. Unable to even get started, `quap` (or rather `optim`, which does the real work) gives up and barks about some weird thing called `vmmin` not being finite. This kind of opaque error message is unfortunately the norm in R. The additional part of the message suggesting `NA` values might be responsible is just `quap` taking a guess.

This is easy to fix. What you need to do here is manually drop all the cases with missing values. This is known as a *complete case analysis*. More automated model fitting commands, like `lm` and `glm`, will silently drop such cases for you. But this isn't always a good thing. In later chapters, you'll see a few reasons why. Please indulge me for now. It's worth learning how to do this yourself. To make a new data frame with only complete cases in it, just use:

*[R code 5.31]*
```r
dcc <- d[ complete.cases(d$K,d$N,d$M) , ]
```

This makes a new data frame, `dcc`, that consists of the 17 rows from `d` that have values in all columns. Now let's work with the new data frame. All that is new in the code is using `dcc` instead of `d`:

*[R code 5.32]*
```r
m5.5_draft <- quap(
    alist(
        K ~ dnorm( mu , sigma ) ,
        mu <- a + bN*N ,
        a ~ dnorm( 0 , 1 ) ,
        bN ~ dnorm( 0 , 1 ) ,
        sigma ~ dexp( 1 )
    ) , data=dcc )
```

Before considering the posterior predictions, let's consider those priors. As in many simple linear regression problems, these priors are harmless. But are they reasonable? It is important to build reasonable priors, because as the model becomes less simple, the priors can be very helpful, but only if they are scientifically reasonable. To simulate and plot 50 prior regression lines:

*[R code 5.33]*
```r
prior <- extract.prior( m5.5_draft )
xseq <- c(-2,2)
mu <- link( m5.5_draft , post=prior , data=list(N=xseq) )
plot( NULL , xlim=xseq , ylim=xseq )
for ( i in 1:50 ) lines( xseq , mu[i,] , col=col.alpha("black",0.3) )
```

### PDF page 167 (book page 151)

**FIGURE 5.8.** Prior predictive distributions for the first primate milk model, `m5.5`. Each plot shows a range of 2 standard deviations for each variable. Left: The vague first guess. These priors are clearly silly. Right: Slightly less silly priors that at least stay within the potential space of observations. *[Figure: two side-by-side scatterplots of prior regression lines. Both have x-axis "neocortex percent (std)" and y-axis "kilocal per g (std)", each running from −2 to 2. Left panel, labeled `a ~ dnorm(0, 1)` and `bN ~ dnorm(0, 1)`, shows ~50 lines with steep and varied slopes crisscrossing the whole plot region. Right panel, labeled `a ~ dnorm(0, 0.2)` and `bN ~ dnorm(0, 0.5)`, shows lines with gentler slopes passing through near the origin and staying mostly within the plotted range.]*

The result is displayed on the left side of Figure 5.8. I've shown a range of 2 standard deviations for both variables. So that is most of the outcome space. These lines are crazy. As in previous examples, we can do better by both tightening the $\alpha$ prior so that it sticks closer to zero. With two standardized variables, when predictor is zero, the expected value of the outcome should also be zero. And the slope $\beta_N$ needs to be a bit tighter as well, so that it doesn't regularly produce impossibly strong relationships. Here's an attempt:

*[R code 5.34]*
```r
m5.5 <- quap(
    alist(
        K ~ dnorm( mu , sigma ) ,
        mu <- a + bN*N ,
        a ~ dnorm( 0 , 0.2 ) ,
        bN ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data=dcc )
```

If you plot these priors, you'll get what is shown on the right side of Figure 5.8. These are still very vague priors, but at least the lines stay within the high probability region of the observable data.

Now let's look at the posterior:

*[R code 5.35]*
```r
precis( m5.5 )
```

```
      mean   sd  5.5% 94.5%
a     0.04 0.15 -0.21  0.29
```

### PDF page 168 (book page 152)

```
bN     0.13 0.22 -0.22  0.49
sigma 1.00 0.16  0.74  1.26
```

From this summary, you can possibly see that this is neither a strong nor very precise association. The standard deviation is almost twice the posterior mean. But as always, it's much easier to see this if we draw a picture. Tables of numbers are golem speak, and we are not golems. We can plot the predicted mean and 89% compatibility interval for the mean to see this more easily:

```r
xseq <- seq( from=min(dcc$N)-0.15 , to=max(dcc$N)+0.15 , length.out=30 )
mu <- link( m5.5 , data=list(N=xseq) )
mu_mean <- apply(mu,2,mean)
mu_PI <- apply(mu,2,PI)
plot( K ~ N , data=dcc )
lines( xseq , mu_mean , lwd=2 )
shade( mu_PI , xseq )
```
*[R code 5.36]*

I display this plot in the upper-left of Figure 5.9. The posterior mean line is weakly positive, but it is highly imprecise. A lot of mildly positive and negative slopes are plausible, given this model and these data.

Now consider another predictor variable, adult female body mass, `mass` in the data frame. Let's use the logarithm of mass, `log(mass)`, as a predictor as well. Why the logarithm of mass instead of the raw mass in kilograms? It is often true that scaling measurements like body mass are related by magnitudes to other variables. Taking the log of a measure translates the measure into magnitudes. So by using the logarithm of body mass here, we're saying that we suspect that the magnitude of a mother's body mass is related to milk energy, in a linear fashion.

Now we construct a similar model, but consider the bivariate relationship between kilocalories and body mass:

```r
m5.6 <- quap(
    alist(
        K ~ dnorm( mu , sigma ) ,
        mu <- a + bM*M ,
        a ~ dnorm( 0 , 0.2 ) ,
        bM ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data=dcc )
precis(m5.6)
```
*[R code 5.37]*

```
        mean   sd  5.5% 94.5%
a       0.05 0.15 -0.20  0.29
bM     -0.28 0.19 -0.59  0.03
sigma   0.95 0.16  0.70  1.20
```

Log-mass is negatively correlated with kilocalories. This influence does seem stronger than that of neocortex percent, although in the opposite direction. It is quite uncertain though, with a wide confidence interval that is consistent with a wide range of both weak and stronger relationships. This regression is shown in the upper-right of Figure 5.9. You should modify

### PDF page 169 (book page 153)

**FIGURE 5.9.** Milk energy and neocortex among primates. In the top two plots, simple bivariate regressions of kilocalories per gram of milk (K) on (left) neocortex percent (N) and (right) log female body mass (M) show weak associations. In the bottom row, a model with both neocortex percent (N) and log body mass (M) shows stronger associations. *[Figure: a 2×2 grid of scatterplots/regression plots, all with y-axis "kilocal per g (std)" ranging −1.0 to 2.0. Top-left: K vs "neocortex percent (std)" (x from −2.0 to 1.5), open blue points with a weakly positive posterior mean line and a wide grey shaded compatibility interval. Top-right: K vs "log body mass (std)" (x from −2 to 1), open blue points with a weakly negative mean line and wide grey shade. Bottom-left, titled "Counterfactual holding M = 0": a strongly positive mean line versus "neocortex percent (std)" with a grey shaded interval, no data points. Bottom-right, titled "Counterfactual holding N = 0": a strongly negative mean line versus "log body mass (std)" with a grey shaded interval, no data points.]*

the code that plotted the upper-left plot in the same figure, to be sure you understand how to do this.

### PDF page 170 (book page 154)

Now let's see what happens when we add both predictor variables at the same time to the regression. This is the multivariate model, in math form:

$$
\begin{aligned}
K_i &\sim \text{Normal}(\mu_i, \sigma) \\
\mu_i &= \alpha + \beta_N N_i + \beta_M M_i \\
\alpha &\sim \text{Normal}(0, 0.2) \\
\beta_n &\sim \text{Normal}(0, 0.5) \\
\beta_m &\sim \text{Normal}(0, 0.5) \\
\sigma &\sim \text{Exponential}(1)
\end{aligned}
$$

Approximating the posterior requires no new tricks:

```r
m5.7 <- quap(
    alist(
        K ~ dnorm( mu , sigma ) ,
        mu <- a + bN*N + bM*M ,
        a ~ dnorm( 0 , 0.2 ) ,
        bN ~ dnorm( 0 , 0.5 ) ,
        bM ~ dnorm( 0 , 0.5 ) ,
        sigma ~ dexp( 1 )
    ) , data=dcc )
precis(m5.7)
```
*[R code 5.38]*

```
        mean   sd  5.5% 94.5%
a       0.07 0.13 -0.15  0.28
bN      0.68 0.25  0.28  1.07
bM     -0.70 0.22 -1.06 -0.35
sigma   0.74 0.13  0.53  0.95
```

By incorporating both predictor variables in the regression, the posterior association of both with the outcome has increased. Visually comparing this posterior to those of the previous two models helps:

```r
plot( coeftab( m5.5 , m5.6 , m5.7 ) , pars=c("bM","bN") )
```
*[R code 5.39]*

*[Figure: a coefficient-comparison (coeftab) plot with a horizontal "Estimate" axis from −1.0 to 1.0. Two grouped sets of rows. Top group "bM": row m5.7 shows a point estimate near −0.7 with a horizontal interval, row m5.6 a point near −0.28 with an interval, and row m5.5 is empty (no bM). Bottom group "bN": row m5.7 shows a point near 0.68 with an interval, row m5.6 is empty (no bN), and row m5.5 a point near 0.13 with an interval. Open circles mark the means; horizontal lines mark compatibility intervals; dotted horizontal guide lines run across each row.]*

The posterior mean for the association of neocortex percent has increased fivefold, and its 89% interval is now entirely above zero. The posterior mean for log body mass has increased 2.5 times in magnitude.

### PDF page 171 (book page 155)

What happened here? Why did adding neocortex and body mass to the same model lead to larger estimated effects of both? This is a context in which there are two variables correlated with the outcome, but one is positively correlated with it and the other is negatively correlated with it. In addition, both of the explanatory variables are positively correlated with one another. Try a simple `pairs` plot to appreciate this correlation: `pairs( ~K + M + N , dcc )`. As a result, they tend to cancel one another out.

This is another case in which multiple regression automatically finds the most revealing cases and uses them to produce inferences. What the regression model does is ask if species that have high neocortex percent *for their body mass* have higher milk energy. Likewise, the model asks if species with high body mass *for their neocortex percent* have higher milk energy. Bigger species, like apes, have milk with less energy. But species with more neocortex tend to have richer milk. The fact that these two variables, body size and neocortex, are correlated across species makes it hard to see these relationships, unless we account for both.

Some DAGs will help. There are at least three graphs consistent with the pattern in these data. Here they are, and then I'll explain each.

*[Figure: Three directed acyclic graphs. Left: M → N along the top, with arrows from both M and N pointing down to K below. Middle: M ← N along the top (arrow from N to M), with arrows from both M and N pointing down to K. Right: M ← U → N along the top, where U is circled (unobserved), with arrows from both M and N pointing down to K.]*

Beginning on the left, the first possibility is that body mass (*M*) influences neocortex percent (*N*). Both then influence kilocalories in milk (*K*). Second, in the middle, neocortex could instead influence body mass. The two variables still end up correlated in the sample. Finally, on the right, there could be an unobserved variable *U* that influences both *M* and *N*, producing a correlation between them. In this book, I'll circle variables that are unobserved. One of the great threats to causal inference is that there are potentially very many unobserved variables that influence an outcome. We'll consider this more in the next chapter.

Which of these graphs is right? We can't tell from the data alone, because these graphs imply the same set of conditional independencies. In this case, there are no conditional independencies—each DAG above implies that all pairs of variables are associated, regardless of what we condition on. A set of DAGs with the same conditional independencies is known as a Markov equivalence set. In the Overthinking box further down, I'll show you how to simulate observations consistent with each of these DAGs show that each can produce the masking phenomenon, and use the `dagitty` package to compute the complete set of Markov equivalent DAGs. Remember that while the data alone can never tell you which causal model is correct, your scientific knowledge of the variables will eliminate a large number of silly, but Markov equivalent, DAGs.

The final thing we'd like to do with these models is to finish Figure 5.9. Let's make *counterfactual* plots to show how the model sees the problem. Once we have multiple predictor variables, we can conduct counterfactual experiments that vary one predictor while holding the others constant. In the real world, such experiments are typically impossible. If we change an animal's body size, natural selection will then change the other features to match it. But these counterfactual plots do help us see how the model views the association between each predictor and the outcome. Here is the code to produce the lower-left plot in Figure 5.9 (page 153).

### PDF page 172 (book page 156)

*[R code 5.40]*

```r
xseq <- seq( from=min(dcc$M)-0.15 , to=max(dcc$M)+0.15 , length.out=30 )
mu <- link( m5.7 , data=data.frame( M=xseq , N=0 ) )
mu_mean <- apply(mu,2,mean)
mu_PI <- apply(mu,2,PI)
plot( NULL , xlim=range(dcc$M) , ylim=range(dcc$K) )
lines( xseq , mu_mean , lwd=2 )
shade( mu_PI , xseq )
```

The reader should try to reproduce the lower-right plot by appropriately modifying this.

**Overthinking: Simulating a masking relationship.** Just as with understanding spurious association (page 143), it may help to simulate data in which two meaningful predictors act to mask one another. In the previous section, I showed three DAGs consistent with this. To simulate data consistent with the first DAG:

*[R code 5.41]*

```r
# M -> K <- N
# M -> N
n <- 100
M <- rnorm( n )
N <- rnorm( n , M )
K <- rnorm( n , N - M )
d_sim <- data.frame(K=K,N=N,M=M)
```

You can quickly see the masking pattern of inferences by replacing `dcc` with `d_sim` in models `m5.5`, `m5.6`, and `m5.7`. Look at the `precis` summaries and you'll see the same masking pattern where the slopes become more extreme in `m5.7`. The other two DAGs can be simulated like this:

*[R code 5.42]*

```r
# M -> K <- N
# N -> M
n <- 100
N <- rnorm( n )
M <- rnorm( n , N )
K <- rnorm( n , N - M )
d_sim2 <- data.frame(K=K,N=N,M=M)

# M -> K <- N
# M <- U -> N
n <- 100
U <- rnorm( n )
N <- rnorm( n , U )
M <- rnorm( n , U )
K <- rnorm( n , N - M )
d_sim3 <- data.frame(K=K,N=N,M=M)
```

In the primate milk example, it may be that the positive association between large body size and neocortex percent arises from a tradeoff between lifespan and learning. Large animals tend to live a long time. And in such animals, an investment in learning may be a better investment, because learning can be amortized over a longer lifespan. Both large body size and large neocortex then influence milk composition, but in different directions, for different reasons. This story implies that the DAG with an arrow from M to N, the first one, is the right one. But with the evidence at hand, we cannot easily see which is right. To compute the Markov equivalence set, let's define the first DAG and ask `dagitty` to do the hard work:

### PDF page 173 (book page 157)

*[R code 5.43]*

```r
dag5.7 <- dagitty( "dag{
    M -> K <- N
    M -> N }" )
coordinates(dag5.7) <- list( x=c(M=0,K=1,N=2) , y=c(M=0.5,K=1,N=0.5) )
MElist <- equivalentDAGs(dag5.7)
```

Now `MElist` should contain six different DAGs. To plot them all, you can use `drawdag(MElist)`.

**5.3. Categorical variables**

A common question for statistical methods is to what extent an outcome changes as a result of presence or absence of a category. A category here means discrete and unordered. For example, consider the different species in the milk energy data again. Some of them are apes, while others are New World monkeys. We might want to ask how predictions should vary when the species is an ape instead of a monkey. Taxonomic group is a categorical variable, because no species can be half-ape and half-monkey (discreteness), and there is no sense in which one is larger or smaller than the other (unordered). Other common examples of categorical variables include:

- Sex: male, female
- Developmental status: infant, juvenile, adult
- Geographic region: Africa, Europe, Melanesia

Many readers will already know that variables like this, routinely called *factors*, can easily be included in linear models. But what is not widely understood is how these variables are included in a model. This is because the computer does all of the work for us, most of the time. But there are some subtleties here that make exposing the machinery worthwhile. In most cases, there are different ways to build a category model. One way may be easier, because it is easier to define the priors. And interpreting estimates for categorical variables can be harder than for regular continuous variables. Knowing how the machine works removes a lot of this difficulty.

**5.3.1. Binary categories.** In the simplest case, the variable of interest has only two categories, like *male* and *female*. Let's rewind to the Kalahari data you met in Chapter 4. Back then, we ignored sex when predicting height, but obviously we expect males and females to have different averages. Take a look at the variables available:

*[R code 5.44]*

```r
data(Howell1)
d <- Howell1
str(d)
```

```
'data.frame':	544 obs. of  4 variables:
 $ height: num  152 140 137 157 145 ...
 $ weight: num  47.8 36.5 31.9 53 41.3 ...
 $ age   : num  63 63 65 41 51 35 32 27 19 54 ...
 $ male  : int  1 0 0 1 0 1 0 1 0 1 ...
```

The `male` variable is our new predictor, an example of a indicator variable. Indicator variables—sometimes also called "dummy" variables—are devices for encoding unordered categories into quantitative models. There is no sense here in which "male" is one more than

### PDF page 174 (book page 158)

"female." The purpose of the `male` variable is to indicate when a person in the sample is "male." So it takes the value 1 whenever the person is male, but it takes the value 0 when the person is female (or any other category). It doesn't matter which category—"male" or "female"—is indicated by the 1. The model won't care. But correctly interpreting the model will demand that you remember, so it's a good idea to name the variable after the category assigned the 1 value.

There are two ways to make a model with this information. The first is to use the indicator variable directly inside the linear model, as if it were a typical predictor variable. The effect of an indicator variable is to turn a parameter on for those cases in the category. Simultaneously, the variable turns the same parameter off for those cases in another category. This will make more sense, once you see it in the mathematical definition of the model. Consider again a linear model of height, as in Chapter 4. Now we'll ignore weight and the other variables and focus only on sex.

$$
\begin{aligned}
h_i &\sim \text{Normal}(\mu_i, \sigma) \\
\mu_i &= \alpha + \beta_m m_i \\
\alpha &\sim \text{Normal}(178, 20) \\
\beta_m &\sim \text{Normal}(0, 10) \\
\sigma &\sim \text{Uniform}(0, 50)
\end{aligned}
$$

where $h$ is height and $m$ is the dummy variable indicating a male individual. The parameter $\beta_m$ influences prediction only for those cases where $m_i = 1$. When $m_i = 0$, it has no effect on prediction, because it is multiplied by zero inside the linear model, $\alpha + \beta_m m_i$, canceling it out, whatever its value. This is just to say that, when $m_i = 1$, the linear model is $\mu_i = \alpha + \beta_m$. And when $m_i = 0$, the linear model is simply $\mu_i = \alpha$.

Using this approach means that $\beta_m$ represents the expected *difference* between males and females in height. The parameter $\alpha$ is used to predict both female and male heights. But male height gets an extra $\beta_m$. This also means that $\alpha$ is no longer the average height in the sample, but rather just the average female height. This can make assigning sensible priors a little harder. If you don't have a sense of the expected difference in height—what would be reasonable before seeing the data?—then this approach to including a category can be too much bother.

Furthermore, this approach necessarily assumes there is more uncertainty about one of the categories—"male" in this case—than the other. Why? Because a prediction for a male includes two parameters and therefore two priors. We can simulate this directly from the priors. The prior distributions for $\mu$ for females and males are:

*[R code 5.45]*
```r
mu_female <- rnorm(1e4,178,20)
mu_male <- rnorm(1e4,178,20) + rnorm(1e4,0,10)
precis( data.frame( mu_female , mu_male ) )
```

```
'data.frame':	10000 obs. of  2 variables:
              mean    sd   5.5%  94.5% histogram
mu_female 178.41 20.04 146.30 209.94   ▁▁▃▇▇▂▁▁
mu_male   177.97 22.40 142.39 214.82  ▁▁▁▃▇▇▂▁▁
```

### PDF page 175 (book page 159)

The prior for males is wider, because it uses both parameters. While in a regression this simple, these priors will wash out very quickly, in general we should be careful. We aren't actually more unsure about male height than female height, *a priori*. Is there another way?

Another approach available to us, using the same information, is to use an index variable instead. An index variable contains integers that correspond to different categories. The integers are just names, but they also let us reference a list of corresponding parameters, one for each category. In this case, we can construct our index like this:

*[R code 5.46]*
```r
d$sex <- ifelse( d$male==1 , 2 , 1 )
str( d$sex )
```

```
 num [1:544] 2 1 1 2 1 2 1 2 1 2 ...
```

Now "1" means female and "2" means male. No order is implied. These are just labels. And the mathematical version of the model becomes:

$$
\begin{aligned}
h_i &\sim \text{Normal}(\mu_i, \sigma) \\
\mu_i &= \alpha_{\text{sex}[i]} \\
\alpha_j &\sim \text{Normal}(178, 20) \qquad \text{, for } j = 1..2 \\
\sigma &\sim \text{Uniform}(0, 50)
\end{aligned}
$$

What this does is create a list of $\alpha$ parameters, one for each unique value in the index variable. So in this case we end up with two $\alpha$ parameters, named $\alpha_1$ and $\alpha_2$. The numbers correspond to the values in the index variable `sex`. I know this seems overly complicated, but it solves our problem with the priors. Now the same prior can be assigned to each, corresponding to the notion that all the categories are the same, prior to the data. Neither category has more prior uncertainty than the other. And as you'll see a bit later, this approach extends really nicely to contexts with more than two categories.

Let's approximate the posterior for the above model, the one using an index variable.

*[R code 5.47]*
```r
m5.8 <- quap(
    alist(
        height ~ dnorm( mu , sigma ) ,
        mu <- a[sex] ,
        a[sex] ~ dnorm( 178 , 20 ) ,
        sigma ~ dunif( 0 , 50 )
    ) , data=d )
precis( m5.8 , depth=2 )
```

```
       mean   sd   5.5%  94.5%
a[1]  134.91 1.61 132.34 137.48
a[2]  142.58 1.70 139.86 145.29
sigma  27.31 0.83  25.98  28.63
```

Note the `depth=2` that I added to `precis`. This tells it to show any vector parameters, like our new a vector. Vector (and matrix) parameters are hidden by `precies` by default, because sometimes there are lots of these and you don't want to inspect their individual values. You'll see what I mean in later chapters.

Interpreting these parameters is easy enough—they are the expected heights in each category. But often we are interested in differences between categories. In this case, what is

### PDF page 176 (book page 160)

the expected difference between females and males? We can compute this using samples from the posterior. In fact, I'll extract posterior samples into a data frame and insert our calculation directly into the same frame:

*[R code 5.48]*
```r
post <- extract.samples(m5.8)
post$diff_fm <- post$a[,1] - post$a[,2]
precis( post , depth=2 )
```

```
quap posterior: 10000 samples from m5.8
          mean   sd   5.5%  94.5%     histogram
sigma    27.29 0.84  25.95  28.63  ▁▁▁▁▃▇▇▇▃▂▁▁▁
a[1]    134.91 1.59 132.37 137.42  ▁▁▁▂▅▇▇▅▂▁▁▁▁
a[2]    142.60 1.71 139.90 145.35     ▁▁▁▅▇▃▁▁▁
diff_fm -7.70 2.33 -11.41  -3.97     ▁▁▁▁▃▇▇▃▁▁▁
```

Our calculation appears at the bottom, as if it were a new parameter in the posterior. This is the expected difference between a female and male in the sample. This kind of calculation is called a contrast. No matter how many categories you have, you can compute the contrast between any two by using samples from the posterior to compute their difference. Then you get the posterior distribution of the difference.

**5.3.2. Many categories.** Binary categories are easy, whether you use an indicator variable or instead an index variable. But when there are more than two categories, the indicator variable approach explodes. You'll need a new indicator variable for each new category. If you have $k$ unique categories, you need $k - 1$ indicator variables. Automated tools like R's `lm` do in fact go this route, constructing $k - 1$ indicator variables for you and returning $k - 1$ parameter estimates.

But we'll instead stick with the index variable approach. It does not change at all when you add more categories. You do get more parameters, of course, just as many as in the indicator variable approach. But the model specification looks just like it does in the binary case. And the priors continue to be easier, unless you really do have prior information about contrasts.

Let's explore an example using the primate milk data again. We're interested now in the `clade` variable, which encodes the broad taxonomic membership of each species:

*[R code 5.49]*
```r
data(milk)
d <- milk
unique(d$clade)
```

```
[1] Strepsirrhine    New World Monkey Old World Monkey Ape            
Levels: Ape New World Monkey Old World Monkey Strepsirrhine
```

We want an index value for each of these four categories. You could do this by hand, but just coercing the factor to an integer will do the job:

*[R code 5.50]*
```r
d$clade_id <- as.integer( d$clade )
```

### PDF page 177 (book page 161)

Let's use a model to measure the average milk energy in each clade. Here's the mathematical version:

$$
\begin{aligned}
K_i &\sim \text{Normal}(\mu_i, \sigma) \\
\mu_i &= \alpha_{\text{CLADE}[i]} \\
\alpha_j &\sim \text{Normal}(0, 0.5) \quad \text{, for } j = 1..4 \\
\sigma &\sim \text{Exponential}(1)
\end{aligned}
$$

Remember, $K$ is the standardized kilocalories. I widened the prior on $\alpha$ a little, to allow the different clades to disperse, if the data wants them to. But I encourage you to play with that prior and repeatedly re-approximate the posterior so you can see how the posterior differences among the categories depend upon it. Firing up `quap` now:

*[margin: R code 5.51]*

```r
d$K <- scale( d$kcal.per.g )
m5.9 <- quap(
    alist(
        K ~ dnorm( mu , sigma ),
        mu <- a[clade_id],
        a[clade_id] ~ dnorm( 0 , 0.5 ),
        sigma ~ dexp( 1 )
    ) , data=d )
labels <- paste( "a[" , 1:4 , "]:" , levels(d$clade) , sep="" )
plot( precis( m5.9 , depth=2 , pars="a" ) , labels=labels ,
    xlab="expected kcal (std)" )
```

*[Figure: an interval (precis) plot with four rows labeled, top to bottom, a[1]:Ape, a[2]:New World Monkey, a[3]:Old World Monkey, a[4]:Strepsirrhine. The x-axis is "expected kcal (std)" with ticks at -1.0, -0.5, 0.0, 0.5, 1.0. Each row shows an open-circle point estimate with a horizontal compatibility-interval bar: Ape (a[1]) is centered near −0.45 and Strepsirrhine (a[4]) near −0.5, both below zero; New World Monkey (a[2]) is near +0.35 and Old World Monkey (a[3]) near +0.65, both above zero.]*

I used the optional `labels` argument to augment the parameter names `a[1]` through `a[4]` with the clade names from the original variable. In practice, you have to be very careful to keep track of which index values go with which categories. Don't trust R's factor variable type to necessarily do things right.

If you have another kind of categorical variable, like diet or habitat, that you'd like to add to the model, the approach is just the same. For example, let's randomly assign these primates to some made up categories: [1] Gryffindor, [2] Hufflepuff, [3] Ravenclaw, and [4] Slytherin.

*[margin: R code 5.52]*

```r
set.seed(63)
d$house <- sample( rep(1:4,each=8) , size=nrow(d) )
```

Now we can include these categories as another predictor in the model:

### PDF page 178 (book page 162)

*[margin: R code 5.53]*

```r
m5.10 <- quap(
    alist(
        K ~ dnorm( mu , sigma ),
        mu <- a[clade_id] + h[house],
        a[clade_id] ~ dnorm( 0 , 0.5 ),
        h[house] ~ dnorm( 0 , 0.5 ),
        sigma ~ dexp( 1 )
    ) , data=d )
```

If you inspect the posterior, you'll see that Slytherin stands out.

**Rethinking: Differences and statistical significance.** A common error in interpretation of parameter estimates is to suppose that because one parameter is sufficiently far from zero—is "significant"—and another parameter is not—is "not significant"—that the difference between the parameters is also significant. This is not necessarily so.[^83] This isn't just an issue for non-Bayesian analysis: If you want to know the distribution of a difference, then you must compute that difference, a *contrast*. It isn't enough to just observe, for example, that a slope among males overlaps a lot with zero while the same slope among females is reliably above zero. You must compute the posterior distribution of the difference in slope between males and females. For example, suppose you have posterior distributions for two parameters, $\beta_f$ and $\beta_m$. $\beta_f$'s mean and standard deviation is $0.15 \pm 0.02$, and $\beta_m$'s is $0.02 \pm 0.10$. So while $\beta_f$ is reliably different from zero ("significant") and $\beta_m$ is not, the difference between the two (assuming they are uncorrelated) is $(0.15 - 0.02) \pm \sqrt{0.02^2 + 0.1^2} \approx 0.13 \pm 0.10$. The distribution of the difference overlaps a lot with zero. In other words, you can be confident that $\beta_f$ is far from zero, but you cannot be sure that the difference between $\beta_f$ and $\beta_m$ is far from zero.

In the context of non-Bayesian significance testing, this phenomenon arises from the fact that statistical significance is inferentially powerful in one way: difference from the null. When $\beta_m$ overlaps with zero, it may also overlap with values very far from zero. Its value is uncertain. So when you then compare $\beta_m$ to $\beta_f$, that comparison is also uncertain, manifesting in the width of the posterior distribution of the difference $\beta_f - \beta_m$. Lurking underneath this example is a more fundamental mistake in interpreting statistical significance: The mistake of accepting the null hypothesis. Whenever an article or book says something like "we found no difference" or "no effect," this usually means that some parameter was not significantly different from zero, and so the authors adopted zero as the estimate. This is both illogical and extremely common.

**5.4. Summary**

This chapter introduced multiple regression, a way of constructing descriptive models for how the mean of a measurement is associated with more than one predictor variable. The defining question of multiple regression is: *What is the value of knowing each predictor, once we already know the other predictors?* Implicit in this question are: (1) a focus on the value of the predictors for description of the sample, instead of forecasting a future sample; and (2) the assumption that the value of each predictor does not depend upon the values of the other predictors. In later chapters, we confront these two issues. But before that, in the next chapter we'll see how adding predictor variables can create as many problems as it can solve.

**5.5. Practice**

**Easy.**

[^83]: (Endnote reference 83; note text appears in the book's endnotes section.)

### PDF page 179 (book page 163)

**5E1.** Which of the linear models below are multiple linear regressions?

(1) $\mu_i = \alpha + \beta x_i$  
(2) $\mu_i = \beta_x x_i + \beta_z z_i$  
(3) $\mu_i = \alpha + \beta(x_i - z_i)$  
(4) $\mu_i = \alpha + \beta_x x_i + \beta_z z_i$

**5E2.** Write down a multiple regression to evaluate the claim: *Animal diversity is linearly related to latitude, but only after controlling for plant diversity.* You just need to write down the model definition.

**5E3.** Write down a multiple regression to evaluate the claim: *Neither amount of funding nor size of laboratory is by itself a good predictor of time to PhD degree; but together these variables are both positively associated with time to degree.* Write down the model definition and indicate which side of zero each slope parameter should be on.

**5E4.** Suppose you have a single categorical predictor with 4 levels (unique values), labeled A, B, C and D. Let $A_i$ be an indicator variable that is 1 where case $i$ is in category $A$. Also suppose $B_i$, $C_i$, and $D_i$ for the other categories. Now which of the following linear models are inferentially equivalent ways to include the categorical variable in a regression? Models are inferentially equivalent when it's possible to compute one posterior distribution from the posterior distribution of another model.

(1) $\mu_i = \alpha + \beta_A A_i + \beta_B B_i + \beta_D D_i$  
(2) $\mu_i = \alpha + \beta_A A_i + \beta_B B_i + \beta_C C_i + \beta_D D_i$  
(3) $\mu_i = \alpha + \beta_B B_i + \beta_C C_i + \beta_D D_i$  
(4) $\mu_i = \alpha_A A_i + \alpha_B B_i + \alpha_C C_i + \alpha_D D_i$  
(5) $\mu_i = \alpha_A(1 - B_i - C_i - D_i) + \alpha_B B_i + \alpha_C C_i + \alpha_D D_i$

**Medium.**

**5M1.** Invent your own example of a spurious correlation. An outcome variable should be correlated with both predictor variables. But when both predictors are entered in the same model, the correlation between the outcome and one of the predictors should mostly vanish (or at least be greatly reduced).

**5M2.** Invent your own example of a masked relationship. An outcome variable should be correlated with both predictor variables, but in opposite directions. And the two predictor variables should be correlated with one another.

**5M3.** It is sometimes observed that the best predictor of fire risk is the presence of firefighters— States and localities with many firefighters also have more fires. Presumably firefighters do not *cause* fires. Nevertheless, this is not a spurious correlation. Instead fires cause firefighters. Consider the same reversal of causal inference in the context of the divorce and marriage data. How might a high divorce rate cause a higher marriage rate? Can you think of a way to evaluate this relationship, using multiple regression?

**5M4.** In the divorce data, States with high numbers of Mormons (members of The Church of Jesus Christ of Latter-day Saints, LDS) have much lower divorce rates than the regression models expected. Find a list of LDS population by State and use those numbers as a predictor variable, predicting divorce rate using marriage rate, median age at marriage, and percent LDS population (possibly standardized). You may want to consider transformations of the raw percent LDS variable.

### PDF page 180 (book page 164)

**5M5.** One way to reason through multiple causation hypotheses is to imagine detailed mechanisms through which predictor variables may influence outcomes. For example, it is sometimes argued that the price of gasoline (predictor variable) is positively associated with lower obesity rates (outcome variable). However, there are at least two important mechanisms by which the price of gas could reduce obesity. First, it could lead to less driving and therefore more exercise. Second, it could lead to less driving, which leads to less eating out, which leads to less consumption of huge restaurant meals. Can you outline one or more multiple regressions that address these two mechanisms? Assume you can have any predictor data you need.

**Hard.** All three exercises below use the same data, `data(foxes)` (part of `rethinking`).[^84] The urban fox (*Vulpes vulpes*) is a successful exploiter of human habitat. Since urban foxes move in packs and defend territories, data on habitat quality and population density is also included. The data frame has five columns:

(1) `group`: Number of the social group the individual fox belongs to  
(2) `avgfood`: The average amount of food available in the territory  
(3) `groupsize`: The number of foxes in the social group  
(4) `area`: Size of the territory  
(5) `weight`: Body weight of the individual fox

**5H1.** Fit two bivariate Gaussian regressions, using `quap`: (1) body weight as a linear function of territory size (`area`), and (2) body weight as a linear function of `groupsize`. Plot the results of these regressions, displaying the MAP regression line and the 95% interval of the mean. Is either variable important for predicting fox body weight?

**5H2.** Now fit a multiple linear regression with `weight` as the outcome and both `area` and `groupsize` as predictor variables. Plot the predictions of the model for each predictor, holding the other predictor constant at its mean. What does this model say about the importance of each variable? Why do you get different results than you got in the exercise just above?

**5H3.** Finally, consider the `avgfood` variable. Fit two more multiple regressions: (1) body weight as an additive function of `avgfood` and `groupsize`, and (2) body weight as an additive function of all three variables, `avgfood` and `groupsize` and `area`. Compare the results of these models to the previous models you've fit, in the first two exercises. (a) Is `avgfood` or `area` a better predictor of body weight? If you had to choose one or the other to include in a model, which would it be? Support your assessment with any tables or plots you choose. (b) When both `avgfood` or `area` are in the same model, their effects are reduced (closer to zero) and their standard errors are larger than when they are included in separate models. Can you explain this result?

[^84]: (Endnote reference 84; note text appears in the book's endnotes section.)
