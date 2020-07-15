Title: How to build a Restricted Boltzmann Machine
Date: 2018-05-22
Tags: machine learning, unsupervised learning, Restricted Boltzmann Machines, RBM, tutorial
Author: Anna Go
Slug: RBM-tutorial
Status: draft

RBMs
====


Sources:
--------
- Hinton: practical guide
- Fischer Igel: tutorial
- Larochelle: lecture notes and videos
- Marlin: Inductive Principles for RBM Learning




This article is meant as a practical tutorial providing basic knowledge and guidance to build an RBM.

General Motivation About RBMs
-----------------------------

Restricted Boltzmann Machines (RBM) are top method for unsupervised learning. In the unsupervised setting, only inputs $x$ are given - there are no labels.
The use of unsupervised learning can be:
- automatically extract meaningful features for your data
- leverage the availability of unlabeled data
- add a data-dependent regularizer to training

A RBM is a two-layer undirected graphical model
the first layer consists of observed data variables (or visible units)
the second layer consists of latent variables (hidden units)
The visible layer is fully connected to the hidden layer via pair-wise potentials, while both the visible and hidden layers are restricted to have no within-layer connections

Define $D$ to be the number of data dimensions and $K$ to be the number of hidden units. The space of visible vectors for a binary RBM is $\mathcal{X}=\{0,1\}^D$, while the space of hidden unit vectors is $\mathcal{H}=\{0,1\}^K$. Define $x$ to be a visible vector of size $D\times 1$ and $h$ to be hidden vector of size $K\times 1$.

The RBM model can be defined in terms of the energy function of a joint configuration of the hidden and visible vectors, $E(x,h)$, where $W$ are the weight parameters, $b$/$c$ are the visible/hidden unit bias parameters. We represent $W$ as a $D\times K$ matrix, $b$ as $D\times 1$ vector and $c$ as $K\times 1$ vector. We define $\theta = \{W,b,c\}$ to be the complete set of parameters for the model. Note that we follow the convention that configurations with high probability have low energy.


The joint probability $P_{\theta}(v,h)$ can in turn be defined through the energy.

The partition function involves a sum over all $s^D$ elements of the set $\mathcal{X}$, as well as the $2^K$ elements of the set $\mathcal{H}$. The probability of the visible vector $P_{\theta}(v)$ is obtained by marginalizing over the space $\mathcal{H}$ of hidden vectors.

An important property of binary hidden unit RBMs is that marginalizing over the hidden vectors can be carried out analytically. This allows dfor an equivalent definition of the RBM model in terms of the **free energy** $F(x)$:

$$
P_{\theta}(x) = \frac{1}{Z} \exp\left( -F_{\theta}(x) \right),
Z = \sum\limits_{x'\in\mathcal{X}} \exp\left( -F_{\theta}(x) \right),
F_{\theta}(x) = -\left[ x^Tb + \sum\limits_{k=1}^{K} \log\left( 1+\exp(x^TW_k+c_k) \right) \right]
$$

Note that the partition function still involves marginalizing over all $2^D$ elements of the set $\mathcal{X}$, rendering the computation of the partition function intractable for even moderate $D$.

The first view is useful for deriving stochastic approximation methods based on alternating sampling of the visible and hidden vectors. The second view is useful for applying inductive principles that can not naturally deal with the presence of latent variables.


RBM represents an ansatz for a probability distribution. The goal of training is to fit the parameters of this distribution such that it resembles the distribution of the training data.
The training data is seen as a sample of the unknown target distribution $q$.



Basic scheme:

- BMs with restricted network topology: units organized in two layers (hidden and visible), no connections within the layers
- visible units correspond to the components of an observation
- hidden units model dependencies between the components of observations, can be viewed as non-lin feature detectors
- parametrized generative models representing a PD
- It is "restricted" because no intra-layer connections.




Energy function:

\begin{aligned}
E_{\theta}(v,h) &=  -v^T W h -v^T a - h^T b \\
       			&= - \sum\limits_{i=1}^V a_i v_i - \sum\limits_{j=1}^H b_j h_j - \sum\limits_{ij} v_i W_{ij} h_j
\end{aligned}

where $v_i, h_j$ are binary states of visible unit $i$ and hidden unit $j$, that is, $v_i\in\{0,1\}^V, h_j\in\{0,1\}^H$.

$a_i$, $b_j$ are their respective biases. $W_{ij}$ is the symmetric connection weight between the units.


The network assigns a probability to every possible pair of visible and hidden vector via

$p(v,h) = \frac{1}{Z} e^{-E(v,h)}$,

where the partition function $Z$ is given by summing over all possible pairs of visible and hidden vectors:

$Z = \sum\limits_{v,h} e^{-E(v,h)}$.

The probability that the network assigns to a visible vector, $v$, is given by summing over all possible hidden vectors:

$
p(v) = \frac{1}{Z} \sum\limits_{h} e^{-E(v,h)}.
$

The lower the energy of an input $v$, the higher its assigned probability.

The derivative of the $\log$ probability of a visible vector with respect to a weight is simple:

$$
	\frac{\partial \log\[p(v)\]}{\partial W_{ij}} = \langle v_i h_j \rangle_{data} - \langle v_i h_j \rangle_{model}
$$

where the angle brackets denote expectation values under the distributions specified by the subscript.



My derivation of this result:

\usepackage{physics}
\begin{document}
\[
\dv{Q}{t} = \dv{s}{t}  \quad
\dv[n]{Q}{t} = \dv[n]{s}{t}  \quad
\pdv{Q}{t} = \pdv{s}{t}  \quad
\pdv[n]{Q}{t} = \pdv[n]{s}{t}  \quad
\pdv{Q}{x}{t} = \pdv{s}{x}{t}  \quad
\]
\[
\fdv{F}{g}
\]


\begin{align}

	\pdv{ \log\[p(v)\] }{ W_{ij} } &= \pdv{ }{ W_{ij} } \log\left[ \frac{1}{Z} \sum\limits_{h} e^{-E(v,h)} \right]\\
	&= \pdv{ }{ W_{ij} } \left{ \log \left[ \sum\limits_{h} e^{-E(v,h)} \right] - \log \left[ Z \right] \right} \\
	&= \left[ \sum\limits_{h} e^{-E(v,h)} \right]^{-1} \pdv{ }{ W_{ij} } \sum\limits_{h} e^{-E(v,h)} - 
	   Z^{-1} \pdv{ }{ W_{ij} } Z \\
	&= \left[ Z p(v) \right]^{-1} \pdv{ }{ W_{ij} } \sum\limits_{h} e^{-E(v,h)} - Z^{-1} \pdv{ }{ W_{ij} } Z \\
	&= \left[ Z p(v) \right]^{-1} \sum\limits_{h} v_i h_j e^{-E(v,h)} - Z^{-1} \sum\limits_{v,h} v_i h_j e^{-E(v,h)} \\
	&= \sum\limits_{h} v_i h_j \frac{p(v,h)}{p(v)} - \sum\limits_{v,h} v_i h_j p(v,h) \\
	&= \sum\limits_{h} v_i h_j p(h|v) - \sum\limits_{v,h} v_i h_j p(v,h)
\end{align}

\begin{align}
	\pdv{ }{ W_{ij} } \sum\limits_{h} e^{-E(v,h)} &= \pdv{ }{ W_{ij} } \sum\limits_{h} \exp\left[ \sum\limits_{k} a_k v_k + \sum\limits_{l} b_l h_l + \sum\limits_{kl} v_k W_{kl} h_l \right] \\
	&= e^{a^Tv} \sum\limits_{h} e^{b^Th} \pdv{ \exp\left[ \sum\limits_{l} b_l h_l \right] }{ W_{ij} } \\
	&= e^{a^Tv} \sum\limits_{h} e^{b^Th} v_i h_j e^{v^T W h} \\
	&= \sum\limits_{h} v_i h_j e^{-E(v,h)}
\end{align}

\begin{align}
	\pdv{ }{ W_{ij} } Z &= \pdv{ }{ W_{ij} } \sum\limits_{v,h} e^{-E(v,h)} \\
						&= \sum\limits_{v} \pdv{ }{ W_{ij} } \sum\limits_{h} e^{-E(v,h)} \\
						&= \sum\limits_{v,h} v_i h_j e^{-E(v,h)}
\end{align}





This leads to a very simple learning rule for performing stochastic steepest ascent on the log probability of the training data:

$$
	\Delta W_{ij} = \eta \left( \langle v_i h_j \rangle_{data} - \langle v_i h_j \rangle_{model} \right)
$$

where $\eta$ is the learning rate.

Because there are no direct connections between hidden units in an RBM, it is very easy to get an unbiased sample of $\langle v_i h_j \rangle_{data}$. GIven a randomly selected training image v, the binary state $h_j$ of each hidden unit $j$ is 1 with probability

$$
	p(h_j=1 | v) = \sigma\left( b_j + \sum_i v_i W_{ij} \right) (eq. 7)
$$

where $\sigma$ is the logistic function. $v_i h_j$ is then an unbiased sample.

Similarly, because there are no connections between visible units in an RMB, it is also very is easy to get an unboased sample of the state of a visible unit given a hidden vector $h$:

$$
	p(v_i=1 | h) = \sigma\left( a_i + \sum_j h_j W_{ij} \right). (eq. 8)
$$

Getting an unbiased sample of $\langle v_i h_j \rangle_{model}$, however, is much more difficult. Can be done by starting at any random state of the visible units and performing alternating Gibbs sampling for a very long time. One iteration of alternating Gibbs sampling consists of updating all of the hidden units in parallel using eq. 7, followed by updating all of the visible units in parallel using eq. 8.


Much faster learning procedure proposed by Hinton in 2002:
- start by setting the visibles to a training vector
- then the states of the hiddens are computed in parallel using eq. 7
- once binary states of the hiddens have been chosen, a "reconstruction" is produced by setting each visible to 1 with a probability given by eq. 8
- the change in a weight is then given by

$$
	\Delta W_{ij} = \eta \left( \langle v_i h_j \rangle_{data} - \langle v_i h_j \rangle_{reconstr} \right)
$$

A simplified version of the same learning rule is applied to the biases, it uses the states of individual units instead of pairwise products.

The learning works well even though it is only crudely approximating the gradient of the log probability of the training data. It is much more closely approximating the gradient of another objective function, called the Contrastive Divergence. The CD is the difference between two KL divergences, but the described procedure ignores one tricky term in this objective function, so it is not even following that gradient. Sutskever and Tieleman have shown that it does not follow the gradient of any function. Nevertheless, it works well enough in many significant applications.


RBM typically learn better models if more steps of alternating Gibbs sampling are used before collecting the statistics for the second term in the learning rule, which will be called the negative statistics. $CD_n$ will refer to denote learning using $n$ full stapes of alternating Gibbs sampling.




3. How to collect statistics when using CD
------------------------------------------

Assume:
- hidden and visible units are binary
- the purpose of learning is to create a good generative model of the set of training vectors


Updating the hidden states:
Assume using CD$_1$; the hiddens should have binary states when they are being driven by a data vector.
The probability of turning on a hidden unit j is computed by applying the logistic function to its total input

$$
	p(h_j=1) = \sigma\left( b_j+\sum\limits_i v_i W_{ij} \right)
$$
and the hidden unit turns on if this probability is greater than a random number uniformly distributed between 0 and 1.

It is very important to make these hidden states binary rather than using the probabilities themselves!

For the last update of the hiddens, however, use the probabilities itself to avoid unnecessary sampling noise.
When using CD$_n$, only the final update of the hiddens should use the probability.



Updating the visible states:
When generating a reconstruction, stochastically pick 0 or 1 with probability determined by the total top-down input:

$$
	p_i = p(v_i=1) = \sigma\left( a_i + \sum\limits_j h_jW_{ij} \right)
$$

However, it is common to use the probability itself instead of sampling a binary value, since it reduces sampling noise and thus allows faster learning. This is not as problematic as in case of the hiddens.


Collecting the statistics needed for learning

SAsuming that the visibles are using real-valued probabilities instead of binary values, there are two sensible ways to collect the positive statistics for the connection between visible unit i and hidden unit j:

$\langle p_i h_j \rangle_{data}$ or $\langle p_i p_j \rangle_{data}$

where $h_j$ is a binary state that takes value 1 with probability $p_j$.
Using $h_j$ is closer to the mathematical model of an RBM, but using $p_j$ usually has less sampling noise which allows slightly faster learning.


Getting a learning signal for CD$_1$:
When the hidden units are being driven by data, use stochastic binary states only.
When the hidden units are being driven by data, use probabilities without sampling.

Assuming the visibles use the logistic function, use probabilities for both the data and the reconstruction.

When collecting pairwise statistics for learning weights or the individual statistics for learning biases, use the probabilities, not the binary states, and make sure the weights have random initial values to break symmetry.










from: Fischer, Igel
-------------------

1. Introduction
---------------

Boltzmann Machines (BMs):

	- bidirectionally connected networks of stochastic processing units
	- or undirected graphical models, also known as Markov random fields
	- can learn important aspects of an unknown probability distribution (PD) based on samples from this distribution
	- learning = adjusting the parameters s.t. the PD represented by the BM fits the training data as well as possible
	- however, the process is difficult and time-consuming

Restricted BMs:

	- BMs with restricted network topology: units organized in two layers (hidden and visible), no connections within the layers
	- visible units correspond to the components of an observation
	- hidden units model dependencies between the components of observations, can be viewed as non-lin feature detectors
	- parametrized generative models representing a PD
	- learning is simpler
	- after successful learning, an RBM provides a closed-form representation of the distribution underlying the observations

Computational difficulties:
	- computing the likelihood of an undirected model or its gradient for inference is i.g. computationally intensive, 
	also for RBMs
	- therefore, sampling-based methods are employed to approximate the likelihood and its gradient
	- samploing from an undirected graphical model is i.g. not straightforward, but for RBMs Markov Chain Monte Carlo (MCMC) methods are easily applicable in the form of Gibbs sampling




- single as well as stacked RBMs can be reinterpreted as deterministic feed-forward NNs
- the NN corresponding to a trained RBM or DBB can be augmented by an output layer, where units in the new added output layer represent labels corresponding to observations; then the model corresponds to a standard neural network for classification or regression that can be further trained by standard supervised learning algos
- this initialization (unsupervised pre-training) of the feed-forward NN's weights based on a generative model helps





2. Graphical Models
-------------------

Zweck of graphical models:

- Probabilistic graphical models describe probability distributions (PDs) 
  by mapping conditional (in)dependence properties between random variables 
  on a graph structure.

- Two sets of RVs X_1, X_2 are cond indep given a set of RVs X_3 if
  p(X_1, X_2 | X_3) = p(X_1|X_3)p(X_2|X_3).

- Visualization by graphs is helpful for

	- understanding and motivating probab models
	- deriving complex computations by using algos exploiting the graph structure


2.1 Undirected Graphs and Markov Random Fields
----------------------------------------------

Fundamental concepts of Graph Theory
------------------------------------

- an undirected graph is a tuple G=(V,E), where V is a finite set of nodes and E is a set of undirected edges
- an edge consists of a pair of nodes from V
- if there exists an edge between two nodes v and w, i.e. {v,w} \elem E, w belongs to the neighborhood of v and v.v.
- the neighborhood \mathcal{N}_v = {w\in V: {w,v}\in E} of v is defined by the dset of nodes connected to v
- a clique is a subset of V in which all nodes are pairwise connected
- a clique is maximal if no node can be added such that the resulting set is still a clique
- denote by C the set of all maximal cliques of an undirected graph
- a path from v_1 to v_m is a sequence of nodes v_1, v_2, ..., v_m \in V with {v_i,v_{i+1}}\in E for i=1,...,m-1
- a set \mathcal{V} \sub V separates two nodes v\notin \mathcal{V} and w\notin \mathcal{V}, if every path from v to w contains a node from \mathcal{V}

- associate a random variable (RV) X_v, taking values in a state space \Lambda_v, with each node v in an undirected graph G=(V,E)
- for slimmer notation, assume \Lambda_v = \Lambda for all v\in V
- the RVs \bold{X}=(X_v)_{v\in V} are called Markov random field (MRF) if
  the joint PD p fulfills the (global) Markov property wrt the graph:

  For all disjunct subsets \mathcal{A}, \mathcal{B}, \mathcal{S} \subset V, 
  where all nodes in \mathcal{A} and \mathcal{B} are separated by \mathcal{S},
  the variables (X_a)_{a\in \mathcal{A}} and (X_b)_{b\in \mathcal{B}} 
  are conditional independent given (X_s)_{s\in \mathcal{S}}, i.e. 
  for all \bold{x}\in\Lambda^{|V|} it holds
  p((x_a)_{a\in\mathcal{A}}|(x_t)_{t\in\mathcal{S}\cup \mathcal{B}}) = p((x_a)_{a\in\mathcal{A}}|(x_t)_{t\in\mathcal{S})

- a set of nodes MB(v) is called the Markov blanket of node v 
  if for any set of nodes \mathcal{B} with v\notin\mathcal{B} we have 
  p(v|MB(v),\mathcal{B}) = p(v|MB(v))
  this means that v is conditional independent from any other variables given MB(v)
- in a MRF, the Markov blanket MB(v) is given by the neighborhood \mathcal{N}_v of v,
  a fact that is also referred to as local Markov property


--> conditional independence of RVs and the factorization properties of the joint PD are closely related
The Hammersley-Clifford Theorem states that a strictly positive distribution p satisfies the Markov property wrt an undirected graph G iff p factorizes over G.
A distribution is said to factorize over an undirected graph G with maximal cliques C if there exists a set of non-negative functions {\psi_C}_{C\subset \mathcal{C}}, called potential functions, with

  \forall \bold{x, \hat{x}} \in \Lambda^{|V|}: (x_c)_{c\in C} = (\hat{x}_c)_{c\in C} \Rightarrow \psi_C(\bold{x}) = \psi_C(\hat{\bold{x}})
  and
  p(x) = \frac{1}{Z} \Prod \limits_{C\in \mathcal{C}} \psi_C(\bold{x})

The normalization constant Z = \sum_{\bold{x}} \Prod_{C\in \mathcal{C}} \psi_C(\bold{x}_C) is called partition function.

If p is strictly positive, the same holds for the potential functions. Thus we can write

p(\bold{x}) = \frac{1}{Z} \Prod \limits_{C\in \mathcal{C}} \psi_C(\bold{x}_C) = ... = \frac{1}{Z} e^{-E(\mathcal{x})}


where E=\sum_{C\in \mathcal{C}} \ln\psi_C(\bold{x}_C) we call the energy function.


Thus, due to the Hammersley-Clifford-Theorem:

The PD of every MRF can be expressed as a Gibbs distribution. 


2.2 Unsupervised Learning
-------------------------

means learning (important aspects of) an unknown distribution $q$ based on sample data.
If the structure of the graphical model is known and the energy function belongs to a known family of functions parameterized by $\theta$, then unsupervised learning of a data distribution with an MRF means adjusting the parameters $\theta$.


Consider training data $S=\{x_1, ..., x_l\}$, with data samples being i.i.d., i.e., independently drawn from some unknown distribution $q$.
Standard way of estimating the parameters of a statistical model is maximum-likelihood estimation. For MRF, this corresponds to finding the parameters that maximize the probability of $S$ under the MRF distribution; i.e., training goal is finding the parameters $\theta$ that maximize the likelihood given the training data.

The likelihood of an MRF maps parameters $\theta$ from the parameter space $\Theta$ to 

$$
	\mathcal{L}(\theta|S) = \prod\limits_{i=1}^l p(x_i|\theta).
$$

Maximizing the likelihood is the same as maximizing the log-likelihood given by:

$$
	\ln \mathcal{L}(\theta|S) = \ln \prod\limits_{i=1}^l p(x_i|\theta) = \sum\limits_{i=1}^l \ln p(x_i|\theta).
$$

For the Gibbs distribution of an MRF it is in general not possible to find the maximum likelihood parameters analytically, and therefore numerical approximation methids are used, such as gradient ascent.

Maximizing the likelohood is equivalent to minimizing the distance between the unknown distribution $q$ underlying $S$ and the distribution $p$ of the MRF in terms of the KL-divergence, which for a finite state space $\Omega$ is given by:

$$
	KL(q||p) = \sum\limits_{x\in\Omega} q(x)\ln\frac{q(x)}{p(x)}
$$

non-symmetric measure

can be written as difference between entropy of $q$ and a second term, only the latter depends on the parameters subject to optimization

Approximating the expectation over $q$ in this term by the training samples from $q$ results in 
the log-likelihood. Therefore, maximizing the log-likelihood corresponds to minimizing KL-divergence.

Optimization by Gradient Ascent
-------------------------------

If it is not possiblet to find parameters maximizing the log-likelihood analytically, the usual way to find them is gradient ascent on the log-likelihood. Update rule:





3. Markov Chains and Markov Chain Monte Carlo Techniques
--------------------------------------------------------

Markov Chains provide a methods to draw samples from probability distributions like the Gibbs distribution of an MRF. Gibbs sampling is a technique often used for MRF training and in particular for training RBMs.

3.1 Markov Chain and Convergence to Stationarity

A Markov Chain is a time descrete stochastic process for which the Markov property holds. That is, a family of random variables $X=\{ X^{(k)} | k\in \mathbb{N}_0 \}$ which take valus in a (finite) set $\Omega$, an for which $\forall k \geq 0$ and $\forall j, i, i_0, ..., i_{k-1} \in \Omega$ it holds

$$
	p_{ij}^k = ...
$$

i.e., the next state of the system depends only on the current state and not on the sequence of states that preceded it.


The chain is called homogeneous if $\forall k\geq 0, p_{ij}^k = p_ij$, and the matrix $\mathbb{P} = (p_{ij})_{i,j\in\Omega}$ is called the transition matrix.

The PD $\mu^{(k)}$ of $X^{(k)}$ is given by $\mu^{(k)T} = \mu^{(0)T}\mathbb{P}$, where $\mu^{0}$ is the PD of $X^{(0)}$, given by the probability vector $\mu^{0} = (\mu^{0}(i))_{i\in\Omega}$ with $\mu^{0}(i) = P(X^{(0)}=i)$.

A PD $\pi$ for which it holds $\pi^T = \pi^T \mathbb{P}$ is called stationary.
If the Markov chain for any time $k$ reached the stationary distribution $\mu^{(k)}=\pi$, all subsequent states will be distributed accordingly, i.e. $\mu^{(k+n)}=\pi \forall n \in \mathbb{N}$.

A sufficient (but not necessary) condition for a distribution $\pi$ to be stationary w.r.t. a Markov chain described by the transition probabilities $p_{ij}, i, j \in \Omega$ is that the **detailed balance**

$$
	\pi(i) p_{ij} = \pi(j) p_{ji}
$$

$\forall i,j \in \Omega$, holds.

Especially relevant are Markov chains for which it is known that there exists a unique stationary distribution.

For finite $\Omega$, this is the case if the Markov chain is **irreducible**.

A Markov chain is irreducible if one can get from any state in $\Omega$ to any other ina finite number of transitions. More formally, if $\forall i,j \in \Omega \exists k\gt 0$ with $P(X^{(k)}=j | X^{(0)}=i) \gt 0$.


A Markov chain is aperiodic if $\forall i \in \Omega$ the greatest common divisor of $\{k|P(X^{(k)}=i|X^{(0)}=i)\gt 0 \hat k\in\mathbb{N}_0\}$ is 1.

An irreducible and aperiodic Markov chain ona finite state space is guaranteed to converge to its stationary distribution. That is, for an arbitrary starting distribution $\mu$ it holds:

$$
	\lim_{k\to\inf} d_V(\mu^TP^k, \pi^T) = 0,
$$

where $d_V$ is the **distance of variation**, defined as

$$
	d_V(\alpha, \beta) = \frac{1}{2}|\alpha-\beta| = \frac{1}{2}\sum\limits_{x\in\Onega}|\alpha(x)-\beta(x)|
$$


for two distributions $\alpha, \beta$ on a finite state space $\Omega$.

MCMC methods make use of the convergence theorem for producing samples from certain distributions by setting up a Markov chain that converges to the desired distributions:

Suppose you want to sample from a finite distribution $q$. You construct an irreducible and aperiodic Markov chain with stationary distribution $\pi = q$ - which is a nontrivial task. If $t$ is large enough, a sample $X^{(t)}$ from the constructed chain is then approximately a sample from $\pi$ and therefore form $q$. Gibbs sampling is such a MCMC method.



3.2 Gibbs Sampling
------------------


belongs to the class of Metropolis-Hastings algorithms.

a simple MCMC algo for producing samples from the joint PD of multiple random variables.

basic idea: update each variable subsequently based on its conditional distribution given the satte of the others.