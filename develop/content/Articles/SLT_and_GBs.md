Title: Statistical Learning Theory and Generalization Bounds
Date: 2018-04-23 13:00
Tags: learning theory, machine learning, supervised learning
Author: Anna Go
Summary: Generalization bounds in Statistical Learning Theory
Slug: generalization-bounds
Status: draft

When setting up a supervised learning task, we define an ansatz for the 
target function $f$ by making an (implicit) assumption about the form of 
$f$. This assumption defines the space of possible functions, which is 
called the **hypothesis space** $\mathcal{H}$. For example, if we assume that 
the target function is linear, then $\mathcal{H}$ can be formally expressed 
as

$$
\mathcal{H} = \{ h: \mathcal{X}\to\mathcal{Y} \,|\, h(x) = ax+b \},
$$

that is the set of all linear functions $h$ mapping from the input space 
$\mathcal{X}$ to the output space $\mathcal{Y}$.

The task of the machine learning algorithm is now to choose from 
$\mathcal{H}$ a single hypothesis $h$ which provides the best estimate 
for the target function $f$. The quality of the estimate is measured 
by the **loss** or **cost function** $L(y,h(x))$, which measures the discrepancy 
between the true label $y$ of $x$ and its prediction $h(x)$. The performance 
of a hypothesis $h$ on the full dataset is evaluated by computing the mean 
loss,

$$
R_{emp}(h) = \frac{1}{m}\sum\limits_{i=1}^{m} L(y_i,h(x_i))
$$

referred to as the **empirical risk**, while the expected value of the loss 
over the true unknown joint probability distribution $P(X,Y)$ is the
(true) risk:

$$
R(h) = \mathbb{E}_{(x,y)\sim P(X,Y)} \left[ L(y,h(x)) \right]
$$

However, minimizing the empirical risk alone is not sufficient; the 
**generalization gap** (GG) - that is the difference between the risk and 
empirical risk - has to be small. Formally, we require that for some small 
positive number $\varepsilon$ the following probability is small:

$$
P\left[ \sup \limits_{h\in\mathcal{H}} \left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right]
$$

Consider that an important underlying assumption of the learning task setting is that 
the samples in the training set are independent and identically distributed (iid), 
that is drawn from the same probability distribution. Given this assumption, we can 
make use of the

Law of Large Numbers
--------------------

> If $x_1,...,x_m$ are $m$ iid samples of a random variable $X$ 
  distributed according to $P$, then for a small $\varepsilon\gt 0$:
  $$
  \lim\limits_{m\to\infty} \mathbb{P}\left[ \left| \mathbb{E}_{X\sim P}[X] - \frac{1}{m}\sum\limits_{i=1}^{m}x_i \right| \gt \varepsilon \right] = 0
  $$

The above is the weak formulation of the Law of Large Numbers, stating 
that when the number of samples goes to infinity, the empirical mean 
over the sample will be (almost) equal to the true expectation value of 
$X$.

Now, the empirical risk $R_{emp}$ is the sample mean of the errors, 
while the risk $R$ is the true mean. Therefore, for a single hypothesis 
we can state:

$$
\lim\limits_{m\to\infty} \mathbb{P}\left[ \left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right] = 0
$$


Hoeffding's inequality
----------------------
quantifies the deviation between random variables and their expected values:

> If $x_1,...,x_m$ are $m$ iid samples of a random variable $X$ 
  distributed according to $P$, and $a \leq x_i \leq b$ for every $i$,
  then for a small $\varepsilon\gt 0$:
  $$
  \mathbb{P}\left[ \left| \mathbb{E}_{X\sim P}[X] - \frac{1}{m}\sum\limits_{i=1}^{m}x_i \right| \gt \varepsilon \right] \leq 2 \exp\left[ \frac{-2m\varepsilon^2}{(b-a)^2} \right].
  $$

Applied to the error (which is normalized, i.e. $0\leq \varepsilon\leq 1$), 
we get the following result for a single hypothesis:

$$
\mathbb{P}\left[ \left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right] \leq 2 e^{-2m\varepsilon^2},
$$

showing that the GG decreases exponentially in the number of training examples $m$.


However, the GG-bound has to take into account the challenge of picking 
the "right" hypothesis $h$ from the hypothesis space $\mathcal{H}$!

Formally, this can be expressed as
$$
\mathbb{P}\left[ \sup_{h\in\mathcal{H}}\left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right] = \mathbb{P}\left[ \bigcup\limits_{h\in\mathcal{H}}\left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right]
$$

where $\bigcup$ denotes the union of events, corresponding to the logical OR operator.


The Union Bound
---------------
or Bool's inequality states that for any finite countable set of events, 
the probability that at least one of the events happens is no greater than 
the sum of the probability of the individual events. Formally,

> For a countable set of events $A_i$, $i=1,2,...$,
  $$
  \mathbb{P}\left[ \bigcup\limits_{i} A_i \right] \leq \sum\limits_i \mathbb{P}\left(A_i \right).
  $$

Applying this, we obtain

$$
\begin{aligned}
\mathbb{P}\left[ \sup_{h\in\mathcal{H}}\left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right] &\leq \sum\limits_{h\in\mathcal{H}} \mathbb{P}\left[ left| R(h)-R_{emp}(h) \right| \gt \varepsilon \right]\\
&\leq 2|\mathcal{H}| e^{-2m\varepsilon^2},
\end{aligned}
$$

where $|\mathcal{H}|$ is the cardinality of the hypothesis space.

Denoting the last expression on the right-hand side as $\delta$, 
we can state that with a confidence $1-\delta$, 

$$
\left| R(h)-R_{emp}(h) \right| \leq \varepsilon
$$

or equivalently,
$$
R(h) \leq R_{emp}(h) + \varepsilon
$$

where
$$
\varepsilon = \sqrt{ \frac{\ln \left|\mathcal{H}\right| + \ln(2/\delta)}{2m} }.
$$

This is a typical result for a *generalization bound* studied extensively 
in statistical learning theory. Various modification of this expression 
exist, depending on the details of the derivation assumptions.



The *sample complexity* of a machine learning algorithm represents the number of training-samples that it needs in order to successfully learn a target function.





$\abs{\mathcal{H}}$ is the cardinality of the hypothesis space, i.e. the number of different functions in the considered function class. In case when $\abs{\mathcal{H}}=\infty$, the epsilon-cover of the class is used, i.e. the class is discretized by clustering hypotheses that are $\epsilon$-close to each other, such that

$$
\abs{ \mathcal{H}_{\epsilon} } = \left(\frac{1}{\epsilon}\right)^d,
$$
where $d$ is the class dimension, typically the VC dimension.


Aside:


The VC dimension
----------------
The Vapnik-Chervonenkis (VC) dimension is a measure for the capacity of a model, i.e. a class of functions $\{f(\alpha)\}$.

R(x)-R_emp(x) is bounded by the expression which is a funciton of VC dim.
Given several different learning machines, we pick the one which minimizes R_emp and the sqrt, i.e. we choose the machine which gives the lowest upper bound on the actual risk. This gives a principled method for choosing a learning machine for a given taskt, and is the essential idea of structured risk minimization.


The VC dim is a property of a set of functions {f(alpha)} and can be defined for various classes of funcitons.

Consider the binary classification task, so that f(alpha,x)\in{-1,1}.

If a given set of m points can be labeled in all possible 2^m ways, and for each labeling, a member of the set {f(alpha)} can be found which correctly assigns those labels, we say that the set of points is hattered by that set of functions. The VC dim for the set of functions {f(alpha)} is defined as the maximum number of training points that can be shattered by {f(alpha)}.

Note that if the VC dim is h, then there exists at least one set of h points that can be shattered, but in general it will not be true that every set of h points can be shattered!


Example: shattering points with oriented hyperplanes in R^n


Three shattered points in the plane - figure

In general, for linear classifiers in R^n, VCdim(\mathcal{H})=n+1.








EXPLAIN HOW VC DIM ESTIMATES THE HYPOTHESIS SPACE CARDINALITY!!!



This bound is not applicable in case of Deep Learning:
The higher expressivity of a DNN would increase the bound, 
that is, it would imply worse generalization. However, it 
is empirically known, that higher expressivity typically 
leads to better generalization results.
Thus, the hypothesis space is not a useful notion in DL.


Consider the input space $\mathcal{X}$ instead: 

The cardinality $|\mathcal{X}|$ is the number of samples, or data points 
$x\in\mathcal{X}$, and each $x$ has an assigned binary label 
$y\in\mathcal{Y}=\{0,1\}$. On total, there are $2^{|\mathcal{X}|}$ possible 
labelings of the input, only one of which is *true* - and the goal of the 
machine learning task is to pick the true labeling from the entire set of 
possibilities.

Essentially, the classification task amounts to partitioning the input space 
in clusters corresponding to the labels - in case of binary classification, 
there are two. The clusters evolve gradually in the process of learning.

The input space $\mathcal{X}$ is divided into $\epsilon$-spheres, denoted as 
$T_{\epsilon}$, meaning that the probability of two data points from the same 
sphere having different labels is less than $\epsilon$. This homogeneity of the 
clusters $T_{\epsilon}$ is achieved through some constraint, which can be expressed 
in the IB formalism as $\langle d_{IB} \rangle = I(X;Y)-I(T;Y)$. Therefore, minimizing
$\langle d_{IB} \rangle$ amounts to maximizing $I(T;Y)$.

Now some information theory: Consider the mapping from $\mathcal{X}$ to $\mathcal{T}$ as 
encoding the input samples $x$ as binary sequences of length $n$.
The total number of (typical) $n$-sequences for $X$ is $2^{nH(X)}$, and for each typical $n$-sequence of $T$-symbols there are $2^{nH(X|T)}$ possible $n$-sequences of $X$.

The number of $n$-sequences that can be transmitted reliably from $X$ to $T$ is
$|\mathcal{T}_{\epsilon}| \sim 2^{H(X)/H(X|T_{\epsilon}})} = 2^{I(T_{\epsilon};X)}$


The number of possible 
function is exponential in the size of this cover, i.e.

$$
\left|\mathcal{H}_{\epsilon}\right| \sim 2^{T_{\epsilon}}
$$

The essential conclusion: the effect of a compression of the input by $K$ bits is equivalent to the effect of increasing the number of training examples by a factor of $2^K$.













