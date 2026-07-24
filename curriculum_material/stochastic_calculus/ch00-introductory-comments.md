# Chapter 0 — Introductory comments
*(PDF pages 7–8; book pages 1–2)*

### PDF page 7 (book page 1)

# Introductory comments

This is an introduction to stochastic calculus. I will assume that the reader has had a post-calculus course in probability or statistics. For much of these notes this is all that is needed, but to have a deep understanding of the subject, one needs to know measure theory and probability from that perspective. My goal is to include discussion for readers with that background as well. I also assume that the reader can write simple computer programs either using a language like C++ or by using software such as Matlab or Mathematica.

---

> More advanced mathematical comments that can be skipped by the reader will be indented with a different font. Comments here will assume that the reader knows that language of measure-theoretic probability theory.

---

We will discuss some of the applications to finance but our main focus will be on the mathematics. Financial mathematics is a kind of applied mathematics, and I will start by making some comments about the use of mathematics in "the real world". The general paradigm is as follows.

- A mathematical model is made of some real world phenomenon. Usually this model requires simplification and does not precisely describe the real situation. One hopes that models are *robust* in the sense that if the model is not very far from reality then its predictions will also be close to accurate.

- The model consists of mathematical *assumptions* about the real world.

- Given these assumptions, one does mathematical analysis to see what they imply. The analysis can be of various types:

### PDF page 8 (book page 2)

  - Rigorous derivations of consequences.
  - Derivations that are plausible but are not mathematically rigorous.
  - Approximations of the mathematical model which lead to tractable calculations.
  - Numerical calculations on a computer.
  - For models that include randomness, *Monte Carlo simulations* using a (pseudo) random number generator.

- If the mathematical analysis is successful it will make predictions about the real world. These are then checked.

- If the predictions are bad, there are two possible reasons:

  - The mathematical analysis was faulty.
  - The model does not sufficiently reflect reality.

The user of mathematics does not always need to know the details of the mathematical analysis, but it is critical to understand the *assumptions* in the model. No matter how precise or sophisticated the analysis is, if the assumptions are bad, one cannot expect a good answer.
