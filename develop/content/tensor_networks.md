Title: Tensor Networks: Putting Quantum Wavefunctions into Machine Learning
Date: 2016-11-7 19:00
Category: Articles
Tags: tensor networks, quantum mechanics, machine learning, kernel learning, support vector machines
Authors: Miles Stoudenmire
Summary: Tensor networks are a powerful tool for compressing quantum wavefunctions developed in the physics community. Parameterizing a special class of models with tensor networks brings the full power of tensor networks to machine learning tasks.
Slug: tensor-network

## Why tensor networks?

If you follow machine learning, you have definitely heard of [neural networks][21].
If you are a physicist, you may have heard of [tensor networks][8] too.
Both are schemes for assembling simple units (neurons or tensors) into complicated functions: 
decision functions in the case of machine learning or wavefunctions in the case of quantum mechanics.

But tensor networks have only linear elements. Neural networks crucially 
require *non-linear* elements for their success (specifically, non-linear [neuron activation functions][1]). 
And neural networks have been so wildly successful in recent years that leading tech companies are 
staking their futures on them. 

So why bother with linear tensor networks if non-linearity is the key to success?

The key is dimensionality. Problems which are difficult to solve in low dimensional spaces
become easier when "lifted" into a higher dimensional space. 
Think how much easier your day would be if you could move freely in the extra 
dimension we call time. Data points hopelessly intertwined in their native, low-dimensional
form can become linearly separable when given the extra breathing room of more dimensions.

But extra dimensions come at a steep price, known as the "curse of dimensionality". 
When constructing a high dimensional space from products of smaller spaces, its dimension
grows exponentially. Optimizing even a linear classifier in an exponentially big space becomes
costly very quickly.

This is the problem tensor networks solve: if you can live with a reduced set of
linear transformations, then tensor networks let you manipulate objects in an exponentially high 
dimensional space easily and efficiently.

Tensor networks can do linear things within spaces so big, there's no reason they couldn't be
as effective as neural networks, which do non-linear things to much smaller spaces.
But whether they can really compete with neural nets remains to be seen!

## Tensor networks in physics

Quantum physicists have faced the challenges of exponentially large spaces
since the days of Dirac. Wavefunctions describing the collective state
of N quantum particles live in just such a high-dimensional space. For decades, approaches
to deal with the huge size of quantum state space relied on using a modest set of ad-hoc variables 
to parameterize a large wavefunction, then optimizing these variables and hoping for the best. 
Or physicists would avoid wavefunctions altogether in favor of large-scale simulations of 
particle motions (e.g. quantum Monte Carlo methods).

But the exponential size of quantum wavefunction space turns out to be an illusion. 
The wavefunctions typically occurring in nature are just a tiny fraction of 
the huge mathematical space they belong to. And nearly all of this small corner 
of wavefunction space is within reach of tensor networks.

The first tensor network developed in the late 80's was the "matrix product state" or MPS. 
An MPS is a scheme to encode wavefunction amplitudes as the
product of matrices (surrounded by boundary vectors, so the result is a 
scalar). For S=1/2 spins on a lattice, there are two matrices associated to each lattice site; 
which matrix goes into the product depends on whether the spin is up or down. 
If the matrix sizes required to capture the true wavefunction 
do not grow with system size, then the MPS format compresses exponentially 
many parameters down to only a linear number of parameters! (That is, linear in the system size.) 

Whether the MPS approach can usefully compress the wavefunction of a physical system
hinges on its dimensionality and how much *quantum entanglement* it has across various spatial cuts.
For "lightly" entangled, one-dimensional quantum states, such as ground states 
of local 1D Hamiltonians, MPS work incredibly well. There is a proof of 
their optimality for a wide set of cases. MPS are even useful for two-dimensional
systems with extra computational effort.

Inspired by the success of the MPS tensor network, other tensor network proposals
followed, such as the PEPS network for two-dimensional quantum systems ([Verstraete,2004][11])
and the MERA network for critical systems ([Vidal,2007][12]). Both of these are trickier to use than
MPS, but offer a more compression, and in the case of MERA, deeper physics insights.

## Tensor network machines

High-dimensional spaces pop up everywhere in machine learning theory. So tensor 
networks seem a natural tool to try (with benefit of hindsight, of course). 
There have already been creative proposals to use MPS
(also known as *tensor trains*) to parameterize Bayesian models ([Novikov,2014][15]); to perform PCA/SVD
analysis of huge matrices ([Lee,2014][16]); to extract useful features from data tensors ([Bengua,2015][20]); and to parameterize neural net layers ([Novikov,2015][17]).

But which machine learning framework is most natural for tensor 
networks, in the sense of applying the full power of optimization techniques, insights, and generalizations
of MPS developed in physics?

Two recent papers propose that tensor networks could be especially powerful 
 in the setting of non-linear kernel learning: [Novikov,Trofimov,Oseledets (2016)][18] and [Stoudenmire,Schwab (2016)][19].
Kernel learning basically means optimizing a decision function of the form
$$
f(\mathbf{x}) = W\cdot\Phi(\mathbf{x})
$$
where @@\mathbf{x}@@ is a moderate-size vector of inputs (e.g. pixels of an image) and the output
@@f(\mathbf{x})@@ determines how to classify each input. 

The function @@\Phi(\mathbf{x})@@ is known as the *feature map*. Its role is to "lift" 
inputs @@\mathbf{x}@@ to a higher dimensional *feature space* before they are classified. 
The feature map @@\Phi@@ is a non-linear yet rather generic and simple function, in the sense of having only a few
adjustable "hyper parameters" (a common example of a feature map is the one associated with the [polynomial kernel][22]).

The weight vector @@W@@ contain the actual parameters of the model to be learned. The clever thing about
kernel learning is although the inputs enter non-linearly via the feature map @@\Phi@@, the
weights @@W@@ enter *linearly* &mdash; the model is just a linear classifier in feature space. 
The number of weights is determined by the dimensionality of the feature space (the target space of @@\Phi@@).
A higher-dimensional feature space can produce a more powerful model, but also requires 
optimizing more weights. In some common approaches, the number of weight parameters
to optimize can be exponentially big or even infinite.

But this smells like a perfect problem for tensor networks: finding the best
set of linear weights in an exponentially big space.


To obtain a weight vector with a structure like a quantum wavefunction, and
suitable for the tensor network approximations used in physics,
recall that combining independent quantum systems corresponds to taking a tensor
product of their state spaces. For a feature map mimicking this rule,
first map each component @@x\_j@@ of the input vector @@\mathbf{x}@@ into a
small d-dimensional vector via a *local feature map* @@\phi(x\_j)@@. Then
combine these local feature vectors using a tensor product:
$$
\Phi^{s\_1 s\_2 \cdots s\_N}(\mathbf{x}) = \phi^{s\_1}(x\_1) \otimes \phi^{s\_2}(x\_2) \otimes \cdots \otimes \phi^{s\_N}(x\_N)
$$
The result is a @@d^N@@ dimensional feature vector. However, it has the structure
of a product-state wavefunction (or rank-1 tensor in applied math parlance), making it
easy to store and manipulate.

<figure>
<img style="width:250px;" src="/images/phi.png"/>
<figcaption>Feature map as a tensor product of local feature maps</figcaption>
</figure>

With the above construction, @@W@@ also has @@d^N@@ components, and has the structure of an
@@N^\text{th}@@ order tensor (N indices of size d). This is an object in the same
mathematical space as a wavefunction of N spins (d=2 corresponding to S=1/2, d=3 to S=1, etc.).
But while some wavefunctions in state space (now feature space) are readily 
compressible into tensor networks, the vast majority cannot be compressed at all. 
Do weights of machine learning models live in the 
same nicely compressible part of state space as tensor networks?

<figure>
<img style="width:350px;" src="/images/decision.png"/>
<figcaption>Decision function with a tensor-product feature map (top) and MPS approximation of weights (bottom)</figcaption>
</figure>

In lieu of a general answer, we did an experiment. Our work ([Stoudenmire,2016][19])
considered grayscale image data of handwritten digits (the MNIST data set). Taking an
ad-hoc local feature map which maps grayscale pixels into two-component vectors mimicking
S=1/2 spins, we trained a model to distinguish the digits 0,1,2,...,9. We approximated
the weight tensor @@W@@ as an MPS and optimized it by minimizing a squared-error cost
function. The results were surprisingly good: for a very modest
size of 100 by 100 matrices in the MPS, we obtained over 99% classification accuracy on the
training and test data sets. The experiments of [Novikov,2016][18] considered another
standard data set and synthetic, highly correlated data and found similarly good results.

## A Linear Path Ahead

Compressing the weight tensor into an MPS is interesting, but what are the benefits for machine learning?

One immediate gain comes from optimizing the weights directly. 
The typical way to avoid the costs 
of high-dimensional feature space is avoid touching the weights by using the so-called "kernel trick" 
which keeps the weights hidden in favor of alternate "dual variables". But this trick
requires constructing a kernel matrix whose number of entries grows quadratically
with training set size.
In the era of big data, this scaling issue is cited
as one reason why neural nets have overtaken kernel methods.
In contrast, optimizing the weights as an MPS scales at
most linearly in the training set size (for a fixed size of the MPS matrices).
The cost of applying or testing the model is independent of training set size.

The simplicity of a model where the decision function depends linearly on the weights
also makes it straightforward to import past insights and powerful optimization
techniques developed in the physics community.
Instead of using gradient descent / backpropagation, we borrowed the powerful DMRG technique
for optimizing the weights (also known as alternating least squares in applied math). 
Not only is DMRG very efficient, but it is adaptive, allowing
the matrix dimensions of our MPS to grow in regions where more resources are needed
and shrink in less important regions, such as near the boundary of an image where the pixels
do not vary. In the future we could take advantage of DMRG developments, such
as the use of conserved "quantum numbers"; continuous MPS for data in the continuum limit;
or real-space parallel DMRG for optimizing large models on distributed hardware.

Finally, tensor networks may enhance interpretability and generalization. While more
work is needed on these fronts, the linearity of tensor networks could lead to rapid
progress. The MPS format already lends itself to an interpretation as 
an "finite state machine" processed in different ways depending
on the input data. Putting in a tensor network like the MERA instead might lead to interpretations
similar to deep neural network architectures, yet easier to analyze 
by virtue of being linear. Intriguingly, a tensor network model need not obey 
the "representer theorem"; this means tensor network models do not just interpolate the 
training set data, which could improve generalization.

Will the tensor network approach continue to be successful for more difficult 
data sets? How do its costs compare to neural networks for problems where 
both yield similar performance? Can tensor networks outperform neural networks
on certain problems? 

Given the excellent track record of tensor networks in physics, and the 
deep theoretical underpinnings of kernel learning the future could be bright.


<br/>
<br/>
~~~~~~~~~~~~~~~~~~~
<br/>
<br/>


<!--

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

-->


## Appendix: A brief history of tensor networks

Tensor networks as a computational tool originated in the field of quantum physics
(not to be confused with [neural tensor networks][23]). Early on
they were considered for describing the mathematical structure of exotic states of quantum
spin models, such as the [AKLT chain][2] ([Accardi,1981][3]; [Lange,1994][4]).

The tensor network known as the matrix product state (MPS) came into prominence with the 
development of the DMRG algorithm ([White,1992][5]; [Schollwoeck,2011][24]), later shown to be a particularly efficient
algorithm for optimizing MPS to approximate ground states of quantum systems ([Ostlund,1995][6]).

Since then, tensor networks have been influential in many areas of physics such as quantum chemistry
([Chan,2011][7]), condensed matter physics ([Bridgeman,2016][8]), and even in quantum gravity, where
tensor networks have been proposed as a model of how gravity could emerge from quantum mechanics
([Swingle,2012][9]; [Quanta Magazine,2015][10]). Some key developments in tensor network technology
were the proposal of the PEPS network for two-dimensional quantum systems ([Verstraete,2004][11])
and the MERA network for critical systems ([Vidal,2007][12]).

More recently, there has been growing interest in tensor networks within the applied mathematics community 
following the proposal of the hierarchical Tucker ([Hackbush,2009][13]) and tensor train ([Oseledets,2011][14]) 
decompositions (respectively known in the physics literature as the tree tensor network and MPS decompositions).


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
[15]: http://www.jmlr.org/proceedings/papers/v32/novikov14.pdf
[16]: http://arxiv.org/abs/1410.6895
[17]: http://arxiv.org/abs/1509.06569
[18]: http://arxiv.org/abs/1605.03795
[19]: http://arxiv.org/abs/1605.05775
[20]: http://arxiv.org/abs/1503.00516
[21]: http://neuralnetworksanddeeplearning.com
[22]: https://en.wikipedia.org/wiki/Polynomial_kernel
[23]: http://www.socher.org/index.php/Main/ReasoningWithNeuralTensorNetworksForKnowledgeBaseCompletion
[24]: http://dx.doi.org/10.1016/j.aop.2010.09.012
