# Chapter 8 — Tree-Based Methods
*(PDF pages 338–373; book pages 331–353)*

*⚠ In progress: 23 of 36 pages transcribed; missing PDF pages 361–373.*

### PDF page 338 (book page 331)

# Chapter 8 — Tree-Based Methods

*[A "Check for updates" badge appears at the top right of the chapter opening page.]*

In this chapter, we describe *tree-based* methods for regression and classification. These involve *stratifying* or *segmenting* the predictor space into a number of simple regions. In order to make a prediction for a given observation, we typically use the mean or the mode response value for the training observations in the region to which it belongs. Since the set of splitting rules used to segment the predictor space can be summarized in a tree, these types of approaches are known as *decision tree* methods.

*[margin: decision tree]*

Tree-based methods are simple and useful for interpretation. However, they typically are not competitive with the best supervised learning approaches, such as those seen in Chapters 6 and 7, in terms of prediction accuracy. Hence in this chapter we also introduce *bagging*, *random forests*, *boosting*, and *Bayesian additive regression trees*. Each of these approaches involves producing multiple trees which are then combined to yield a single consensus prediction. We will see that combining a large number of trees can often result in dramatic improvements in prediction accuracy, at the expense of some loss in interpretation.

**8.1 The Basics of Decision Trees**

Decision trees can be applied to both regression and classification problems. We first consider regression problems, and then move on to classification.

**8.1.1 Regression Trees**

In order to motivate *regression trees*, we begin with a simple example.

*[margin: regression tree]*

© Springer Nature Switzerland AG 2023
G. James et al., *An Introduction to Statistical Learning*, Springer Texts in Statistics,
https://doi.org/10.1007/978-3-031-38747-0_8

### PDF page 339 (book page 332)

**FIGURE 8.1.** *For the* `Hitters` *data, a regression tree for predicting the log salary of a baseball player, based on the number of years that he has played in the major leagues and the number of hits that he made in the previous year. At a given internal node, the label (of the form $X_j < t_k$) indicates the left-hand branch emanating from that split, and the right-hand branch corresponds to $X_j \geq t_k$. For instance, the split at the top of the tree results in two large branches. The left-hand branch corresponds to* `Years<4.5`, *and the right-hand branch corresponds to* `Years>=4.5`. *The tree has two internal nodes and three terminal nodes, or leaves. The number in each leaf is the mean of the response for the observations that fall there.* *[Figure: a green dendrogram-style regression tree. The root split, labeled `Years < 4.5`, sends the left branch down to a terminal leaf labeled 5.11; the right branch descends to a second internal node labeled `Hits < 117.5`, whose left and right branches end in terminal leaves labeled 6.00 and 6.74 respectively.]*

**Predicting Baseball Players' Salaries Using Regression Trees**

We use the `Hitters` data set to predict a baseball player's `Salary` based on `Years` (the number of years that he has played in the major leagues) and `Hits` (the number of hits that he made in the previous year). We first remove observations that are missing `Salary` values, and log-transform `Salary` so that its distribution has more of a typical bell-shape. (Recall that `Salary` is measured in thousands of dollars.)

Figure 8.1 shows a regression tree fit to this data. It consists of a series of splitting rules, starting at the top of the tree. The top split assigns observations having `Years<4.5` to the left branch.[^1] The predicted salary for these players is given by the mean response value for the players in the data set with `Years<4.5`. For such players, the mean log salary is 5.107, and so we make a prediction of $e^{5.107}$ thousands of dollars, i.e. \$165,174, for these players. Players with `Years>=4.5` are assigned to the right branch, and then that group is further subdivided by `Hits`. Overall, the tree stratifies or segments the players into three regions of predictor space: players who have played for four or fewer years, players who have played for five or more years and who made fewer than 118 hits last year, and players who have played for five or more years and who made at least 118 hits last year. These three regions can be written as $R_1 =$ {X | `Years<4.5`}, $R_2 =$ {X | `Years>=4.5`, `Hits<117.5`}, and $R_3 =$ {X | `Years>=4.5`, `Hits>=117.5`}. Figure 8.2 illustrates

[^1]: Both `Years` and `Hits` are integers in these data; the function used to fit this tree labels the splits at the midpoint between two adjacent values.

### PDF page 340 (book page 333)

**FIGURE 8.2.** *The three-region partition for the* `Hitters` *data set from the regression tree illustrated in Figure 8.1.* *[Figure: a scatterplot of the* `Hitters` *data with* `Years` *on the horizontal axis (labeled 1 at the left, 4.5, and 24 at the right) and* `Hits` *on the vertical axis (labeled 1, 117.5, and 238 along the right-hand edge). Orange points are scattered throughout. A green vertical line at* `Years` *= 4.5 splits the plot, and a green horizontal line at* `Hits` *= 117.5 runs from that vertical line to the right edge. The left strip is labeled $R_1$, the lower-right region is labeled $R_2$, and the upper-right region is labeled $R_3$.]*

the regions as a function of `Years` and `Hits`. The predicted salaries for these three groups are \$1,000$\times e^{5.107}$ =\$165,174, \$1,000$\times e^{5.999}$ =\$402,834, and \$1,000$\times e^{6.740}$ =\$845,346 respectively.

In keeping with the *tree* analogy, the regions $R_1$, $R_2$, and $R_3$ are known as *terminal nodes* or *leaves* of the tree. *[margin: terminal node]* *[margin: leaf]* As is the case for Figure 8.1, decision trees are typically drawn *upside down*, in the sense that the leaves are at the bottom of the tree. The points along the tree where the predictor space is split are referred to as *internal nodes*. *[margin: internal node]* In Figure 8.1, the two internal nodes are indicated by the text `Years<4.5` and `Hits<117.5`. We refer to the segments of the trees that connect the nodes as *branches*. *[margin: branch]*

We might interpret the regression tree displayed in Figure 8.1 as follows: `Years` is the most important factor in determining `Salary`, and players with less experience earn lower salaries than more experienced players. Given that a player is less experienced, the number of hits that he made in the previous year seems to play little role in his salary. But among players who have been in the major leagues for five or more years, the number of hits made in the previous year does affect salary, and players who made more hits last year tend to have higher salaries. The regression tree shown in Figure 8.1 is likely an over-simplification of the true relationship between `Hits`, `Years`, and `Salary`. However, it has advantages over other types of regression models (such as those seen in Chapters 3 and 6): it is easier to interpret, and has a nice graphical representation.

**Prediction via Stratification of the Feature Space**

We now discuss the process of building a regression tree. Roughly speaking, there are two steps.

1. We divide the predictor space — that is, the set of possible values for $X_1, X_2, \ldots, X_p$ — into $J$ distinct and non-overlapping regions, $R_1, R_2, \ldots, R_J$.

### PDF page 341 (book page 334)

2. For every observation that falls into the region $R_j$, we make the same prediction, which is simply the mean of the response values for the training observations in $R_j$.

For instance, suppose that in Step 1 we obtain two regions, $R_1$ and $R_2$, and that the response mean of the training observations in the first region is 10, while the response mean of the training observations in the second region is 20. Then for a given observation $X = x$, if $x \in R_1$ we will predict a value of 10, and if $x \in R_2$ we will predict a value of 20.

We now elaborate on Step 1 above. How do we construct the regions $R_1, \ldots, R_J$? In theory, the regions could have any shape. However, we choose to divide the predictor space into high-dimensional rectangles, or *boxes*, for simplicity and for ease of interpretation of the resulting predictive model. The goal is to find boxes $R_1, \ldots, R_J$ that minimize the RSS, given by

$$\sum_{j=1}^{J} \sum_{i \in R_j} (y_i - \hat{y}_{R_j})^2, \tag{8.1}$$

where $\hat{y}_{R_j}$ is the mean response for the training observations within the $j$th box. Unfortunately, it is computationally infeasible to consider every possible partition of the feature space into $J$ boxes. For this reason, we take a *top-down*, *greedy* approach that is known as *recursive binary splitting*. *[margin: recursive binary splitting]* The approach is *top-down* because it begins at the top of the tree (at which point all observations belong to a single region) and then successively splits the predictor space; each split is indicated via two new branches further down on the tree. It is *greedy* because at each step of the tree-building process, the *best* split is made at that particular step, rather than looking ahead and picking a split that will lead to a better tree in some future step.

In order to perform recursive binary splitting, we first select the predictor $X_j$ and the cutpoint $s$ such that splitting the predictor space into the regions $\{X|X_j < s\}$ and $\{X|X_j \geq s\}$ leads to the greatest possible reduction in RSS. (The notation $\{X|X_j < s\}$ means *the region of predictor space in which $X_j$ takes on a value less than $s$*.) That is, we consider all predictors $X_1, \ldots, X_p$, and all possible values of the cutpoint $s$ for each of the predictors, and then choose the predictor and cutpoint such that the resulting tree has the lowest RSS. In greater detail, for any $j$ and $s$, we define the pair of half-planes

$$R_1(j,s) = \{X|X_j < s\} \ \text{ and } \ R_2(j,s) = \{X|X_j \geq s\}, \tag{8.2}$$

and we seek the value of $j$ and $s$ that minimize the equation

$$\sum_{i:\, x_i \in R_1(j,s)} (y_i - \hat{y}_{R_1})^2 + \sum_{i:\, x_i \in R_2(j,s)} (y_i - \hat{y}_{R_2})^2, \tag{8.3}$$

where $\hat{y}_{R_1}$ is the mean response for the training observations in $R_1(j,s)$, and $\hat{y}_{R_2}$ is the mean response for the training observations in $R_2(j,s)$. Finding the values of $j$ and $s$ that minimize (8.3) can be done quite quickly, especially when the number of features $p$ is not too large.

Next, we repeat the process, looking for the best predictor and best cutpoint in order to split the data further so as to minimize the RSS within

### PDF page 342 (book page 335)

**FIGURE 8.3.** Top Left: *A partition of two-dimensional feature space that could not result from recursive binary splitting.* Top Right: *The output of recursive binary splitting on a two-dimensional example.* Bottom Left: *A tree corresponding to the partition in the top right panel.* Bottom Right: *A perspective plot of the prediction surface corresponding to that tree.* *[Figure: four panels. Top left — a rectangle with axes $X_1$ (horizontal) and $X_2$ (vertical), divided by line segments into five irregular regions in a pinwheel-like arrangement that no sequence of binary splits could produce. Top right — a rectangle with axes $X_1$ and $X_2$, split by a vertical line at $t_1$, with the left part split horizontally at $t_2$ into $R_1$ (below) and $R_2$ (above); to the right of $t_1$ a second vertical line at $t_3$ leaves the narrow strip $R_3$, and the far-right part is split horizontally at $t_4$ into $R_4$ (below) and $R_5$ (above). Bottom left — the corresponding binary tree drawn upside down: root split $X_1 \leq t_1$; the left child splits on $X_2 \leq t_2$ giving leaves $R_1$ and $R_2$; the right child splits on $X_1 \leq t_3$ giving leaf $R_3$ and a further split $X_2 \leq t_4$ giving leaves $R_4$ and $R_5$. Bottom right — a three-dimensional perspective plot over the $X_1$–$X_2$ plane showing the piecewise-constant prediction surface as five flat plateaus at different heights, shaded from magenta (low) to cyan (high).]*

each of the resulting regions. However, this time, instead of splitting the entire predictor space, we split one of the two previously identified regions. We now have three regions. Again, we look to split one of these three regions further, so as to minimize the RSS. The process continues until a stopping criterion is reached; for instance, we may continue until no region contains more than five observations.

Once the regions $R_1, \ldots, R_J$ have been created, we predict the response for a given test observation using the mean of the training observations in the region to which that test observation belongs.

A five-region example of this approach is shown in Figure 8.3.

**Tree Pruning**

The process described above may produce good predictions on the training set, but is likely to overfit the data, leading to poor test set performance. This is because the resulting tree might be too complex. A smaller tree

### PDF page 343 (book page 336)

with fewer splits (that is, fewer regions $R_1, \ldots, R_J$) might lead to lower variance and better interpretation at the cost of a little bias. One possible alternative to the process described above is to build the tree only so long as the decrease in the RSS due to each split exceeds some (high) threshold. This strategy will result in smaller trees, but is too short-sighted since a seemingly worthless split early on in the tree might be followed by a very good split—that is, a split that leads to a large reduction in RSS later on.

Therefore, a better strategy is to grow a very large tree $T_0$, and then *prune* it back in order to obtain a *subtree*. How do we determine the best way to prune the tree? Intuitively, our goal is to select a subtree that leads to the lowest test error rate. Given a subtree, we can estimate its test error using cross-validation or the validation set approach. However, estimating the cross-validation error for every possible subtree would be too cumbersome, since there is an extremely large number of possible subtrees. Instead, we need a way to select a small set of subtrees for consideration.

*[margin: prune]* *[margin: subtree]*

*Cost complexity pruning*—also known as *weakest link pruning*—gives us a way to do just this. Rather than considering every possible subtree, we consider a sequence of trees indexed by a nonnegative tuning parameter $\alpha$. For each value of $\alpha$ there corresponds a subtree $T \subset T_0$ such that

*[margin: cost complexity pruning]* *[margin: weakest link pruning]*

$$ \sum_{m=1}^{|T|} \sum_{i:\, x_i \in R_m} (y_i - \hat{y}_{R_m})^2 + \alpha|T| \tag{8.4} $$

is as small as possible. Here $|T|$ indicates the number of terminal nodes of the tree $T$, $R_m$ is the rectangle (i.e. the subset of predictor space) corresponding to the $m$th terminal node, and $\hat{y}_{R_m}$ is the predicted response associated with $R_m$—that is, the mean of the training observations in $R_m$. The tuning parameter $\alpha$ controls a trade-off between the subtree's complexity and its fit to the training data. When $\alpha = 0$, then the subtree $T$ will simply equal $T_0$, because then (8.4) just measures the training error. However, as $\alpha$ increases, there is a price to pay for having a tree with many terminal nodes, and so the quantity (8.4) will tend to be minimized for a smaller subtree. Equation 8.4 is reminiscent of the lasso (6.7) from Chapter 6, in which a similar formulation was used in order to control the complexity of a linear model.

It turns out that as we increase $\alpha$ from zero in (8.4), branches get pruned from the tree in a nested and predictable fashion, so obtaining the whole sequence of subtrees as a function of $\alpha$ is easy. We can select a value of $\alpha$ using a validation set or using cross-validation. We then return to the full data set and obtain the subtree corresponding to $\alpha$. This process is summarized in Algorithm 8.1.

Figures 8.4 and 8.5 display the results of fitting and pruning a regression tree on the `Hitters` data, using nine of the features. First, we randomly divided the data set in half, yielding 132 observations in the training set and 131 observations in the test set. We then built a large regression tree on the training data and varied $\alpha$ in (8.4) in order to create subtrees with different numbers of terminal nodes. Finally, we performed six-fold cross-validation in order to estimate the cross-validated MSE of the trees as

### PDF page 344 (book page 337)

**Algorithm 8.1** *Building a Regression Tree*

1. Use recursive binary splitting to grow a large tree on the training data, stopping only when each terminal node has fewer than some minimum number of observations.

2. Apply cost complexity pruning to the large tree in order to obtain a sequence of best subtrees, as a function of $\alpha$.

3. Use K-fold cross-validation to choose $\alpha$. That is, divide the training observations into $K$ folds. For each $k = 1, \ldots, K$:

    (a) Repeat Steps 1 and 2 on all but the $k$th fold of the training data.

    (b) Evaluate the mean squared prediction error on the data in the left-out $k$th fold, as a function of $\alpha$.

    Average the results for each value of $\alpha$, and pick $\alpha$ to minimize the average error.

4. Return the subtree from Step 2 that corresponds to the chosen value of $\alpha$.

a function of $\alpha$. (We chose to perform six-fold cross-validation because 132 is an exact multiple of six.) The unpruned regression tree is shown in Figure 8.4. The green curve in Figure 8.5 shows the CV error as a function of the number of leaves,[^2] while the orange curve indicates the test error. Also shown are standard error bars around the estimated errors. For reference, the training error curve is shown in black. The CV error is a reasonable approximation of the test error: the CV error takes on its minimum for a three-node tree, while the test error also dips down at the three-node tree (though it takes on its lowest value at the ten-node tree). The pruned tree containing three terminal nodes is shown in Figure 8.1.

**8.1.2 Classification Trees**

A *classification tree* is very similar to a regression tree, except that it is used to predict a qualitative response rather than a quantitative one. Recall that for a regression tree, the predicted response for an observation is given by the mean response of the training observations that belong to the same terminal node. In contrast, for a classification tree, we predict that each observation belongs to the *most commonly occurring class* of training observations in the region to which it belongs. In interpreting the results of a classification tree, we are often interested not only in the class prediction corresponding to a particular terminal node region, but also in the *class proportions* among the training observations that fall into that region.

*[margin: classification tree]*

The task of growing a classification tree is quite similar to the task of growing a regression tree. Just as in the regression setting, we use recursive

[^2]: Although CV error is computed as a function of $\alpha$, it is convenient to display the result as a function of $|T|$, the number of leaves; this is based on the relationship between $\alpha$ and $|T|$ in the original tree grown to all the training data.

### PDF page 345 (book page 338)

**FIGURE 8.4.** *Regression tree analysis for the* `Hitters` *data. The unpruned tree that results from top-down greedy splitting on the training data is shown.*

*[Figure: a large green binary tree drawn upside down. The root split is* `Years < 4.5`*. Left branch:* `RBI < 60.5`*, whose left child is* `Putouts < 82` *(leaf 5.487 on the left, and a further split* `Years < 3.5` *giving leaves 4.622 and 5.183) and whose right child is* `Years < 3.5` *(leaves 5.394 and 6.189). Right branch:* `Hits < 117.5`*, whose left child is* `Walks < 43.5` *(a further split* `Runs < 47.5` *giving leaves 6.015 and 5.571, and leaf 6.407) and whose right child is* `Walks < 52.5` *(leaf 6.549, and a further split* `RBI < 80.5` *whose left child* `Years < 6.5` *gives leaves 6.459 and 7.007, with leaf 7.289 on the right).]*

binary splitting to grow a classification tree. However, in the classification setting, RSS cannot be used as a criterion for making the binary splits. A natural alternative to RSS is the *classification error rate*. Since we plan to assign an observation in a given region to the *most commonly occurring class* of training observations in that region, the classification error rate is simply the fraction of the training observations in that region that do not belong to the most common class:

*[margin: classification error rate]*

$$ E = 1 - \max_k (\hat{p}_{mk}). \tag{8.5} $$

Here $\hat{p}_{mk}$ represents the proportion of training observations in the $m$th region that are from the $k$th class. However, it turns out that classification error is not sufficiently sensitive for tree-growing, and in practice two other measures are preferable.

The *Gini index* is defined by

*[margin: Gini index]*

$$ G = \sum_{k=1}^{K} \hat{p}_{mk}(1 - \hat{p}_{mk}), \tag{8.6} $$

a measure of total variance across the $K$ classes. It is not hard to see that the Gini index takes on a small value if all of the $\hat{p}_{mk}$'s are close to zero or one. For this reason the Gini index is referred to as a measure of

### PDF page 346 (book page 339)

**FIGURE 8.5.** *Regression tree analysis for the* `Hitters` *data. The training, cross-validation, and test MSE are shown as a function of the number of terminal nodes in the pruned tree. Standard error bands are displayed. The minimum cross-validation error occurs at a tree size of three.*

*[Figure: line plot with Tree Size (2, 4, 6, 8, 10) on the x-axis and Mean Squared Error (0.0 to 1.0) on the y-axis. Three curves with error bars are shown, labeled in a legend at the upper right: Training (black), Cross-Validation (green), and Test (orange). All three drop steeply from tree size one (Training ≈ 0.74, Test ≈ 0.87) to a minimum near tree size three (≈ 0.34–0.42); thereafter the training error continues to decline gradually to about 0.22 at size ten, while the cross-validation error rises to about 0.50 and the test error settles around 0.33–0.39.]*

node *purity*—a small value indicates that a node contains predominantly observations from a single class.

An alternative to the Gini index is *entropy*, given by

*[margin: entropy]*

$$ D = -\sum_{k=1}^{K} \hat{p}_{mk} \log \hat{p}_{mk}. \tag{8.7} $$

Since $0 \leq \hat{p}_{mk} \leq 1$, it follows that $0 \leq -\hat{p}_{mk} \log \hat{p}_{mk}$. One can show that the entropy will take on a value near zero if the $\hat{p}_{mk}$'s are all near zero or near one. Therefore, like the Gini index, the entropy will take on a small value if the $m$th node is pure. In fact, it turns out that the Gini index and the entropy are quite similar numerically.

When building a classification tree, either the Gini index or the entropy are typically used to evaluate the quality of a particular split, since these two approaches are more sensitive to node purity than is the classification error rate. Any of these three approaches might be used when *pruning* the tree, but the classification error rate is preferable if prediction accuracy of the final pruned tree is the goal.

Figure 8.6 shows an example on the `Heart` data set. These data contain a binary outcome `HD` for 303 patients who presented with chest pain. An outcome value of `Yes` indicates the presence of heart disease based on an angiographic test, while `No` means no heart disease. There are 13 predictors including `Age`, `Sex`, `Chol` (a cholesterol measurement), and other heart and lung function measurements. Cross-validation results in a tree with six terminal nodes.

In our discussion thus far, we have assumed that the predictor variables take on continuous values. However, decision trees can be constructed even in the presence of qualitative predictor variables. For instance, in the `Heart` data, some of the predictors, such as `Sex`, `Thal` (Thallium stress test),

### PDF page 347 (book page 340)

*[Figure, top panel: a large unpruned classification tree for the* `Heart` *data. The root split is* `Thal:a`*. Both children split on* `Ca < 0.5`*. On the left subtree, the left child splits on* `MaxHR < 161.5` *(leading down through* `RestBP < 157`*,* `Chol < 244`*,* `MaxHR < 156`*, and* `MaxHR < 145.5`*, with leaves* No*,* Yes*,* No*,* No*,* Yes*,* No*) and the right child splits on* `ChestPain:bc` *(with* `Chol < 244` *giving leaves* No*,* No*, and* `Sex < 0.5` *giving leaves* No*,* Yes*). On the right subtree, the left child splits on* `Slope < 1.5` *(with* `Age < 52` *giving leaves* Yes*,* No*, and* `Thal:b` *giving leaf* No *and* `ChestPain:a` *giving leaves* No*,* Yes*) and the right child splits on* `Oldpeak < 1.1` *(with* `RestECG < 1` *giving leaves* Yes*,* Yes*, and leaf* Yes*).]*

*[Figure, bottom left panel: error curves plotted against Tree Size (x-axis ticks at 5, 10, 15) with Error from 0.0 to 0.6 on the y-axis. A legend at the upper right labels Training (black), Cross-Validation (orange), and Test (green). All three curves fall sharply from about 0.45–0.47 at the smallest tree sizes; the training error continues down to roughly 0.10–0.12, while the cross-validation and test errors flatten out around 0.24–0.27 with overlapping standard error bars.]*

*[Figure, bottom right panel: the pruned tree. The root split is* `Thal:a`*; both children split on* `Ca < 0.5`*. On the left, one child splits on* `MaxHR < 161.5` *(leaves* No*,* No*) and the other on* `ChestPain:bc` *(leaves* No*,* Yes*). On the right, the* `Ca < 0.5` *node has leaves* Yes*,* Yes*.]*

**FIGURE 8.6.** `Heart` *data.* Top: *The unpruned tree.* Bottom Left: *Cross-validation error, training, and test error, for different sizes of the pruned tree.* Bottom Right: *The pruned tree corresponding to the minimal cross-validation error.*

and `ChestPain`, are qualitative. Therefore, a split on one of these variables amounts to assigning some of the qualitative values to one branch and assigning the remaining to the other branch. In Figure 8.6, some of the internal nodes correspond to splitting qualitative variables. For instance, the top internal node corresponds to splitting `Thal`. The text `Thal:a` indicates that the left-hand branch coming out of that node consists of observations with the first value of the `Thal` variable (normal), and the right-hand node consists of the remaining observations (fixed or reversible defects). The text `ChestPain:bc` two splits down the tree on the left indicates that the left-hand branch coming out of that node consists of observations with the second and third values of the `ChestPain` variable, where the possible values are typical angina, atypical angina, non-anginal pain, and asymptomatic.

Figure 8.6 has a surprising characteristic: some of the splits yield two terminal nodes that have the *same predicted value*. For instance, consider the split `RestECG<1` near the bottom right of the unpruned tree. Regardless of the value of `RestECG`, a response value of `Yes` is predicted for those ob-

### PDF page 348 (book page 341)

servations. Why, then, is the split performed at all? The split is performed because it leads to increased *node purity*. That is, all 9 of the observations corresponding to the right-hand leaf have a response value of `Yes`, whereas 7/11 of those corresponding to the left-hand leaf have a response value of `Yes`. Why is node purity important? Suppose that we have a test observation that belongs to the region given by that right-hand leaf. Then we can be pretty certain that its response value is `Yes`. In contrast, if a test observation belongs to the region given by the left-hand leaf, then its response value is probably `Yes`, but we are much less certain. Even though the split `RestECG<1` does not reduce the classification error, it improves the Gini index and the entropy, which are more sensitive to node purity.

**8.1.3 Trees Versus Linear Models**

Regression and classification trees have a very different flavor from the more classical approaches for regression and classification presented in Chapters 3 and 4. In particular, linear regression assumes a model of the form

$$ f(X) = \beta_0 + \sum_{j=1}^{p} X_j \beta_j, \tag{8.8} $$

whereas regression trees assume a model of the form

$$ f(X) = \sum_{m=1}^{M} c_m \cdot 1_{(X \in R_m)} \tag{8.9} $$

where $R_1, \ldots, R_M$ represent a partition of feature space, as in Figure 8.3.

Which model is better? It depends on the problem at hand. If the relationship between the features and the response is well approximated by a linear model as in (8.8), then an approach such as linear regression will likely work well, and will outperform a method such as a regression tree that does not exploit this linear structure. If instead there is a highly non-linear and complex relationship between the features and the response as indicated by model (8.9), then decision trees may outperform classical approaches. An illustrative example is displayed in Figure 8.7. The relative performances of tree-based and classical approaches can be assessed by estimating the test error, using either cross-validation or the validation set approach (Chapter 5).

Of course, other considerations beyond simply test error may come into play in selecting a statistical learning method; for instance, in certain settings, prediction using a tree may be preferred for the sake of interpretability and visualization.

**8.1.4 Advantages and Disadvantages of Trees**

Decision trees for regression and classification have a number of advantages over the more classical approaches seen in Chapters 3 and 4:

- ▲ Trees are very easy to explain to people. In fact, they are even easier to explain than linear regression!

### PDF page 349 (book page 342)

**FIGURE 8.7.** Top Row: *A two-dimensional classification example in which the true decision boundary is linear, and is indicated by the shaded regions. A classical approach that assumes a linear boundary (left) will outperform a decision tree that performs splits parallel to the axes (right).* Bottom Row: *Here the true decision boundary is non-linear. Here a linear model is unable to capture the true decision boundary (left), whereas a decision tree is successful (right).* *[Figure: a 2×2 grid of plots, each with $X_1$ on the horizontal axis and $X_2$ on the vertical axis, both ranging from about −2 to 2, and green/yellow shaded regions indicating the two classes. Top left: the true boundary is a straight diagonal line separating a green upper region from a yellow lower region, and a single straight black line traces it exactly. Top right: the same green/yellow diagonal shading is overlaid with axis-parallel black segments forming a staircase of rectangular regions that only crudely approximates the diagonal. Bottom left: the true class regions are a yellow rectangle occupying $X_1 > -1$, $X_2 < 1$ with green elsewhere, and a straight diagonal black line—the linear model—cuts across it, failing to match. Bottom right: the same green/yellow rectangular regions are reproduced exactly by two axis-parallel black splits, a vertical line at $X_1 = -1$ and a horizontal line at $X_2 = 1$.]*

- ▲ Some people believe that decision trees more closely mirror human decision-making than do the regression and classification approaches seen in previous chapters.

- ▲ Trees can be displayed graphically, and are easily interpreted even by a non-expert (especially if they are small).

- ▲ Trees can easily handle qualitative predictors without the need to create dummy variables.

- ▼ Unfortunately, trees generally do not have the same level of predictive accuracy as some of the other regression and classification approaches seen in this book.

- ▼ Additionally, trees can be very non-robust. In other words, a small change in the data can cause a large change in the final estimated tree.

However, by aggregating many decision trees, using methods like *bagging*, *random forests*, and *boosting*, the predictive performance of trees can be substantially improved. We introduce these concepts in the next section.

### PDF page 350 (book page 343)

**8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees**

An *ensemble* method is an approach that combines many simple "building block" models in order to obtain a single and potentially very powerful model. These simple building block models are sometimes known as *weak learners*, since they may lead to mediocre predictions on their own.

*[margin: ensemble]*

*[margin: weak learners]*

We will now discuss bagging, random forests, boosting, and Bayesian additive regression trees. These are ensemble methods for which the simple building block is a regression or a classification tree.

**8.2.1 Bagging**

The bootstrap, introduced in Chapter 5, is an extremely powerful idea. It is used in many situations in which it is hard or even impossible to directly compute the standard deviation of a quantity of interest. We see here that the bootstrap can be used in a completely different context, in order to improve statistical learning methods such as decision trees.

The decision trees discussed in Section 8.1 suffer from *high variance*. This means that if we split the training data into two parts at random, and fit a decision tree to both halves, the results that we get could be quite different. In contrast, a procedure with *low variance* will yield similar results if applied repeatedly to distinct data sets; linear regression tends to have low variance, if the ratio of $n$ to $p$ is moderately large. *Bootstrap aggregation*, or *bagging*, is a general-purpose procedure for reducing the variance of a statistical learning method; we introduce it here because it is particularly useful and frequently used in the context of decision trees.

*[margin: bagging]*

Recall that given a set of $n$ independent observations $Z_1, \ldots, Z_n$, each with variance $\sigma^2$, the variance of the mean $\bar{Z}$ of the observations is given by $\sigma^2/n$. In other words, *averaging a set of observations reduces variance*. Hence a natural way to reduce the variance and increase the test set accuracy of a statistical learning method is to take many training sets from the population, build a separate prediction model using each training set, and average the resulting predictions. In other words, we could calculate $\hat{f}^1(x), \hat{f}^2(x), \ldots, \hat{f}^B(x)$ using $B$ separate training sets, and average them in order to obtain a single low-variance statistical learning model, given by

$$\hat{f}_{\mathrm{avg}}(x) = \frac{1}{B}\sum_{b=1}^{B}\hat{f}^b(x).$$

Of course, this is not practical because we generally do not have access to multiple training sets. Instead, we can bootstrap, by taking repeated samples from the (single) training data set. In this approach we generate $B$ different bootstrapped training data sets. We then train our method on the $b$th bootstrapped training set in order to get $\hat{f}^{*b}(x)$, and finally average all the predictions, to obtain

$$\hat{f}_{\mathrm{bag}}(x) = \frac{1}{B}\sum_{b=1}^{B}\hat{f}^{*b}(x).$$

### PDF page 351 (book page 344)

**FIGURE 8.8.** *Bagging and random forest results for the* `Heart` *data. The test error (black and orange) is shown as a function of $B$, the number of bootstrapped training sets used. Random forests were applied with $m = \sqrt{p}$. The dashed line indicates the test error resulting from a single classification tree. The green and blue traces show the OOB error, which in this case is — by chance — considerably lower.* *[Figure: a line plot with "Number of Trees" on the horizontal axis (0 to 300) and "Error" on the vertical axis (0.10 to 0.30). Four jagged step-like traces, all highly volatile for small numbers of trees, with a legend at lower right: "Test: Bagging" (black), "Test: RandomForest" (orange), "OOB: Bagging" (green), and "OOB: RandomForest" (blue). The two test-error traces settle onto constant levels—orange at about 0.22 beyond roughly 70 trees, and black at about 0.245 beyond roughly 165 trees—while the two OOB traces continue to fluctuate across the whole range, the green around 0.19 and the blue around 0.165. A horizontal dashed line runs across the plot at about 0.255.]*

This is called bagging.

While bagging can improve predictions for many regression methods, it is particularly useful for decision trees. To apply bagging to regression trees, we simply construct $B$ regression trees using $B$ bootstrapped training sets, and average the resulting predictions. These trees are grown deep, and are not pruned. Hence each individual tree has high variance, but low bias. Averaging these $B$ trees reduces the variance. Bagging has been demonstrated to give impressive improvements in accuracy by combining together hundreds or even thousands of trees into a single procedure.

Thus far, we have described the bagging procedure in the regression context, to predict a quantitative outcome $Y$. How can bagging be extended to a classification problem where $Y$ is qualitative? In that situation, there are a few possible approaches, but the simplest is as follows. For a given test observation, we can record the class predicted by each of the $B$ trees, and take a *majority vote*: the overall prediction is the most commonly occurring class among the $B$ predictions.

*[margin: majority vote]*

Figure 8.8 shows the results from bagging trees on the `Heart` data. The test error rate is shown as a function of $B$, the number of trees constructed using bootstrapped training data sets. We see that the bagging test error rate is slightly lower in this case than the test error rate obtained from a single tree. The number of trees $B$ is not a critical parameter with bagging; using a very large value of $B$ will not lead to overfitting. In practice we

### PDF page 352 (book page 345)

use a value of $B$ sufficiently large that the error has settled down. Using $B = 100$ is sufficient to achieve good performance in this example.

**_Out-of-Bag_ Error Estimation**

It turns out that there is a very straightforward way to estimate the test error of a bagged model, without the need to perform cross-validation or the validation set approach. Recall that the key to bagging is that trees are repeatedly fit to bootstrapped subsets of the observations. One can show that on average, each bagged tree makes use of around two-thirds of the observations.[^3] The remaining one-third of the observations not used to fit a given bagged tree are referred to as the *out-of-bag* (OOB) observations. *[margin: out-of-bag]* We can predict the response for the $i$th observation using each of the trees in which that observation was OOB. This will yield around $B/3$ predictions for the $i$th observation. In order to obtain a single prediction for the $i$th observation, we can average these predicted responses (if regression is the goal) or can take a majority vote (if classification is the goal). This leads to a single OOB prediction for the $i$th observation. An OOB prediction can be obtained in this way for each of the $n$ observations, from which the overall OOB MSE (for a regression problem) or classification error (for a classification problem) can be computed. The resulting OOB error is a valid estimate of the test error for the bagged model, since the response for each observation is predicted using only the trees that were not fit using that observation. Figure 8.8 displays the OOB error on the `Heart` data. It can be shown that with $B$ sufficiently large, OOB error is virtually equivalent to leave-one-out cross-validation error. The OOB approach for estimating the test error is particularly convenient when performing bagging on large data sets for which cross-validation would be computationally onerous.

**Variable Importance Measures**

As we have discussed, bagging typically results in improved accuracy over prediction using a single tree. Unfortunately, however, it can be difficult to interpret the resulting model. Recall that one of the advantages of decision trees is the attractive and easily interpreted diagram that results, such as the one displayed in Figure 8.1. However, when we bag a large number of trees, it is no longer possible to represent the resulting statistical learning procedure using a single tree, and it is no longer clear which variables are most important to the procedure. Thus, bagging improves prediction accuracy at the expense of interpretability.

Although the collection of bagged trees is much more difficult to interpret than a single tree, one can obtain an overall summary of the importance of each predictor using the RSS (for bagging regression trees) or the Gini index (for bagging classification trees). In the case of bagging regression trees, we can record the total amount that the RSS (8.1) is decreased due to splits over a given predictor, averaged over all $B$ trees. A large value indicates an important predictor. Similarly, in the context of bagging classification

[^3]: This relates to Exercise 2 of Chapter 5.

### PDF page 353 (book page 346)

**FIGURE 8.9.** *A variable importance plot for the* `Heart` *data. Variable importance is computed using the mean decrease in Gini index, and expressed relative to the maximum.* *[Figure: a horizontal bar chart of variable importance for the Heart data, with red bars ordered from smallest at top to largest at bottom. From top to bottom the variables are Fbs, RestECG, ExAng, Sex, Slope, Chol, Age, RestBP, MaxHR, Oldpeak, ChestPain, Ca, and Thal; the x-axis is labeled "Variable Importance" with ticks at 0, 20, 40, 60, 80, and 100. Thal has the longest bar, reaching 100, followed by Ca at roughly 55 and ChestPain at roughly 44, down to Fbs with a barely visible bar near 0.]*

trees, we can add up the total amount that the Gini index (8.6) is decreased by splits over a given predictor, averaged over all $B$ trees.

A graphical representation of the *variable importances* in the `Heart` data is shown in Figure 8.9. We see the mean decrease in Gini index for each variable, relative to the largest. The variables with the largest mean decrease in Gini index are `Thal`, `Ca`, and `ChestPain`. *[margin: variable importance]*

**8.2.2 Random Forests**

*Random forests* provide an improvement over bagged trees by way of a small tweak that *decorrelates* the trees. As in bagging, we build a number of decision trees on bootstrapped training samples. But when building these decision trees, each time a split in a tree is considered, *a random sample of $m$ predictors* is chosen as split candidates from the full set of $p$ predictors. The split is allowed to use only one of those $m$ predictors. A fresh sample of $m$ predictors is taken at each split, and typically we choose $m \approx \sqrt{p}$—that is, the number of predictors considered at each split is approximately equal to the square root of the total number of predictors (4 out of the 13 for the `Heart` data). *[margin: random forest]*

In other words, in building a random forest, at each split in the tree, the algorithm is *not even allowed to consider* a majority of the available predictors. This may sound crazy, but it has a clever rationale. Suppose that there is one very strong predictor in the data set, along with a number of other moderately strong predictors. Then in the collection of bagged trees, most or all of the trees will use this strong predictor in the top split. Consequently, all of the bagged trees will look quite similar to each other.

### PDF page 354 (book page 347)

Hence the predictions from the bagged trees will be highly correlated. Unfortunately, averaging many highly correlated quantities does not lead to as large of a reduction in variance as averaging many uncorrelated quantities. In particular, this means that bagging will not lead to a substantial reduction in variance over a single tree in this setting.

Random forests overcome this problem by forcing each split to consider only a subset of the predictors. Therefore, on average $(p - m)/p$ of the splits will not even consider the strong predictor, and so other predictors will have more of a chance. We can think of this process as *decorrelating* the trees, thereby making the average of the resulting trees less variable and hence more reliable.

The main difference between bagging and random forests is the choice of predictor subset size $m$. For instance, if a random forest is built using $m = p$, then this amounts simply to bagging. On the `Heart` data, random forests using $m = \sqrt{p}$ leads to a reduction in both test error and OOB error over bagging (Figure 8.8).

Using a small value of $m$ in building a random forest will typically be helpful when we have a large number of correlated predictors. We applied random forests to a high-dimensional biological data set consisting of expression measurements of 4,718 genes measured on tissue samples from 349 patients. There are around 20,000 genes in humans, and individual genes have different levels of activity, or expression, in particular cells, tissues, and biological conditions. In this data set, each of the patient samples has a qualitative label with 15 different levels: either normal or 1 of 14 different types of cancer. Our goal was to use random forests to predict cancer type based on the 500 genes that have the largest variance in the training set. We randomly divided the observations into a training and a test set, and applied random forests to the training set for three different values of the number of splitting variables $m$. The results are shown in Figure 8.10. The error rate of a single tree is 45.7 %, and the null rate is 75.4 %.[^4] We see that using 400 trees is sufficient to give good performance, and that the choice $m = \sqrt{p}$ gave a small improvement in test error over bagging ($m = p$) in this example. As with bagging, random forests will not overfit if we increase $B$, so in practice we use a value of $B$ sufficiently large for the error rate to have settled down.

**8.2.3 Boosting**

We now discuss *boosting*, yet another approach for improving the predictions resulting from a decision tree. Like bagging, boosting is a general approach that can be applied to many statistical learning methods for regression or classification. Here we restrict our discussion of boosting to the context of decision trees. *[margin: boosting]*

Recall that bagging involves creating multiple copies of the original training data set using the bootstrap, fitting a separate decision tree to each copy, and then combining all of the trees in order to create a single predic-

[^4]: The null rate results from simply classifying each observation to the dominant class overall, which is in this case the normal class.

### PDF page 355 (book page 348)

**FIGURE 8.10.** *Results from random forests for the 15-class gene expression data set with* $p = 500$ *predictors. The test error is displayed as a function of the number of trees. Each colored line corresponds to a different value of* $m$*, the number of predictors available for splitting at each interior tree node. Random forests* $(m < p)$ *lead to a slight improvement over bagging* $(m = p)$*. A single classification tree has an error rate of 45.7 %.* *[Figure: a line plot with "Number of Trees" on the x-axis (ticks at 0, 100, 200, 300, 400, 500) and "Test Classification Error" on the y-axis (ticks at 0.2, 0.3, 0.4, 0.5). A legend in the upper right identifies three curves: $m=p$ (orange), $m=p/2$ (light blue), and $m=\sqrt{p}$ (green). All three curves begin near or above 0.5 at very few trees and fall steeply, leveling off by roughly 25–50 trees near 0.3 and then flattening for the rest of the range. The green $m=\sqrt{p}$ curve is lowest, dipping to about 0.20 near 70 trees and settling around 0.21; the orange $m=p$ curve settles around 0.24 and the light blue $m=p/2$ curve slightly above it around 0.25.]*

tive model. Notably, each tree is built on a bootstrap data set, independent of the other trees. Boosting works in a similar way, except that the trees are grown *sequentially*: each tree is grown using information from previously grown trees. Boosting does not involve bootstrap sampling; instead each tree is fit on a modified version of the original data set.

Consider first the regression setting. Like bagging, boosting involves combining a large number of decision trees, $\hat{f}^1, \ldots, \hat{f}^B$. Boosting is described in Algorithm 8.2.

What is the idea behind this procedure? Unlike fitting a single large decision tree to the data, which amounts to *fitting the data hard* and potentially overfitting, the boosting approach instead *learns slowly*. Given the current model, we fit a decision tree to the residuals from the model. That is, we fit a tree using the current residuals, rather than the outcome $Y$, as the response. We then add this new decision tree into the fitted function in order to update the residuals. Each of these trees can be rather small, with just a few terminal nodes, determined by the parameter $d$ in the algorithm. By fitting small trees to the residuals, we slowly improve $\hat{f}$ in areas where it does not perform well. The shrinkage parameter $\lambda$ slows the process down even further, allowing more and different shaped trees to attack the residuals. In general, statistical learning approaches that *learn slowly* tend to perform well. Note that in boosting, unlike in bagging, the construction of each tree depends strongly on the trees that have already been grown.

We have just described the process of boosting regression trees. Boosting classification trees proceeds in a similar but slightly more complex way, and the details are omitted here.

### PDF page 356 (book page 349)

---

**Algorithm 8.2** *Boosting for Regression Trees*

---

1. Set $\hat{f}(x) = 0$ and $r_i = y_i$ for all $i$ in the training set.

2. For $b = 1, 2, \ldots, B$, repeat:

   (a) Fit a tree $\hat{f}^b$ with $d$ splits ($d+1$ terminal nodes) to the training data $(X, r)$.

   (b) Update $\hat{f}$ by adding in a shrunken version of the new tree:

   $$\hat{f}(x) \leftarrow \hat{f}(x) + \lambda \hat{f}^b(x). \tag{8.10}$$

   (c) Update the residuals,

   $$r_i \leftarrow r_i - \lambda \hat{f}^b(x_i). \tag{8.11}$$

3. Output the boosted model,

$$\hat{f}(x) = \sum_{b=1}^{B} \lambda \hat{f}^b(x). \tag{8.12}$$

---

Boosting has three tuning parameters:

1. The number of trees $B$. Unlike bagging and random forests, boosting can overfit if $B$ is too large, although this overfitting tends to occur slowly if at all. We use cross-validation to select $B$.

2. The shrinkage parameter $\lambda$, a small positive number. This controls the rate at which boosting learns. Typical values are 0.01 or 0.001, and the right choice can depend on the problem. Very small $\lambda$ can require using a very large value of $B$ in order to achieve good performance.

3. The number $d$ of splits in each tree, which controls the complexity of the boosted ensemble. Often $d = 1$ works well, in which case each tree is a *stump*, consisting of a single split. In this case, the boosted ensemble is fitting an additive model, since each term involves only a single variable. More generally $d$ is the *interaction depth*, and controls the interaction order of the boosted model, since $d$ splits can involve at most $d$ variables.

*[margin: stump]*

*[margin: interaction depth]*

In Figure 8.11, we applied boosting to the 15-class cancer gene expression data set, in order to develop a classifier that can distinguish the normal class from the 14 cancer classes. We display the test error as a function of the total number of trees and the interaction depth $d$. We see that simple stumps with an interaction depth of one perform well if enough of them are included. This model outperforms the depth-two model, and both outperform a random forest. This highlights one difference between boosting and random forests: in boosting, because the growth of a particular tree takes into account the other trees that have already been grown, smaller

### PDF page 357 (book page 350)

*[Figure: line plot of test classification error (y-axis, 0.05–0.25) versus number of trees (x-axis, 0 to 5000). Three curves, per the legend: orange "Boosting: depth=1", light blue "Boosting: depth=2", and green "RandomForest: m=$\sqrt{p}$". All curves start near 0.20–0.245 at few trees and drop rapidly; the random forest levels off around 0.13, boosting with depth=2 around 0.10, and boosting with depth=1 around 0.08.]*

**FIGURE 8.11.** *Results from performing boosting and random forests on the 15-class gene expression data set in order to predict* cancer *versus* normal. *The test error is displayed as a function of the number of trees. For the two boosted models,* $\lambda = 0.01$. *Depth-1 trees slightly outperform depth-2 trees, and both outperform the random forest, although the standard errors are around 0.02, making none of these differences significant. The test error rate for a single tree is 24 %.*

trees are typically sufficient. Using smaller trees can aid in interpretability as well; for instance, using stumps leads to an additive model.

**8.2.4  Bayesian Additive Regression Trees**

Finally, we discuss *Bayesian additive regression trees* (BART), another ensemble method that uses decision trees as its building blocks. For simplicity, we present BART for regression (as opposed to classification).

*[margin: Bayesian additive regression trees]*

Recall that bagging and random forests make predictions from an average of regression trees, each of which is built using a random sample of data and/or predictors. Each tree is built separately from the others. By contrast, boosting uses a weighted sum of trees, each of which is constructed by fitting a tree to the residual of the current fit. Thus, each new tree attempts to capture signal that is not yet accounted for by the current set of trees. BART is related to both approaches: each tree is constructed in a random manner as in bagging and random forests, and each tree tries to capture signal not yet accounted for by the current model, as in boosting. The main novelty in BART is the way in which new trees are generated.

Before we introduce the BART algorithm, we define some notation. We let $K$ denote the number of regression trees, and $B$ the number of iterations for which the BART algorithm will be run. The notation $\hat{f}_k^b(x)$ represents the prediction at $x$ for the $k$th regression tree used in the $b$th iteration. At the end of each iteration, the $K$ trees from that iteration will be summed, i.e. $\hat{f}^b(x) = \sum_{k=1}^{K} \hat{f}_k^b(x)$ for $b = 1, \ldots, B$.

In the first iteration of the BART algorithm, all trees are initialized to have a single root node, with $\hat{f}_k^1(x) = \frac{1}{nK}\sum_{i=1}^{n} y_i$, the mean of the response

### PDF page 358 (book page 351)

**FIGURE 8.12.** *A schematic of perturbed trees from the BART algorithm.* (a): *The kth tree at the (b−1)st iteration,* $\hat{f}_k^{b-1}(X)$, *is displayed. Panels (b)–(d) display three of many possibilities for* $\hat{f}_k^b(X)$, *given the form of* $\hat{f}_k^{b-1}(X)$. (b): *One possibility is that* $\hat{f}_k^b(X)$ *has the same structure as* $\hat{f}_k^{b-1}(X)$, *but with different predictions at the terminal nodes.* (c): *Another possibility is that* $\hat{f}_k^b(X)$ *results from pruning* $\hat{f}_k^{b-1}(X)$. (d): *Alternatively,* $\hat{f}_k^b(X)$ *may have more terminal nodes than* $\hat{f}_k^{b-1}(X)$. *[Figure: four decision-tree diagrams in a 2×2 arrangement, each with a title above it. Top left, titled "(a): $\hat{f}_k^{b-1}(X)$": the root split is `X < 169.17`; its left branch splits on `X < 114.305`, whose left child is the leaf −0.5031 and whose right child splits on `X < 140.35` into leaves 0.2667 and −0.2470; the root's right child is the leaf 0.4079. Top right, titled "(b): Possibility #1 for $\hat{f}_k^b(X)$": an identical structure (`X < 169.17`, `X < 114.305`, `X < 140.35`) but with leaf values −0.5110, 0.2693, −0.2649, and 0.4221. Bottom left, titled "(c): Possibility #2 for $\hat{f}_k^b(X)$": a single split `X < 169.17` with the two leaves −0.1218 and 0.4079. Bottom right, titled "(d): Possibility #3 for $\hat{f}_k^b(X)$": the root split `X < 169.17`, whose left branch splits on `X < 114.305`; that node's left child splits on `X < 106.755` into leaves −0.05089 and −1.03100, and its right child splits on `X < 140.35` into leaves 0.26670 and −0.24700; the root's right child is the leaf 0.40790.]*

values divided by the total number of trees. Thus, $\hat{f}^1(x) = \sum_{k=1}^{K} \hat{f}_k^1(x) = \frac{1}{n}\sum_{i=1}^{n} y_i$.

In subsequent iterations, BART updates each of the $K$ trees, one at a time. In the $b$th iteration, to update the $k$th tree, we subtract from each response value the predictions from all but the $k$th tree, in order to obtain a *partial residual*

$$r_i = y_i - \sum_{k' < k} \hat{f}_{k'}^b(x_i) - \sum_{k' > k} \hat{f}_{k'}^{b-1}(x_i)$$

for the $i$th observation, $i = 1, \ldots, n$. Rather than fitting a fresh tree to this partial residual, BART randomly chooses a perturbation to the tree from the previous iteration ($\hat{f}_k^{b-1}$) from a set of possible perturbations, favoring ones that improve the fit to the partial residual. There are two components to this perturbation:

1. We may change the structure of the tree by adding or pruning branches.

2. We may change the prediction in each terminal node of the tree.

Figure 8.12 illustrates examples of possible perturbations to a tree.

The output of BART is a collection of prediction models,

$$\hat{f}^b(x) = \sum_{k=1}^{K} \hat{f}_k^b(x), \text{ for } b = 1, 2, \ldots, B.$$

### PDF page 359 (book page 352)

**Algorithm 8.3** *Bayesian Additive Regression Trees*

1. Let $\hat{f}_1^1(x) = \hat{f}_2^1(x) = \cdots = \hat{f}_K^1(x) = \frac{1}{nK}\sum_{i=1}^{n} y_i$.

2. Compute $\hat{f}^1(x) = \sum_{k=1}^{K}\hat{f}_k^1(x) = \frac{1}{n}\sum_{i=1}^{n} y_i$.

3. For $b = 2, \ldots, B$:

    (a) For $k = 1, 2, \ldots, K$:

        i. For $i = 1, \ldots, n$, compute the current partial residual

$$r_i = y_i - \sum_{k' < k} \hat{f}_{k'}^b(x_i) - \sum_{k' > k} \hat{f}_{k'}^{b-1}(x_i).$$

        ii. Fit a new tree, $\hat{f}_k^b(x)$, to $r_i$, by randomly perturbing the $k$th tree from the previous iteration, $\hat{f}_k^{b-1}(x)$. Perturbations that improve the fit are favored.

    (b) Compute $\hat{f}^b(x) = \sum_{k=1}^{K}\hat{f}_k^b(x)$.

4. Compute the mean after $L$ burn-in samples,

$$\hat{f}(x) = \frac{1}{B-L}\sum_{b=L+1}^{B}\hat{f}^b(x).$$

We typically throw away the first few of these prediction models, since models obtained in the earlier iterations — known as the *burn-in* period — tend not to provide very good results. We can let $L$ denote the number of burn-in iterations; for instance, we might take $L = 200$. Then, to obtain a single prediction, we simply take the average after the burn-in iterations, $\hat{f}(x) = \frac{1}{B-L}\sum_{b=L+1}^{B}\hat{f}^b(x)$. However, it is also possible to compute quantities other than the average: for instance, the percentiles of $\hat{f}^{L+1}(x), \ldots, \hat{f}^B(x)$ provide a measure of uncertainty in the final prediction. The overall BART procedure is summarized in Algorithm 8.3.

*[margin: burn-in]*

A key element of the BART approach is that in Step 3(a)ii., we do *not* fit a fresh tree to the current partial residual: instead, we try to improve the fit to the current partial residual by slightly modifying the tree obtained in the previous iteration (see Figure 8.12). Roughly speaking, this guards against overfitting since it limits how "hard" we fit the data in each iteration. Furthermore, the individual trees are typically quite small. We limit the tree size in order to avoid overfitting the data, which would be more likely to occur if we grew very large trees.

Figure 8.13 shows the result of applying BART to the `Heart` data, using $K = 200$ trees, as the number of iterations is increased to $10,000$. During the initial iterations, the test and training errors jump around a bit. After this initial burn-in period, the error rates settle down. We note that there is only a small difference between the training error and the test error, indicating that the tree perturbation process largely avoids overfitting.

### PDF page 360 (book page 353)

**FIGURE 8.13.** *BART and boosting results for the* `Heart` *data. Both training and test errors are displayed. After a burn-in period of* 100 *iterations (shown in gray), the error rates for BART settle down. Boosting begins to overfit after a few hundred iterations.* *[Figure: a line plot with "Number of Iterations" on the horizontal axis, drawn on a log scale with ticks at 5, 10, 50, 100, 500, and 5000, and "Error" on the vertical axis from 0.0 to 0.5. A gray shaded rectangle spans the left portion of the plot, up to 100 iterations, marking the burn-in period. A legend in the upper right lists four traces: "BART Training Error" (orange), which starts near 0.14, dips to about 0.10, and stays flat near 0.12 throughout; "BART Test Error" (light blue), which starts near 0.185, fluctuates up to about 0.22 during burn-in, and settles at roughly 0.19; "Boosting Training Error" (dark blue), which starts near 0.46, falls steeply during burn-in to about 0.13, and continues declining to essentially 0.0 by several thousand iterations; and "Boosting Test Error" (green), which also starts near 0.46, falls to about 0.20 near 100 iterations, then climbs steadily to roughly 0.28 at the right edge of the plot.]*

The training and test errors for boosting are also displayed in Figure 8.13. We see that the test error for boosting approaches that of BART, but then begins to increase as the number of iterations increases. Furthermore, the training error for boosting decreases as the number of iterations increases, indicating that boosting has overfit the data.

Though the details are outside of the scope of this book, it turns out that the BART method can be viewed as a *Bayesian* approach to fitting an ensemble of trees: each time we randomly perturb a tree in order to fit the residuals, we are in fact drawing a new tree from a *posterior* distribution. (Of course, this Bayesian connection is the motivation for BART's name.) Furthermore, Algorithm 8.3 can be viewed as a *Markov chain Monte Carlo* algorithm for fitting the BART model.

*[margin: Markov chain Monte Carlo]*

When we apply BART, we must select the number of trees $K$, the number of iterations $B$, and the number of burn-in iterations $L$. We typically choose large values for $B$ and $K$, and a moderate value for $L$: for instance, $K = 200$, $B = 1,000$, and $L = 100$ is a reasonable choice. BART has been shown to have very impressive out-of-box performance — that is, it performs well with minimal tuning.

**8.2.5 Summary of Tree Ensemble Methods**

Trees are an attractive choice of weak learner for an ensemble method for a number of reasons, including their flexibility and ability to handle
