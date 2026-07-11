# Appendix A — Rstudio
*(PDF pages 189–195; booklet pages 171–177)*


### PDF page 189 (booklet page 171)

# Appendix A — Rstudio

**A.1  How to Install R Studio**

In order to run $R$ and $R$ studio on your system, you need to follow the following steps in the same order.

**A.1.1  Install $R$**

Follow the steps below with respect to the operating system you are using.
To install $R$ on your computer (legally for free!), go to the home website of R: http://www.r-project.org/ *[the URL is hand-underlined]*

1 Click download CRAN in the left bar
2 Choose a download site
3 Choose the operation [sic] system you are using (Windows/Mac/Linux)
4 Download R 3.3.1. (Choose default answers for all questions)

**A.1.2  Install R Studio**

Go to the following website:
https://www.rstudio.com/products/rstudio/download2/ *[the URL is hand-underlined]*

Choose the appropriate installer file for your operating system, download it and then run it to install R studio.

**A.1.3  R Studio Layout**

The $R$ Studio interface consists of several windows.
**Bottom left:** console window (also called command window). Here you can type simple commands after the ">".
**Top left:** editor window (also called script window). Collections of commands (scripts) can

### PDF page 190 (booklet page 172)

be edited and saved. When you don't get this window, you can open it with File $\rightarrow$ New $\rightarrow$ R script.

**Top right**: workspace / history window. In the workspace window you can see which data and values $R$ has in its memory. You can view and edit the values by clicking on them. The history window shows what has been typed before.

**Bottom right**: files / plots / packages / help window. Here you can open files, view plots (also previous plots), install and load packages or use the help function.

**A.1.4 Working Directory**

Your working directory is the folder on your computer in which you are currently working. When you ask $R$ to open a certain file, it will look in the working directory for this file, and when you tell $R$ to save a data file or figure, it will save it in the working directory. Before you start working, please set your working directory to where all your data and script files are or should be stored.

The following command will lead you to your current working directory:

```r
getwd()
```

You can also set up your own working directory by

```r
setwd("C/:Nandram")
```

*[sic: the path is printed as `"C/:Nandram"`; the drive prefix should be `C:/`]*

**A.1.5 Libraries and packages**

With the standard installation, most common packages are installed. To get a list of all installed packages, go to the packages window or type

```r
library()
```

in the console window. There are many more packages available on the $R$ website. If you want to install and use a package (for example, the package called "coda") you should:

1. Install the package: click install packages in the packages window and type geometry [sic: "geometry" — the package under discussion is "coda"] or type

```r
install.packages("coda")
```

in the command window.

2. Load the package: check box in front of geometry [sic] or type

```r
library("coda")
```

### PDF page 191 (booklet page 173)

in the command window.

## A.2 Basic Tutorial for Data Analysis

In this tutorial, we will design a basic data analysis program by utilizing the features of R Studio to create some visual representation of that data.

### A.2.1 Importing Data in R Studio

For this tutorial we will use the sample census data set ACS, a .csv file There are two ways to import this data in $R$ Studio. One way is to import the data programmatically directly from the internet: *(the sentence "…a .csv file There are two ways…" is missing its period after "file" [sic])*

$$acs < -read.csv(url("http://stat511.cwick.co.nz/homeworks/acs\_or.csv"))$$

We can create $R$ data file and import text or csv file as follows:

```r
##
## Create your own data file in R
##
setwd("C:/Nandram")
#
# Enter data
weight <- c(120, 100, 90, 110, 10)
height <- c(180, 160, 140, 160, 190)
# combine variables
mydat <- cbind(weight, height)
mydat
# weight height
#[1,]   120   180
#[2,]   100   160
#[3,]    90   140
#[4,]   110   160
#[5,]   140   190
#Save as data frame format
mydat <- data.frame(mydat)
# save in text format with tab delimit
write.table(mydat, "C:/Nandram/mydat.txt", sep="\t")
# save in R format
save(mydat, file = "C:/Nandram/mydat.Rdata")
# - - - - - - - - - - - - - - - - - - - - - - - - -
#
```

*(sic: the fifth element of `weight` is entered as `10`, but the printed `mydat` output shows `140` in row `[5,]`. The booklet's code and its quoted output are inconsistent; both are reproduced as printed. The commented dashed line near the bottom is drawn as a row of hand-spaced hyphens in the typeset source.)*

> ✔ Verified: The printed `mydat` output matches `cbind(weight, height)` for rows 1–4 and all heights, and row 5 of weight is the documented typo (typed 10, printed 140).

### PDF page 192 (booklet page 174)

```r
## Import data in R
#
# lmport text format data
mydat <- read.table("C:/Nandram/mydat.txt", header = TRUE, sep ="\t")
# mean of each variable
apply(mydat,2,mean)
# weight height
#112   166
#
# Import R data format
load("C:/Nandram/mydat.Rdata")
```

*(sic: the third comment line reads "lmport" — a lowercase L, not a capital I — where the surrounding lines read "Import". The glyph in the scan is an unserifed vertical stroke, unlike the serifed capital I elsewhere; reading is confident but not magnification-verified.)*

To read csv file in R:

```r
read.csv("[filename].csv")
```

You can also use RStudio menus: Workspaces - Import Dataset - From Text Files... Any dataset can be viewed by executing the following line:

```r
View(acs)
```

where `acs` is the variable dataset is assigned to.

**A.2.2 Manipulating Data**

You can use various transformation features of $R$ to access and manipulate the data. To access a particular column if the data type is dataframe, for example age_husband in our case, execute

```r
acs$age_husband
```

To access data as a vector if the data type is dataframe or matrix, execute

```r
acs[,3]
```

**A.2.3 Save and Export Data File**

The R script file can be saved as a .R file to your local computer through Studio menu: File - Save - ...
The R Studio environment can also be saved to your local computer through the environment window.

### PDF page 193 (booklet page 175)

**A.2.4 Load Data File**

You can open saved .$R$ files through the $R$ Studio menu: File - Open file - ...
You can also load saved R environments through the environment window.

**A.2.5 Simple Statistics**

Following functions can be used to calculate the statistics of a variable "acs$age_husband".
Mean: mean(acs$age_husband)
Median: median(acs$age_husband)
Quantile: quantile(acs Sage_wife) *[sic: reads "acs Sage_wife"; evidently `acs$age_wife`]*
Variance: var(acs$age_wife)
Standard Deviation: sd(acs$age_wife)
Sum: sumlacs$age_husband [sic] Product: prod(acs$age husband) [sic] max(acs$age_husband) or min(acs$age_husbaı *[the line runs off the right edge of the scan; the final characters of `min(acs$age_husband)` are cut off]*
or smallest element
rowSums(acs$age_husband) (or colSums(acs$age_husband)): sums of all numbers in each row
(or column) of a matrix. The result is a vector.
You can also get the statistical summary of the dataset by just running on either a column
or the complete dataset:

```r
summary(acs)
```

**A.2.6 Plotting Data**

A very liked feature of $R$ studio is its built in data visualizer for R. Any data set imported
in $R$ can visualized [sic] using the plot and several other functions of R. For Example, to create
a scatter plot of a data set, you can run the following command in consol [sic]

```r
plot(x=acs$age_husband,y=acs$age_wife,type='p')
```

where 'p' set the plot type as point. You can also choose line by changing type variable
to 'l'. For data distribution plots, there are several features tools and packages available in
$R$ that you can use to draw any kind of distribution. For example, to draw a Histogram of
a dataset, you can run the command

```r
hist(acs$number_children)
```

Similarly for Bar Plots, run the following set of commands

```r
counts <- table(acs$bedrooms)
barplot(counts, main="Bedrooms Distribution", xlab="Number of Bedrooms")
```

### PDF page 194 (booklet page 176)

You can get a Box Plot by running the command

```r
boxplot(acs$bedrooms)
```

Your plots can be saved as images or .pdf files through the plot wondow [sic]:
Export - Save as Image / Save as PDF - ...

**A.2.7 Draw Random Samples**

If you would like to draw a random sample from some standard distributions, you can use R functions. For example, to get 100 random samples from a Normal distribution, Gamma distribution, Beta distribution and Binomial distribution, run the commands respectively

```r
rnorm (n = 100, mean = 0, sd = 1)
rgamma (n = 100, shape = 2, rate = 1)
rbeta (n = 100, shape = 2, rate = 1)
rbinom (n = 100, size = 1000, prob = 0.1)
```

*(sic: the `rbeta` call is printed with arguments `shape` and `rate`, copying the `rgamma` line; R's `rbeta` takes `shape1` and `shape2`.)*

You can also make the density plot. For example, you can get the density function for a standard normal distribution with the command:

```r
dnorm(x, mean=0, sd = 1)
```

**A.2.8 Help in $R$ and Communication with Internet**

If you know R-command, you can get help as follows:

```r
?table
?var
?mean
?summary
?plot
?hist
```

If we don't know R-command name we can still get help as follows:

```r
?? "Hyper Geometric Distribution"
?? "Normal distribution"
??regression
```

If we don't know command in R, we can get help in R through internet.

### PDF page 195 (booklet page 177)

*(Note: the page prints 177, not the 190 predicted from the page-count estimate.)*

For example, if we want help how to do frequency table in R. Google it as "Frequency table in R". R bloggers website has example: "How to Get the Frequency Table of a Categorical Variable as a Data Frame in R" as follows:

```r
head(subset(mtcars, select = 'gear'))
factor(mtcars$gear)
w = table (mtcars$gear)
```

If you want to know how to draw exponential random variable in R, google it as "exponential random variable in R".

```r
random.exponential <- rexp(n=100,rate-1) #Draw 100 exponential samples
hist(random.exponential) #Draw histogram for exponential samples
```

*(sic: `rate-1` — the argument should be `rate=1`.)*

If you want help in linear regression in R. Google it as "linear regression in R". R-blogger has example given as follows:

```r
alligator = data.frame(
lnLength = c(3.87,3.61,4.33,3.43,3.81,3.83,3.46,3.76,3.50,3.58,4.19,3.78,3.71,3.73,3.78)
lnWeight = c(4.87,3.93,6.46,3.33,4.38,4.70,3.50,4.50,3.58, 3.64, 5.90, 4.43, 4.38, 4.42, 4.25)
)
#
alli.mod1 = lm(lnWeight~lnLength, data = alligator)
alli.mod1
#
summary(alli.mod1)
```

*(The booklet's italic code font makes "ln" and "In" indistinguishable; these are the log-transformed length and weight of the standard alligator dataset. [sic: the two `c(...)` arguments inside `data.frame(` are not separated by a comma.])*

If we want help in sub setting data frame in R. Google is as "subset data in r".
There is example <u>How to Subset Data Frames in R- For Dummies</u>: as follows for iris dataset:

```r
str(iris)
iris[1:5,] # row 1-5 and all columns
iris[ c("Sepal.Length", "Sepal.Width")]
iris[, 'Sepal.Length']
iris[, 'Sepal.Length', drop=FALSE]
class(iris)
head(iris) # first six observation
dim(iris) # dimension
```

For you to be able to use some $R$ commands, to run your code, you must install the appropriate R-package. In such cases first install required packages and run "library". We have just given you a basic introduction to R. With some ideas of any basic programming language, with these basic R commands, you will be able to write programming language, with these basic R commands, you will be able to write more extensive codes.

*(sic: the final sentence repeats the clause "with these basic R commands, you will be able to write" — transcribed as printed.)*
