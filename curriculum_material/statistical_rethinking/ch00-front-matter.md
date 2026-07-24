# Front matter
*(PDF pages 1–6; book pages vii–ix)*

### PDF page 1 (no printed page number)

# Statistical Rethinking²

## A Bayesian Course with Examples in R and Stan

Second Edition

Richard McElreath

This version compiled December 8, 2019

### PDF page 2 (no printed page number)

*(Blank page.)*

### PDF page 3 (book page vii)

# Contents

| Section | Page |
|---|---:|
| Preface to the Second Edition | xi |
| Preface | xiii |
|   Audience | xiii |
|   Teaching strategy | xiv |
|   How to use this book | xiv |
|   Installing the `rethinking` R package | xviii |
|   Acknowledgments | xix |
| Chapter 1. The Golem of Prague | 1 |
|   1.1. Statistical golems | 1 |
|   1.2. Statistical rethinking | 4 |
|   1.3. Tools for golem engineering | 10 |
|   1.4. Summary | 17 |
| Chapter 2. Small Worlds and Large Worlds | 19 |
|   2.1. The garden of forking data | 20 |
|   2.2. Building a model | 28 |
|   2.3. Components of the model | 32 |
|   2.4. Making the model go | 36 |
|   2.5. Summary | 46 |
|   2.6. Practice | 46 |
| Chapter 3. Sampling the Imaginary | 49 |
|   3.1. Sampling from a grid-approximate posterior | 52 |
|   3.2. Sampling to summarize | 53 |
|   3.3. Sampling to simulate prediction | 61 |
|   3.4. Summary | 68 |
|   3.5. Practice | 69 |
| Chapter 4. Geocentric Models | 73 |
|   4.1. Why normal distributions are normal | 74 |
|   4.2. A language for describing models | 79 |
|   4.3. Gaussian model of height | 81 |
|   4.4. Linear prediction | 94 |
|   4.5. Curves from lines | 113 |
|   4.6. Summary | 123 |
|   4.7. Practice | 123 |
| Chapter 5. The Many Variables & The Spurious Waffles | 127 |
|   5.1. Spurious association | 129 |
|   5.2. Masked relationship | 148 |

### PDF page 4 (book page viii)

| Section | Page |
|---|---:|
|   5.3. Categorical variables | 157 |
|   5.4. Summary | 162 |
|   5.5. Practice | 162 |
| Chapter 6. The Haunted DAG & The Causal Terror | 165 |
|   6.1. Multicollinearity | 167 |
|   6.2. Post-treatment bias | 174 |
|   6.3. Collider bias | 180 |
|   6.4. Confronting confounding | 187 |
|   6.5. Summary | 193 |
|   6.6. Practice | 193 |
| Chapter 7. Ulysses’ Compass | 195 |
|   7.1. The problem with parameters | 197 |
|   7.2. Entropy and accuracy | 206 |
|   7.3. Golem Taming: Regularization | 218 |
|   7.4. Predicting predictive accuracy | 221 |
|   7.5. Model comparison | 229 |
|   7.6. Summary | 239 |
|   7.7. Practice | 239 |
| Chapter 8. Conditional Manatees | 241 |
|   8.1. Building an interaction | 243 |
|   8.2. Symmetry of interactions | 254 |
|   8.3. Continuous interactions | 257 |
|   8.4. Summary | 264 |
|   8.5. Practice | 265 |
| Chapter 9. Markov Chain Monte Carlo | 269 |
|   9.1. Good King Markov and His island kingdom | 270 |
|   9.2. Metropolis Algorithms | 273 |
|   9.3. Hamiltonian Monte Carlo | 276 |
|   9.4. Easy HMC: `ulam` | 284 |
|   9.5. Care and feeding of your Markov chain | 293 |
|   9.6. Summary | 303 |
|   9.7. Practice | 303 |
| Chapter 10. Big Entropy and the Generalized Linear Model | 307 |
|   10.1. Maximum entropy | 308 |
|   10.2. Generalized linear models | 320 |
|   10.3. Maximum entropy priors | 329 |
|   10.4. Summary | 329 |
| Chapter 11. God Spiked the Integers | 331 |
|   11.1. Binomial regression | 332 |
|   11.2. Poisson regression | 353 |
|   11.3. Multinomial and categorical models | 366 |
|   11.4. Censoring and survival | 373 |
|   11.5. Summary | 378 |
|   11.6. Practice | 378 |
| Chapter 12. Monsters and Mixtures | 381 |
|   12.1. Over-dispersed counts | 381 |

### PDF page 5 (book page ix)

| Section | Page |
|---|---:|
|   12.2. Zero-inflated outcomes | 388 |
|   12.3. Ordered categorical outcomes | 392 |
|   12.4. Ordered categorical predictors | 403 |
|   12.5. Summary | 409 |
|   12.6. Practice | 409 |
| Chapter 13. Models With Memory | 413 |
|   13.1. Example: Multilevel tadpoles | 415 |
|   13.2. Varying effects and the underfitting/overfitting trade-off | 422 |
|   13.3. More than one type of cluster | 429 |
|   13.4. Divergent transitions and non-centered priors | 434 |
|   13.5. Multilevel posterior predictions | 440 |
|   13.6. Summary | 445 |
|   13.7. Practice | 445 |
| Chapter 14. Adventures in Covariance | 449 |
|   14.1. Varying slopes by construction | 451 |
|   14.2. Advanced varying slopes | 461 |
|   14.3. Instruments and causal designs | 468 |
|   14.4. Social relations as correlated varying effects | 475 |
|   14.5. Continuous categories and the Gaussian process | 481 |
|   14.6. Summary | 498 |
|   14.7. Practice | 499 |
| Chapter 15. Missing Data and Other Opportunities | 501 |
|   15.1. Measurement error | 503 |
|   15.2. Missing data | 511 |
|   15.3. Categorical errors and discrete absences | 528 |
|   15.4. Summary | 533 |
|   15.5. Practice | 533 |
| Chapter 16. Generalized Linear Madness | 537 |
|   16.1. Geometric people | 538 |
|   16.2. Hidden minds and observed behavior | 543 |
|   16.3. Ordinary differential nut cracking | 549 |
|   16.4. Population dynamics | 553 |
|   16.5. Summary | 562 |
|   16.6. Practice | 562 |
| Chapter 17. Horoscopes | 565 |
| Endnotes | 569 |
| Bibliography | 583 |
| Citation index | 595 |

### PDF page 6 (no printed page number)

*(Blank page.)*
