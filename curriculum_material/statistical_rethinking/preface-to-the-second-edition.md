# Preface to the Second Edition
*(PDF pages 7–8; book pages xi–xii)*

### PDF page 7 (book page xi)

# Preface to the Second Edition

It came as a complete surprise to me that I wrote a statistics book. It is even more surprising how popular the book has become. But I had set out to write the statistics book that I wish I could have had in graduate school. No one should have to learn this stuff the way I did. I am glad there is an audience to benefit from the book.

It consumed 5 years to write it. There was an initial set of course notes, melted down and hammered into a first 200 page manuscript. I discarded that first manuscript. But it taught me the outline of the book I really wanted to write. Then several years of teaching with the manuscript further refined it.

Really I could have continued refining it every year. Going to press carries the penalty of freezing a dynamic process of both learning how to teach the material and keeping up with changes in the material. As time goes on, I see more elements of the book that I wish I had done differently. I’ve also received a lot of feedback on the book, and that feedback has given me ideas for improving it.

So in the second edition, I put those ideas into action. The goal with a second edition is only to refine the strategy that made the first edition a success. The major changes are:

**The R package has some new tools.** The `map` tool from the first edition is still here, but now it is named `quap`. This renaming is just to avoid misunderstanding. We just used it to get a quadratic approximation to the posterior. So now is named as such [sic]. A bigger change is that `map2stan` has been replaced by `ulam`. The new `ulam` is very similar to `map2stan`, and in many cases can be used identically. But it is also much more flexible, mainly because it does not make any assumptions about GLM structure and allows explicit variable types within the formula list. All the `map2stan` code is still in the package and will continue to work. But now `ulam` allows for much more, especially in later chapters. Both of these tools allow sampling from the prior distribution, using `extract.prior`, as well as the posterior. This helps with the next change.

**Much more prior predictive simulation.** A prior predictive simulation means simulating predictions from a model, using only the prior distribution instead of the posterior distribution. This is very useful for understanding the implications of a prior. There was only a vestigial amount of this in the first edition. Now most modeling examples have some prior predictive simulation. I think this is most useful addition to the second edition [sic], since it helps so much with understanding not only priors but also the model itself.

**More emphasis on the distinction between prediction and inference.** Chapter 5, the chapter on multiple regression, has been split into two chapters. The first chapter focuses on helpful aspects of regression. The second focuses on ways that it can mislead. This allows as

### PDF page 8 (book page xii)

well a more direct discussion of causal inference. This means that DAGs—directed acyclic graphs—make an appearance. The chapter on overfitting, Chapter 7 now, is also more direct in cautioning about the predictive nature of information criteria and cross-validation. Cross-validation and importance sampling approximations of it (PSIS-LOO) are now discussed explicitly.

**Now model types.** Chapter 4 now ends with B-splines. The chapter on count models, Chapter 11, now includes an item-response (factor analytic) example. Chapter 12 contains a survival analysis with censoring. Chapter 14 has an example of a phylogenetic distance regression. And there is an entirely new chapter, Chapter 16, that focuses on models that are not easily conceived of as GLMMs.

**Some new data examples.** There are some new data examples, such as the Japanese cherry blossoms historical time series and a larger primate evolution data set with 300 species and a matching phylogeny.

**More presentation of raw Stan models.** There are several places now where raw Stan model code is explained, inside optional boxes. I hope this makes a transition to working directly in Stan easier. But the main text remains R script, using the `rethinking` package’s teaching tools.

**Kindness and persistence.** As in the first edition, I have tried to make the material as kind as possible. None of this stuff is easy, and the journey into understanding is long and haunted. It is important that readers expect that confusion and partial understanding are normal. This is also the reason that I have not changed the basic modeling strategy in the book.

First, I force the reader to explicitly specify every assumption of the model. Some readers of the first edition lobbied me to use simplified formula tools like `brms` or `rstanarm`. Those are fantastic packages, and graduating to use them after this book is recommended. But I don’t see how a person can come to understand the model when using those tools. The priors being hidden isn’t the most limiting part. Instead, since linear model formulas like `y ~ (1|x) + z` don’t show the parameters, nor even all of the terms, it is not easy to see how the mathematical model relates to the code. It is ultimately kinder to be a bit cruel and require more work. So the formula lists remain. In this book, you are programming the log-posterior, down to the exact relationship between each variable and coefficient. You’ll thank me later.

Second, half the book goes by before MCMC appears. Some readers of the first edition wanted me to start instead with MCMC. I do not do this because Bayes is not about MCMC. We seek the posterior distribution, but there are many legitimate approximations of it, and MCMC is just one set of strategies. Using quadratic approximation in the first half also allows a clearer tie to non-Bayesian algorithms. And since finding the quadratic approximation is fast, it means readers don’t have to struggle with too many things at once. Again, it is about being kind.

Richard McElreath  
Leipzig, 10 August 2019
