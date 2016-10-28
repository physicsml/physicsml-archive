Title: Tensor Networks: Putting Quantum Wavefunctions into Machine Learning
Date: 2016-10-27 10:00
Category: Articles
Tags: tensor networks, quantum mechanics, machine learning, kernel learning, support vector machines
Authors: Miles Stoudenmire
Summary: Tensor networks are a powerful tool for compressing quantum wavefunctions developed in the physics community. 
Slug: tensor-network
Status: draft

## Why tensor networks?

If you follow machine learning, you have definitely heard of neural networks. 
If you are a physicist, you may have heard of tensor networks too.
Both are schemes for assembling small units into very complex functions: a decision/classification function in the case of machine learning or a wavefunction in the case of quantum mechanics.

But tensor networks differ from neural networks as they are composed only of linear elements. Neural networks crucially require *non-linear* elements for their success (specifically, [neuron activation functions][1]). And neural networks have been so wildly successful in recent years that leading tech companies are staking their entire futures on them. 

So why bother with linear tensor networks if non-linearity is the key to success?

The key is dimensionality. Problems which are difficult to solve in low dimensional spaces
 become easier when "lifted" into a higher dimensional space. 
 Think how much easier your day would be if you could move freely in that extra 
dimension we call time. Data points which are hopelessly intertwined in their native, low-dimensional
form can become linearly separable when given the extra breathing room of more dimensions.

But extra dimensions come at a price, known as the "curse of dimensionality". 
When constructing a high dimensional space from products of smaller spaces, the number of dimensions
grows exponentially. Even optimizing a linear classifier in an exponentially big space becomes
costly very quickly.

This is the problem tensor networks solve: if you can get away with a restricted set of
linear transformations, then tensor networks let you manipulate objects in an exponentially high 
dimensional space easily and efficiently.

Tensor networks can do linear things within spaces that are so big, there's no reason they couldn't be
as effective as neural networks, which do non-linear things to much smaller spaces.

## Taking off to feature space

Lifting data into a high-dimensional space to classify it is not a new idea. It is the starting
point for the very elegant support vector machine (SVM) method, and non-linear kernel learning
methods more broadly.

Before classifying an input data vector @@\mathbf{x}@@, kernel methods lift the vector to a higher-dimensional
*feature space* by applying a feature map @@\Phi(\mathbf{x})@@ to them.

As a simple example, say the input vector is @@\mathbf{x} = (x\_1,x\_2)@@. Then we can lift this vector
by defining a feature map as follows:
$$
\Phi(\mathbf{x}) = (1,\,x\_1,\,x\_2,\, x\_1^2 ,\,x\_2^2)
$$
This non-linear map takes the two-dimensional vector @@\mathbf{x}@@ into a five-dimensional vector @@\Phi(\mathbf{x})@@.

We then classify our data with a decision function of the form
$$
f(\mathbf{x}) = W \cdot \Phi(\mathbf{x})
$$
which is just a linear classifier applied to the vector @@\Phi(\mathbf{x})@@.
It is a linear classifier in *feature space*.

What have we gained? Linear classifiers are straightforward to optimize. If there is a hyperplane that
can separate our data, it only takes a bit of linear algebra to find it. By solving a linear problem,
we get the full power of a non-linear decision function. (@@\Phi(\mathbf{x})@@ is non-linear so
@@f(\mathbf{x})@@ will be too.)

As an example, say we need to separate all inputs @@\mathbf{x}@@ with
@@|\mathbf{x}| < 1@@ from all other inputs with @@|\mathbf{x}| > 1@@. The decision boundary
will be a circle, which we cannot make with a plain "unlifted" linear classifier of the 
form @@\mathbf{n} \cdot \mathbf{x}@@. But in our lifted model, by choosing @@W = (-1,0,0,1,1)@@ we obtain
an @@f(\mathbf{x})@@ which is negative for points inside our circle and positive for points outside.

There is a catch of course: a feature map like the example above may not be high-dimensional or 
non-linear enough to make the data separable for the toughest problems. We can try to solve this 
by mapping to a really high dimensional space as follows:

\begin{align}
\Phi(\mathbf{x}) = & (1,\,x\_1,\,x\_2,\,\ldots,\,x\_N,\, \\\\
 &\  x\_1\cdot x\_2,\ \ \ x\_1 \cdot x\_3,\,\ldots \\\\
 &\  x\_1 \cdot x\_2 \cdot x\_3,\ \ \  x\_1 \cdot x\_2 \cdot x\_4,\,\ldots \\\\
 &\  \ldots, \\\\
 &\  x\_1 \cdot x\_2 \cdot x\_3 \cdot x\_4 \cdots x\_N \, )
\end{align}

The above feature map has all possible products of the components of @@\mathbf{x}@@ to all orders.
But if you count the number of terms above,
you will see that @@\Phi(\mathbf{x})@@ is a @@2^N@@-dimensional vector where @@N@@ is the number of entries
of @@\mathbf{x}@@. That means the weight vector @@W@@ would need to be @@2^N@@ dimensional also. 
There is no way to directly manipulate a vector that large once @@N@@ gets bigger than 40 or so.

## Tensor network machines

Quantum physicists have known about the difficulties of 
exponential spaces since the days of Dirac. Wavefunctions describing the collective
state of @@N@@ quantum particles live in just such a high-dimensional space. For decades, approaches
for dealing with these huge wavefunctions relied on guessing a good, small set of parameters 
to optimize and hoping for the best. Or physicists avoided wavefunctions 
in favor of large-scale simulations of the particle motions (quantum Monte Carlo methods).

But it turns out the exponential size of quantum wavefunction space
is mostly an illusion. The kinds of wavefunctions that normally occur in nature
make up just a tiny fraction of the larger space they belong to. This smaller corner
of wavefunction space is precisely the part tensor networks can reach.


(--- Done through here ---)


## Other applications of tensor networks to machine learning and data

Putting MRFs on a tensor train. Novikov. JMLR 2014. http://jmlr.org/proceedings/papers/v32/novikov14.pdf
Tensorizing neural networks. Novikov. NIPS 2015 https://arxiv.org/abs/1509.06569
Matrix Product State for Feature Extraction of Higher-Order Tensors. Bengua. 2015. https://arxiv.org/abs/1503.00516
Very Large-Scale Singular Value Decomposition Using Tensor Train Networks. Lee & Cichocki. 2014. https://arxiv.org/abs/1410.6895

## A brief history of tensor networks

Tensor networks as a computational tool originated in the field of quantum physics. Early on
they were considered for describing the mathematical structure of exotic states of quantum
spin models, such as the [AKLT chain][2] ([Accardi,1981][3]; [Lange,1994][4]).

The tensor network known as the matrix product state (MPS) came into prominence with the 
development of the DMRG algorithm ([White,1992][5]), later shown to be a particularly efficient
algorithm for optimizing MPS for representing ground states of quantum systems ([Ostlund,1995][6]).

Since then, tensor networks have been influential in many areas of physics such as quantum chemistry
([Chan,2011][7]), condensed matter physics ([Bridgeman,2016][8]), and even in quantum gravity, where
tensor networks have been proposed for understanding how gravity could emerge from quantum mechanics
([Swingle,2012][9]; [Quanta Magazine,2015][10]). Some key developments in tensor network technology
were the proposal of the PEPS network for two-dimensional quantum systems ([Verstraete,2004][11])
and the MERA network for critical systems ([Vidal,2007][12]).

More recently, there has been growing interest in tensor networks within the applied mathematics community 
following the proposal of the hierarchical Tucker ([Hackbush,2009][13]) and tensor train ([Oseledets,2011][14]) 
decompositions (originally known as the tree tensor network and MPS decompositions, respectively, in the physics literature).


[1]: https://en.wikipedia.org/wiki/Activation_function
[2]: https://en.wikipedia.org/wiki/AKLT_model
[3]: http://www.sciencedirect.com/science/article/pii/0370157381900703
[4]: https://arxiv.org/abs/cond-mat/9409107
[5]: http://link.aps.org/doi/10.1103/PhysRevLett.69.2863
[6]: http://dx.doi.org/10.1103/PhysRevLett.75.3537
[7]: http://www.annualreviews.org/doi/abs/10.1146/annurev-physchem-032210-103338
[8]: https://arxiv.org/abs/1603.03039
[9]: https://doi.org/10.1103/PhysRevD.86.065007
[10]: https://www.quantamagazine.org/20150428-how-quantum-pairs-stitch-space-time/
[11]: https://arxiv.org/abs/cond-mat/0407066
[12]: http://link.aps.org/doi/10.1103/PhysRevLett.99.220405
[13]: http://rdcu.be/l1K0
[14]: http://dx.doi.org/10.1137/090752286
