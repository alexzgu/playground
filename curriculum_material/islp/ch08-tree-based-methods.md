# Chapter 8 — Tree-Based Methods
*(PDF pages 338–373; book pages 331–335)*

*⚠ In progress: 5 of 36 pages transcribed; missing PDF pages 343–373.*

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
