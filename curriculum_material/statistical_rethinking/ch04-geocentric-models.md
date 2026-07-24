# Chapter 4 — Geocentric Models
*(PDF pages 89–142; book pages 73–85)*

*⚠ In progress: 13 of 54 pages transcribed; missing PDF pages 102–142.*

### PDF page 89 (book page 73)

# Chapter 4 — Geocentric Models

History has been unkind to Ptolemy. Claudius Ptolemy (born 90 CE, died 168 CE) was an Egyptian mathematician and astronomer, most famous for his geocentric model of the solar system. These days, when scientists wish to mock someone, they might compare him to a supporter of the geocentric model. But Ptolemy was a genius. His mathematical model of the motions of the planets (Figure 4.1) was extremely accurate. To achieve its accuracy, it employed a device known as an *epicycle*, a circle on a circle. It is even possible to have epi-epicycles, circles on circles on circles. With enough epicycles in the right places, Ptolemy's model could predict with accuracy greater than anyone had achieved before him. And so the model was utilized for over a thousand years. And Ptolemy and people like him, toiling over centuries, worked it all out without the aid of a computer. Anyone should be flattered to be compared to Ptolemy.

The trouble of course is that the geocentric model is wrong, in many respects. If you used it to plot the path of your Mars probe, you'd miss the red planet by quite a distance. But for spotting Mars in the night sky, it remains an excellent model. It would have to be re-calibrated every century or so, depending upon which heavenly body you wish to locate. But the geocentric model continues to make useful predictions, provided those predictions remain within a narrow domain of questioning.

The strategy of using epicycles might seem crazy, once you know the correct structure of the solar system. But it turns out that the ancients had hit upon a generalized system of approximation. Given enough circles embedded in enough places, the Ptolemaic strategy is the same as a *Fourier series*, a way of decomposing a periodic function (like an orbit) into a series of sine and cosine functions. So no matter the actual arrangement of planets and moons, a geocentric model can be built to describe their paths against the night sky.

**Linear regression** is the geocentric model of applied statistics. By "linear regression," we will mean a family of simple statistical golems that attempt to learn about the mean and variance of some measurement, using an additive combination of other measurements. Like geocentrism, linear regression can usefully describe a very large variety of natural phenomena. Like geocentrism, linear regression is a descriptive model that corresponds to many different process models. If we read its structure too literally, we're likely to make mistakes. But used wisely, these little linear golems continue to be useful.

This chapter introduces linear regression as a Bayesian procedure. Under a probability interpretation, which is necessary for Bayesian work, linear regression uses a Gaussian (normal) distribution to describe our golem's uncertainty about some measurement of interest. This type of model is simple, flexible, and commonplace. Like all statistical models, it is not universally useful. But linear regression has a strong claim to being foundational, in the

### PDF page 90 (book page 74)

**FIGURE 4.1.** The Ptolemaic Universe, in which complex motion of the planets in the night sky was explained by orbits within orbits, called *epicycles*. The model is incredibly wrong, yet makes quite good predictions. *[Figure: a schematic line diagram of the Ptolemaic system. A large dotted circle — the orbit itself — is drawn around a center marked by a small open circle; the Earth, drawn as a small globe icon and labeled "Earth", sits just to the left of that center, and a solid black dot labeled *equant* sits just to its right. A straight line runs from the center up to a filled dot on the upper part of the large circle; that dot is the center of a smaller dotted circle labeled *epicycle*, on which rides an open circle labeled "planet" (arrows indicate the planet's motion around the epicycle and the epicycle's motion along the large circle). An arrow from the lower right points up at the large dotted circle with the label *deferent*. A heavy dashed curve traces the resulting looping (retrograde) path of the planet, spiraling through a small loop at the left and continuing off toward the lower left, where it ends in an arrowhead.]*

sense that once you learn to build and interpret linear regression models, you can more easily move on to other types of regression which are less normal.

**4.1. Why normal distributions are normal**

Suppose you and a thousand of your closest friends line up on the halfway line of a soccer field (football pitch). Each of you has a coin in your hand. At the sound of the whistle, you begin flipping the coins. Each time a coin comes up heads, that person moves one step towards the left-hand goal. Each time a coin comes up tails, that person moves one step towards the right-hand goal. Each person flips the coin 16 times, follows the implied moves, and then stands still. Now we measure the distance of each person from the halfway line. Can you predict what proportion of the thousand people who are standing on the halfway line? How about the proportion 5 yards left of the line?

It's hard to say where any individual person will end up, but you can say with great confidence what the collection of positions will be. The distances will be distributed in approximately normal, or Gaussian, fashion. This is true even though the underlying distribution is binomial. It does this because there are so many more possible ways to realize a sequence of left-right steps that sums to zero. There are slightly fewer ways to realize a sequence that ends up one step left or right of zero, and so on, with the number of possible sequences declining in the characteristic bell curve of the normal distribution.

**4.1.1. Normal by addition.** Let's see this result, by simulating this experiment in R. To show that there's nothing special about the underlying coin flip, assume instead that each step is different from all the others, a random distance between zero and one yard. Thus a coin is flipped, a distance between zero and one yard is taken in the indicated direction, and the process repeats. To simulate this, we generate for each person a list of 16 random numbers between −1 and 1. These are the individual steps. Then we add these steps together to get the position after 16 steps. Then we need to replicate this procedure 1000 times. This is the sort of task that would be harrowing in a point-and-click interface, but it is made trivial by the command line. Here's a single line to do the whole thing:

### PDF page 91 (book page 75)

**FIGURE 4.2.** Random walks on the soccer field converge to a normal distribution. The more steps are taken, the closer the match between the real empirical distribution of positions and the ideal normal distribution, superimposed in the last plot in the bottom panel. *[Figure: a two-part figure. Top panel: a line plot of position (vertical axis, ticks at −6, −3, 0, 3, 6) against step number (horizontal axis, ticks at 0, 4, 8, 12, 16), showing 100 light-blue random-walk trajectories all starting at position 0 and fanning out into a widening band as the step number grows; one trajectory is highlighted in black, drifting downward to about −5 by step 16. Three vertical dashed lines mark steps 4, 8, and 16. Bottom panel: three density plots, each with position on the horizontal axis (ticks at −6, −3, 0, 3, 6) and Density on the vertical axis. Left, titled "4 steps" (Density ticks 0.0, 0.1, 0.2, 0.3): a jagged blue density, roughly bell-shaped but visibly irregular and slightly flat-topped, spanning about −4 to 4. Middle, titled "8 steps" (Density ticks 0.00, 0.10, 0.20): a jagged blue density, wider and more bell-like, spanning about −6 to 6. Right, titled "16 steps" (Density ticks 0.00, 0.10, 0.20): a jagged blue density with a smooth black normal curve superimposed on it, the two matching closely across the range −6 to 6.]*

**R code 4.1**

```r
pos <- replicate( 1000 , sum( runif(16,-1,1) ) )
```

You can plot the distribution of final positions in a number of different ways, including `hist(pos)` and `plot(density(pos))`. In FIGURE 4.2, I show the result of these random walks and how their distribution evolves as the number of steps increases. The top panel plots 100 different, independent random walks, with one highlighted in black. The vertical dashes indicate the locations corresponding to the distribution plots underneath, measured after 4, 8, and 16 steps. Although the distribution of positions starts off seemingly idiosyncratic, after 16 steps, it has already taken on a familiar outline. The familiar "bell" curve of the Gaussian distribution is emerging from the randomness. Go ahead and experiment with even larger numbers of steps to verify for yourself that the distribution of positions is stabilizing on the Gaussian. You can square the step sizes and transform them in a number of arbitrary ways, without changing the result: Normality emerges. Where does it come from?

Any process that adds together random values from the same distribution converges to a normal. But it's not easy to grasp why addition should result in a bell curve of sums.64 Here's a conceptual way to think of the process. Whatever the average value of the source distribution, each sample from it can be thought of as a fluctuation from that average value. When we begin to add these fluctuations together, they also begin to cancel one another out. A large positive fluctuation will cancel a large negative one. The more terms in the sum, the more chances for each fluctuation to be canceled by another, or by a series of smaller ones in the opposite direction. So eventually the most likely sum, in the sense that there are the

### PDF page 92 (book page 76)

most ways to realize it, will be a sum in which every fluctuation is canceled by another, a sum of zero (relative to the mean).65

It doesn't matter what shape the underlying distribution possesses. It could be uniform, like in our example above, or it could be (nearly) anything else.66 Depending upon the underlying distribution, the convergence might be slow, but it will be inevitable. Often, as in this example, convergence is rapid.

**4.1.2. Normal by multiplication.** Here's another way to get a normal distribution. Suppose the growth rate of an organism is influenced by a dozen loci, each with several alleles that code for more growth. Suppose also that all of these loci interact with one another, such that each increase growth by a percentage. This means that their effects multiply, rather than add. For example, we can sample a random growth rate for this example with this line of code:

**R code 4.2**

```r
prod( 1 + runif(12,0,0.1) )
```

This code just samples 12 random numbers between 1.0 and 1.1, each representing a proportional increase in growth. Thus 1.0 means no additional growth and 1.1 means a 10% increase. The product of all 12 is computed and returned as output. Now what distribution do you think these random products will take? Let's generate 10,000 of them and see:

**R code 4.3**

```r
growth <- replicate( 10000 , prod( 1 + runif(12,0,0.1) ) )
dens( growth , norm.comp=TRUE )
```

The reader should execute this code in R and see that the distribution is approximately normal again. I said normal distributions arise from summing random fluctuations, which is true. But the effect at each locus was multiplied by the effects at all the others, not added. So what's going on here?

We again get convergence towards a normal distribution, because the effect at each locus is quite small. Multiplying small numbers is approximately the same as addition. For example, if there are two loci with alleles increasing growth by 10% each, the product is:

$$1.1 \times 1.1 = 1.21$$

We could also approximate this product by just adding the increases, and be off by only 0.01:

$$1.1 \times 1.1 = (1 + 0.1)(1 + 0.1) = 1 + 0.2 + 0.01 \approx 1.2$$

The smaller the effect of each locus, the better this additive approximation will be. In this way, small effects that multiply together are approximately additive, and so they also tend to stabilize on Gaussian distributions. Verify this for yourself by comparing:

**R code 4.4**

```r
big <- replicate( 10000 , prod( 1 + runif(12,0,0.5) ) )
small <- replicate( 10000 , prod( 1 + runif(12,0,0.01) ) )
```

The interacting growth deviations, as long as they are sufficiently small, converge to a Gaussian distribution. In this way, the range of causal forces that tend towards Gaussian distributions extends well beyond purely additive interactions.

### PDF page 93 (book page 77)

**4.1.3. Normal by log-multiplication.** But wait, there’s more. Large deviates that are multiplied together do not produce Gaussian distributions, but they do tend to produce Gaussian distributions on the log scale. For example:

**R code 4.5**

```r
log.big <- replicate( 10000 , log(prod(1 + runif(12,0,0.5))) )
```

Yet another Gaussian distribution. We get the Gaussian distribution back, because adding logs is equivalent to multiplying the original numbers. So even multiplicative interactions of large deviations can produce Gaussian distributions, once we measure the outcomes on the log scale. Since measurement scales are arbitrary, there’s nothing suspicious about this transformation. After all, it’s natural to measure sound and earthquakes and even information (Chapter 7) on a log scale.

**4.1.4. Using Gaussian distributions.** We’re going to spend the rest of this chapter using the Gaussian distribution as a skeleton for our hypotheses, building up models of measurements as aggregations of normal distributions. The justifications for using the Gaussian distribution fall into two broad categories: (1) ontological and (2) epistemological.

**4.1.4.1.** *Ontological justification.* The world is full of Gaussian distributions, approximately. As a mathematical idealization, we’re never going to experience a perfect Gaussian distribution. But it is a widespread pattern, appearing again and again at different scales and in different domains. Measurement errors, variations in growth, and the velocities of molecules all tend towards Gaussian distributions. These processes do this because at their heart, these processes add together fluctuations. And repeatedly adding finite fluctuations results in a distribution of sums that have shed all information about the underlying process, aside from mean and spread.

One consequence of this is that statistical models based on Gaussian distributions cannot reliably identify micro-process. This recalls the modeling philosophy from Chapter 1 (page 6). But it also means that these models can do useful work, even when they cannot identify process. If we had to know the development biology of height before we could build a statistical model of height, human biology would be sunk.

There are many other patterns in nature, so make no mistake in assuming that the Gaussian pattern is universal. In later chapters, we’ll see how other useful and common patterns, like the exponential and gamma and Poisson, also arise from natural processes. The Gaussian is a member of a family of fundamental natural distributions known as the EXPONENTIAL FAMILY. All of the members of this family are important for working science, because they populate our world.

**4.1.4.2.** *Epistemological justification.* But the natural occurrence of the Gaussian distribution is only one reason to build models around it. Another route to justifying the Gaussian as our choice of skeleton, and a route that will help us appreciate later why it is often a poor choice, is that it represents a particular state of ignorance. When all we know or are willing to say about a distribution of measures (measures are continuous values on the real number line) is their mean and variance, then the Gaussian distribution arises as the most consistent with our assumptions.

That is to say that the Gaussian distribution is the most natural expression of our state of ignorance, because if all we are willing to assume is that a measure has finite variance, the Gaussian distribution is the shape that can be realized in the largest number of ways and does not introduce any new assumptions. It is the least surprising and least informative

### PDF page 94 (book page 78)

assumption to make. In this way, the Gaussian is the distribution most consistent with our assumptions. Or rather, it is the most consistent with our golem’s assumptions. If you don’t think the distribution should be Gaussian, then that implies that you know something else that you should tell your golem about, something that would improve inference.

This epistemological justification is premised on INFORMATION THEORY and MAXIMUM ENTROPY. We’ll dwell on information theory in Chapter 7 and maximum entropy in Chapter 10. Then in later chapters, other common and useful distributions will be used to build *generalized linear models* (GLMs). When these other distributions are introduced, you’ll learn the constraints that make them the uniquely most appropriate (consistent with our assumptions) distributions.

For now, let’s take the ontological and epistemological justifications of just the Gaussian distribution as reasons to start building models of measures around it. Throughout all of this modeling, keep in mind that using a model is not equivalent to swearing an oath to it. The golem is your servant, not the other way around. Later on, we will see good reasons not to use Gaussian distributions.

> **Rethinking: Heavy tails.** The Gaussian distribution is very common in nature and has some nice statistical properties as well. But there are some risks in using it as a default data model. The extreme ends of a distribution are known as its tails. And the Gaussian distribution has some very thin tails—there is very little probability in them. Instead most of the mass in the Gaussian lies within one standard deviation of the mean. Many natural (and unnatural) processes have much heavier tails. These processes have much higher probabilities of producing extreme events. A real and important example is financial time series—the ups and downs of a stock market can look Gaussian in the short term, but over medium and long periods, extreme shocks make the Gaussian model (and anyone who uses it) look foolish.67 Historical time series may behave similarly, and any inference for example of trends in warfare are prone to heavy-tailed surprises.68 We’ll consider alternatives to the Gaussian later.

> **Overthinking: Gaussian distribution.** You don’t have to memorize the Gaussian probability distribution formula to make good use of it. You’re [sic] computer already knows it. But a little knowledge of its form can help demystify it. The probability *density* (see below) of some value $y$, given a Gaussian (normal) distribution with mean $\mu$ and standard deviation $\sigma$, is:
>
> $$
> p(y \mid \mu, \sigma) =
> \frac{1}{\sqrt{2\pi\sigma^2}}
> \exp\left(-\frac{(y-\mu)^2}{2\sigma^2}\right)
> $$
>
> This looks monstrous. But the important bit is just the $(y-\mu)^2$ bit. This is the part that gives the normal distribution its fundamental shape, a quadratic shape. Once you exponentiate the quadratic shape, you get the classic bell curve. The rest of it just scales and standardizes the distribution so that it sums to one, as all probability distributions must. But an expression as simple as $\exp(-y^2)$ yields the Gaussian prototype. Try it in R: `curve( exp( -x^2 ) , from=-3 , to=3 )`.
>
> The Gaussian is a continuous distribution, unlike the discrete distributions of earlier chapters. This means that the value $y$ in the Gaussian distribution can be any continuous value. The binomial, in contrast, requires integers. Probability distributions with only discrete outcomes, like the binomial, are called *probability mass functions* and denoted $\Pr$. Continuous ones like the Gaussian are called *probability density functions*, denoted with $p$ or just plain old $f$, depending upon author and tradition. For mathematical reasons, probability densities, but not masses, can be greater than 1. Try `dnorm(0,0,0.1)`, for example, which is the way to make R calculate $p(0 \mid 0, 0.1)$. The answer, about

### PDF page 95 (book page 79)

> 4, is no mistake. Probability *density* is the rate of change in cumulative probability. So where cumulative probability is increasing rapidly, density can easily exceed 1. But if we calculate the area under the density function, it will never exceed 1. Such areas are also called *probability mass*.
>
> You can usually ignore all these density/mass details while doing computational work. In the conceptual parts of this book, I’ll treat them identically. But it’s good to be aware of the distinction. Sometimes the difference matters.
>
> The Gaussian distribution is routinely seen without $\sigma$ but with another parameter, $\tau$. The parameter $\tau$ in this context is usually called *precision* and defined as $\tau = 1/\sigma^2$. When $\sigma$ is large, $\tau$ is small. This change of parameters gives us the equivalent formula (just substitute $\sigma = 1/\sqrt{\tau}$):
>
> $$
> p(y \mid \mu, \tau) =
> \sqrt{\frac{\tau}{2\pi}}
> \exp\left(-\frac{1}{2}\tau(y-\mu)^2\right)
> $$
>
> This form is common in Bayesian data analysis, and Bayesian model fitting software, such as BUGS or JAGS, sometimes requires using $\tau$ rather than $\sigma$.

**4.2. A language for describing models**

This book adopts a standard language for describing and coding statistical models. You find this language in many statistical texts and in nearly all statistical journals, as it is general to both Bayesian and non-Bayesian modeling. Scientists increasingly use this same language to describe their statistical methods, as well. So learning this language is an investment, no matter where you are headed next.

Here’s the approach, in abstract. There will be many examples later, but it is important to get the general recipe before seeing these.

1. First, we recognize a set of variables that we wish to understand. Some of these variables are observable. We call these *data*. Others are unobservable things like rates and averages. We call these *parameters*.

2. For each variable, we define it either in terms of the other variables or in terms of a probability distribution. These definitions make it possible to learn about associations between variables.

3. The combination of variables and their probability distributions defines a *joint generative model* that can be used both to simulate hypothetical observations as well as analyze real ones.

This outline applies to models in every field, from astronomy to art history. The biggest difficulty usually lies in the subject matter—which variables matter and how does theory tell us to connect them?—not in the mathematics.

After all these decisions are made—and most of them will come to seem automatic to you before long—we summarize the model with something mathy like:

$$
\begin{aligned}
y_i &\sim \text{Normal}(\mu_i, \sigma)\\
\mu_i &= \beta x_i\\
\beta &\sim \text{Normal}(0, 10)\\
\sigma &\sim \text{Exponential}(1)\\
x_i &\sim \text{Normal}(0, 1)
\end{aligned}
$$

If that doesn’t make much sense, good. That indicates that you are holding the right textbook, since this book teaches you how to read and write these mathematical model descriptions.

### PDF page 96 (book page 80)

We won’t do any mathematical manipulation of them. Instead, they provide an unambiguous way to define and communicate our models. Once you get comfortable with their grammar, when you start reading these mathematical descriptions in other books or in scientific journals, you’ll find them less obtuse.

The approach above surely isn’t the only way to describe statistical modeling, but it is a widespread and productive language. Once a scientist learns this language, it becomes easier to communicate the assumptions of our models. We no longer have to remember seemingly arbitrary lists of bizarre conditions like *homoscedasticity* (constant variance), because we can just read these conditions from the model definitions. We will also be able to see natural ways to change these assumptions, instead of feeling trapped within some procrustean model type, like regression or multiple regression or ANOVA or ANCOVA or such. These are all the same kind of model, and that fact becomes obvious once we know how to talk about models as mappings of one set of variables through a probability distribution onto another set of variables. Fundamentally, these models define the ways values of some variables can arise, given values of other variables (Chapter 2).

**4.2.1. Re-describing the globe tossing model.** It’s good to work with examples. Recall the proportion of water problem from previous chapters. The model in that case was always:

$$W \sim \text{Binomial}(N, p)$$

$$p \sim \text{Uniform}(0, 1)$$

where $W$ was the observed count of water, $N$ was the total number of tosses, and $p$ was the proportion of water on the globe. Read the above statement as:

> The count $W$ is distributed binomially with sample size $N$ and probability $p$.
> The prior for $p$ is assumed to be uniform between zero and one.

Once we know the model in this way, we automatically know all of its assumptions. We know the binomial distribution assumes that each sample (globe toss) is independent of the others, and so we also know that the model assumes that sample points are independent of one another.

For now, we’ll focus on simple models like the above. In these models, the first line defines the likelihood function used in Bayes’ theorem. The other lines define priors. Both of the lines in this model are STOCHASTIC, as indicated by the $\sim$ symbol. A stochastic relationship is just a mapping of a variable or parameter onto a distribution. It is *stochastic* because no single instance of the variable on the left is known with certainty. Instead, the mapping is probabilistic: Some values are more plausible than others, but very many different values are plausible under any model. Later, we’ll have models with deterministic definitions in them as well.

> **Overthinking: From model definition to Bayes’ theorem.** To relate the mathematical format above to Bayes’ theorem, you could use the model definition to define the posterior distribution:
>
> $$\Pr(p|w, n) = \frac{\text{Binomial}(w|n, p)\text{Uniform}(p|0, 1)}{\int \text{Binomial}(w|n, p)\text{Uniform}(p|0, 1)dp}$$
>
> That monstrous denominator is just the average likelihood again. It standardizes the posterior to sum to 1. The action is in the numerator, where the posterior probability of any particular value of $p$ is seen again to be proportional to the product of the likelihood and prior. In R code form, this is the same grid approximation calculation you’ve been using all along. In a form recognizable as the above expression:

### PDF page 97 (book page 81)

> **R code 4.6**
>
> ```r
> w <- 6; n <- 9;
> p_grid <- seq(from=0,to=1,length.out=100)
> posterior <- dbinom(w,n,p_grid)*dunif(p_grid,0,1)
> posterior <- posterior/sum(posterior)
> ```
>
> Compare to the calculations in earlier chapters.

**4.3. Gaussian model of height**

Let’s build a linear regression model now. Well, it’ll be a “regression” once we have a predictor variable in it. For now, we’ll get the scaffold in place and construct the predictor variable in the next section.

We’ll work through this material by using real sets of data. In this case, we want a single measurement variable to model as a Gaussian distribution. There will be two parameters describing the distribution’s shape, the mean $\mu$ and the standard deviation $\sigma$. Bayesian updating will allow us to consider every possible combination of values for $\mu$ and $\sigma$ and to score each combination by its relative plausibility, in light of the data. These relative plausibilities are the posterior probabilities of each combination of values $\mu, \sigma$.

Another way to say the above is this. There are an infinite number of possible Gaussian distributions. Some have small means. Others have large means. Some are wide, with a large $\sigma$. Others are narrow. We want our Bayesian machine to consider every possible distribution, each defined by a combination of $\mu$ and $\sigma$, and rank them by posterior plausibility. Posterior plausibility provides a measure of the logical compatibility of each possible distribution with the data and model.

In practice we’ll use approximations to the formal analysis. So we won’t really consider every possible value of $\mu$ and $\sigma$. But that won’t cost us anything in most cases. Instead the thing to worry about is keeping in mind that the “estimate” here will be the entire posterior distribution, not any point within it. And as a result, the posterior distribution will be a distribution of Gaussian distributions. Yes, a distribution of distributions. If that doesn’t make sense yet, then that just means you are being honest with yourself. Hold on, work hard, and it will make plenty of sense before long.

**4.3.1. The data.** The data contained in `data(Howell1)` are partial census data for the Dobe area !Kung San, compiled from interviews conducted by Nancy Howell in the late 1960s.69 For the non-anthropologists reading along, the !Kung San are the most famous foraging population of the 20th century, largely because of detailed quantitative studies by people like Howell.

Load the data and place them into a convenient object with:

**R code 4.7**

```r
library(rethinking)
data(Howell1)
d <- Howell1
```

What you have now is a *data frame* named simply `d`. I use the name `d` over and over again in this book to refer to the data frame we are working with at the moment. I keep its name short to save you typing. A *data frame* is a special kind of object in R. It is a table with

### PDF page 98 (book page 82)

named columns, corresponding to variables, and numbered rows, corresponding to individual cases. In this example, the cases are individuals. Inspect the structure of the data frame, the same way you can inspect the structure of any symbol in R:

**R code 4.8**

```r
str( d )
```

```
'data.frame': 544 obs. of  4 variables:
 $ height: num  152 140 137 157 145 ...
 $ weight: num  47.8 36.5 31.9 53 41.3 ...
 $ age   : num  63 63 65 41 51 35 32 27 19 54 ...
 $ male  : int  1 0 0 1 0 1 0 1 0 1 ...
```

We can also use `rethinking`’s `precis` summary function, which we’ll also use to summarize posterior distributions later on:

**R code 4.9**

```r
precis( d )
```

```
'data.frame': 544 obs. of 4 variables:
        mean    sd  5.5%  94.5%     histogram
height 138.26 27.60 81.11 165.74 ▁▁▁▁▁▁▁▂▁▇▇▅▁
weight  35.61 14.72  9.36  54.50 ▁▂▃▂▂▂▂▅▇▇▃▂▁
age     29.34 20.75  1.00  66.13 ▇▅▅▃▅▂▂▁▁
male     0.47  0.50  0.00   1.00 ▇▁▁▁▁▁▁▁▁▇
```

If you cannot see the histograms on your system, use instead `precis(d,hist=FALSE)`. This data frame contains four columns. Each column has 544 entries, so there are 544 individuals in these data. Each individual has a recorded height (centimeters), weight (kilograms), age (years), and “maleness” (0 indicating female and 1 indicating male).

We’re going to work with just the `height` column, for the moment. The column containing the heights is really just a regular old R *vector*, the kind of list we have been working with in many of the code examples. You can access this vector by using its name:

**R code 4.10**

```r
d$height
```

Read the symbol `$` as *extract*, as in *extract the column named* `height` *from the data frame* `d`. All it does is give you the column that follows it.

> **Overthinking: Data frames.** It might seem like this whole data frame thing is kind of annoying, right now. If we’re working with only one column here, why bother with this `d` thing at all? You don’t have to use a data frame, as you can just pass raw vectors to every command we’ll use in this book. But keeping related variables in the same data frame is a huge convenience. Once we have more than one variable, and we wish to model one as a function of the others, you’ll better see the value of the data frame. You won’t have to wait long.
>
> More technically, a data frame is a special kind of `list` in R. So you access the individual variables with the usual list “double bracket” notation, like `d[[1]]` for the first variable or `d[['x']]` for the variable named `x`. Unlike regular lists, however, data frames force all variables to have the same length. That isn’t always a good thing. And that’s why some statistical packages, like the powerful Stan Markov chain sampler (mc-stan.org), accept plain lists of data, rather than proper data frames.

All we want for now are heights of adults in the sample. The reason to filter out non-adults for now is that height is strongly correlated with age, before adulthood. Later in the

### PDF page 99 (book page 83)

chapter, I'll ask you to tackle the age problem. But for now, better to postpone it. You can filter the data frame down to individuals of age 18 or greater with:

**R code 4.11**

```r
d2 <- d[ d$age >= 18 , ]
```

We'll be working with the data frame `d2` now. It should have 352 rows (individuals) in it.

> **Overthinking: Index magic.** The square bracket notation used in the code above is *index* notation. It is very powerful, but also quite compact and confusing. The data frame `d` is a matrix, a rectangular grid of values. You can access any value in the matrix with `d[row,col]`, replacing `row` and `col` with row and column numbers. If `row` or `col` are lists of numbers, then you get more than one row or column. If you leave the spot for `row` or `col` blank, then you get all of whatever you leave blank. For example, `d[ 3 , ]` gives all columns at row 3. Typing `d[,]` just gives you the entire matrix, because it returns all rows and all columns.
>
> So what `d[ d$age >= 18 , ]` does is give you all of the rows in which `d$age` is greater-than-or-equal-to 18. It also gives you all of the columns, because the spot after the comma is blank. The result is stored in `d2`, the new data frame containing only adults. With a little practice, you can use this square bracket index notion [sic] to perform custom searches of your data, much like performing a database query.

**4.3.2. The model.** Our goal is to model these values using a Gaussian distribution. First, go ahead and plot the distribution of heights, with `dens(d2$height)`. These data look rather Gaussian in shape, as is typical of height data. This may be because height is a sum of many small growth factors. As you saw at the start of the chapter, a distribution of sums tends to converge to a Gaussian distribution. Whatever the reason, adult heights from a single population are nearly always approximately normal.

So it's reasonable for the moment to adopt the stance that the model should use a Gaussian distribution for the probability distribution of the data. But be careful about choosing the Gaussian distribution only when the plotted outcome variable looks Gaussian to you. Gawking at the raw data, to try to decide how to model them, is usually not a good idea. The data could be a mixture of different Gaussian distributions, for example, and in that case you won't be able to detect the underlying normality just by eyeballing the outcome distribution. Furthermore, as mentioned earlier in this chapter, the empirical distribution needn't be actually Gaussian in order to justify using a Gaussian probability distribution.

So which Gaussian distribution? There are an infinite number of them, with an infinite number of different means and standard deviations. We're ready to write down the general model and compute the plausibility of each combination of $\mu$ and $\sigma$. To define the heights as normally distributed with a mean $\mu$ and standard deviation $\sigma$, we write:

$$h_i \sim \text{Normal}(\mu, \sigma)$$

In many books you'll see the same model written as $h_i \sim \mathcal{N}(\mu, \sigma)$, which means the same thing. The symbol $h$ refers to the list of heights, and the subscript $i$ means *each individual element of this list*. It is conventional to use $i$ because it stands for *index*. The index $i$ takes on row numbers, and so in this example can take any value from 1 to 352 (the number of heights in `d2$height`). As such, the model above is saying that all the golem knows about each height measurement is defined by the same normal distribution, with mean $\mu$ and standard deviation $\sigma$. Before long, those little $i$'s are going to show up on the right-hand side of the

### PDF page 100 (book page 84)

model definition, and you'll be able to see why we must bother with them. So don't ignore the *i*, even if it seems like useless ornamentation right now.

> **Rethinking: Independent and identically distributed.** The short model above is sometimes described as assuming that the values $h_i$ are *independent and identically distributed*, which may be abbreviated i.i.d., iid, or IID. You might even see the same model written:
>
> $$h_i \stackrel{\text{iid}}{\sim} \text{Normal}(\mu, \sigma).$$
>
> "iid" indicates that each value $h_i$ has the same probability function, independent of the other $h$ values and using the same parameters. A moment's reflection tells us that this is hardly ever true, in a physical sense. Whether measuring the same distance repeatedly or studying a population of heights, it is hard to argue that every measurement is independent of the others. For example, heights within families are correlated because of alleles shared through recent shared ancestry.
>
> The i.i.d. assumption doesn't have to seem awkward, however, as long as you remember that probability is inside the golem, not outside in the world. The i.i.d. assumption is about how the golem represents its uncertainty. It is an *epistemological* assumption. It is not a physical assumption about the world, an *ontological* one, unless you insist that it is. E. T. Jaynes (1922–1998) called this the *mind projection fallacy*, the mistake of confusing epistemological claims with ontological claims.70
>
> The point isn't to say epistemology trumps reality, but rather that in ignorance of such correlations the most conservative distribution to use is i.i.d.71 This issue will return in Chapter 10. Furthermore, there is a mathematical result known as *de Finetti's theorem* that tells us that values which are EXCHANGEABLE can be approximated by mixtures of i.i.d. distributions. Colloquially, exchangeable values can be reordered. The practical impact of this is that "i.i.d." as an assumption cannot be read too literally, as different process models again correspond to the same statistical model (as argued in Chapter 1). Even furthermore, there are many types of correlation that do little or nothing to the overall shape of a distribution, but only affect the precise sequence in which values appear. For example, pairs of sisters have highly correlated heights. But the overall distribution of female height remains almost perfectly normal. In such cases, i.i.d. remains perfectly useful, despite ignoring the correlations. Consider for example that Markov chain Monte Carlo (Chapter 9) can use highly correlated sequential samples to estimate most any iid distribution we like.

To complete the model, we're going to need some priors. The parameters to be estimated are both $\mu$ and $\sigma$, so we need a prior $\Pr(\mu, \sigma)$, the joint prior probability for all parameters. In most cases, priors are specified independently for each parameter, which amounts to assuming $\Pr(\mu, \sigma) = \Pr(\mu) \Pr(\sigma)$. Then we can write:

$$
\begin{aligned}
h_i &\sim \text{Normal}(\mu, \sigma) && \text{[likelihood]}\\
\mu &\sim \text{Normal}(178, 20) && [\mu \text{ prior}]\\
\sigma &\sim \text{Uniform}(0, 50) && [\sigma \text{ prior}]
\end{aligned}
$$

The labels on the right are not part of the model, but instead just notes to help you keep track of the purpose of each line. The prior for $\mu$ is a broad Gaussian prior, centered on 178cm, with 95% of probability between $178 \pm 40$.

Why 178 cm? Your author is 178 cm tall. And the range from 138 cm to 218 cm encompasses a huge range of plausible mean heights for human populations. So domain-specific information has gone into this prior. Everyone knows something about human height and can set a reasonable and vague prior of this kind. But in many regression problems, as you'll see later, using prior information is more subtle, because parameters don't always have such clear physical meaning.

### PDF page 101 (book page 85)

Whatever the prior, it's a very good idea to plot your priors, so you have a sense of the assumption they build into the model. In this case:

**R code 4.12**

```r
curve( dnorm( x , 178 , 20 ) , from=100 , to=250 )
```

Execute that code yourself, to see that the golem is assuming that the average height (not each individual height) is almost certainly between 140 cm and 220 cm. So this prior carries a little information, but not a lot. The $\sigma$ prior is a truly flat prior, a uniform one, that functions just to constrain $\sigma$ to have positive probability between zero and 50cm. View it with:

**R code 4.13**

```r
curve( dunif( x , 0 , 50 ) , from=-10 , to=60 )
```

A standard deviation like $\sigma$ must be positive, so bounding it at zero makes sense. How should we pick the upper bound? In this case, a standard deviation of 50cm would imply that 95% of individual heights lie within 100cm of the average height. That's a very large range.

All this talk is nice, but it'll help to really see what these priors imply about the distribution of individual heights. This is an essential part of your modeling, the PRIOR PREDICTIVE simulation. Once you've chosen priors for $h$, $\mu$, and $\sigma$, these imply a joint prior distribution of individual heights. By simulating from this distribution, you can see what your choices imply about observable height. This helps you diagnose bad choices. Lots of conventional choices are indeed bad ones, and we'll be able to see this by conducting prior predictive simulations.

Okay, so how to do this? You can quickly simulate heights by sampling from the prior, like you sampled from the posterior back in Chapter 3. Remember, every posterior is also potentially a prior for a subsequent analysis, so you can process priors just like posteriors.

**R code 4.14**

```r
sample_mu <- rnorm( 1e4 , 178 , 20 )
sample_sigma <- runif( 1e4 , 0 , 50 )
prior_h <- rnorm( 1e4 , sample_mu , sample_sigma )
dens( prior_h )
```

This density, as well as the individual densities for $\mu$ and $\sigma$, as shown in FIGURE 4.3. It displays a vaguely bell-shaped density with thick tails. It is the expected distribution of heights, averaged over the prior. Notice that the prior probability distribution of height is not itself Gaussian. This is okay. The distribution you see is not an empirical expectation, but rather the distribution of relative plausibilities of different heights, before seeing the data.

Prior predictive simulation is very useful for assigning sensible priors, because it can be quite hard to anticipate how priors influence the observable variables. As an example, consider a much flatter and less informative prior for $\mu$, like $\mu \sim \text{Normal}(178, 100)$. Priors with such large standard deviations are quite common in Bayesian models, but the [sic] are hardly ever sensible. Let's use simulation again to see the implied heights:

**R code 4.15**

```r
sample_mu <- rnorm( 1e4 , 178 , 100 )
prior_h <- rnorm( 1e4 , sample_mu , sample_sigma )
dens( prior_h )
```

The result is displayed in the lower right of FIGURE 4.3. Now the model, before seeing the data, expects 4% of people, those left of the dashed line, to have negative height. It also
