# Front matter
*(PDF pages 1–16; book pages v–xvii)*

### PDF page 1 (no printed page number)

# Design and Analysis of Experiments

**Eighth Edition**

Douglas C. Montgomery

*[Cover image: A mound of dark wine grapes in the foreground, with vineyard rows softly out of focus in the background.]*

### PDF page 2 (no printed page number)

# Design and Analysis of Experiments

**Eighth Edition**

**DOUGLAS C. MONTGOMERY**

*Arizona State University*

WILEY

John Wiley & Sons, Inc.

### PDF page 3 (no printed page number)

| | |
|---|---|
| VICE PRESIDENT AND PUBLISHER | Donald Fowley |
| ACQUISITIONS EDITOR | Linda Ratts |
| CONTENT MANAGER | Lucille Buonocore |
| PRODUCTION EDITOR | Anna Melhorn |
| MARKETING MANAGER | Christopher Ruel |
| DESIGN DIRECTOR | Harry Nolan |
| SENIOR DESIGNER | Maureen Eide |
| EDITORIAL ASSISTANT | Christopher Teja |
| PRODUCTION SERVICES | Namit Grover/Thomson Digital |
| COVER PHOTO | Nik Wheeler/Corbis Images |
| COVER DESIGN | Wendy Lai |

This book was set in Times by Thomson Digital and printed and bound by Courier Westford. The cover was printed by Courier Westford.

This book is printed on acid-free paper. ∞

Founded in 1807, John Wiley & Sons, Inc. has been a valued source of knowledge and understanding for more than 200 years, helping people around the world meet their needs and fulfill their aspirations. Our company is built on a foundation of principles that include responsibility to the communities we serve and where we live and work. In 2008, we launched a Corporate Citizenship Initiative, a global effort to address the environmental, social, economic, and ethical challenges we face in our business. Among the issues we are addressing are carbon impact, paper specifications and procurement, ethical conduct within our business and among our vendors, and community and charitable support. For more information, please visit our website: www.wiley.com/go/citizenship.

Copyright © 2013, 2009, 2005, 2001, 1997 John Wiley & Sons, Inc. All rights reserved. No part of this publication may be reproduced, stored in a retrieval system or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, scanning or otherwise, except as permitted under Sections 107 or 108 of the 1976 United States Copyright Act, without either the prior written permission of the Publisher, or authorization through payment of the appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923, website www.copyright.com. Requests to the Publisher for permission should be addressed to the Permissions Department, John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030-5774, (201) 748-6011, fax (201) 748-6008, website www.wiley.com/go/permissions.

Evaluation copies are provided to qualified academics and professionals for review purposes only, for use in their courses during the next academic year. These copies are licensed and may not be sold or transferred to a third party. Upon completion of the review period, please return the evaluation copy to Wiley. Return instructions and a free of charge return shipping label are available at www.wiley.com/go/returnlabel. Outside of the United States, please contact your local representative.

To order books or for customer service, please call 1-800-CALL WILEY (225-5945).

***Library of Congress Cataloging-in-Publication Data:***

Montgomery, Douglas C.  
Design and analysis of experiments / Douglas C. Montgomery. — Eighth edition.  
&nbsp;&nbsp;&nbsp;&nbsp;pages cm  
&nbsp;&nbsp;&nbsp;&nbsp;Includes bibliographical references and index.  
ISBN 978-1-118-14692-7  
1. Experimental design. &nbsp; I. Title.  
QA279.M66 2013  
519.5’7—dc23  
2012000877

ISBN 978-1118-14692-7

10 9 8 7 6 5 4 3 2 1

### PDF page 4 (book page v)

**Preface**

**Audience**

This is an introductory textbook dealing with the design and analysis of experiments. It is based on college-level courses in design of experiments that I have taught over nearly 40 years at Arizona State University, the University of Washington, and the Georgia Institute of Technology. It also reflects the methods that I have found useful in my own professional practice as an engineering and statistical consultant in many areas of science and engineering, including the research and development activities required for successful technology commercialization and product realization.

The book is intended for students who have completed a first course in statistical methods. This background course should include at least some techniques of descriptive statistics, the standard sampling distributions, and an introduction to basic concepts of confidence intervals and hypothesis testing for means and variances. Chapters 10, 11, and 12 require some familiarity with matrix algebra.

Because the prerequisites are relatively modest, this book can be used in a second course on statistics focusing on statistical design of experiments for undergraduate students in engineering, the physical and chemical sciences, statistics, mathematics, and other fields of science. For many years I have taught a course from the book at the first-year graduate level in engineering. Students in this course come from all of the fields of engineering, materials science, physics, chemistry, mathematics, operations research life sciences, and statistics. I have also used this book as the basis of an industrial short course on design of experiments for practicing technical professionals with a wide variety of backgrounds. There are numerous examples illustrating all of the design and analysis techniques. These examples are based on real-world applications of experimental design and are drawn from many different fields of engineering and the sciences. This adds a strong applications flavor to an academic course for engineers and scientists and makes the book useful as a reference tool for experimenters in a variety of disciplines.

### PDF page 5 (book page vi)

**About the Book**

The eighth edition is a major revision of the book. I have tried to maintain the balance between design and analysis topics of previous editions; however, there are many new topics and examples, and I have reorganized much of the material. There is much more emphasis on the computer in this edition.

**Design-Expert, JMP, and Minitab Software**

During the last few years a number of excellent software products to assist experimenters in both the design and analysis phases of this subject have appeared. I have included output from three of these products, Design-Expert, JMP, and Minitab at many points in the text. Minitab and JMP are widely available general-purpose statistical software packages that have good data analysis capabilities and that handles the analysis of experiments with both fixed and random factors (including the mixed model). Design-Expert is a package focused exclusively on experimental design. All three of these packages have many capabilities for construction and evaluation of designs and extensive analysis features. Student versions of Design-Expert and JMP are available as a packaging option with this book, and their use is highly recommended. I urge all instructors who use this book to incorporate computer software into your course. (In my course, I bring a laptop computer and use a computer projector in every lecture, and every design or analysis topic discussed in class is illustrated with the computer.) To request this book with the student version of JMP or Design-Expert included, contact your local Wiley representative. You can find your local Wiley representative by going to www.wiley.com/college and clicking on the tab for “Who’s My Rep?”

**Empirical Model**

I have continued to focus on the connection between the experiment and the model that the experimenter can develop from the results of the experiment. Engineers (and physical, chemical and life scientists to a large extent) learn about physical mechanisms and their underlying mechanistic models early in their academic training, and throughout much of their professional careers they are involved with manipulation of these models.

Statistically designed experiments offer the engineer a valid basis for developing an *empirical* model of the system being investigated. This empirical model can then be manipulated (perhaps through a response surface or contour plot, or perhaps mathematically) just as any other engineering model. I have discovered through many years of teaching that this viewpoint is very effective in creating enthusiasm in the engineering community for statistically designed experiments. Therefore, the notion of an underlying empirical model for the experiment and response surfaces appears early in the book and receives much more emphasis.

**Factorial Designs**

I have expanded the material on factorial and fractional factorial designs (Chapters 5–9) in an effort to make the material flow more effectively from both the reader’s and the instructor’s viewpoint and to place more emphasis on the empirical model. There is new material on a number of important topics, including follow-up experimentation following a fractional factorial, nonregular and nonorthogonal designs, and small, efficient resolution IV and V designs. Nonregular fractions as alternatives to traditional minimum aberration fractions in 16 runs and analysis methods for these design are discussed and illustrated.

### PDF page 6 (book page vii)

**Additional Important Changes**

I have added a lot of material on optimal designs and their application. The chapter on response surfaces (Chapter 11) has several new topics and problems. I have expanded Chapter 12 on robust parameter design and process robustness experiments. Chapters 13 and 14 discuss experiments involving random effects and some applications of these concepts to nested and split-plot designs. The residual maximum likelihood method is now widely available in software and I have emphasized this technique throughout the book. Because there is expanding industrial interest in nested and split-plot designs, Chapters 13 and 14 have several new topics. Chapter 15 is an overview of important design and analysis topics: nonnormality of the response, the Box–Cox method for selecting the form of a transformation, and other alternatives; unbalanced factorial experiments; the analysis of covariance, including covariates in a factorial design, and repeated measures. I have also added new examples and problems from various fields, including biochemistry and biotechnology.

**Experimental Design**

Throughout the book I have stressed the importance of experimental design as a tool for engineers and scientists to use for product design and development as well as process development and improvement. The use of experimental design in developing products that are robust to environmental factors and other sources of variability is illustrated. I believe that the use of experimental design early in the product cycle can substantially reduce development lead time and cost, leading to processes and products that perform better in the field and have higher reliability than those developed using other approaches.

The book contains more material than can be covered comfortably in one course, and I hope that instructors will be able to either vary the content of each course offering or discuss some topics in greater depth, depending on class interest. There are problem sets at the end of each chapter. These problems vary in scope from computational exercises, designed to reinforce the fundamentals, to extensions or elaboration of basic principles.

**Course Suggestions**

My own course focuses extensively on factorial and fractional factorial designs. Consequently, I usually cover Chapter 1, Chapter 2 (very quickly), most of Chapter 3, Chapter 4 (excluding the material on incomplete blocks and only mentioning Latin squares briefly), and I discuss Chapters 5 through 8 on factorials and two-level factorial and fractional factorial designs in detail. To conclude the course, I introduce response surface methodology (Chapter 11) and give an overview of random effects models (Chapter 13) and nested and split-plot designs (Chapter 14). I always require the students to complete a term project that involves designing, conducting, and presenting the results of a statistically designed experiment. I require them to do this in teams because this is the way that much industrial experimentation is conducted. They must present the results of this project, both orally and in written form.

**The Supplemental Text Material**

For the eighth edition I have prepared supplemental text material for each chapter of the book. Often, this supplemental material elaborates on topics that could not be discussed in greater detail in the book. I have also presented some subjects that do not appear directly in the book, but an introduction to them could prove useful to some students and professional practitioners. Some of this material is at a higher mathematical level than the text. I realize that instructors use this book

### PDF page 7 (book page viii)

with a wide array of audiences, and some more advanced design courses could possibly benefit from including several of the supplemental text material topics. This material is in electronic form on the World Wide Website for this book, located at www.wiley.com/college/montgomery.

**Website**

Current supporting material for instructors and students is available at the website www.wiley.com/college/montgomery. This site will be used to communicate information about innovations and recommendations for effectively using this text. The supplemental text material described above is available at the site, along with electronic versions of data sets used for examples and homework problems, a course syllabus, and some representative student term projects from the course at Arizona State University.

**Student Companion Site**

The student’s section of the textbook website contains the following:

1. The supplemental text material described above
2. Data sets from the book examples and homework problems, in electronic form
3. Sample Student Projects

**Instructor Companion Site**

The instructor’s section of the textbook website contains the following:

4. Solutions to the text problems
5. The supplemental text material described above
6. PowerPoint lecture slides
7. Figures from the text in electronic format, for easy inclusion in lecture slides
8. Data sets from the book examples and homework problems, in electronic form
9. Sample Syllabus
10. Sample Student Projects

The instructor’s section is for instructor use only, and is password-protected. Visit the Instructor Companion Site portion of the website, located at www.wiley.com/college/montgomery, to register for a password.

**Student Solutions Manual**

*[Margin icon: an open book, marking problems included in the Student Solutions Manual.]*

The purpose of the Student Solutions Manual is to provide the student with an in-depth understanding of how to apply the concepts presented in the textbook. Along with detailed instructions on how to solve the selected chapter exercises, insights from practical applications are also shared.

Solutions have been provided for problems selected by the author of the text. Occasionally a group of “continued exercises” is presented and provides the student with a full solution for a specific data set. Problems that are included in the Student Solutions Manual are indicated by an icon appearing in the text margin next to the problem statement.

This is an excellent study aid that many text users will find extremely helpful. The Student Solutions Manual may be ordered in a set with the text, or purchased separately. Contact your local Wiley representative to request the set for your bookstore, or purchase the Student Solutions Manual from the Wiley website.

### PDF page 8 (book page ix)

**Acknowledgments**

I express my appreciation to the many students, instructors, and colleagues who have used the six earlier editions of this book and who have made helpful suggestions for its revision. The contributions of Dr. Raymond H. Myers, Dr. G. Geoffrey Vining, Dr. Brad Jones, Dr. Christine Anderson-Cook, Dr. Connie M. Borror, Dr. Scott Kowalski, Dr. Dennis Lin, Dr. John Ramberg, Dr. Joseph Pignatiello, Dr. Lloyd S. Nelson, Dr. Andre Khuri, Dr. Peter Nelson, Dr. John A. Cornell, Dr. Saeed Maghsoodlo, Dr. Don Holcomb, Dr. George C. Runger, Dr. Bert Keats, Dr. Dwayne Rollier, Dr. Norma Hubele, Dr. Murat Kulahci, Dr. Cynthia Lowry, Dr. Russell G. Heikes, Dr. Harrison M. Wadsworth, Dr. William W. Hines, Dr. Arvind Shah, Dr. Jane Ammons, Dr. Diane Schaub, Mr. Mark Anderson, Mr. Pat Whitcomb, Dr. Pat Spagon, and Dr. William DuMouche were particularly valuable. My current and former Department Chairs, Dr. Ron Askin and Dr. Gary Hogg, have provided an intellectually stimulating environment in which to work.

The contributions of the professional practitioners with whom I have worked have been invaluable. It is impossible to mention everyone, but some of the major contributors include Dr. Dan McCarville of Mindspeed Corporation, Dr. Lisa Custer of the George Group; Dr. Richard Post of Intel; Mr. Tom Bingham, Mr. Dick Vaughn, Dr. Julian Anderson, Mr. Richard Alkire, and Mr. Chase Neilson of the Boeing Company; Mr. Mike Goza, Mr. Don Walton, Ms. Karen Madison, Mr. Jeff Stevens, and Mr. Bob Kohm of Alcoa; Dr. Jay Gardiner, Mr. John Butora, Mr. Dana Lesher, Mr. Lolly Marwah, Mr. Leon Mason of IBM; Dr. Paul Tobias of IBM and Sematech; Ms. Elizabeth A. Peck of The Coca-Cola Company; Dr. Sadri Khalessi and Mr. Franz Wagner of Signetics; Mr. Robert V. Baxley of Monsanto Chemicals; Mr. Harry Peterson-Nedry and Dr. Russell Boyles of Precision Castparts Corporation; Mr. Bill New and Mr. Randy Schmid of Allied-Signal Aerospace; Mr. John M. Fluke, Jr. of the John Fluke Manufacturing Company; Mr. Larry Newton and Mr. Kip Howlett of Georgia-Pacific; and Dr. Ernesto Ramos of BBN Software Products Corporation.

I am indebted to Professor E. S. Pearson and the *Biometrika* Trustees, John Wiley & Sons, Prentice Hall, The American Statistical Association, The Institute of Mathematical Statistics, and the editors of *Biometrics* for permission to use copyrighted material. Dr. Lisa Custer and Dr. Dan McCorville did an excellent job of preparing the solutions that appear in the Instructor’s Solutions Manual, and Dr. Cheryl Jennings and Dr. Sarah Streett provided effective and very helpful proofreading assistance. I am grateful to NASA, the Office of Naval Research, the National Science Foundation, the member companies of the NSF/Industry/University Cooperative Research Center in Quality and Reliability Engineering at Arizona State University, and the IBM Corporation for supporting much of my research in engineering statistics and experimental design.

DOUGLAS C. MONTGOMERY  
TEMPE, ARIZONA

### PDF page 9 (no printed page number)

*(Blank page.)*

### PDF page 10 (book page xi)

**Contents**

**Preface** — v

**1 Introduction** — 1

1.1 Strategy of Experimentation — 1  
1.2 Some Typical Applications of Experimental Design — 8  
1.3 Basic Principles — 11  
1.4 Guidelines for Designing Experiments — 14  
1.5 A Brief History of Statistical Design — 21  
1.6 Summary: Using Statistical Techniques in Experimentation — 22  
1.7 Problems — 23

**2 Simple Comparative Experiments** — 25

2.1 Introduction — 25  
2.2 Basic Statistical Concepts — 27  
2.3 Sampling and Sampling Distributions — 30  
2.4 Inferences About the Differences in Means, Randomized Designs — 36  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.1 Hypothesis Testing — 36  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.2 Confidence Intervals — 43  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.3 Choice of Sample Size — 44  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.4 The Case Where $\sigma_1^2 \ne \sigma_2^2$ — 48  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.5 The Case Where $\sigma_1^2$ and $\sigma_2^2$ Are Known — 50  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.6 Comparing a Single Mean to a Specified Value — 50  
&nbsp;&nbsp;&nbsp;&nbsp;2.4.7 Summary — 51  
2.5 Inferences About the Differences in Means, Paired Comparison Designs — 53  
&nbsp;&nbsp;&nbsp;&nbsp;2.5.1 The Paired Comparison Problem — 53  
&nbsp;&nbsp;&nbsp;&nbsp;2.5.2 Advantages of the Paired Comparison Design — 56  
2.6 Inferences About the Variances of Normal Distributions — 57  
2.7 Problems — 59

### PDF page 11 (book page xii)

**3 Experiments with a Single Factor: The Analysis of Variance** — 65

3.1 An Example — 66  
3.2 The Analysis of Variance — 68  
3.3 Analysis of the Fixed Effects Model — 70  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.1 Decomposition of the Total Sum of Squares — 71  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.2 Statistical Analysis — 73  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.3 Estimation of the Model Parameters — 78  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.4 Unbalanced Data — 79  
3.4 Model Adequacy Checking — 80  
&nbsp;&nbsp;&nbsp;&nbsp;3.4.1 The Normality Assumption — 80  
&nbsp;&nbsp;&nbsp;&nbsp;3.4.2 Plot of Residuals in Time Sequence — 82  
&nbsp;&nbsp;&nbsp;&nbsp;3.4.3 Plot of Residuals Versus Fitted Values — 83  
&nbsp;&nbsp;&nbsp;&nbsp;3.4.4 Plots of Residuals Versus Other Variables — 88  
3.5 Practical Interpretation of Results — 89  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.1 A Regression Model — 89  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.2 Comparisons Among Treatment Means — 90  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.3 Graphical Comparisons of Means — 91  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.4 Contrasts — 92  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.5 Orthogonal Contrasts — 94  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.6 Scheffé’s Method for Comparing All Contrasts — 96  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.7 Comparing Pairs of Treatment Means — 97  
&nbsp;&nbsp;&nbsp;&nbsp;3.5.8 Comparing Treatment Means with a Control — 101  
3.6 Sample Computer Output — 102  
3.7 Determining Sample Size — 105  
&nbsp;&nbsp;&nbsp;&nbsp;3.7.1 Operating Characteristic Curves — 105  
&nbsp;&nbsp;&nbsp;&nbsp;3.7.2 Specifying a Standard Deviation Increase — 108  
&nbsp;&nbsp;&nbsp;&nbsp;3.7.3 Confidence Interval Estimation Method — 109  
3.8 Other Examples of Single-Factor Experiments — 110  
&nbsp;&nbsp;&nbsp;&nbsp;3.8.1 Chocolate and Cardiovascular Health — 110  
&nbsp;&nbsp;&nbsp;&nbsp;3.8.2 A Real Economy Application of a Designed Experiment — 110  
&nbsp;&nbsp;&nbsp;&nbsp;3.8.3 Discovering Dispersion Effects — 114  
3.9 The Random Effects Model — 116  
&nbsp;&nbsp;&nbsp;&nbsp;3.9.1 A Single Random Factor — 116  
&nbsp;&nbsp;&nbsp;&nbsp;3.9.2 Analysis of Variance for the Random Model — 117  
&nbsp;&nbsp;&nbsp;&nbsp;3.9.3 Estimating the Model Parameters — 118  
3.10 The Regression Approach to the Analysis of Variance — 125  
&nbsp;&nbsp;&nbsp;&nbsp;3.10.1 Least Squares Estimation of the Model Parameters — 125  
&nbsp;&nbsp;&nbsp;&nbsp;3.10.2 The General Regression Significance Test — 126  
3.11 Nonparametric Methods in the Analysis of Variance — 128  
&nbsp;&nbsp;&nbsp;&nbsp;3.11.1 The Kruskal–Wallis Test — 128  
&nbsp;&nbsp;&nbsp;&nbsp;3.11.2 General Comments on the Rank Transformation — 130  
3.12 Problems — 130

**4 Randomized Blocks, Latin Squares, and Related Designs** — 139

4.1 The Randomized Complete Block Design — 139  
&nbsp;&nbsp;&nbsp;&nbsp;4.1.1 Statistical Analysis of the RCBD — 141  
&nbsp;&nbsp;&nbsp;&nbsp;4.1.2 Model Adequacy Checking — 149

### PDF page 12 (book page xiii)

&nbsp;&nbsp;&nbsp;&nbsp;4.1.3 Some Other Aspects of the Randomized Complete Block Design — 150  
&nbsp;&nbsp;&nbsp;&nbsp;4.1.4 Estimating Model Parameters and the General Regression Significance Test — 155  
4.2 The Latin Square Design — 158  
4.3 The Graeco-Latin Square Design — 165  
4.4 Balanced Incomplete Block Designs — 168  
&nbsp;&nbsp;&nbsp;&nbsp;4.4.1 Statistical Analysis of the BIBD — 168  
&nbsp;&nbsp;&nbsp;&nbsp;4.4.2 Least Squares Estimation of the Parameters — 172  
&nbsp;&nbsp;&nbsp;&nbsp;4.4.3 Recovery of Interblock Information in the BIBD — 174  
4.5 Problems — 177

**5 Introduction to Factorial Designs** — 183

5.1 Basic Definitions and Principles — 183  
5.2 The Advantage of Factorials — 186  
5.3 The Two-Factor Factorial Design — 187  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1 An Example — 187  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.2 Statistical Analysis of the Fixed Effects Model — 189  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.3 Model Adequacy Checking — 198  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.4 Estimating the Model Parameters — 198  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.5 Choice of Sample Size — 201  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.6 The Assumption of No Interaction in a Two-Factor Model — 202  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.7 One Observation per Cell — 203  
5.4 The General Factorial Design — 206  
5.5 Fitting Response Curves and Surfaces — 211  
5.6 Blocking in a Factorial Design — 219  
5.7 Problems — 225

**6 The $2^k$ Factorial Design** — 233

6.1 Introduction — 233  
6.2 The $2^2$ Design — 234  
6.3 The $2^3$ Design — 241  
6.4 The General $2^k$ Design — 253  
6.5 A Single Replicate of the $2^k$ Design — 255  
6.6 Additional Examples of Unreplicated $2^k$ Design — 268  
6.7 $2^k$ Designs are Optimal Designs — 280  
6.8 The Addition of Center Points to the $2^k$ Design — 285  
6.9 Why We Work with Coded Design Variables — 290  
6.10 Problems — 292

**7 Blocking and Confounding in the $2^k$ Factorial Design** — 304

7.1 Introduction — 304  
7.2 Blocking a Replicated $2^k$ Factorial Design — 305  
7.3 Confounding in the $2^k$ Factorial Design — 306

### PDF page 13 (book page xiv)

7.4 Confounding the $2^k$ Factorial Design in Two Blocks — 306  
7.5 Another Illustration of Why Blocking Is Important — 312  
7.6 Confounding the $2^k$ Factorial Design in Four Blocks — 313  
7.7 Confounding the $2^k$ Factorial Design in $2^p$ Blocks — 315  
7.8 Partial Confounding — 316  
7.9 Problems — 319

**8 Two-Level Fractional Factorial Designs** — 320

8.1 Introduction — 320  
8.2 The One-Half Fraction of the $2^k$ Design — 321  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.1 Definitions and Basic Principles — 321  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.2 Design Resolution — 323  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.3 Construction and Analysis of the One-Half Fraction — 324  
8.3 The One-Quarter Fraction of the $2^k$ Design — 333  
8.4 The General $2^{k-p}$ Fractional Factorial Design — 340  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.1 Choosing a Design — 340  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.2 Analysis of $2^{k-p}$ Fractional Factorials — 343  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.3 Blocking Fractional Factorials — 344  
8.5 Alias Structures in Fractional Factorials and other Designs — 349  
8.6 Resolution III Designs — 351  
&nbsp;&nbsp;&nbsp;&nbsp;8.6.1 Constructing Resolution III Designs — 351  
&nbsp;&nbsp;&nbsp;&nbsp;8.6.2 Fold Over of Resolution III Fractions to Separate Aliased Effects — 353  
&nbsp;&nbsp;&nbsp;&nbsp;8.6.3 Plackett-Burman Designs — 357  
8.7 Resolution IV and V Designs — 366  
&nbsp;&nbsp;&nbsp;&nbsp;8.7.1 Resolution IV Designs — 366  
&nbsp;&nbsp;&nbsp;&nbsp;8.7.2 Sequential Experimentation with Resolution IV Designs — 367  
&nbsp;&nbsp;&nbsp;&nbsp;8.7.3 Resolution V Designs — 373  
8.8 Supersaturated Designs — 374  
8.9 Summary — 375  
8.10 Problems — 376

**9 Additional Design and Analysis Topics for Factorial and Fractional Factorial Designs** — 394

9.1 The $3^k$ Factorial Design — 395  
&nbsp;&nbsp;&nbsp;&nbsp;9.1.1 Notation and Motivation for the $3^k$ Design — 395  
&nbsp;&nbsp;&nbsp;&nbsp;9.1.2 The $3^2$ Design — 396  
&nbsp;&nbsp;&nbsp;&nbsp;9.1.3 The $3^3$ Design — 397  
&nbsp;&nbsp;&nbsp;&nbsp;9.1.4 The General $3^k$ Design — 402  
9.2 Confounding in the $3^k$ Factorial Design — 402  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.1 The $3^k$ Factorial Design in Three Blocks — 403  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.2 The $3^k$ Factorial Design in Nine Blocks — 406  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.3 The $3^k$ Factorial Design in $3^p$ Blocks — 407  
9.3 Fractional Replication of the $3^k$ Factorial Design — 408  
&nbsp;&nbsp;&nbsp;&nbsp;9.3.1 The One-Third Fraction of the $3^k$ Factorial Design — 408  
&nbsp;&nbsp;&nbsp;&nbsp;9.3.2 Other $3^{k-p}$ Fractional Factorial Designs — 410

### PDF page 14 (book page xv)

9.4 Factorials with Mixed Levels — 412  
&nbsp;&nbsp;&nbsp;&nbsp;9.4.1 Factors at Two and Three Levels — 412  
&nbsp;&nbsp;&nbsp;&nbsp;9.4.2 Factors at Two and Four Levels — 414  
9.5 Nonregular Fractional Factorial Designs — 415  
&nbsp;&nbsp;&nbsp;&nbsp;9.5.1 Nonregular Fractional Factorial Designs for 6, 7, and 8 Factors in 16 Runs — 418  
&nbsp;&nbsp;&nbsp;&nbsp;9.5.2 Nonregular Fractional Factorial Designs for 9 Through 14 Factors in 16 Runs — 425  
&nbsp;&nbsp;&nbsp;&nbsp;9.5.3 Analysis of Nonregular Fractional Factorial Designs — 427  
9.6 Constructing Factorial and Fractional Factorial Designs Using an Optimal Design Tool — 431  
&nbsp;&nbsp;&nbsp;&nbsp;9.6.1 Design Optimality Criteria — 433  
&nbsp;&nbsp;&nbsp;&nbsp;9.6.2 Examples of Optimal Designs — 433  
&nbsp;&nbsp;&nbsp;&nbsp;9.6.3 Extensions of the Optimal Design Approach — 443  
9.7 Problems — 444

**10 Fitting Regression Models** — 449

10.1 Introduction — 449  
10.2 Linear Regression Models — 450  
10.3 Estimation of the Parameters in Linear Regression Models — 451  
10.4 Hypothesis Testing in Multiple Regression — 462  
&nbsp;&nbsp;&nbsp;&nbsp;10.4.1 Test for Significance of Regression — 462  
&nbsp;&nbsp;&nbsp;&nbsp;10.4.2 Tests on Individual Regression Coefficients and Groups of Coefficients — 464  
10.5 Confidence Intervals in Multiple Regression — 467  
&nbsp;&nbsp;&nbsp;&nbsp;10.5.1 Confidence Intervals on the Individual Regression Coefficients — 467  
&nbsp;&nbsp;&nbsp;&nbsp;10.5.2 Confidence Interval on the Mean Response — 468  
10.6 Prediction of New Response Observations — 468  
10.7 Regression Model Diagnostics — 470  
&nbsp;&nbsp;&nbsp;&nbsp;10.7.1 Scaled Residuals and PRESS — 470  
&nbsp;&nbsp;&nbsp;&nbsp;10.7.2 Influence Diagnostics — 472  
10.8 Testing for Lack of Fit — 473  
10.9 Problems — 475

**11 Response Surface Methods and Designs** — 478

11.1 Introduction to Response Surface Methodology — 478  
11.2 The Method of Steepest Ascent — 480  
11.3 Analysis of a Second-Order Response Surface — 486  
&nbsp;&nbsp;&nbsp;&nbsp;11.3.1 Location of the Stationary Point — 486  
&nbsp;&nbsp;&nbsp;&nbsp;11.3.2 Characterizing the Response Surface — 488  
&nbsp;&nbsp;&nbsp;&nbsp;11.3.3 Ridge Systems — 495  
&nbsp;&nbsp;&nbsp;&nbsp;11.3.4 Multiple Responses — 496  
11.4 Experimental Designs for Fitting Response Surfaces — 500  
&nbsp;&nbsp;&nbsp;&nbsp;11.4.1 Designs for Fitting the First-Order Model — 501  
&nbsp;&nbsp;&nbsp;&nbsp;11.4.2 Designs for Fitting the Second-Order Model — 501  
&nbsp;&nbsp;&nbsp;&nbsp;11.4.3 Blocking in Response Surface Designs — 507  
&nbsp;&nbsp;&nbsp;&nbsp;11.4.4 Optimal Designs for Response Surfaces — 511  
11.5 Experiments with Computer Models — 523  
11.6 Mixture Experiments — 530  
11.7 Evolutionary Operation — 540  
11.8 Problems — 544

### PDF page 15 (book page xvi)

**12 Robust Parameter Design and Process Robustness Studies** — 554

12.1 Introduction — 554  
12.2 Crossed Array Designs — 556  
12.3 Analysis of the Crossed Array Design — 558  
12.4 Combined Array Designs and the Response Model Approach — 561  
12.5 Choice of Designs — 567  
12.6 Problems — 570

**13 Experiments with Random Factors** — 573

13.1 Random Effects Models — 573  
13.2 The Two-Factor Factorial with Random Factors — 574  
13.3 The Two-Factor Mixed Model — 581  
13.4 Sample Size Determination with Random Effects — 587  
13.5 Rules for Expected Mean Squares — 588  
13.6 Approximate $F$ Tests — 592  
13.7 Some Additional Topics on Estimation of Variance Components — 596  
&nbsp;&nbsp;&nbsp;&nbsp;13.7.1 Approximate Confidence Intervals on Variance Components — 597  
&nbsp;&nbsp;&nbsp;&nbsp;13.7.2 The Modified Large-Sample Method — 600  
13.8 Problems — 601

**14 Nested and Split-Plot Designs** — 604

14.1 The Two-Stage Nested Design — 604  
&nbsp;&nbsp;&nbsp;&nbsp;14.1.1 Statistical Analysis — 605  
&nbsp;&nbsp;&nbsp;&nbsp;14.1.2 Diagnostic Checking — 609  
&nbsp;&nbsp;&nbsp;&nbsp;14.1.3 Variance Components — 611  
&nbsp;&nbsp;&nbsp;&nbsp;14.1.4 Staggered Nested Designs — 612  
14.2 The General $m$-Stage Nested Design — 614  
14.3 Designs with Both Nested and Factorial Factors — 616  
14.4 The Split-Plot Design — 621  
14.5 Other Variations of the Split-Plot Design — 627  
&nbsp;&nbsp;&nbsp;&nbsp;14.5.1 Split-Plot Designs with More Than Two Factors — 627  
&nbsp;&nbsp;&nbsp;&nbsp;14.5.2 The Split-Split-Plot Design — 632  
&nbsp;&nbsp;&nbsp;&nbsp;14.5.3 The Strip-Split-Plot Design — 636  
14.6 Problems — 637

**15 Other Design and Analysis Topics** — 642

15.1 Nonnormal Responses and Transformations — 643  
&nbsp;&nbsp;&nbsp;&nbsp;15.1.1 Selecting a Transformation: The Box–Cox Method — 643  
&nbsp;&nbsp;&nbsp;&nbsp;15.1.2 The Generalized Linear Model — 645

### PDF page 16 (book page xvii)

15.2 Unbalanced Data in a Factorial Design — 652  
&nbsp;&nbsp;&nbsp;&nbsp;15.2.1 Proportional Data: An Easy Case — 652  
&nbsp;&nbsp;&nbsp;&nbsp;15.2.2 Approximate Methods — 654  
&nbsp;&nbsp;&nbsp;&nbsp;15.2.3 The Exact Method — 655  
15.3 The Analysis of Covariance — 655  
&nbsp;&nbsp;&nbsp;&nbsp;15.3.1 Description of the Procedure — 656  
&nbsp;&nbsp;&nbsp;&nbsp;15.3.2 Computer Solution — 664  
&nbsp;&nbsp;&nbsp;&nbsp;15.3.3 Development by the General Regression Significance Test — 665  
&nbsp;&nbsp;&nbsp;&nbsp;15.3.4 Factorial Experiments with Covariates — 667  
15.4 Repeated Measures — 677  
15.5 Problems — 679

**Appendix** — 683

**Table I.** Cumulative Standard Normal Distribution — 684  
**Table II.** Percentage Points of the $t$ Distribution — 686  
**Table III.** Percentage Points of the $\chi^2$ Distribution — 687  
**Table IV.** Percentage Points of the $F$ Distribution — 688  
**Table V.** Operating Characteristic Curves for the Fixed Effects Model Analysis of Variance — 693  
**Table VI.** Operating Characteristic Curves for the Random Effects Model Analysis of Variance — 697  
**Table VII.** Percentage Points of the Studentized Range Statistic — 701  
**Table VIII.** Critical Values for Dunnett’s Test for Comparing Treatments with a Control — 703  
**Table IX.** Coefficients of Orthogonal Polynomials — 705  
**Table X.** Alias Relationships for $2^{k-p}$ Fractional Factorial Designs with $k \le 15$ and $n \le 64$ — 706

**Bibliography** — 719

**Index** — 725
