Title: Papers
Date: 2016-10-27 11:00

## Applying Machine Learning to Physics


- ["Deep Learning Phase Segregation"](
http://arxiv.org/abs/1803.08993v1
"Phase segregation, the process by which the components of a binary mixture
spontaneously separate, is a key process in the evolution and design of many
chemical, mechanical, and biological systems. In this work, we present a
data-driven approach for the learning, modeling, and prediction of phase
segregation. A direct mapping between an initially dispersed, immiscible binary
fluid and the equilibrium concentration field is learned by conditional
generative convolutional neural networks. Concentration field predictions by
the deep learning model conserve phase fraction, correctly predict phase
transition, and reproduce area, perimeter, and total free energy distributions
up to 98% accuracy."),
Amir Barati Farimani, Joseph Gomes, Rishi Sharma, Franklin L. Lee, Vijay S. Pande,
arXiv: [1803.08993](http://arxiv.org/abs/1803.08993v1),
3/2018

- ["A high-bias, low-variance introduction to Machine Learning for
  physicists"](
http://arxiv.org/abs/1803.08823v1
"Machine Learning (ML) is one of the most exciting and dynamic areas of modern
research and application. The purpose of this review is to provide an
introduction to the core concepts and tools of machine learning in a manner
easily understood and intuitive to physicists. The review begins by covering
fundamental concepts in ML and modern statistics such as the bias-variance
tradeoff, overfitting, regularization, and generalization before moving on to
more advanced topics in both supervised and unsupervised learning. Topics
covered in the review include ensemble models, deep learning and neural
networks, clustering and data visualization, energy-based models (including
MaxEnt models and Restricted Boltzmann Machines), and variational methods.
Throughout, we emphasize the many natural connections between ML and
statistical physics. A notable aspect of the review is the use of Python
notebooks to introduce modern ML/statistical packages to readers using
physics-inspired datasets (the Ising Model and Monte-Carlo simulations of
supersymmetric decays of proton-proton collisions). We conclude with an
extended outlook discussing possible uses of machine learning for furthering
our understanding of the physical world as well as open problems in ML where
physicists maybe able to contribute. (Notebooks are available at
https://physics.bu.edu/~pankajm/MLnotebooks.html )"),
Pankaj Mehta, Marin Bukov, Ching-Hao Wang, Alexandre G. R. Day, Clint Richardson, Charles K. Fisher, David J. Schwab,
arXiv: [1803.08823](http://arxiv.org/abs/1803.08823v1),
3/2018


- ["Parameter diagnostics of phases and phase transition learning by neural
  networks"](
http://arxiv.org/abs/1802.09876v1
"We present an analysis of neural network-based machine learning schemes for
phases and phase transitions in theoretical condensed matter research, focusing
on neural networks with a single hidden layer. Such shallow neural networks
were previously found to be efficient in classifying phases and locating phase
transitions of various basic model systems. In order to rationalize the
emergence of the classification process and for identifying any underlying
physical quantities, it is feasible to examine the weight matrices and the
convolutional filter kernels that result from the learning process of such
shallow networks. Furthermore, we demonstrate how the learning-by-confusing
scheme can be used, in combination with a simple threshold-value classification
method, to diagnose the learning parameters of neural networks. In particular,
we study the classification process of both fully-connected and convolutional
neural networks for the two-dimensional Ising model with extended domain wall
configurations included in the low-temperature regime. Moreover, we consider
the two-dimensional XY model and contrast the performance of the
learning-by-confusing scheme and convolutional neural networks trained on bare
spin configurations to the case of preprocessed samples with respect to vortex
configurations. We discuss these findings in relation to similar recent
investigations and possible further applications."),
Philippe Suchsland, Stefan Wessel,
arXiv: [1802.09876](http://arxiv.org/abs/1802.09876v1),
2/2018

- ["Advantages of versatile neural-network decoding for topological codes"](
http://arxiv.org/abs/1802.08680v1
"Finding optimal correction of errors in generic stabilizer codes is a
computationally hard problem, even for simple noise models. While this task can
be simplified for codes with some structure, such as topological stabilizer
codes, developing good and efficient decoders still remains a challenge. In our
work, we systematically study a very versatile class of decoders based on
feedforward neural networks. To demonstrate adaptability, we apply neural
decoders to the triangular color and toric codes under various noise models
with realistic features, such as spatially-correlated errors. We report that
neural decoders provide significant improvement over leading efficient decoders
in terms of the error-correction threshold. Using neural networks simplifies
the process of designing well-performing decoders, and does not require prior
knowledge of the underlying noise model."),
Nishad Maskara, Aleksander Kubica, Tomas Jochym-O'Connor,
arXiv: [1802.08680](http://arxiv.org/abs/1802.08680v1),
2/2018

- ["Reinforcement Learning with Neural Networks for Quantum Feedback"](
http://arxiv.org/abs/1802.05267v1
"Artificial neural networks are revolutionizing science. While the most
prevalent technique involves supervised training on queries with a known
correct answer, more advanced challenges often require discovering answers
autonomously. In reinforcement learning, control strategies are improved
according to a reward function. The power of this approach has been highlighted
by spectactular recent successes, such as playing Go. So far, it has remained
an open question whether neural-network-based reinforcement learning can be
successfully applied in physics. Here, we show how to use this method for
finding quantum feedback schemes, where a network-based "agent" interacts with
and occasionally decides to measure a quantum system. We illustrate the utility
by finding gate sequences that preserve the quantum information stored in a
small collection of qubits against noise. This specific application will help
to find hardware-adapted feedback schemes for small quantum modules while
demonstrating more generally the promise of neural-network based reinforcement
learning in physics."),
Thomas Fösel, Petru Tighineanu, Talitha Weiss, Florian Marquardt,
arXiv: [1802.05267](https://arxiv.org/abs/1802.05267v2),
2/2018

- ["Online Learning of Quantum States"](
http://arxiv.org/abs/1802.09025v1
"Suppose we have many copies of an unknown $n$-qubit state $\rho$. We measure
some copies of $\rho$ using a known two-outcome measurement $E_{1}$, then other
copies using a measurement $E_{2}$, and so on. At each stage $t$, we generate a
current hypothesis $\sigma_{t}$ about the state $\rho$, using the outcomes of
the previous measurements. We show that it is possible to do this in a way that
guarantees that $|\operatorname{Tr}(E_{i} \sigma_{t}) -
\operatorname{Tr}(E_{i}\rho) |$, the error in our prediction for the next
measurement, is at least $\varepsilon$ at most $\operatorname{O}\!\left(n /
\varepsilon^2 \right) $ times. Even in the "non-realizable" setting---where
there could be arbitrary noise in the measurement outcomes---we show how to
output hypothesis states that do significantly worse than the best possible
states at most $\operatorname{O}\!\left(\sqrt {Tn}\right) $ times on the first
$T$ measurements. These results generalize a 2007 theorem by Aaronson on the
PAC-learnability of quantum states, to the online and regret-minimization
settings. We give three different ways to prove our results---using convex
optimization, quantum postselection, and sequential fat-shattering
dimension---which have different advantages in terms of parameters and
portability."),
Scott Aaronson, Xinyi Chen, Elad Hazan, Ashwin Nayak,
arXiv: [1802.09025](http://arxiv.org/abs/1802.09025v1),
2/2018


- ["Deep neural decoders for near term fault-tolerant experiments"](
http://arxiv.org/abs/1802.06441v1
"Finding efficient decoders for quantum error correcting codes adapted to
realistic experimental noise in fault-tolerant devices represents a significant
challenge. In this paper we introduce several decoding algorithms complemented
by deep neural decoders and apply them to analyze several fault-tolerant error
correction protocols such as the surface code as well as Steane and Knill error
correction. Our methods require no knowledge of the underlying noise model
afflicting the quantum device making them appealing for real-world experiments.
Our analysis is based on a full circuit-level noise model. It considers both
distance-three and five codes, and is performed near the codes pseudo-threshold
regime. Training deep neural decoders in low noise rate regimes appears to be a
challenging machine learning endeavour. We provide a detailed description of
our neural network architectures and training methodology. We then discuss both
the advantages and limitations of deep neural decoders. Lastly, we provide a
rigorous analysis of the decoding runtime of trained deep neural decoders and
compare our methods with anticipated gate times in future quantum devices.
Given the broad applications of our decoding schemes, we believe that the
methods presented in this paper could have practical applications for near term
fault-tolerant experiments."),
Christopher Chamberland, Pooya Ronagh,
arXiv: [1802.06441](http://arxiv.org/abs/1802.06441v1),
2/2018

- ["Neural Network Renormalization Group"](
http://arxiv.org/abs/1802.02840v1
"We present a variational renormalization group approach using deep generative
model composed of bijectors. The model can learn hierarchical transformations
between physical variables and renormalized collective variables. It can
directly generate statistically independent physical configurations by
iterative refinement at various length scales. The generative model has an
exact and tractable likelihood, which provides renormalized energy function of
the collective variables and supports unbiased rejection sampling of the
physical variables. To train the neural network, we employ probability density
distillation, in which the training loss is a variational upper bound of the
physical free energy. The approach could be useful for automatically
identifying collective variables and effective field theories."),
Shuo-Hui Li, Lei Wang,
arXiv: [1802.02840](http://arxiv.org/abs/1802.02840v1),
2/2018

- ["Deep UQ: Learning deep neural network surrogate models for high
  dimensional uncertainty quantification"](
http://arxiv.org/abs/1802.00850v1
"State-of-the-art computer codes for simulating real physical systems are
often characterized by a vast number of input parameters. Performing
uncertainty quantification (UQ) tasks with Monte Carlo (MC) methods is almost
always infeasible because of the need to perform hundreds of thousands or even
millions of forward model evaluations in order to obtain convergent statistics.
One, thus, tries to construct a cheap-to-evaluate surrogate model to replace
the forward model solver. For systems with large numbers of input parameters,
one has to deal with the curse of dimensionality - the exponential increase in
the volume of the input space, as the number of parameters increases linearly.
In this work, we demonstrate the use of deep neural networks (DNN) to construct
surrogate models for numerical simulators. We parameterize the structure of the
DNN in a manner that lends the DNN surrogate the interpretation of recovering a
low dimensional nonlinear manifold. The model response is a parameterized
nonlinear function of the low dimensional projections of the input. We think of
this low dimensional manifold as a nonlinear generalization of the notion of
the active subspace. Our approach is demonstrated with a problem on uncertainty
propagation in a stochastic elliptic partial differential equation (SPDE) with
uncertain diffusion coefficient. We deviate from traditional formulations of
the SPDE problem by not imposing a specific covariance structure on the random
diffusion coefficient. Instead, we attempt to solve a more challenging problem
of learning a map between an arbitrary snapshot of the diffusion field and the
response."),
Rohit Tripathy, Ilias Bilionis,
arXiv: [1802.00850](http://arxiv.org/abs/1802.00850v1),
2/2018

- ["Experimentally detecting a quantum change point via Bayesian inference"](
http://arxiv.org/abs/1801.07508v1
"Detecting a change point is a crucial task in statistics that has been
recently extended to the quantum realm. A source state generator that emits a
series of single photons in a default state suffers an alteration at some point
and starts to emit photons in a mutated state. The problem consists in
identifying the point where the change took place. In this work, we consider a
learning agent that applies Bayesian inference on experimental data to solve
this problem. This learning machine adjusts the measurement over each photon
according to the past experimental results finds the change position in an
online fashion. Our results show that the local-detection success probability
can be largely improved by using such a machine learning technique. This
protocol provides a tool for improvement in many applications where a sequence
of identical quantum states is required."),
Shang Yu, Chang-Jiang Huang, Jian-Shun Tang, Zhih-Ahn Jia, Yi-Tao Wang, Zhi-Jin Ke, Wei Liu, Xiao Liu, Zong-Quan Zhou, Ze-Di Cheng, Jin-Shi Xu, Yu-Chun Wu, Yuan-Yuan Zhao, Guo-Yong Xiang, Chuan-Feng Li, Guang-Can Guo, Gael Sentís, Ramon Muñoz-Tapia,
arXiv: [1801.07508](http://arxiv.org/abs/1801.07508v1),
1/2018

- ["Generative Models for Stochastic Processes Using Convolutional Neural
  Networks"](
http://arxiv.org/abs/1801.03523v1
"The present paper aims to demonstrate the usage of Convolutional Neural
Networks as a generative model for stochastic processes, enabling researchers
from a wide range of fields (such as quantitative finance and physics) to
develop a general tool for forecasts and simulations without the need to
identify/assume a specific system structure or estimate its parameters."),
Fernando Fernandes Neto,
arXiv: [1801.03523](http://arxiv.org/abs/1801.03523v1),
1/2018

- ["Pattern recognition techniques for Boson Sampling validation"](
http://arxiv.org/abs/1712.06863v1
"The difficulty of validating large-scale quantum devices, such as Boson
Samplers, poses a major challenge for any research program that aims to show
quantum advantages over classical hardware. To address this problem, we propose
a novel data-driven approach wherein models are trained to identify common
pathologies using unsupervised machine learning methods. We illustrate this
idea by training a classifier that exploits K-means clustering to distinguish
between Boson Samplers that use indistinguishable photons from those that do
not. We train the model on numerical simulations of small-scale Boson Samplers
and then validate the pattern recognition technique on larger numerical
simulations as well as on photonic chips in both traditional Boson Sampling and
scattershot experiments. The effectiveness of such method relies on
particle-type-dependent internal correlations present in the output
distributions. This approach performs substantially better on the test data
than previous methods and underscores the ability to further generalize its
operation beyond the scope of the examples that it was trained on."),
Iris Agresti, Niko Viggianiello, Fulvio Flamini, Nicolò Spagnolo, Andrea Crespi, Roberto Osellame, Nathan Wiebe, Fabio Sciarrino,
arXiv: [1712.06863](http://arxiv.org/abs/1712.06863v1),
12/2017

- ["Towards reduction of autocorrelation in HMC by machine learning"](
http://arxiv.org/abs/1712.03893v1
"In this paper we propose new algorithm to reduce autocorrelation in Markov
chain Monte-Carlo algorithms for euclidean field theories on the lattice. Our
proposing algorithm is the Hybrid Monte-Carlo algorithm (HMC) with restricted
Boltzmann machine. We examine the validity of the algorithm by employing the
phi-fourth theory in three dimension. We observe reduction of the
autocorrelation both in symmetric and broken phase as well. Our proposing
algorithm provides consistent central values of expectation values of the
action density and one-point Green's function with ones from the original HMC
in both the symmetric phase and broken phase within the statistical error. On
the other hand, two-point Green's functions have slight difference between one
calculated by the HMC and one by our proposing algorithm in the symmetric
phase. Furthermore, near the criticality, the distribution of the one-point
Green's function differs from the one from HMC. We discuss the origin of
discrepancies and its improvement."),
Akinori Tanaka, Akio Tomiya,
arXiv: [1712.03893](http://arxiv.org/abs/1712.03893v1),
12/2017

- ["Deep Neural Network Detects Quantum Phase Transition"](
http://arxiv.org/abs/1712.00371v1
"We detect the quantum phase transition of a quantum many-body system by
mapping the observed results of the quantum state onto a neural network. In the
present study, we utilized the simplest case of a quantum many-body system,
namely a one-dimensional chain of Ising spins with the transverse Ising model.
We prepared several spin configurations, which were obtained using repeated
observations of the model for a particular strength of the transverse field, as
input data for the neural network. Although the proposed method can be employed
using experimental observations of quantum many-body systems, we tested our
technique with spin configurations generated by a quantum Monte Carlo
simulation without initial relaxation. The neural network successfully
classified the strength of transverse field only from the spin configurations,
leading to consistent estimations of the critical point of our model $\Gamma_c
=J$."),
Shunta Arai, Masayuki Ohzeki, Kazuyuki Tanaka,
arXiv: [1712.00371](http://arxiv.org/abs/1712.00371v1),
12/2017

- ["Experimental learning of quantum states"](
http://arxiv.org/abs/1712.00127v1
"The number of parameters describing a quantum state is well known to grow
exponentially with the number of particles. This scaling clearly limits our
ability to do tomography to systems with no more than a few qubits and has been
used to argue against the universal validity of quantum mechanics itself.
However, from a computational learning theory perspective, it can be shown
that, in a probabilistic setting, quantum states can be approximately learned
using only a linear number of measurements. Here we experimentally demonstrate
this linear scaling in optical systems with up to 6 qubits. Our results
highlight the power of computational learning theory to investigate quantum
information, provide the first experimental demonstration that quantum states
can be "probably approximately learned" with access to a number of copies of
the state that scales linearly with the number of qubits, and pave the way to
probing quantum states at new, larger scales."),
Andrea Rocchetto, Scott Aaronson, Simone Severini, Gonzalo Carvacho, Davide Poderini, Iris Agresti, Marco Bentivegna, Fabio Sciarrino,
arXiv: [1712.00127](http://arxiv.org/abs/1712.00127v1),
11/2017

- ["Machine learning vortices at the Kosterlitz-Thouless transition"](
http://arxiv.org/abs/1710.09842v1
"Efficient and automated classification of phases from minimally processed
data is one goal of machine learning in condensed matter and statistical
physics. Supervised algorithms trained on raw samples of microstates can
successfully detect conventional phase transitions via learning a bulk feature
such as an order parameter. In this paper, we investigate whether neural
networks can learn to classify phases based on topological defects. We address
this question on the two-dimensional classical XY model which exhibits a
Kosterlitz-Thouless transition. We find significant feature engineering of the
raw spin states is required to convincingly claim that features of the vortex
configurations are responsible for learning the transition temperature. We
further show a single-layer network does not correctly classify the phases of
the XY model, while a convolutional network easily performs classification by
learning the global magnetization. Finally, we design a deep network capable of
learning vortices without feature engineering. We demonstrate the detection of
vortices does not necessarily result in the best classification accuracy,
especially for lattices of less than approximately 1000 spins. For larger
systems, it remains a difficult task to learn vortices."),
Matthew J. S. Beach, Anna Golubeva, Roger G. Melko,
arXiv: [1710.09842](http://arxiv.org/abs/1710.09842v1),
10/2017

- ["Machine learning out-of-equilibrium phases of matter"](
http://arxiv.org/abs/1711.00020v1
"Neural network based machine learning is emerging as a powerful tool for
obtaining phase diagrams when traditional regression schemes using local
equilibrium order parameters are not available, as in many-body localized or
topological phases. Nevertheless, instances of machine learning offering new
insights have been rare up to now. Here we show that a single feed-forward
neural network can decode the defining structures of two distinct MBL phases
and a thermalizing phase, using entanglement spectra obtained from individual
eigenstates. For this, we introduce a simplicial geometry based method for
extracting multi-partite phase boundaries. We find that this method outperforms
conventional metrics (like the entanglement entropy) for identifying MBL phase
transitions, revealing a sharper phase boundary and shedding new insight into
the topology of the phase diagram. Furthermore, the phase diagram we acquire
from a single disorder configuration confirms that the machine-learning based
approach we establish here can enable speedy exploration of large phase spaces
that can assist with the discovery of new MBL phases. To our knowledge this
work represents the first example of a machine learning approach revealing new
information beyond conventional knowledge."),
Jordan Venderley, Vedika Khemani, Eun-Ah Kim,
arXiv: [1711.00020](http://arxiv.org/abs/1711.00020v1),
10/2017

- ["Learning hard quantum distributions with variational autoencoders"](
http://arxiv.org/abs/1710.00725v1
"Studying general quantum many-body systems is one of the major challenges in
modern physics because it requires an amount of computational resources that
scales exponentially with the size of the system.Simulating the evolution of a
state, or even storing its description, rapidly becomes intractable for exact
classical algorithms. Recently, machine learning techniques, in the form of
restricted Boltzmann machines, have been proposed as a way to efficiently
represent certain quantum states with applications in state tomography and
ground state estimation. Here, we introduce a new representation of states
based on variational autoencoders. Variational autoencoders are a type of
generative model in the form of a neural network. We probe the power of this
representation by encoding probability distributions associated with states
from different classes. Our simulations show that deep networks give a better
representation for states that are hard to sample from, while providing no
benefit for random states. This suggests that the probability distributions
associated to hard quantum states might have a compositional structure that can
be exploited by layered neural networks. Specifically, we consider the
learnability of a class of quantum states introduced by Fefferman and Umans.
Such states are provably hard to sample for classical computers, but not for
quantum ones, under plausible computational complexity assumptions. The good
level of compression achieved for hard states suggests these methods can be
suitable for characterising states of the size expected in first generation
quantum hardware."),
Andrea Rocchetto, Edward Grant, Sergii Strelchuk, Giuseppe Carleo, Simone Severini,
arXiv: [1710.00725](http://arxiv.org/abs/1710.00725v1),
10/2017

- ["Combining Machine Learning and Physics to Understand Glassy Systems"](
http://arxiv.org/abs/1709.08015v1
"Our understanding of supercooled liquids and glasses has lagged significantly
behind that of simple liquids and crystalline solids. This is in part due to
the many possibly relevant degrees of freedom that are present due to the
disorder inherent to these systems and in part to non-equilibrium effects which
are difficult to treat in the standard context of statistical physics. Together
these issues have resulted in a field whose theories are under-constrained by
experiment and where fundamental questions are still unresolved. Mean field
results have been successful in infinite dimensions but it is unclear to what
extent they apply to realistic systems and assume uniform local structure. At
odds with this are theories premised on the existence of structural defects.
However, until recently it has been impossible to find structural signatures
that are predictive of dynamics. Here we summarize and recast the results from
several recent papers offering a data driven approach to building a
phenomenological theory of disordered materials by combining machine learning
with physical intuition."),
Samuel S. Schoenholz,
arXiv: [1709.08015](http://arxiv.org/abs/1709.08015v1),
9/2017



- ["By-passing the Kohn-Sham equations with machine learning"](
http://arxiv.org/abs/1609.02815v3
"Last year, at least 30,000 scientific papers used the Kohn-Sham scheme of
density functional theory to solve electronic structure problems in a wide
variety of scientific fields, ranging from materials science to biochemistry to
astrophysics. Machine learning holds the promise of learning the kinetic energy
functional via examples, by-passing the need to solve the Kohn-Sham equations.
This should yield substantial savings in computer time, allowing either larger
systems or longer time-scales to be tackled, but attempts to machine-learn this
functional have been limited by the need to find its derivative. The present
work overcomes this difficulty by directly learning the density-potential and
energy-density maps for test systems and various molecules. Both improved
accuracy and lower computational cost with this method are demonstrated by
reproducing DFT energies for a range of molecular geometries generated during
molecular dynamics simulations. Moreover, the methodology could be applied
directly to quantum chemical calculations, allowing construction of density
functionals of quantum-chemical accuracy."),
Felix Brockherde, Leslie Vogt, Li Li, Mark E. Tuckerman, Kieron Burke, Klaus-Robert Müller,
arXiv: [1609.02815](http://arxiv.org/abs/1609.02815v3),
9/2016

- ["Learning Disordered Topological Phases by Statistical Recovery of
  Symmetry"](
http://arxiv.org/abs/1709.05790v2
"In this letter, we apply the artificial neural network in a supervised manner
to map out the quantum phase diagram of disordered topological superconductor
in class DIII. Given the disorder that keeps the discrete symmetries of the
ensemble as a whole, translational symmetry which is broken in the
quasiparticle distribution individually is recovered statistically by taking an
ensemble average. By using this, we classify the phases by the artificial
neural network that learned the quasiparticle distribution in the clean limit,
and show that the result is totally consistent with the calculation by the
transfer matrix method or noncommutative geometry approach. If all three
phases, namely the $\mathbb{Z}_2$, trivial, and the thermal metal phases appear
in the clean limit, the machine can classify them with high confidence over the
entire phase diagram. If only the former two phases are present, we find that
the machine remains confused in the certain region, leading us to conclude the
detection of the unknown phase which is eventually identified as the thermal
metal phase. In our method, only the first moment of the quasiparticle
distribution is used for input, but application to a wider variety of systems
is expected by the inclusion of higher moments."),
Nobuyuki Yoshioka, Yutaka Akagi, Hosho Katsura,
arXiv: [1709.05790](http://arxiv.org/abs/1709.05790v2),
9/2017

- ["Restricted-Boltzmann-Machine Learning for Solving Strongly Correlated
  Quantum Systems"](
http://arxiv.org/abs/1709.06475v2
"We develop a machine learning method to construct accurate ground-state wave
functions of strongly interacting and entangled quantum spin as well as
fermionic models on lattices. A restricted Boltzmann machine algorithm in the
form of an artificial neural network is combined with a conventional
variational Monte Carlo method with pair product (geminal) wave functions and
quantum number projections. The combination allows an application of the
machine learning scheme to interacting fermionic systems. The combined method
substantially improves the accuracy beyond that ever achieved by each method
separately, in the Heisenberg as well as Hubbard models on square lattices,
thus proving its power as a highly accurate quantum many-body solver."),
Yusuke Nomura, Andrew S. Darmawan, Youhei Yamaji, Masatoshi Imada,
arXiv: [1709.06475](http://arxiv.org/abs/1709.06475v2),
9/2017

- ["Identifying Product Order with Restricted Boltzmann Machines"](
http://arxiv.org/abs/1709.02597v1
"Unsupervised machine learning via a restricted Boltzmann machine is an useful
tool in distinguishing an ordered phase from a disordered phase. Here we study
its application on the two-dimensional Ashkin-Teller model, which features a
partially ordered product phase. We train the neural network with spin
configuration data generated by Monte Carlo simulations and show that distinct
features of the product phase can be learned from non-ergodic samples resulting
from symmetry breaking. Careful analysis of the weight matrices inspires us to
define a nontrivial machine-learning motivated quantity of the product form,
which resembles the conventional product order parameter."),
Wen-Jia Rao, Zhenyu Li, Qiong Zhu, Mingxing Luo, Xin Wan,
arXiv: [1709.02597](http://arxiv.org/abs/1709.02597v1),
9/2017

- ["Machine learning & artificial intelligence in the quantum domain"](
http://arxiv.org/abs/1709.02779v1
"Quantum information technologies, and intelligent learning systems, are both
emergent technologies that will likely have a transforming impact on our
society. The respective underlying fields of research -- quantum information
(QI) versus machine learning (ML) and artificial intelligence (AI) -- have
their own specific challenges, which have hitherto been investigated largely
independently. However, in a growing body of recent work, researchers have been
probing the question to what extent these fields can learn and benefit from
each other. QML explores the interaction between quantum computing and ML,
investigating how results and techniques from one field can be used to solve
the problems of the other. Recently, we have witnessed breakthroughs in both
directions of influence. For instance, quantum computing is finding a vital
application in providing speed-ups in ML, critical in our "big data" world.
Conversely, ML already permeates cutting-edge technologies, and may become
instrumental in advanced quantum technologies. Aside from quantum speed-up in
data analysis, or classical ML optimization used in quantum experiments,
quantum enhancements have also been demonstrated for interactive learning,
highlighting the potential of quantum-enhanced learning agents. Finally, works
exploring the use of AI for the very design of quantum experiments, and for
performing parts of genuine research autonomously, have reported their first
successes. Beyond the topics of mutual enhancement, researchers have also
broached the fundamental issue of quantum generalizations of ML/AI concepts.
This deals with questions of the very meaning of learning and intelligence in a
world that is described by quantum mechanics. In this review, we describe the
main ideas, recent developments, and progress in a broad spectrum of research
investigating machine learning and artificial intelligence in the quantum
domain."),
Vedran Dunjko, Hans J. Briegel,
arXiv: [1709.02779](http://arxiv.org/abs/1709.02779v1),
9/2017

- ["Phase Diagrams of Three-Dimensional Anderson and Quantum Percolation
  Models using Deep Three-Dimensional Convolutional Neural Network"](
http://arxiv.org/abs/1709.00812v2
"The three-dimensional Anderson model is a well-studied model of disordered
electron systems that shows the delocalization--localization transition. As in
our previous papers on two- and three-dimensional (2D, 3D) quantum phase
transitions [J. Phys. Soc. Jpn. {\bf 85}, 123706 (2016), {\bf 86}, 044708
(2017)], we used an image recognition algorithm based on a multilayered
convolutional neural network. However, in contrast to previous papers in which
2D image recognition was used, we applied 3D image recognition to analyze
entire 3D wave functions. We show that a full phase diagram of the
disorder-energy plane is obtained once the 3D convolutional neural network has
been trained at the band center. We further demonstrate that the full phase
diagram for 3D quantum bond and site percolations can be drawn by training the
3D Anderson model at the band center."),
Tomohiro Mano, Tomi Ohtsuki,
arXiv: [1709.00812](http://arxiv.org/abs/1709.00812v2),
9/2017

- ["Machine Learning Spatial Geometry from Entanglement Features"](
http://arxiv.org/abs/1709.01223v2
"Motivated by the close relations of the renormalization group with both the
holography duality and the deep learning, we propose that the holographic
geometry can emerge from deep learning the entanglement feature of a quantum
many-body state. We develop a concrete algorithm, call the entanglement feature
learning (EFL), based on the random tensor network (RTN) model for the tensor
network holography. We show that each RTN can be mapped to a Boltzmann machine,
trained by the entanglement entropies over all subregions of a given quantum
many-body state. The goal is to construct the optimal RTN that best reproduce
the entanglement feature. The RTN geometry can then be interpreted as the
emergent holographic geometry. We demonstrate the EFL algorithm on 1D free
fermion system and observe the emergence of the hyperbolic geometry (AdS$_3$
spatial geometry) as we tune the fermion system towards the gapless critical
point (CFT$_2$ point)."),
Yi-Zhuang You, Zhao Yang, Xiao-Liang Qi,
arXiv: [1709.01223](http://arxiv.org/abs/1709.01223v2),
9/2017

- ["Machine Learning Topological Invariants with Neural Networks"](
http://arxiv.org/abs/1708.09401v3
"In this Letter we supervisedly train neural networks to distinguish different
topological phases in the context of topological band insulators. After
training with Hamiltonians of one-dimensional insulators with chiral symmetry,
the neural network can predict their topological winding numbers with nearly
100% accuracy, even for Hamiltonians with larger winding numbers that are not
included in the training data. These results show a remarkable success that the
neural network can capture the global and nonlinear topological features of
quantum phases from local inputs. By opening up the neural network, we confirm
that the network does learn the discrete version of the winding number formula.
We also make a couple of remarks regarding the role of the symmetry and the
opposite effect of regularization techniques when applying machine learning to
physical systems."),
Pengfei Zhang, Huitao Shen, Hui Zhai,
arXiv: [1708.09401](http://arxiv.org/abs/1708.09401v3),
8/2017

- ["Extensive deep neural networks"](
http://arxiv.org/abs/1708.06686v1
"We present a procedure for training and evaluating a deep neural network
which can efficiently infer extensive parameters of arbitrarily large systems,
doing so with O(N) complexity. We use a form of domain decomposition for
training and inference, where each sub-domain (tile) is comprised of a
non-overlapping focus region surrounded by an overlapping context region. The
relative sizes of focus and context are physically motivated and depend on the
locality length scale of the problem. Extensive deep neural networks (EDNN) are
a formulation of convolutional neural networks which provide a flexible and
general approach, based on physical constraints, to describe multi-scale
interactions. They are well suited to massively parallel inference, as no
inter-thread communication is necessary during evaluation. Example uses for
learning simple spin models, Laplacian (derivative) operator, and approximating
many-body quantum mechanical operators (within the density functional theory
approach) are demonstrated."),
Iryna Luchak, Kyle Mills, Kevin Ryczko, Adam Domurad, Isaac Tamblyn,
arXiv: [1708.06686](http://arxiv.org/abs/1708.06686v1),
8/2017

- ["Learning Fermionic Critical Points"](
http://arxiv.org/abs/1708.04762v2
"We use determinant Quantum Monte Carlo (DQMC), in combination with the
principal component analysis (PCA) approach to unsupervised learning, to
extract information about phase transitions in several of the most fundamental
Hamiltonians describing strongly correlated materials. We first explore the
zero temperature antiferromagnet to singlet transition in the Periodic Anderson
Model, the Mott insulating transition in the Hubbard model on a honeycomb
lattice, and the magnetic transition in the 1/6-filled Lieb lattice. We then
discuss the prospects for learning finite temperature superconducting
transitions in the attractive Hubbard model, for which there is no sign
problem. Finally, we investigate finite temperature CDW transitions in the
Holstein model, where the electrons are coupled to phonon degrees of freedom.
We examine the different behaviors associated with providing
Hubbard-Stratonovich auxiliary fields configurations on both the entire
space-time lattice and on a single imaginary time slice, or other quantities,
such as equal-time Green's and pair-pair correlation functions."),
Natanael C. Costa, Wenjian Hu, Z. J. Bai, Richard T. Scalettar, Rajiv R. P. Singh,
arXiv: [1708.04762](http://arxiv.org/abs/1708.04762v2),
8/2017

- ["Deep Learning the Ising Model Near Criticality"](
http://arxiv.org/abs/1708.04622v1
"It is well established that neural networks with deep architectures perform
better than shallow networks for many tasks in machine learning. In statistical
physics, while there has been recent interest in representing physical data
with generative modelling, the focus has been on shallow neural networks. A
natural question to ask is whether deep neural networks hold any advantage over
shallow networks in representing such data. We investigate this question by
using unsupervised, generative graphical models to learn the probability
distribution of a two-dimensional Ising system. Deep Boltzmann machines, deep
belief networks, and deep restricted Boltzmann networks are trained on thermal
spin configurations from this system, and compared to the shallow architecture
of the restricted Boltzmann machine. We benchmark the models, focussing on the
accuracy of generating energetic observables near the phase transition, where
these quantities are most difficult to approximate. Interestingly, after
training the generative networks, we observe that the accuracy essentially
depends only on the number of neurons in the first hidden layer of the network,
and not on other model details such as network depth or model type. This is
evidence that shallow networks are more efficient than deep networks at
representing physical probability distributions associated with Ising systems
near criticality."),
Alan Morningstar, Roger G. Melko,
arXiv: [1708.04622](http://arxiv.org/abs/1708.04622v1),
8/2017

- ["Spectral Dynamics of Learning Restricted Boltzmann Machines"](
http://arxiv.org/abs/1708.02917v2
"The Restricted Boltzmann Machine (RBM), an important tool used in machine
learning in particular for unsupervized learning tasks, is investigated from
the perspective of its spectral properties. Starting from empirical
observations, we propose a generic statistical ensemble for the weight matrix
of the RBM and characterize its mean evolution. This let us show how in the
linear regime, in which the RBM is found to operate at the beginning of the
training, the statistical properties of the data drive the selection of the
unstable modes of the weight matrix. A set of equations characterizing the
non-linear regime is then derived, unveiling in some way how the selected modes
interact in later stages of the learning procedure and defining a deterministic
learning curve for the RBM."),
Aurélien Decelle, Giancarlo Fissore, Cyril Furtlehner,
arXiv: [1708.02917](http://arxiv.org/abs/1708.02917v2),
8/2017

- ["Solving the Bose-Hubbard model with machine learning"](
http://arxiv.org/abs/1707.09723v1
"Motivated by the recent successful application of artificial neural networks
to quantum many-body problems [G. Carleo and M. Troyer, Science {\bf 355}, 602
(2017)], a method to calculate the ground state of the Bose-Hubbard model using
a feedforward neural network is proposed. The results are in good agreement
with those obtained by exact diagonalization and the Gutzwiller approximation.
The method of neural-network quantum states is promising for solving quantum
many-body problems of ultracold atoms in optical lattices."),
Hiroki Saito,
arXiv: [1707.09723](http://arxiv.org/abs/1707.09723v1),
7/2017

- ["Quantum dynamics in transverse-field Ising models from classical
  networks"](
http://arxiv.org/abs/1707.06656v4
"The efficient representation of quantum many-body states with classical
resources is a key challenge in quantum many-body theory. In this work we
analytically construct classical networks for the description of the quantum
dynamics in transverse-field Ising models that can be solved efficiently using
Monte Carlo techniques. Our perturbative construction encodes time-evolved
quantum states of spin-1/2 systems in a network of classical spins with local
couplings and can be directly generalized to other spin systems and higher
spins. Using this construction we compute the transient dynamics in one, two,
and three dimensions including local observables, entanglement production, and
Loschmidt amplitudes using Monte Carlo algorithms and demonstrate the accuracy
of this approach by comparisons to exact results. We include a mapping to
equivalent artificial neural networks, which were recently introduced to
provide a universal structure for classical network wave functions."),
Markus Schmitt, Markus Heyl,
arXiv: [1707.06656](http://arxiv.org/abs/1707.06656v4),
7/2017

- ["Learning the Einstein-Podolsky-Rosen correlations on a Restricted
  Boltzmann Machine"](
http://arxiv.org/abs/1707.03114v2
"We construct a hidden variable model for the EPR correlations using a
Restricted Boltzmann Machine. The model reproduces the expected correlations
and thus violates the Bell inequality, as required by Bell's theorem. Unlike
most hidden-variable models, this model does not violate the $locality$
assumption in Bell's argument. Rather, it violates $measurement$
$independence$, albeit in a decidedly non-conspiratorial way."),
Steven Weinstein,
arXiv: [1707.03114](http://arxiv.org/abs/1707.03114v2),
7/2017

- ["Quantum phase recognition via unsupervised machine learning"](
http://arxiv.org/abs/1707.00663v1
"The application of state-of-the-art machine learning techniques to
statistical physic problems has seen a surge of interest for their ability to
discriminate phases of matter by extracting essential features in the many-body
wavefunction or the ensemble of correlators sampled in Monte Carlo simulations.
Here we introduce a gener- alization of supervised machine learning approaches
that allows to accurately map out phase diagrams of inter- acting many-body
systems without any prior knowledge, e.g. of their general topology or the
number of distinct phases. To substantiate the versatility of this approach,
which combines convolutional neural networks with quantum Monte Carlo sampling,
we map out the phase diagrams of interacting boson and fermion models both at
zero and finite temperatures and show that first-order, second-order, and
Kosterlitz-Thouless phase transitions can all be identified. We explicitly
demonstrate that our approach is capable of identifying the phase transition to
non-trivial many-body phases such as superfluids or topologically ordered
phases without supervision."),
Peter Broecker, Fakher F. Assaad, Simon Trebst,
arXiv: [1707.00663](http://arxiv.org/abs/1707.00663v1),
7/2017

- ["Deep neural networks for direct, featureless learning through
  observation: the case of 2d spin models"](
http://arxiv.org/abs/1706.09779v1
"We train a deep convolutional neural network to accurately predict the
energies and magnetizations of Ising model configurations, using both the
traditional nearest-neighbour Hamiltonian, as well as a long-range screened
Coulomb Hamiltonian. We demonstrate the capability of a convolutional deep
neural network in predicting the nearest-neighbour energy of the 4x4 Ising
model. Using its success at this task, we motivate the study of the larger 8x8
Ising model, showing that the deep neural network can learn the
nearest-neighbour Ising Hamiltonian after only seeing a vanishingly small
fraction of configuration space. Additionally, we show that the neural network
has learned both the energy and magnetization operators with sufficient
accuracy to replicate the low-temperature Ising phase transition. Finally, we
teach the convolutional deep neural network to accurately predict a long-range
interaction through a screened Coulomb Hamiltonian. In this case, the benefits
of the neural network become apparent; it is able to make predictions with a
high degree of accuracy, 1600 times faster than a CUDA-optimized "exact"
calculation."),
K. Mills, I. Tamblyn,
arXiv: [1706.09779](http://arxiv.org/abs/1706.09779v1),
6/2017

- ["Inverse Ising inference by combining Ornstein-Zernike theory with deep
  learning"](
http://arxiv.org/abs/1706.08466v1
"Inferring a generative model from data is a fundamental problem in machine
learning. It is well-known that the Ising model is the maximum entropy model
for binary variables which reproduces the sample mean and pairwise
correlations. Learning the parameters of the Ising model from data is the
challenge. We establish an analogy between the inverse Ising problem and the
Ornstein-Zernike formalism in liquid state physics. Rather than analytically
deriving the closure relation, we use a deep neural network to learn the
closure from simulations of the Ising model. We show, using simulations as well
as biochemical datasets, that the deep neural network model outperforms
systematic field-theoretic expansions and can generalize well beyond the
parameter regime of the training data. The neural network is able to learn from
synthetic data, which can be generated with relative ease, to give accurate
predictions on real world datasets."),
Alpha A. Lee,
arXiv: [1706.08466](http://arxiv.org/abs/1706.08466v1),
6/2017

- ["Unsupervised Learning of Frustrated Classical Spin Models I: Principle
  Component Analysis"](
http://arxiv.org/abs/1706.07977v2
"This work aims at the goal whether the artificial intelligence can recognize
phase transition without the prior human knowledge. If this becomes successful,
it can be applied to, for instance, analyze data from quantum simulation of
unsolved physical models. Toward this goal, we first need to apply the machine
learning algorithm to well-understood models and see whether the outputs are
consistent with our prior knowledge, which serves as the benchmark of this
approach. In this work, we feed the compute with data generated by the
classical Monte Carlo simulation for the XY model in frustrated triangular and
union jack lattices, which has two order parameters and exhibits two phase
transitions. We show that the outputs of the principle component analysis agree
very well with our understanding of different orders in different phases, and
the temperature dependences of the major components detect the nature and the
locations of the phase transitions. Our work offers promise for using machine
learning techniques to study sophisticated statistical models, and our results
can be further improved by using principle component analysis with kernel
tricks and the neural network method."),
Ce Wang, Hui Zhai,
arXiv: [1706.07977](http://arxiv.org/abs/1706.07977v2),
6/2017

- ["Self-Learning Phase Boundaries by Active Contours"](
http://arxiv.org/abs/1706.08111v1
"We introduce a fully automatic self-learning scheme for detecting phase
boundaries. This method extends the previously introduced confusion scheme for
learning phase transitions, by using a cooperative network that learns to
optimize the guess for the transition point. The networks together are capable
of finding transition points for fully unlabeled data. This improvement allows
us to efficiently study 1D and 2D parameter spaces, where for the latter we
utilize an active contour model -- the snake -- from computer vision as a
representation of the learned phase boundary. The snakes, equipped with neural
networks, can learn while they move in the parameter space and thereby detect
phase boundaries automatically."),
Ye-Hua Liu, Evert P. L. van Nieuwenburg,
arXiv: [1706.08111](http://arxiv.org/abs/1706.08111v1),
6/2017

- ["Machine-learning-assisted correction of correlated qubit errors in a
  topological code"](
http://arxiv.org/abs/1705.07855v3
"A fault-tolerant quantum computation requires an efficient means to detect
and correct errors that accumulate in encoded quantum information. In the
context of machine learning, neural networks are a promising new approach to
quantum error correction. Here we show that a recurrent neural network can be
trained, using only experimentally accessible data, to detect errors in a
widely used topological code, the surface code, with a performance above that
of the established minimum-weight perfect matching (or blossom) decoder. The
performance gain is achieved because the neural network decoder can detect
correlations between bit-flip (X) and phase-flip (Z) errors. The machine
learning algorithm adapts to the physical system, hence no noise model is
needed. The long short-term memory layers of the recurrent neural network
maintain their performance over a large number of quantum error correction
cycles, making it a practical decoder for forthcoming experimental realizations
of the surface code."),
P. Baireuther, T. E. O'Brien, B. Tarasinski, C. W. J. Beenakker,
arXiv: [1705.07855](http://arxiv.org/abs/1705.07855v3),
5/2017

- ["Self-Learning Monte Carlo Method: Continuous-Time Algorithm"](
http://arxiv.org/abs/1705.06724v2
"The recently-introduced self-learning Monte Carlo method is a general-purpose
numerical method that speeds up Monte Carlo simulations by training an
effective model to propose uncorrelated configurations in the Markov chain. We
implement this method in the framework of continuous time Monte Carlo method
with auxiliary field in quantum impurity models. We introduce and train a
diagram generating function (DGF) to model the probability distribution of
auxiliary field configurations in continuous imaginary time, at all orders of
diagrammatic expansion. By using DGF to propose global moves in configuration
space, we show that the self-learning continuous-time Monte Carlo method can
significantly reduce the computational complexity of the simulation."),
Yuki Nagai, Huitao Shen, Yang Qi, Junwei Liu, Liang Fu,
arXiv: [1705.06724](http://arxiv.org/abs/1705.06724v2),
5/2017

- ["Criticality & Deep Learning II: Momentum Renormalisation Group"](
http://arxiv.org/abs/1705.11023v1
"Guided by critical systems found in nature we develop a novel mechanism
consisting of inhomogeneous polynomial regularisation via which we can induce
scale invariance in deep learning systems. Technically, we map our deep
learning (DL) setup to a genuine field theory, on which we act with the
Renormalisation Group (RG) in momentum space and produce the flow equations of
the couplings; those are translated to constraints and consequently interpreted
as "critical regularisation" conditions in the optimiser; the resulting
equations hence prove to be sufficient conditions for - and serve as an elegant
and simple mechanism to induce scale invariance in any deep learning setup."),
Dan Oprisa, Peter Toth,
arXiv: [1705.11023](http://arxiv.org/abs/1705.11023v1),
5/2017

- ["Construction of Hamiltonians by supervised learning of energy and
  entanglement spectra"](
http://arxiv.org/abs/1705.05372v4
"Correlated many-body problems ubiquitously appear in various fields of
physics such as condensed matter physics, nuclear physics, and statistical
physics. However, due to the interplay of the large number of degrees of
freedom, it is generically impossible to treat these problems from first
principles. Thus the construction of a proper model, namely effective
Hamiltonian, is essential. Here, we propose a simple scheme of constructing
Hamiltonians from given energy or entanglement spectra with machine learning.
We apply the proposed scheme to the Hubbard model at the half-filling, and
compare the obtained effective low-energy spin-1/2 model with several analytic
results based on the high order perturbation theory which have been
inconsistent with each other. We also show that our approach can be used to
construct the entanglement Hamiltonian of a quantum many-body state from its
entanglement spectrum as well. We exemplify this using the ground states of the
$S=1/2$ two-leg Heisenberg ladders. We observe a qualitative difference between
the entanglement Hamiltonians of the two phases (the Haldane phase and the Rung
Singlet phase) of the model due to the different origin of the entanglement. In
the Haldane phase, we find that the entanglement Hamiltonian is non-local by
nature, and the locality can be restored by introducing the anisotropy and
turning the system into the large-$D$ phase. Possible applications to the study
of strongly-correlated systems and the model construction from experimental
data are discussed."),
Hiroyuki Fujita, Yuya O. Nakagawa, Sho Sugiura, Masaki Oshikawa,
arXiv: [1705.05372](http://arxiv.org/abs/1705.05372v4),
5/2017

- ["Machine Learning of Explicit Order Parameters: From the Ising Model to
  SU(2) Lattice Gauge Theory"](
http://arxiv.org/abs/1705.05582v1
"We present a procedure for reconstructing the decision function of an
artificial neural network as a simple function of the input, provided the
decision function is sufficiently symmetric. In this case one can easily deduce
the quantity by which the neural network classifies the input. The procedure is
embedded into a pipeline of machine learning algorithms able to detect the
existence of different phases of matter, to determine the position of phase
transitions and to find explicit expressions of the physical quantities by
which the algorithm distinguishes between phases. We assume no prior knowledge
about the Hamiltonian or the order parameters except Monte Carlo-sampled
configurations. The method is applied to the Ising Model and SU(2) lattice
gauge theory. In both systems we deduce the explicit expressions of the known
order parameters from the decision functions of the neural networks."),
Sebastian Johann Wetzel, Manuel Scherzer,
arXiv: [1705.05582](http://arxiv.org/abs/1705.05582v1),
5/2017

- ["Machine Learning $Z_2$ Quantum Spin Liquids with
  Quasi-particle Statistics"](
http://arxiv.org/abs/1705.01947v2
"After decades of progress and effort, obtaining a phase diagram for a
strongly-correlated topological system still remains a challenge. Although in
principle one could turn to Wilson loops and long-range entanglement,
evaluating these non-local observables at many points in phase space can be
prohibitively costly. With growing excitement over topological quantum
computation comes the need for an efficient approach for obtaining topological
phase diagrams. Here we turn to machine learning using quantum loop topography
(QLT), a notion we have recently introduced. Specifically, we propose a
construction of QLT that is sensitive to quasi-particle statistics. We then use
mutual statistics between the spinons and visons to detect a $Z_2$
quantum spin liquid in a multi-parameter phase space. We successfully obtain
the quantum phase boundary between the topological and trivial phases using a
simple feed-forward neural network. Furthermore, we demonstrate advantages of
our approach for the evaluation of phase diagrams relating to speed and
storage. Such statistics-based machine learning of topological phases opens new
efficient routes to studying topological phase diagrams in strongly correlated
systems."),
Yi Zhang, Roger G. Melko, Eun-Ah Kim,
arXiv: [1705.01947](http://arxiv.org/abs/1705.01947v2),
5/2017

- ["Decoding Small Surface Codes with Feedforward Neural Networks"](
http://arxiv.org/abs/1705.00857v1
"Surface codes reach high error thresholds when decoded with known algorithms,
but the decoding time will likely exceed the available time budget, especially
for near-term implementations. To decrease the decoding time, we reduce the
decoding problem to a classification problem that a feedforward neural network
can solve. We investigate quantum error correction and fault tolerance at small
code distances using neural network-based decoders, demonstrating that the
neural network can generalize to inputs that were not provided during training
and that they can reach similar or better decoding performance compared to
previous algorithms. We conclude by discussing the time required by a
feedforward neural network decoder in hardware."),
Savvas Varsamopoulos, Ben Criger, Koen Bertels,
arXiv: [1705.00857](http://arxiv.org/abs/1705.00857v1),
5/2017

- ["A Separability-Entanglement Classifier via Machine Learning"](
http://arxiv.org/abs/1705.01523v3
"The problem of determining whether a given quantum state is entangled lies at
the heart of quantum information processing, which is known to be an NP-hard
problem in general. Despite the proposed many methods such as the positive
partial transpose (PPT) criterion and the k-symmetric extendibility criterion
to tackle this problem in practice, none of them enables a general, effective
solution to the problem even for small dimensions. Explicitly, separable states
form a high-dimensional convex set, which exhibits a vastly complicated
structure. In this work, we build a new separability-entanglement classifier
underpinned by machine learning techniques. Our method outperforms the existing
methods in generic cases in terms of both speed and accuracy, opening up the
avenues to explore quantum entanglement via the machine learning approach."),
Sirui Lu, Shilin Huang, Keren Li, Jun Li, Jianxin Chen, Dawei Lu, Zhengfeng Ji, Yi Shen, Duanlu Zhou, Bei Zeng,
arXiv: [1705.01523](http://arxiv.org/abs/1705.01523v3),
5/2017

- ["Reinforcement Learning in Different Phases of Quantum Control"](
http://arxiv.org/abs/1705.00565v2
"The ability to prepare a physical system in a desired quantum state is
central to many areas of physics such as nuclear magnetic resonance, cold
atoms, and quantum computing. Preparing states quickly and with high fidelity
remains a formidable challenge. In this work we implement cutting-edge
Reinforcement Learning (RL) techniques and show that their performance rivals
gradient-based optimal control methods at the task of finding short,
high-fidelity driving protocols from an initial to a target state in
non-integrable many-body quantum systems of interacting qubits. The quantum
state preparation problem, viewed as an optimization problem, is shown to
exhibit a spin-glass-like phase transition in the space of protocols as a
function of the protocol duration. Our RL-aided approach helps identify
variational protocols with nearly optimal fidelity, even in the glassy phase,
where optimal state preparation appears exponentially hard. This study
highlights the usefulness of RL for applications in out-of-equilibrium quantum
physics."),
Marin Bukov, Alexandre G. R. Day, Dries Sels, Phillip Weinberg, Anatoli Polkovnikov, Pankaj Mehta,
arXiv: [1705.00565](http://arxiv.org/abs/1705.00565v2),
5/2017

- ["Deterministic Quantum Annealing Expectation-Maximization Algorithm"](
http://arxiv.org/abs/1704.05822v1
"Maximum likelihood estimation (MLE) is one of the most important methods in
machine learning, and the expectation-maximization (EM) algorithm is often used
to obtain maximum likelihood estimates. However, EM heavily depends on initial
configurations and fails to find the global optimum. On the other hand, in the
field of physics, quantum annealing (QA) was proposed as a novel optimization
approach. Motivated by QA, we propose a quantum annealing extension of EM,
which we call the deterministic quantum annealing expectation-maximization
(DQAEM) algorithm. We also discuss its advantage in terms of the path integral
formulation. Furthermore, by employing numerical simulations, we illustrate how
it works in MLE and show that DQAEM outperforms EM."),
Hideyuki Miyahara, Koji Tsumura, Yuki Sughiyama,
arXiv: [1704.05822](http://arxiv.org/abs/1704.05822v1),
4/2017

- ["Mutual Information, Neural Networks and the Renormalization Group"](
http://arxiv.org/abs/1704.06279v1
"Physical systems differing in their microscopic details often display
strikingly similar behaviour when probed at low energies. Those universal
properties, largely determining their physical characteristics, are revealed by
the powerful renormalization group (RG) procedure, which systematically retains
"slow" degrees of freedom and integrates out the rest. However, the important
degrees of freedom may be difficult to identify. Here we demonstrate a machine
learning (ML) algorithm capable of identifying the relevant degrees of freedom
without any prior knowledge about the system. We introduce an artificial neural
network based on a model-independent, information-theoretic characterization of
a real-space RG procedure, performing this task. We apply the algorithm to
classical statistical physics problems in two dimensions."),
Maciej Koch-Janusz, Zohar Ringel,
arXiv: [1704.06279](http://arxiv.org/abs/1704.06279v1),
4/2017

- ["Kernel methods for interpretable machine learning of order parameters"](
http://arxiv.org/abs/1704.05848v1
"Machine learning is capable of discriminating phases of matter, and finding
associated phase transitions, directly from large data sets of raw state
configurations. In the context of condensed matter physics, most progress in
the field of supervised learning has come from employing neural networks as
classifiers. Although very powerful, such algorithms suffer from a lack of
interpretability, which is usually desired in scientific applications in order
to associate learned features with physical phenomena. In this paper, we
explore support vector machines (SVMs) which are a class of supervised kernel
methods that provide interpretable decision functions. We find that SVMs can
learn the mathematical form of physical discriminators, such as order
parameters and Hamiltonian constraints, for a set of two-dimensional spin
models: the ferromagnetic Ising model, a conserved-order-parameter Ising model,
and the Ising gauge theory. The ability of SVMs to provide interpretable
classification highlights their potential for automating feature detection in
both synthetic and experimental data sets for condensed matter and other
many-body systems."),
Pedro Ponte, Roger G. Melko,
arXiv: [1704.05848](http://arxiv.org/abs/1704.05848v1),
4/2017

- ["Approximating quantum many-body wave-functions using artificial neural
  networks"](
http://arxiv.org/abs/1704.05148v4
"In this paper, we demonstrate the expressibility of artificial neural
networks (ANNs) in quantum many-body physics by showing that a feed-forward
neural network with a small number of hidden layers can be trained to
approximate with high precision the ground states of some notable quantum
many-body systems. We consider the one-dimensional free bosons and fermions,
spinless fermions on a square lattice away from half-filling, as well as
frustrated quantum magnetism with a rapidly oscillating ground-state
characteristic function. In the latter case, an ANN with a standard
architecture fails, while that with a slightly modified one successfully learns
the frustration-induced complex sign rule in the ground state and approximates
the ground states with high precisions. As an example of practical use of our
method, we also perform the variational method to explore the ground state of
an anti-ferromagnetic $J_1-J_2$ Heisenberg model."),
Zi Cai, Jinguo Liu,
arXiv: [1704.05148](http://arxiv.org/abs/1704.05148v4),
4/2017

- ["Probing many-body localization with neural networks"](
http://arxiv.org/abs/1704.01578v2
"We show that a simple artificial neural network trained on entanglement
spectra of individual states of a many-body quantum system can be used to
determine the transition between a many-body localized and a thermalizing
regime. Specifically, we study the Heisenberg spin-1/2 chain in a random
external field. We employ a multilayer perceptron with a single hidden layer,
which is trained on labeled entanglement spectra pertaining to the fully
localized and fully thermal regimes. We then apply this network to classify
spectra belonging to states in the transition region. For training, we use a
cost function that contains, in addition to the usual error and regularization
parts, a term that favors a confident classification of the transition region
states. The resulting phase diagram is in good agreement with the one obtained
by more conventional methods and can be computed for small systems. In
particular, the neural network outperforms conventional methods in classifying
individual eigenstates pertaining to a single disorder realization. It allows
us to map out the structure of these eigenstates across the transition with
spatial resolution. Furthermore, we analyze the network operation using the
dreaming technique to show that the neural network correctly learns by itself
the power-law structure of the entanglement spectra in the many-body localized
regime."),
Frank Schindler, Nicolas Regnault, Titus Neupert,
arXiv: [1704.01578](http://arxiv.org/abs/1704.01578v2),
4/2017

- ["Discovering Phases, Phase Transitions and Crossovers through
  Unsupervised Machine Learning: A critical examination"](
http://arxiv.org/abs/1704.00080v2
"We apply unsupervised machine learning techniques, mainly principal component
analysis (PCA), to compare and contrast the phase behavior and phase
transitions in several classical spin models - the square and
triangular-lattice Ising models, the Blume-Capel model, a highly degenerate
biquadratic-exchange spin-one Ising (BSI) model, and the 2D XY model, and
examine critically what machine learning is teaching us. We find that
quantified principal components from PCA not only allow exploration of
different phases and symmetry-breaking, but can distinguish phase transition
types and locate critical points. We show that the corresponding weight vectors
have a clear physical interpretation, which is particularly interesting in the
frustrated models such as the triangular antiferromagnet, where they can point
to incipient orders. Unlike the other well-studied models, the properties of
the BSI model are less well known. Using both PCA and conventional Monte Carlo
analysis, we demonstrate that the BSI model shows an absence of phase
transition and macroscopic ground-state degeneracy. The failure to capture the
`charge' correlations (vorticity) in the BSI model (XY model) from raw spin
configurations points to some of the limitations of PCA. Finally, we employ a
nonlinear unsupervised machine learning procedure, the `antoencoder method',
and demonstrate that it too can be trained to capture phase transitions and
critical points."),
Wenjian Hu, Rajiv R. P. Singh, Richard T. Scalettar,
arXiv: [1704.00080](http://arxiv.org/abs/1704.00080v2),
3/2017

- ["Many-body quantum state tomography with neural networks"](
http://arxiv.org/abs/1703.05334v2
"The experimental realization of increasingly complex synthetic quantum
systems calls for the development of general theoretical methods, to validate
and fully exploit quantum resources. Quantum-state tomography (QST) aims at
reconstructing the full quantum state from simple measurements, and therefore
provides a key tool to obtain reliable analytics. Brute-force approaches to
QST, however, demand resources growing exponentially with the number of
constituents, making it unfeasible except for small systems. Here we show that
machine learning techniques can be efficiently used for QST of highly-entangled
states, in both one and two dimensions. Remarkably, the resulting approach
allows one to reconstruct traditionally challenging many-body quantities - such
as the entanglement entropy - from simple, experimentally accessible
measurements. This approach can benefit existing and future generations of
devices ranging from quantum computers to ultra-cold atom quantum simulators."),
Giacomo Torlai, Guglielmo Mazzola, Juan Carrasquilla, Matthias Troyer, Roger Melko, Giuseppe Carleo,
arXiv: [1703.05334](http://arxiv.org/abs/1703.05334v2),
3/2017

- ["Unsupervised learning of phase transitions: from principal component
  analysis to variational autoencoders"](
http://arxiv.org/abs/1703.02435v2
"We employ unsupervised machine learning techniques to learn latent parameters
which best describe states of the two-dimensional Ising model and the
three-dimensional XY model. These methods range from principal component
analysis to artificial neural network based variational autoencoders. The
states are sampled using a Monte-Carlo simulation above and below the critical
temperature. We find that the predicted latent parameters correspond to the
known order parameters. The latent representation of the states of the models
in question are clustered, which makes it possible to identify phases without
prior knowledge of their existence or the underlying Hamiltonian. Furthermore,
we find that the reconstruction loss function can be used as a universal
identifier for phase transitions."),
Sebastian Johann Wetzel,
arXiv: [1703.02435](http://arxiv.org/abs/1703.02435v2),
3/2017

- ["Neural network representation of tensor network and chiral states"](
http://arxiv.org/abs/1701.06246v1
"We study the representational power of a Boltzmann machine (a type of neural
network) in quantum many-body systems. We prove that any (local) tensor network
state has a (local) neural network representation. The construction is almost
optimal in the sense that the number of parameters in the neural network
representation is almost linear in the number of nonzero parameters in the
tensor network representation. Despite the difficulty of representing (gapped)
chiral topological states with local tensor networks, we construct a
quasi-local neural network representation for a chiral p-wave superconductor.
This demonstrates the power of Boltzmann machines."),
Yichen Huang, Joel E. Moore,
arXiv: [1701.06246](http://arxiv.org/abs/1701.06246v1),
1/2017

- ["Equivalence of restricted Boltzmann machines and tensor network states"](
http://arxiv.org/abs/1701.04831v2
"The restricted Boltzmann machine (RBM) is one of the fundamental building
blocks of deep learning. RBM finds wide applications in dimensional reduction,
feature extraction, and recommender systems via modeling the probability
distributions of a variety of input data including natural images, speech
signals, and customer ratings, etc. We build a bridge between RBM and tensor
network states (TNS) widely used in quantum many-body physics research. We
devise efficient algorithms to translate an RBM into the commonly used TNS.
Conversely, we give sufficient and necessary conditions to determine whether a
TNS can be transformed into an RBM of given architectures. Revealing these
general and constructive connections can cross-fertilize both deep learning and
quantum many-body physics. Notably, by exploiting the entanglement entropy
bound of TNS, we can rigorously quantify the expressive power of RBM on complex
data sets. Insights into TNS and its entanglement capacity can guide the design
of more powerful deep learning architectures. On the other hand, RBM can
represent quantum many-body states with fewer parameters compared to TNS, which
may allow more efficient classical simulations."),
Jing Chen, Song Cheng, Haidong Xie, Lei Wang, Tao Xiang,
arXiv: [1701.04831](http://arxiv.org/abs/1701.04831v2),
1/2017

- ["Efficient Representation of Quantum Many-body States with Deep Neural
  Networks"](
http://arxiv.org/abs/1701.05039v1
"The challenge of quantum many-body problems comes from the difficulty to
represent large-scale quantum states, which in general requires an
exponentially large number of parameters. Recently, a connection has been made
between quantum many-body states and the neural network representation
(\textit{arXiv:1606.02318}). An important open question is what characterizes
the representational power of deep and shallow neural networks, which is of
fundamental interest due to popularity of the deep learning methods. Here, we
give a rigorous proof that a deep neural network can efficiently represent most
physical states, including those generated by any polynomial size quantum
circuits or ground states of many body Hamiltonians with polynomial-size gaps,
while a shallow network through a restricted Boltzmann machine cannot
efficiently represent those states unless the polynomial hierarchy in
computational complexity theory collapses."),
Xun Gao, Lu-Ming Duan,
arXiv: [1701.05039](http://arxiv.org/abs/1701.05039v1),
1/2017

- ["Quantum Entanglement in Neural Network States"](
http://arxiv.org/abs/1701.04844v3
"Machine learning, one of today's most rapidly growing interdisciplinary
fields, promises an unprecedented perspective for solving intricate quantum
many-body problems. Understanding the physical aspects of the representative
artificial neural-network states is recently becoming highly desirable in the
applications of machine learning techniques to quantum many-body physics. Here,
we study the quantum entanglement properties of neural-network states, with a
focus on the restricted-Boltzmann-machine (RBM) architecture. We prove that the
entanglement of all short-range RBM states satisfies an area law for arbitrary
dimensions and bipartition geometry. For long-range RBM states we show by using
an exact construction that such states could exhibit volume-law entanglement,
implying a notable capability of RBM in representing efficiently quantum states
with massive entanglement. We further examine generic RBM states with random
weight parameters. We find that their averaged entanglement entropy obeys
volume-law scaling and meantime strongly deviates from the Page-entropy of the
completely random pure states. We show that their entanglement spectrum has no
universal part associated with random matrix theory and bears a Poisson-type
level statistics. Using reinforcement learning, we demonstrate that RBM is
capable of finding the ground state (with power-law entanglement) of a model
Hamiltonian with long-range interaction. In addition, we show, through a
concrete example of the one-dimensional symmetry-protected topological cluster
states, that the RBM representation may also be used as a tool to analytically
compute the entanglement spectrum. Our results uncover the unparalleled power
of artificial neural networks in representing quantum many-body states, which
paves a novel way to bridge computer science based machine learning techniques
to outstanding quantum condensed matter physics problems."),
Dong-Ling Deng, Xiaopeng Li, S. Das Sarma,
arXiv: [1701.04844](http://arxiv.org/abs/1701.04844v3),
1/2017

- ["Restricted Boltzmann Machines for the Long Range Ising Models"](
http://arxiv.org/abs/1701.00246v1
"We set up Restricted Boltzmann Machines (RBM) to reproduce the Long Range
Ising (LRI) models of the Ohmic type in one dimension. The RBM parameters are
tuned by using the standard machine learning procedure with an additional
method of Configuration with Probability (CwP). The quality of resultant RBM
are evaluated through the susceptibility with respect to the magnetic external
field. We compare the results with those by Block Decimation Renormalization
Group (BDRG) method, and our RBM clear the test with satisfactory precision."),
Ken-Ichi Aoki, Tamao Kobayashi,
arXiv: [1701.00246](http://arxiv.org/abs/1701.00246v1),
1/2017

- ["Reinforcement Learning Using Quantum Boltzmann Machines"](
http://arxiv.org/abs/1612.05695v2
"We investigate whether quantum annealers with select chip layouts can
outperform classical computers in reinforcement learning tasks. We associate a
transverse field Ising spin Hamiltonian with a layout of qubits similar to that
of a deep Boltzmann machine (DBM) and use simulated quantum annealing (SQA) to
numerically simulate quantum sampling from this system. We design a
reinforcement learning algorithm in which the set of visible nodes representing
the states and actions of an optimal policy are the first and last layers of
the deep network. In absence of a transverse field, our simulations show that
DBMs train more effectively than restricted Boltzmann machines (RBM) with the
same number of weights. Since sampling from Boltzmann distributions of a DBM is
not classically feasible, this is evidence of advantage of a non-Turing
sampling oracle. We then develop a framework for training the network as a
quantum Boltzmann machine (QBM) in the presence of a significant transverse
field for reinforcement learning. This further improves the reinforcement
learning method using DBMs."),
Daniel Crawford, Anna Levit, Navid Ghadermarzy, Jaspreet S. Oberoi, Pooya Ronagh,
arXiv: [1612.05695](http://arxiv.org/abs/1612.05695v2),
12/2016

- ["Self-Learning Monte Carlo Method in Fermion Systems"](
http://arxiv.org/abs/1611.09364v1
"We develop the self-learning Monte Carlo (SLMC) method, a general-purpose
numerical method recently introduced to simulate many-body systems, for
studying interacting fermion systems. Our method uses a highly-efficient update
algorithm, which we design and dub "cumulative update", to generate new
candidate configurations in the Markov chain based on a self-learned bosonic
effective model. From general analysis and numerical study of the double
exchange model as an example, we find the SLMC with cumulative update
drastically reduces the computational cost of the simulation, while remaining
statistically exact. Remarkably, its computational complexity is far less than
the conventional algorithm with local updates."),
Junwei Liu, Huitao Shen, Yang Qi, Zi Yang Meng, Liang Fu,
arXiv: [1611.09364](http://arxiv.org/abs/1611.09364v1),
11/2016

- ["Sampling algorithms for validation of supervised learning models for
  Ising-like systems"](
http://arxiv.org/abs/1611.05891v1
"In this paper, we build and explore supervised learning models of
ferromagnetic system behavior, using Monte-Carlo sampling of the spin
configuration space generated by the 2D Ising model. Given the enormous size of
the space of all possible Ising model realizations, the question arises as to
how to choose a reasonable number of samples that will form physically
meaningful and non-intersecting training and testing datasets. Here, we propose
a sampling technique called ID-MH that uses the Metropolis-Hastings algorithm
creating Markov process across energy levels within the predefined
configuration subspace. We show that application of this method retains phase
transitions in both training and testing datasets and serves the purpose of
validation of a machine learning algorithm. For larger lattice dimensions,
ID-MH is not feasible as it requires knowledge of the complete configuration
space. As such, we develop a new "block-ID" sampling strategy: it decomposes
the given structure into square blocks with lattice dimension no greater than 5
and uses ID-MH sampling of candidate blocks. Further comparison of the
performance of commonly used machine learning methods such as random forests,
decision trees, k nearest neighbors and artificial neural networks shows that
the PCA-based Decision Tree regressor is the most accurate predictor of
magnetizations of the Ising model. For energies, however, the accuracy of
prediction is not satisfactory, highlighting the need to consider more
algorithmically complex methods (e.g., deep learning)."),
Nataliya Portman, Isaac Tamblyn,
arXiv: [1611.05891](http://arxiv.org/abs/1611.05891v1),
11/2016

- ["Quantum Loop Topography for Machine Learning"](
http://arxiv.org/abs/1611.01518v2
"Despite rapidly growing interest in harnessing machine learning in the study
of quantum many-body systems, training neural networks to identify quantum
phases is a nontrivial challenge. The key challenge is in efficiently
extracting essential information from the many-body Hamiltonian or wave
function and turning the information into an image that can be fed into a
neural network. When targeting topological phases, this task becomes
particularly challenging as topological phases are defined in terms of
non-local properties. Here we introduce quantum loop topography (QLT): a
procedure of constructing a multi-dimensional image from the "sample"
Hamiltonian or wave function by evaluating two-point operators that form loops
at independent Monte Carlo steps. The loop configuration is guided by
characteristic response for defining the phase, which is Hall conductivity for
the cases at hand. Feeding QLT to a fully-connected neural network with a
single hidden layer, we demonstrate that the architecture can be effectively
trained to distinguish Chern insulator and fractional Chern insulator from
trivial insulators with high fidelity. In addition to establishing the first
case of obtaining a phase diagram with topological quantum phase transition
with machine learning, the perspective of bridging traditional condensed matter
theory with machine learning will be broadly valuable."),
Yi Zhang, Eun-Ah Kim,
arXiv: [1611.01518](http://arxiv.org/abs/1611.01518v2),
11/2016

- ["Learning phase transitions by confusion"](
http://arxiv.org/abs/1610.02048v1
"Classifying phases of matter is a central problem in physics. For quantum
mechanical systems, this task can be daunting owing to the exponentially large
Hilbert space. Thanks to the available computing power and access to ever
larger data sets, classification problems are now routinely solved using
machine learning techniques. Here, we propose to use a neural network based
approach to find phase transitions depending on the performance of the neural
network after training it with deliberately incorrectly labelled data. We
demonstrate the success of this method on the topological phase transition in
the Kitaev chain, the thermal phase transition in the classical Ising model,
and the many-body-localization transition in a disordered quantum spin chain.
Our method does not depend on order parameters, knowledge of the topological
content of the phases, or any other specifics of the transition at hand. It
therefore paves the way to a generic tool to identify unexplored phase
transitions."),
Evert P. L. van Nieuwenburg, Ye-Hua Liu, Sebastian D. Huber,
arXiv: [1610.02048](http://arxiv.org/abs/1610.02048v1),
10/2016

- ["A Neural Decoder for Topological Codes"](
http://arxiv.org/abs/1610.04238v1
"We present an algorithm for error correction in topological codes that
exploits modern machine learning techniques. Our decoder is constructed from a
stochastic neural network called a Boltzmann machine, of the type extensively
used in deep learning. We provide a general prescription for the training of
the network and a decoding strategy that is applicable to a wide variety of
stabilizer codes with very little specialization. We demonstrate the neural
decoder numerically on the well-known two dimensional toric code with
phase-flip errors."),
Giacomo Torlai, Roger G. Melko,
arXiv: [1610.04238](http://arxiv.org/abs/1610.04238v1),
10/2016

- ["Self-Learning Monte Carlo Method"](
http://arxiv.org/abs/1610.03137v2
"Monte Carlo simulation is an unbiased numerical tool for studying classical
and quantum many-body systems. One of its bottlenecks is the lack of general
and efficient update algorithm for large size systems close to phase transition
or with strong frustrations, for which local updates perform badly. In this
work, we propose a new general-purpose Monte Carlo method, dubbed self-learning
Monte Carlo (SLMC), in which an efficient update algorithm is first learned
from the training data generated in trial simulations and then used to speed up
the actual simulation. We demonstrate the efficiency of SLMC in a spin model at
the phase transition point, achieving a 10-20 times speedup."),
Junwei Liu, Yang Qi, Zi Yang Meng, Liang Fu,
arXiv: [1610.03137](http://arxiv.org/abs/1610.03137v2),
10/2016

- ["Accelerate Monte Carlo Simulations with Restricted Boltzmann Machines"](
http://arxiv.org/abs/1610.02746v2
"Despite their exceptional flexibility and popularity, the Monte Carlo methods
often suffer from slow mixing times for challenging statistical physics
problems. We present a general strategy to overcome this difficulty by adopting
ideas and techniques from the machine learning community. We fit the
unnormalized probability of the physical model to a feedforward neural network
and reinterpret the architecture as a restricted Boltzmann machine. Then,
exploiting its feature detection ability, we utilize the restricted Boltzmann
machine for efficient Monte Carlo updates and to speed up the simulation of the
original physical system. We implement these ideas for the Falicov-Kimball
model and demonstrate improved acceptance ratio and autocorrelation time near
the phase transition point."),
Li Huang, Lei Wang,
arXiv: [1610.02746](http://arxiv.org/abs/1610.02746v2),
10/2016

- ["Machine Learning Topological States"](
http://arxiv.org/abs/1609.09060v2
"Artificial neural networks and machine learning have now reached a new era
after several decades of improvement where applications are to explode in many
fields of science, industry, and technology. Here, we use artificial neural
networks to study an intriguing phenomenon in quantum physics--- the
topological phases of matter. We find that certain topological states, either
symmetry-protected or with intrinsic topological order, can be represented with
classical artificial neural networks. This is demonstrated by using three
concrete spin systems, the one-dimensional (1D) symmetry-protected topological
cluster state and the 2D and 3D toric code states with intrinsic topological
orders. For all three cases we show rigorously that the topological ground
states can be represented by short-range neural networks in an \textit{exact}
and \textit{efficient} fashion---the required number of hidden neurons is as
small as the number of physical spins and the number of parameters scales only
\textit{linearly} with the system size. For the 2D toric-code model, we find
that the proposed short-range neural networks can describe the excited states
with abelain anyons and their nontrivial mutual statistics as well. In
addition, by using reinforcement learning we show that neural networks are
capable of finding the topological ground states of non-integrable Hamiltonians
with strong interactions and studying their topological phase transitions. Our
results demonstrate explicitly the exceptional power of neural networks in
describing topological quantum states, and at the same time provide valuable
guidance to machine learning of topological phases in generic lattice models."),
Dong-Ling Deng, Xiaopeng Li, S. Das Sarma,
arXiv: [1609.09060](http://arxiv.org/abs/1609.09060v2),
9/2016

- ["Pure density functional for strong correlations and the thermodynamic
  limit from machine learning"](
http://arxiv.org/abs/1609.03705v1
"We use density-matrix renormalization group, applied to a one-dimensional
model of continuum Hamiltonians, to accurately solve chains of hydrogen atoms
of various separations and numbers of atoms. We train and test a
machine-learned approximation to $F[n]$, the universal part of the electronic
density functional, to within quantum chemical accuracy. Our calculation (a)
bypasses the standard Kohn-Sham approach, avoiding the need to find orbitals,
(b) includes the strong correlation of highly-stretched bonds without any
specific difficulty (unlike all standard DFT approximations) and (c) is so
accurate that it can be used to find the energy in the thermodynamic limit to
quantum chemical accuracy."),
Li Li, Thomas E. Baker, Steven R. White, Kieron Burke,
arXiv: [1609.03705](http://arxiv.org/abs/1609.03705v1),
9/2016

- ["Machine Learning Phases of Strongly Correlated Fermions"](
http://arxiv.org/abs/1609.02552v3
"Machine learning offers an unprecedented perspective for the problem of
classifying phases in condensed matter physics. We employ neural-network
machine learning techniques to distinguish finite-temperature phases of the
strongly correlated fermions on cubic lattices. We show that a three
dimensional convolutional network trained on auxiliary field configurations
produced by quantum Monte Carlo simulations of the Hubbard model can correctly
predict the magnetic phase diagram of the model at the average density of one
(half filling). We then use the network, trained at half filling, to explore
the trend in the transition temperature as the system is doped away from half
filling. This transfer learning approach predicts that the instability to the
magnetic phase extends to at least 5% doping in this region. Our results pave
the way for other machine learning applications in correlated quantum many-body
systems."),
Kelvin Ch'ng, Juan Carrasquilla, Roger G. Melko, Ehsan Khatami,
arXiv: [1609.02552](http://arxiv.org/abs/1609.02552v3),
9/2016

- ["Machine learning quantum phases of matter beyond the fermion sign
  problem"](
http://arxiv.org/abs/1608.07848v1
"State-of-the-art machine learning techniques promise to become a powerful
tool in statistical mechanics via their capacity to distinguish different
phases of matter in an automated way. Here we demonstrate that convolutional
neural networks (CNN) can be optimized for quantum many-fermion systems such
that they correctly identify and locate quantum phase transitions in such
systems. Using auxiliary-field quantum Monte Carlo (QMC) simulations to sample
the many-fermion system, we show that the Green's function (but not the
auxiliary field) holds sufficient information to allow for the distinction of
different fermionic phases via a CNN. We demonstrate that this QMC + machine
learning approach works even for systems exhibiting a severe fermion sign
problem where conventional approaches to extract information from the Green's
function, e.g.~in the form of equal-time correlation functions, fail. We expect
that this capacity of hierarchical machine learning techniques to circumvent
the fermion sign problem will drive novel insights into some of the most
fundamental problems in statistical physics."),
Peter Broecker, Juan Carrasquilla, Roger G. Melko, Simon Trebst,
arXiv: [1608.07848](http://arxiv.org/abs/1608.07848v1),
8/2016

- ["Quantum gate learning in engineered qubit networks: Toffoli gate with
  always-on interactions"](
http://arxiv.org/abs/1509.04298v2
"We put forward a strategy to encode a quantum operation into the unmodulated
dynamics of a quantum network without the need of external control pulses,
measurements or active feedback. Our optimization scheme, inspired by
supervised machine learning, consists in engineering the pairwise couplings
between the network qubits so that the target quantum operation is encoded in
the natural reduced dynamics of a network section. The efficacy of the proposed
scheme is demonstrated by the finding of uncontrolled four-qubit networks that
implement either the Toffoli gate, the Fredkin gate, or remote logic
operations. The proposed Toffoli gate is stable against imperfections, has a
high-fidelity for fault tolerant quantum computation, and is fast, being based
on the non-equilibrium dynamics."),
Leonardo Banchi, Nicola Pancotti, Sougato Bose,
arXiv: [1509.04298](http://arxiv.org/abs/1509.04298v2),
9/2015

- ["Learning Thermodynamics with Boltzmann Machines"](
http://arxiv.org/abs/1606.02718v1
"A Boltzmann machine is a stochastic neural network that has been extensively
used in the layers of deep architectures for modern machine learning
applications. In this paper, we develop a Boltzmann machine that is capable of
modelling thermodynamic observables for physical systems in thermal
equilibrium. Through unsupervised learning, we train the Boltzmann machine on
data sets constructed with spin configurations importance-sampled from the
partition function of an Ising Hamiltonian at different temperatures using
Monte Carlo (MC) methods. The trained Boltzmann machine is then used to
generate spin states, for which we compare thermodynamic observables to those
computed by direct MC sampling. We demonstrate that the Boltzmann machine can
faithfully reproduce the observables of the physical system. Further, we
observe that the number of neurons required to obtain accurate results
increases as the system is brought close to criticality."),
Giacomo Torlai, Roger G. Melko,
arXiv: [1606.02718](http://arxiv.org/abs/1606.02718v1),
6/2016

- ["Solving the Quantum Many-Body Problem with Artificial Neural Networks"](
http://arxiv.org/abs/1606.02318v1
"The challenge posed by the many-body problem in quantum physics originates
from the difficulty of describing the non-trivial correlations encoded in the
exponential complexity of the many-body wave function. Here we demonstrate that
systematic machine learning of the wave function can reduce this complexity to
a tractable computational form, for some notable cases of physical interest. We
introduce a variational representation of quantum states based on artificial
neural networks with variable number of hidden neurons. A
reinforcement-learning scheme is then demonstrated, capable of either finding
the ground-state or describing the unitary time evolution of complex
interacting quantum systems. We show that this approach achieves very high
accuracy in the description of equilibrium and dynamical properties of
prototypical interacting spins models in both one and two dimensions, thus
offering a new powerful tool to solve the quantum many-body problem."),
Giuseppe Carleo, Matthias Troyer,
arXiv: [1606.02318](http://arxiv.org/abs/1606.02318v1),
6/2016

- ["Discovering Phase Transitions with Unsupervised Learning"](
http://arxiv.org/abs/1606.00318v2
"Unsupervised learning is a discipline of machine learning which aims at
discovering patterns in big data sets or classifying the data into several
categories without being trained explicitly. We show that unsupervised learning
techniques can be readily used to identify phases and phases transitions of
many body systems. Starting with raw spin configurations of a prototypical
Ising model, we use principal component analysis to extract relevant low
dimensional representations the original data and use clustering analysis to
identify distinct phases in the feature space. This approach successfully finds
out physical concepts such as order parameter and structure factor to be
indicators of the phase transition. We discuss future prospects of discovering
more complex phases and phase transitions using unsupervised learning
techniques."),
Lei Wang,
arXiv: [1606.00318](http://arxiv.org/abs/1606.00318v2),
6/2016

- ["Machine learning phases of matter"](
http://arxiv.org/abs/1605.01735v1
"Neural networks can be used to identify phases and phase transitions in
condensed matter systems via supervised machine learning. Readily programmable
through modern software libraries, we show that a standard feed-forward neural
network can be trained to detect multiple types of order parameter directly
from raw state configurations sampled with Monte Carlo. In addition, they can
detect highly non-trivial states such as Coulomb phases, and if modified to a
convolutional neural network, topological phases with no conventional order
parameter. We show that this classification occurs within the neural network
without knowledge of the Hamiltonian or even the general locality of
interactions. These results demonstrate the power of machine learning as a
basic research tool in the field of condensed matter and statistical physics."),
Juan Carrasquilla, Roger G. Melko,
arXiv: [1605.01735](http://arxiv.org/abs/1605.01735v1),
5/2016

- ["Understanding Machine-learned Density Functionals"](
http://arxiv.org/abs/1404.1333v2
"Kernel ridge regression is used to approximate the kinetic energy of
non-interacting fermions in a one-dimensional box as a functional of their
density. The properties of different kernels and methods of cross-validation
are explored, and highly accurate energies are achieved. Accurate {\em
constrained optimal densities} are found via a modified Euler-Lagrange
constrained minimization of the total energy. A projected gradient descent
algorithm is derived using local principal component analysis. Additionally, a
sparse grid representation of the density can be used without degrading the
performance of the methods. The implications for machine-learned density
functional approximations are discussed."),
Li Li, John C. Snyder, Isabelle M. Pelaschier, Jessica Huang, Uma-Naresh Niranjan, Paul Duncan, Matthias Rupp, Klaus-Robert Müller, Kieron Burke,
arXiv: [1404.1333](http://arxiv.org/abs/1404.1333v2),
4/2014


## Physics-Inspired Ideas Applied to Machine Learning



- ["Protection against Cloning for Deep Learning"](
http://arxiv.org/abs/1803.10995v1
"The susceptibility of deep learning to adversarial attack can be understood
in the framework of the Renormalisation Group (RG) and the vulnerability of a
specific network may be diagnosed provided the weights in each layer are known.
An adversary with access to the inputs and outputs could train a second network
to clone these weights and, having identified a weakness, use them to compute
the perturbation of the input data which exploits it. However, the RG framework
also provides a means to poison the outputs of the network imperceptibly,
without affecting their legitimate use, so as to prevent such cloning of its
weights and thereby foil the generation of adversarial data."),
Richard Kenway,
arXiv: [1803.10995](http://arxiv.org/abs/1803.10995v1),
3/2018

- ["Bridging Many-Body Quantum Physics and Deep Learning via Tensor Networks"](
http://arxiv.org/abs/1803.09780v1
"The harnessing of modern computational abilities for many-body wave-function
representations is naturally placed as a prominent avenue in contemporary
condensed matter physics. Specifically, highly expressive computational schemes
that are able to efficiently represent the entanglement properties of
many-particle systems are of interest. In the seemingly unrelated field of
machine learning, deep network architectures have exhibited an unprecedented
ability to tractably encompass the dependencies characterizing hard learning
tasks such as image classification. However, key questions regarding deep
learning architecture design still have no adequate theoretical answers. In
this paper, we establish a Tensor Network (TN) based common language between
the two disciplines, which allows us to offer bidirectional contributions. By
showing that many-body wave-functions are structurally equivalent to mappings
of ConvACs and RACs, we construct their TN equivalents, and suggest quantum
entanglement measures as natural quantifiers of dependencies in such networks.
Accordingly, we propose a novel entanglement based deep learning design scheme.
In the other direction, we identify that an inherent re-use of information in
state-of-the-art deep learning architectures is a key trait that distinguishes
them from TNs. We suggest a new TN manifestation of information re-use, which
enables TN constructs of powerful architectures such as deep recurrent networks
and overlapping convolutional networks. This allows us to theoretically
demonstrate that the entanglement scaling supported by these architectures can
surpass that of commonly used TNs in 1D, and can support volume law
entanglement in 2D polynomially more efficiently than RBMs. We thus provide
theoretical motivation to shift trending neural-network based wave-function
representations closer to state-of-the-art deep learning architectures."),
Yoav Levine, Or Sharir, Nadav Cohen, Amnon Shashua,
arXiv: [1803.09780](http://arxiv.org/abs/1803.09780v1),
3/2018

- ["Learning architectures based on quantum entanglement: a simple matrix
  product state algorithm for image recognition"](
http://arxiv.org/abs/1803.09111v1
"It is a fundamental, but still elusive question whether methods based on
quantum mechanics, in particular on quantum entanglement, can be used for
classical information processing and machine learning. Even partial answer to
this question would bring important insights to both fields of both machine
learning and quantum mechanics. In this work, we implement simple numerical
experiments, related to pattern/images classification, in which we represent
the classifiers by quantum matrix product states (MPS). Classical machine
learning algorithm is then applied to these quantum states. We explicitly show
how quantum features (i.e., single-site and bipartite entanglement) can emerge
in such represented images; entanglement characterizes here the importance of
data, and this information can be practically used to improve the learning
procedures. Thanks to the low demands on the dimensions and number of the
unitary matrices, necessary to construct the MPS, we expect such numerical
experiments could open new paths in classical machine learning, and shed at
same time lights on generic quantum simulations/computations."),
Yuhan Liu, Xiao Zhang, Maciej Lewenstein, Shi-Ju Ran,
arXiv: [1803.09111](http://arxiv.org/abs/1803.09111v1),
3/2018



- ["Comparing Dynamics: Deep Neural Networks versus Glassy Systems"](
http://arxiv.org/abs/1803.06969v1
"We analyze numerically the training dynamics of deep neural networks (DNN) by
using methods developed in statistical physics of glassy systems. The two main
issues we address are the complexity of the loss-landscape and of the dynamics
within it, and to what extent DNNs share similarities with glassy systems. Our
findings, obtained for different architectures and datasets, suggest that
during the training process the dynamics slows down because of an increasingly
large number of flat directions. At large times, when the loss is approaching
zero, the system diffuses at the bottom of the landscape. Despite some
similarities with the dynamics of mean-field glassy systems, in particular, the
absence of barrier crossing, we find distinctive dynamical behaviors in the two
cases, showing that the statistical properties of the corresponding loss and
energy landscapes are different. In contrast, when the network is
under-parametrized we observe a typical glassy behavior, thus suggesting the
existence of different phases depending on whether the network is
under-parametrized or over-parametrized."),
M. Baity-Jesi, L. Sagun, M. Geiger, S. Spigler, G. Ben Arous, C. Cammarota, Y. LeCun, M. Wyart, G. Biroli,
arXiv: [1803.06969](http://arxiv.org/abs/1803.06969v1),
3/2018

- ["Vulnerability of Deep Learning"](
http://arxiv.org/abs/1803.06111v1
"The Renormalisation Group (RG) provides a framework in which it is possible
to assess whether a deep-learning network is sensitive to small changes in the
input data and hence prone to error, or susceptible to adversarial attack.
Distinct classification outputs are associated with different RG fixed points
and sensitivity to small changes in the input data is due to the presence of
relevant operators at a fixed point. A numerical scheme, based on Monte Carlo
RG ideas, is proposed for identifying the existence of relevant operators and
the corresponding directions of greatest sensitivity in the input data. Thus, a
trained deep-learning network may be tested for its robustness and, if it is
vulnerable to attack, dangerous perturbations of the input data identified."),
Richard Kenway,
arXiv: [1803.06111](http://arxiv.org/abs/1803.06111v1),
3/2018

- ["Thermodynamics of Restricted Boltzmann Machines and related learning
  dynamics"](
http://arxiv.org/abs/1803.01960v1
"We analyze the learning process of the restricted Boltzmann machine (RBM), a
certain type of generative models used in the context of unsupervised learning.
In a first step, we investigate the thermodynamics properties by considering a
realistic statistical ensemble of RBM, assuming the information content of the
RBM to be mainly reflected by spectral properties of its weight matrix W. A
phase diagram is obtained which seems at first sight similar to the one of the
Sherrington-Kirkpatrick (SK) model with ferromagnetic couplings. The main
difference resides in the structure of the ferromagnetic phase which may or may
not be of compositional type, depending mainly on the distribution's kurtosis
of the singular vectors components of W. In a second step the learning dynamics
of an RBM from arbitrary data is studied in thermodynamic limit. A "typical"
learning trajectory is shown to solve an effective dynamical equation, based on
the aforementioned ensemble average and involving explicitly order parameters
obtained from the thermodynamic analysis. This accounts in particular for the
dominant singular values evolution and how this is driven by the input data: in
the linear regime at the beginning of the learning, they correspond to unstable
deformation modes of W reflecting dominant covariance modes of the data. In the
non-linear regime it is seen how the selected modes interact in later stages of
the learning procedure, by eventually imposing a matching between order
parameters with their empirical counterparts estimated from the data.
Experiments on both artificial and real data illustrate these considerations,
showing in particular how the RBM operates in the ferromagnetic compositional
phase."),
Aurélien Decelle, Giancarlo Fissore, Cyril Furtlehner,
arXiv: [1803.01960](http://arxiv.org/abs/1803.01960v1),
3/2018

- ["Energy-entropy competition and the effectiveness of stochastic gradient
  descent in machine learning"](
http://arxiv.org/abs/1803.01927v1
"Finding parameters that minimise a loss function is at the core of many
machine learning methods. The Stochastic Gradient Descent algorithm is widely
used and delivers state of the art results for many problems. Nonetheless,
Stochastic Gradient Descent typically cannot find the global minimum, thus its
empirical effectiveness is hitherto mysterious. We derive a correspondence
between parameter inference and free energy minimisation in statistical
physics. The degree of undersampling plays the role of temperature. Analogous
to the energy-entropy competition in statistical physics, wide but shallow
minima can be optimal if the system is undersampled, as is typical in many
applications. Moreover, we show that the stochasticity in the algorithm has a
non-trivial correlation structure which systematically biases it towards wide
minima. We illustrate our argument with two prototypical models: image
classification using deep learning, and a linear neural network where we can
analytically reveal the relationship between entropy and out-of-sample error."),
Yao Zhang, Andrew M. Saxe, Madhu S. Advani, Alpha A. Lee,
arXiv: [1803.01927](http://arxiv.org/abs/1803.01927v1),
3/2018



- ["Energy-entropy competition and the effectiveness of stochastic gradient
  descent in machine learning"](
http://arxiv.org/abs/1803.01927v1
"Finding parameters that minimise a loss function is at the core of many
machine learning methods. The Stochastic Gradient Descent algorithm is widely
used and delivers state of the art results for many problems. Nonetheless,
Stochastic Gradient Descent typically cannot find the global minimum, thus its
empirical effectiveness is hitherto mysterious. We derive a correspondence
between parameter inference and free energy minimisation in statistical
physics. The degree of undersampling plays the role of temperature. Analogous
to the energy-entropy competition in statistical physics, wide but shallow
minima can be optimal if the system is undersampled, as is typical in many
applications. Moreover, we show that the stochasticity in the algorithm has a
non-trivial correlation structure which systematically biases it towards wide
minima. We illustrate our argument with two prototypical models: image
classification using deep learning, and a linear neural network where we can
analytically reveal the relationship between entropy and out-of-sample error."),
Yao Zhang, Andrew M. Saxe, Madhu S. Advani, Alpha A. Lee,
arXiv: [1803.01927](http://arxiv.org/abs/1803.01927v1),
3/2018


- ["The Mean-Field Approximation: Information Inequalities, Algorithms, and
  Complexity"](
http://arxiv.org/abs/1802.06126v2
"The mean field approximation to the Ising model is a canonical variational
tool that is used for analysis and inference in Ising models. We provide a
simple and optimal bound for the KL error of the mean field approximation for
Ising models on general graphs, and extend it to higher order Markov random
fields. Our bound improves on previous bounds obtained in work in the graph
limit literature by Borgs, Chayes, Lov\'asz, S\'os, and Vesztergombi and
another recent work by Basak and Mukherjee. Our bound is tight up to lower
order terms. Building on the methods used to prove the bound, along with
techniques from combinatorics and optimization, we study the algorithmic
problem of estimating the (variational) free energy for Ising models and
general Markov random fields. For a graph $G$ on $n$ vertices and interaction
matrix $J$ with Frobenius norm $\| J \|_F$, we provide algorithms that
approximate the free energy within an additive error of $\epsilon n \|J\|_F$ in
time $\exp(poly(1/\epsilon))$. We also show that approximation within $(n
\|J\|_F)^{1-\delta}$ is NP-hard for every $\delta > 0$. Finally, we provide
more efficient approximation algorithms, which find the optimal mean field
approximation, for ferromagnetic Ising models and for Ising models satisfying
Dobrushin's condition."),
Vishesh Jain, Frederic Koehler, Elchanan Mossel,
arXiv: [1802.06126](http://arxiv.org/abs/1802.06126v2),
2/2018

- ["Inferring relevant features: from QFT to PCA"](
http://arxiv.org/abs/1802.05756v1
"In many-body physics, renormalization techniques are used to extract aspects
of a statistical or quantum state that are relevant at large scale, or for low
energy experiments. Recent works have proposed that these features can be
formally identified as those perturbations of the states whose
distinguishability most resist coarse-graining. Here, we examine whether this
same strategy can be used to identify important features of an unlabeled
dataset. This approach indeed results in a technique very similar to kernel PCA
(principal component analysis), but with a kernel function that is
automatically adapted to the data, or "learned". We test this approach on
handwritten digits, and find that the most relevant features are significantly
better for classification than those obtained from a simple gaussian kernel."),
Cédric Bény,
arXiv: [1802.05756](http://arxiv.org/abs/1802.05756v1),
2/2018

- ["Critical Percolation as a Framework to Analyze the Training of Deep
  Networks"](
http://arxiv.org/abs/1802.02154v1
"In this paper we approach two relevant deep learning topics: i) tackling of
graph structured input data and ii) a better understanding and analysis of deep
networks and related learning algorithms. With this in mind we focus on the
topological classification of reachability in a particular subset of planar
graphs (Mazes). Doing so, we are able to model the topology of data while
staying in Euclidean space, thus allowing its processing with standard CNN
architectures. We suggest a suitable architecture for this problem and show
that it can express a perfect solution to the classification task. The shape of
the cost function around this solution is also derived and, remarkably, does
not depend on the size of the maze in the large maze limit. Responsible for
this behavior are rare events in the dataset which strongly regulate the shape
of the cost function near this global minimum. We further identify an obstacle
to learning in the form of poorly performing local minima in which the network
chooses to ignore some of the inputs. We further support our claims with
training experiments and numerical analysis of the cost function on networks
with up to $128$ layers."),
Zohar Ringel, Rodrigo de Bem,
arXiv: [1802.02154](http://arxiv.org/abs/1802.02154v1),
2/2018

- ["Scale-invariant Feature Extraction of Neural Network and Renormalization
  Group Flow"](
http://arxiv.org/abs/1801.07172v1
"Theoretical understanding of how deep neural network (DNN) extracts features
from input images is still unclear, but it is widely believed that the
extraction is performed hierarchically through a process of coarse-graining. It
reminds us of the basic concept of renormalization group (RG) in statistical
physics. In order to explore possible relations between DNN and RG, we use the
Restricted Boltzmann machine (RBM) applied to Ising model and construct a flow
of model parameters (in particular, temperature) generated by the RBM. We show
that the unsupervised RBM trained by spin configurations at various
temperatures from $T=0$ to $T=6$ generates a flow along which the temperature
approaches the critical value $T_c=2.27$. This behavior is opposite to the
typical RG flow of the Ising model. By analyzing various properties of the
weight matrices of the trained RBM, we discuss why it flows towards $T_c$ and
how the RBM learns to extract features of spin configurations."),
Satoshi Iso, Shotaro Shiba, Sumito Yokoo,
arXiv: [1801.07172](http://arxiv.org/abs/1801.07172v1),
1/2018

- ["A relativistic extension of Hopfield neural networks via the mechanical
  analogy"](
http://arxiv.org/abs/1801.01743v1
"We propose a modification of the cost function of the Hopfield model whose
salient features shine in its Taylor expansion and result in more than pairwise
interactions with alternate signs, suggesting a unified framework for handling
both with deep learning and network pruning. In our analysis, we heavily rely
on the Hamilton-Jacobi correspondence relating the statistical model with a
mechanical system. In this picture, our model is nothing but the relativistic
extension of the original Hopfield model (whose cost function is a quadratic
form in the Mattis magnetization which mimics the non-relativistic Hamiltonian
for a free particle). We focus on the low-storage regime and solve the model
analytically by taking advantage of the mechanical analogy, thus obtaining a
complete characterization of the free energy and the associated
self-consistency equations in the thermodynamic limit. On the numerical side,
we test the performances of our proposal with MC simulations, showing that the
stability of spurious states (limiting the capabilities of the standard Hebbian
construction) is sensibly reduced due to presence of unlearning contributions
in this extended framework."),
Adriano Barra, Matteo Beccaria, Alberto Fachechi,
arXiv: [1801.01743](http://arxiv.org/abs/1801.01743v1),
1/2018

- ["Learning Relevant Features of Data with Multi-scale Tensor Networks"](
http://arxiv.org/abs/1801.00315v1
"Inspired by coarse-graining approaches used in physics, we show how similar
algorithms can be adapted for data. The resulting algorithms are based on
layered tree tensor networks and scale linearly with both the dimension of the
input and the training set size. Computing most of the layers with an
unsupervised algorithm, then optimizing just the top layer for supervised
classification of the MNIST and fashion-MNIST data sets gives very good
results. We also discuss mixing a prior guess for supervised weights together
with an unsupervised representation of the data, yielding a smaller number of
features nevertheless able to give good performance."),
E. M. Stoudenmire,
arXiv: [1801.00315](http://arxiv.org/abs/1801.00315v1),
12/2017

- ["Information Perspective to Probabilistic Modeling: Boltzmann Machines
  versus Born Machines"](
http://arxiv.org/abs/1712.04144v1
"We compare and contrast the statistical physics and quantum physics inspired
approaches for unsupervised generative modeling of classical data. The two
approaches represent probabilities of observed data using energy-based models
and quantum states respectively.Classical and quantum information patterns of
the target datasets therefore provide principled guidelines for structural
design and learning in these two approaches. Taking the restricted Boltzmann
machines (RBM) as an example, we analyze the information theoretical bounds of
the two approaches. We verify our reasonings by comparing the performance of
RBMs of various architectures on the standard MNIST datasets."),
Song Cheng, Jing Chen, Lei Wang,
arXiv: [1712.04144](http://arxiv.org/abs/1712.04144v1),
12/2017

- ["Stochastic gradient descent performs variational inference, converges to
  limit cycles for deep networks"](
http://arxiv.org/abs/1710.11029v2
"Stochastic gradient descent (SGD) is widely believed to perform implicit
regularization when used to train deep neural networks, but the precise manner
in which this occurs has thus far been elusive. We prove that SGD minimizes an
average potential over the posterior distribution of weights along with an
entropic regularization term. This potential is however not the original loss
function in general. So SGD does perform variational inference, but for a
different loss than the one used to compute the gradients. Even more
surprisingly, SGD does not even converge in the classical sense: we show that
the most likely trajectories of SGD for deep networks do not behave like
Brownian motion around critical points. Instead, they resemble closed loops
with deterministic components. We prove that such "out-of-equilibrium" behavior
is a consequence of highly non-isotropic gradient noise in SGD; the covariance
matrix of mini-batch gradients for deep networks has a rank as small as 1% of
its dimension. We provide extensive empirical validation of these claims,
proven in the appendix."),
Pratik Chaudhari, Stefano Soatto,
arXiv: [1710.11029](http://arxiv.org/abs/1710.11029v2),
10/2017

- ["A Correspondence Between Random Neural Networks and Statistical Field
  Theory"](
http://arxiv.org/abs/1710.06570v1
"A number of recent papers have provided evidence that practical design
questions about neural networks may be tackled theoretically by studying the
behavior of random networks. However, until now the tools available for
analyzing random neural networks have been relatively ad-hoc. In this work, we
show that the distribution of pre-activations in random neural networks can be
exactly mapped onto lattice models in statistical physics. We argue that
several previous investigations of stochastic networks actually studied a
particular factorial approximation to the full lattice model. For random linear
networks and random rectified linear networks we show that the corresponding
lattice models in the wide network limit may be systematically approximated by
a Gaussian distribution with covariance between the layers of the network. In
each case, the approximate distribution can be diagonalized by Fourier
transformation. We show that this approximation accurately describes the
results of numerical simulations of wide random neural networks. Finally, we
demonstrate that in each case the large scale behavior of the random networks
can be approximated by an effective field theory."),
Samuel S. Schoenholz, Jeffrey Pennington, Jascha Sohl-Dickstein,
arXiv: [1710.06570](http://arxiv.org/abs/1710.06570v1),
10/2017

- ["Entanglement Entropy of Target Functions for Image Classification and
  Convolutional Neural Network"](
http://arxiv.org/abs/1710.05520v1
"The success of deep convolutional neural network (CNN) in computer vision
especially image classification problems requests a new information theory for
function of image, instead of image itself. In this article, after establishing
a deep mathematical connection between image classification problem and quantum
spin model, we propose to use entanglement entropy, a generalization of
classical Boltzmann-Shannon entropy, as a powerful tool to characterize the
information needed for representation of general function of image. We prove
that there is a sub-volume-law bound for entanglement entropy of target
functions of reasonable image classification problems. Therefore target
functions of image classification only occupy a small subspace of the whole
Hilbert space. As a result, a neural network with polynomial number of
parameters is efficient for representation of such target functions of image.
The concept of entanglement entropy can also be useful to characterize the
expressive power of different neural networks. For example, we show that to
maintain the same expressive power, number of channels $D$ in a convolutional
neural network should scale with the number of convolution layers $n_c$ as
$D\sim D_0^{\frac{1}{n_c}}$. Therefore, deeper CNN with large $n_c$ is more
efficient than shallow ones."),
Ya-Hui Zhang,
arXiv: [1710.05520](http://arxiv.org/abs/1710.05520v1),
10/2017

- ["Machine Learning by Two-Dimensional Hierarchical Tensor Networks: A
  Quantum Information Theoretic Perspective on Deep Architectures"](
http://arxiv.org/abs/1710.04833v1
"The resemblance between the methods used in studying quantum-many body
physics and in machine learning has drawn considerable attention. In
particular, tensor networks (TNs) and deep learning architectures bear striking
similarities to the extent that TNs can be used for machine learning. Previous
results used one-dimensional TNs in image recognition, showing limited
scalability and a high bond dimension. In this work, we train two-dimensional
hierarchical TNs to solve image recognition problems, using a training
algorithm derived from the multipartite entanglement renormalization ansatz
(MERA). This approach overcomes scalability issues and implies novel
mathematical connections among quantum many-body physics, quantum information
theory, and machine learning. While keeping the TN unitary in the training
phase, TN states can be defined, which optimally encodes each class of the
images into a quantum many-body state. We study the quantum features of the TN
states, including quantum entanglement and fidelity. We suggest these
quantities could be novel properties that characterize the image classes, as
well as the machine learning tasks. Our work could be further applied to
identifying possible quantum properties of certain artificial intelligence
methods."),
Ding Liu, Shi-Ju Ran, Peter Wittek, Cheng Peng, Raul Blázquez García, Gang Su, Maciej Lewenstein,
arXiv: [1710.04833](http://arxiv.org/abs/1710.04833v1),
10/2017

- ["Neural Networks Quantum States, String-Bond States and chiral
  topological states"](
http://arxiv.org/abs/1710.04045v2
"Neural Networks Quantum States have been recently introduced as an Ansatz for
describing the wave function of quantum many-body systems. We show that there
are strong connections between Neural Networks Quantum States in the form of
Restricted Boltzmann Machines and some classes of Tensor Network states in
arbitrary dimension. In particular we demonstrate that short-range Restricted
Boltzmann Machines are Entangled Plaquette States, while fully connected
Restricted Boltzmann Machines are String-Bond States with a non-local geometry
and low bond dimension. These results shed light on the underlying architecture
of Restricted Boltzmann Machines and their efficiency at representing many-body
quantum states. String-Bond States also provide a generic way of enhancing the
power of Neural Networks Quantum States and a natural generalization to systems
with larger local Hilbert space. We compare the advantages and drawbacks of
these different classes of states and present a method to combine them
together. This allows us to benefit from both the entanglement structure of
Tensor Networks and the efficiency of Neural Network Quantum States into a
single Ansatz capable of targeting the wave function of strongly correlated
systems. While it remains a challenge to describe states with chiral
topological order using traditional Tensor Networks, we show that Neural
Networks Quantum States and their String-Bond States extension can describe a
lattice Fractional Quantum Hall state exactly. In addition, we provide
numerical evidence that Neural Networks Quantum States can approximate a chiral
spin liquid with better accuracy than Entangled Plaquette States and local
String-Bond States. Our results demonstrate the efficiency of neural networks
to describe complex quantum wave functions and pave the way towards the use of
String-Bond States as a tool in more traditional machine learning applications."),
Ivan Glasser, Nicola Pancotti, Moritz August, Ivan D. Rodriguez, J. Ignacio Cirac,
arXiv: [1710.04045](http://arxiv.org/abs/1710.04045v2),
10/2017

- ["Mean-field theory of input dimensionality reduction in unsupervised deep
  neural networks"](
http://arxiv.org/abs/1710.01467v2
"Deep neural networks as powerful tools are widely used in various domains.
However, the nature of computations at each layer of the deep networks is far
from being well understood. Increasing the interpretability of deep neural
networks is thus important. Here, we construct a mean-field framework to
understand how compact representations are developed across layers, not only in
deterministic random deep networks but also in generative deep networks where
network parameters are learned from input data. Our theory shows that the deep
computation implements a dimensionality reduction while maintaining a finite
level of weak correlations between neurons for possible feature extraction.
This work may pave the way for understanding how a sensory hierarchy works in
general."),
Haiping Huang,
arXiv: [1710.01467](http://arxiv.org/abs/1710.01467v2),
10/2017


- ["Machine Learning by Two-Dimensional Hierarchical Tensor Networks: A
  Quantum Information Theoretic Perspective on Deep Architectures"](
http://arxiv.org/abs/1710.04833v1
"The resemblance between the methods used in studying quantum-many body
physics and in machine learning has drawn considerable attention. In
particular, tensor networks (TNs) and deep learning architectures bear striking
similarities to the extent that TNs can be used for machine learning. Previous
results used one-dimensional TNs in image recognition, showing limited
scalability and a high bond dimension. In this work, we train two-dimensional
hierarchical TNs to solve image recognition problems, using a training
algorithm derived from the multipartite entanglement renormalization ansatz
(MERA). This approach overcomes scalability issues and implies novel
mathematical connections among quantum many-body physics, quantum information
theory, and machine learning. While keeping the TN unitary in the training
phase, TN states can be defined, which optimally encodes each class of the
images into a quantum many-body state. We study the quantum features of the TN
states, including quantum entanglement and fidelity. We suggest these
quantities could be novel properties that characterize the image classes, as
well as the machine learning tasks. Our work could be further applied to
identifying possible quantum properties of certain artificial intelligence
methods."),
Ding Liu, Shi-Ju Ran, Peter Wittek, Cheng Peng, Raul Blázquez García, Gang Su, Maciej Lewenstein,
arXiv: [1710.04833](http://arxiv.org/abs/1710.04833v1),
10/2017

- ["Unsupervised Generative Modeling Using Matrix Product States"](
http://arxiv.org/abs/1709.01662v2
"Generative modeling, which learns joint probability distribution from
training data and generates samples according to it, is an important task in
machine learning and artificial intelligence. Inspired by probabilistic
interpretation of quantum physics, we propose a generative model using matrix
product states, which is a tensor network originally proposed for describing
(particularly one-dimensional) entangled quantum states. Our model enjoys
efficient learning by utilizing the density matrix renormalization group method
which allows dynamic adjusting dimensions of the tensors, and offers an
efficient direct sampling approach, Zipper, for generative tasks. We apply our
method to generative modeling of several standard datasets including the
principled Bars and Stripes, random binary patterns and the MNIST handwritten
digits, to illustrate ability of our model, and discuss features as well as
drawbacks of our model over popular generative models such as Hopfield model,
Boltzmann machines and generative adversarial networks. Our work shed light on
many interesting directions for future exploration on the development of
quantum-inspired algorithms for unsupervised machine learning, which is of
possibility of being realized by a quantum device."),
Zhao-Yu Han, Jun Wang, Heng Fan, Lei Wang, Pan Zhang,
arXiv: [1709.01662](http://arxiv.org/abs/1709.01662v2),
9/2017

- ["Deep Learning and Quantum Entanglement: Fundamental Connections with
  Implications to Network Design"](
http://arxiv.org/abs/1704.01552v2
"Deep convolutional networks have witnessed unprecedented success in various
machine learning applications. Formal understanding on what makes these
networks so successful is gradually unfolding, but for the most part there are
still significant mysteries to unravel. The inductive bias, which reflects
prior knowledge embedded in the network architecture, is one of them. In this
work, we establish a fundamental connection between the fields of quantum
physics and deep learning. We use this connection for asserting novel
theoretical observations regarding the role that the number of channels in each
layer of the convolutional network fulfills in the overall inductive bias.
Specifically, we show an equivalence between the function realized by a deep
convolutional arithmetic circuit (ConvAC) and a quantum many-body wave
function, which relies on their common underlying tensorial structure. This
facilitates the use of quantum entanglement measures as well-defined
quantifiers of a deep network's expressive ability to model intricate
correlation structures of its inputs. Most importantly, the construction of a
deep ConvAC in terms of a Tensor Network is made available. This description
enables us to carry a graph-theoretic analysis of a convolutional network, with
which we demonstrate a direct control over the inductive bias of the deep
network via its channel numbers, that are related to the min-cut in the
underlying graph. This result is relevant to any practitioner designing a
network for a specific task. We theoretically analyze ConvACs, and empirically
validate our findings on more common ConvNets which involve ReLU activations
and max pooling. Beyond the results described above, the description of a deep
convolutional network in well-defined graph-theoretic tools and the formal
connection to quantum entanglement, are two interdisciplinary bridges that are
brought forth by this work."),
Yoav Levine, David Yakira, Nadav Cohen, Amnon Shashua,
arXiv: [1704.01552](http://arxiv.org/abs/1704.01552v2),
4/2017

- ["Reinforcement Learning Using Quantum Boltzmann Machines"](
http://arxiv.org/abs/1612.05695v2
"We investigate whether quantum annealers with select chip layouts can
outperform classical computers in reinforcement learning tasks. We associate a
transverse field Ising spin Hamiltonian with a layout of qubits similar to that
of a deep Boltzmann machine (DBM) and use simulated quantum annealing (SQA) to
numerically simulate quantum sampling from this system. We design a
reinforcement learning algorithm in which the set of visible nodes representing
the states and actions of an optimal policy are the first and last layers of
the deep network. In absence of a transverse field, our simulations show that
DBMs train more effectively than restricted Boltzmann machines (RBM) with the
same number of weights. Since sampling from Boltzmann distributions of a DBM is
not classically feasible, this is evidence of advantage of a non-Turing
sampling oracle. We then develop a framework for training the network as a
quantum Boltzmann machine (QBM) in the presence of a significant transverse
field for reinforcement learning. This further improves the reinforcement
learning method using DBMs."),
Daniel Crawford, Anna Levit, Navid Ghadermarzy, Jaspreet S. Oberoi, Pooya Ronagh,
arXiv: [1612.05695](http://arxiv.org/abs/1612.05695v2),
12/2016

- ["Low-Rank Tensor Networks for Dimensionality Reduction and Large-Scale
  Optimization Problems: Perspectives and Challenges PART 1"](
http://arxiv.org/abs/1609.00893v3
"Machine learning and data mining algorithms are becoming increasingly
important in analyzing large volume, multi-relational and multi--modal
datasets, which are often conveniently represented as multiway arrays or
tensors. It is therefore timely and valuable for the multidisciplinary research
community to review tensor decompositions and tensor networks as emerging tools
for large-scale data analysis and data mining. We provide the mathematical and
graphical representations and interpretation of tensor networks, with the main
focus on the Tucker and Tensor Train (TT) decompositions and their extensions
or generalizations.
  Keywords: Tensor networks, Function-related tensors, CP decomposition, Tucker
models, tensor train (TT) decompositions, matrix product states (MPS), matrix
product operators (MPO), basic tensor operations, multiway component analysis,
multilinear blind source separation, tensor completion, linear/multilinear
dimensionality reduction, large-scale optimization problems, symmetric
eigenvalue decomposition (EVD), PCA/SVD, huge systems of linear equations,
pseudo-inverse of very large matrices, Lasso and Canonical Correlation Analysis
(CCA) (This is Part 1)"),
A. Cichocki, N. Lee, I. V. Oseledets, A. -H. Phan, Q. Zhao, D. Mandic,
arXiv: [1609.00893](http://arxiv.org/abs/1609.00893v3),
9/2016

- ["Why does deep and cheap learning work so well?"](
http://arxiv.org/abs/1608.08225v4
"We show how the success of deep learning could depend not only on mathematics
but also on physics: although well-known mathematical theorems guarantee that
neural networks can approximate arbitrary functions well, the class of
functions of practical interest can frequently be approximated through "cheap
learning" with exponentially fewer parameters than generic ones. We explore how
properties frequently encountered in physics such as symmetry, locality,
compositionality, and polynomial log-probability translate into exceptionally
simple neural networks. We further argue that when the statistical process
generating the data is of a certain hierarchical form prevalent in physics and
machine-learning, a deep neural network can be more efficient than a shallow
one. We formalize these claims using information theory and discuss the
relation to the renormalization group. We prove various "no-flattening
theorems" showing when efficient linear deep networks cannot be accurately
approximated by shallow ones without efficiency loss, for example, we show that
$n$ variables cannot be multiplied using fewer than 2^n neurons in a single
hidden layer."),
Henry W. Lin, Max Tegmark, David Rolnick,
arXiv: [1608.08225](http://arxiv.org/abs/1608.08225v4),
8/2016

- ["Supervised Learning with Quantum-Inspired Tensor Networks"](
http://arxiv.org/abs/1605.05775v2
"Tensor networks are efficient representations of high-dimensional tensors
which have been very successful for physics and mathematics applications. We
demonstrate how algorithms for optimizing such networks can be adapted to
supervised learning tasks by using matrix product states (tensor trains) to
parameterize models for classifying images. For the MNIST data set we obtain
less than 1% test set classification error. We discuss how the tensor network
form imparts additional structure to the learned model and suggest a possible
generative interpretation."),
E. Miles Stoudenmire, David J. Schwab,
arXiv: [1605.05775](http://arxiv.org/abs/1605.05775v2),
5/2016

- ["Exponential Machines"](
http://arxiv.org/abs/1605.03795v3
"Modeling interactions between features improves the performance of machine
learning solutions in many domains (e.g. recommender systems or sentiment
analysis). In this paper, we introduce Exponential Machines (ExM), a predictor
that models all interactions of every order. The key idea is to represent an
exponentially large tensor of parameters in a factorized format called Tensor
Train (TT). The Tensor Train format regularizes the model and lets you control
the number of underlying parameters. To train the model, we develop a
stochastic Riemannian optimization procedure, which allows us to fit tensors
with 2^160 entries. We show that the model achieves state-of-the-art
performance on synthetic data with high-order interactions and that it works on
par with high-order factorization machines on a recommender system dataset
MovieLens 100K."),
Alexander Novikov, Mikhail Trofimov, Ivan Oseledets,
arXiv: [1605.03795](http://arxiv.org/abs/1605.03795v3),
5/2016

- ["Quantum Boltzmann Machine"](
http://arxiv.org/abs/1601.02036v1
"Inspired by the success of Boltzmann Machines based on classical Boltzmann
distribution, we propose a new machine learning approach based on quantum
Boltzmann distribution of a transverse-field Ising Hamiltonian. Due to the
non-commutative nature of quantum mechanics, the training process of the
Quantum Boltzmann Machine (QBM) can become nontrivial. We circumvent the
problem by introducing bounds on the quantum probabilities. This allows us to
train the QBM efficiently by sampling. We show examples of QBM training with
and without the bound, using exact diagonalization, and compare the results
with classical Boltzmann training. We also discuss the possibility of using
quantum annealing processors like D-Wave for QBM training and application."),
Mohammad H. Amin, Evgeny Andriyash, Jason Rolfe, Bohdan Kulchytskyy, Roger Melko,
arXiv: [1601.02036](http://arxiv.org/abs/1601.02036v1),
1/2016

- ["An exact mapping between the Variational Renormalization Group and Deep
  Learning"](
http://arxiv.org/abs/1410.3831v1
"Deep learning is a broad set of techniques that uses multiple layers of
representation to automatically learn relevant features directly from
structured data. Recently, such techniques have yielded record-breaking results
on a diverse set of difficult machine learning tasks in computer vision, speech
recognition, and natural language processing. Despite the enormous success of
deep learning, relatively little is understood theoretically about why these
techniques are so successful at feature learning and compression. Here, we show
that deep learning is intimately related to one of the most important and
successful techniques in theoretical physics, the renormalization group (RG).
RG is an iterative coarse-graining scheme that allows for the extraction of
relevant features (i.e. operators) as a physical system is examined at
different length scales. We construct an exact mapping from the variational
renormalization group, first introduced by Kadanoff, and deep learning
architectures based on Restricted Boltzmann Machines (RBMs). We illustrate
these ideas using the nearest-neighbor Ising Model in one and two-dimensions.
Our results suggests that deep learning algorithms may be employing a
generalized RG-like scheme to learn relevant features from data."),
Pankaj Mehta, David J. Schwab,
arXiv: [1410.3831](http://arxiv.org/abs/1410.3831v1),
10/2014

- ["Tensor Networks for Big Data Analytics and Large-Scale Optimization
  Problems"](
http://arxiv.org/abs/1407.3124v2
"In this paper we review basic and emerging models and associated algorithms
for large-scale tensor networks, especially Tensor Train (TT) decompositions
using novel mathematical and graphical representations. We discus the concept
of tensorization (i.e., creating very high-order tensors from lower-order
original data) and super compression of data achieved via quantized tensor
train (QTT) networks. The purpose of a tensorization and quantization is to
achieve, via low-rank tensor approximations "super" compression, and
meaningful, compact representation of structured data. The main objective of
this paper is to show how tensor networks can be used to solve a wide class of
big data optimization problems (that are far from tractable by classical
numerical methods) by applying tensorization and performing all operations
using relatively small size matrices and tensors and applying iteratively
optimized and approximative tensor contractions.
  Keywords: Tensor networks, tensor train (TT) decompositions, matrix product
states (MPS), matrix product operators (MPO), basic tensor operations,
tensorization, distributed representation od data optimization problems for
very large-scale problems: generalized eigenvalue decomposition (GEVD),
PCA/SVD, canonical correlation analysis (CCA)."),
Andrzej Cichocki,
arXiv: [1407.3124](http://arxiv.org/abs/1407.3124v2),
7/2014


## Quantum Computation and Quantum Algorithms for Machine Learning



- ["Towards Quantum Machine Learning with Tensor Networks"](
http://arxiv.org/abs/1803.11537v1
"Machine learning is a promising application of quantum computing, but
challenges remain as near-term devices will have a limited number of physical
qubits and high error rates. Motivated by the usefulness of tensor networks for
machine learning in the classical context, we propose quantum computing
approaches to both discriminative and generative learning, with circuits based
on tree and matrix product state tensor networks that could have benefits for
near-term devices. The result is a unified framework where classical and
quantum computing can benefit from the same theoretical and algorithmic
developments, and the same model can be trained classically then transferred to
the quantum setting for additional optimization. Tensor network circuits can
also provide qubit-efficient schemes where, depending on the architecture, the
number of physical qubits required scales only logarithmically with, or
independently of the input or output data sizes. We demonstrate our proposals
with numerical experiments, training a discriminative model to perform
handwriting recognition using a optimization procedure that could be carried
out on quantum hardware, and testing the noise resilience of the trained model."),
William Huggins, Piyush Patel, K. Birgitta Whaley, E. Miles Stoudenmire,
arXiv: [1803.11537](http://arxiv.org/abs/1803.11537v1),
3/2018

- ["Barren plateaus in quantum neural network training landscapes"](
http://arxiv.org/abs/1803.11173v1
"Many experimental proposals for noisy intermediate scale quantum devices
involve training a parameterized quantum circuit with a classical optimization
loop. Such hybrid quantum-classical algorithms are popular for applications in
quantum simulation, optimization, and machine learning. Due to its simplicity
and hardware efficiency, random circuits are often proposed as initial guesses
for exploring the space of quantum states. We show that the exponential
dimension of Hilbert space and the gradient estimation complexity make this
choice unsuitable for hybrid quantum-classical algorithms run on more than a
few qubits. Specifically, we show that for a wide class of reasonable
parameterized quantum circuits, the probability that the gradient along any
reasonable direction is non-zero to some fixed precision is exponentially small
as a function of the number of qubits. We argue that this is related to the
2-design characteristic of random circuits, and that solutions to this problem
must be studied."),
Jarrod R. McClean, Sergio Boixo, Vadim N. Smelyanskiy, Ryan Babbush, Hartmut Neven,
arXiv: [1803.11173](http://arxiv.org/abs/1803.11173v1),
3/2018

- ["Quantum algorithms for training Gaussian Processes"](
http://arxiv.org/abs/1803.10520v1
"Gaussian processes (GPs) are important models in supervised machine learning.
Training in Gaussian processes refers to selecting the covariance functions and
the associated parameters in order to improve the outcome of predictions, the
core of which amounts to evaluating the logarithm of the marginal likelihood
(LML) of a given model. LML gives a concrete measure of the quality of
prediction that a GP model is expected to achieve. The classical computation of
LML typically carries a polynomial time overhead with respect to the input
size. We propose a quantum algorithm that computes the logarithm of the
determinant of a Hermitian matrix, which runs in logarithmic time for sparse
matrices. This is applied in conjunction with a variant of the quantum linear
system algorithm that allows for logarithmic time computation of the form
$\mathbf{y}^TA^{-1}\mathbf{y}$, where $\mathbf{y}$ is a dense vector and $A$ is
the covariance matrix. We hence show that quantum computing can be used to
estimate the LML of a GP with exponentially improved efficiency under certain
conditions."),
Zhikuan Zhao, Jack K. Fitzsimons, Michael A. Osborne, Stephen J. Roberts, Joseph F. Fitzsimons,
arXiv: [1803.10520](http://arxiv.org/abs/1803.10520v1),
3/2018



- ["Measurement-based adaptation protocol with quantum reinforcement
  learning"](
http://arxiv.org/abs/1803.05340v1
"Machine learning employs dynamical algorithms that mimic the human capacity
to learn, where the reinforcement learning ones are among the most similar to
humans in this respect. On the other hand, adaptability is an essential aspect
to perform any task efficiently in a changing environment, and it is
fundamental for many purposes, such as natural selection. Here, we propose an
algorithm based on successive measurements to adapt one quantum state to a
reference unknown state, in the sense of achieving maximum overlap. The
protocol naturally provides many identical copies of the reference state, such
that in each measurement iteration more information about it is obtained. In
our protocol, we consider a system composed of three parts, the "environment"
system, which provides the reference state copies; the register, which is an
auxiliary subsystem that interacts with the environment to acquire information
from it; and the agent, which corresponds to the quantum state that is adapted
by digital feedback with input corresponding to the outcome of the measurements
on the register. With this proposal we can achieve an average fidelity between
the environment and the agent of more than $90\% $ with less than $30$
iterations of the protocol. In addition, we extend the formalism to $ d
$-dimensional states, reaching an average fidelity of around $80\% $ in less
than $400$ iterations for $d=$ 11, for a variety of genuinely quantum as well
as semiclassical states. This work paves the way for the development of quantum
reinforcement learning protocols using quantum data, and the future deployment
of semi-autonomous quantum systems."),
F. Albarrán-Arriagada, J. C. Retamal, E. Solano, L. Lamata,
arXiv: [1803.05340](http://arxiv.org/abs/1803.05340v1),
3/2018



- ["Quantum Variational Autoencoder"](
http://arxiv.org/abs/1802.05779v1
"Variational autoencoders (VAEs) are powerful generative models with the
salient ability to perform inference. Here, we introduce a \emph{quantum
variational autoencoder} (QVAE): a VAE whose latent generative process is
implemented as a quantum Boltzmann machine (QBM). We show that our model can be
trained end-to-end by maximizing a well-defined loss-function: a "quantum"
lower-bound to a variational approximation of the log-likelihood. We use
quantum Monte Carlo (QMC) simulations to train and evaluate the performance of
QVAEs. To achieve the best performance, we first create a VAE platform with
discrete latent space generated by a restricted Boltzmann machine (RBM). Our
model achieves state-of-the-art performance on the MNIST dataset when compared
against similar approaches that only involve discrete variables in the
generative process. We consider QVAEs with a smaller number of latent units to
be able to perform QMC simulations, which are computationally expensive. We
show that QVAEs can be trained effectively in regimes where quantum effects are
relevant despite training via the quantum bound. Our findings open the way to
the use of quantum computers to train QVAEs to achieve competitive performance
for generative models. Placing a QBM in the latent space of a VAE leverages the
full potential of current and next-generation quantum computers as sampling
devices."),
Amir Khoshaman, Walter Vinci, Brandon Denis, Evgeny Andriyash, Mohammad H. Amin,
arXiv: [1802.05779](http://arxiv.org/abs/1802.05779v1),
2/2018

- ["Learning DNFs under product distributions via μ-biased quantum
  Fourier sampling"](
http://arxiv.org/abs/1802.05690v1
"We show that DNF formulae can be quantum PAC-learned in polynomial time under
product distributions using a quantum example oracle. The best classical
algorithm (without access to membership queries) runs in superpolynomial time.
Our result extends the work by Bshouty and Jackson (1998) that proved that DNF
formulae are efficiently learnable under the uniform distribution using a
quantum example oracle. Our proof is based on a new quantum algorithm that
efficiently samples the coefficients of a {\mu}-biased Fourier transform."),
Varun Kanade, Andrea Rocchetto, Simone Severini,
arXiv: [1802.05690](http://arxiv.org/abs/1802.05690v1),
2/2018

- ["Taking gradients through experiments: LSTMs and memory proximal policy
  optimization for black-box quantum control"](
http://arxiv.org/abs/1802.04063v1
"In this work we introduce the application of black-box quantum control as an
interesting rein- forcement learning problem to the machine learning community.
We analyze the structure of the reinforcement learning problems arising in
quantum physics and argue that agents parameterized by long short-term memory
(LSTM) networks trained via stochastic policy gradients yield a general method
to solving them. In this context we introduce a variant of the proximal policy
optimization (PPO) algorithm called the memory proximal policy optimization
(MPPO) which is based on this analysis. We then show how it can be applied to
specific learning tasks and present results of nu- merical experiments showing
that our method achieves state-of-the-art results for several learning tasks in
quantum control with discrete and continouous control parameters."),
Moritz August, José Miguel Hernández-Lobato,
arXiv: [1802.04063](http://arxiv.org/abs/1802.04063v1),
2/2018

- ["Leveraging Adiabatic Quantum Computation for Election Forecasting"](
http://arxiv.org/abs/1802.00069v1
"Accurate, reliable sampling from fully-connected graphs with arbitrary
correlations is a difficult problem. Such sampling requires knowledge of the
probabilities of observing every possible state of a graph. As graph size
grows, the number of model states becomes intractably large and efficient
computation requires full sampling be replaced with heuristics and algorithms
that are only approximations of full sampling. This work investigates the
potential impact of adiabatic quantum computation for sampling purposes,
building on recent successes training Boltzmann machines using a quantum
device. We investigate the use case of quantum computation to train Boltzmann
machines for predicting the 2016 Presidential election."),
Maxwell Henderson, John Novak, Tristan Cook,
arXiv: [1802.00069](http://arxiv.org/abs/1802.00069v1),
1/2018

- ["A Quantum Extension of Variational Bayes Inference"](
http://arxiv.org/abs/1712.04709v1
"Variational Bayes (VB) inference is one of the most important algorithms in
machine learning and widely used in engineering and industry. However, VB is
known to suffer from the problem of local optima. In this Letter, we generalize
VB by using quantum mechanics, and propose a new algorithm, which we call
quantum annealing variational Bayes (QAVB) inference. We then show that QAVB
drastically improve the performance of VB by applying them to a clustering
problem described by a Gaussian mixture model. Finally, we discuss an intuitive
understanding on how QAVB works well."),
Hideyuki Miyahara, Yuki Sughiyama,
arXiv: [1712.04709](http://arxiv.org/abs/1712.04709v1),
12/2017

- ["Hardening Quantum Machine Learning Against Adversaries"](
http://arxiv.org/abs/1711.06652v1
"Security for machine learning has begun to become a serious issue for present
day applications. An important question remaining is whether emerging quantum
technologies will help or hinder the security of machine learning. Here we
discuss a number of ways that quantum information can be used to help make
quantum classifiers more secure or private. In particular, we demonstrate a
form of robust principal component analysis that, under some circumstances, can
provide an exponential speedup relative to robust methods used at present. To
demonstrate this approach we introduce a linear combinations of unitaries
Hamiltonian simulation method that we show functions when given an imprecise
Hamiltonian oracle, which may be of independent interest. We also introduce a
new quantum approach for bagging and boosting that can use quantum
superposition over the classifiers or splits of the training set to aggregate
over many more models than would be possible classically. Finally, we provide a
private form of $k$--means clustering that can be used to prevent an all
powerful adversary from learning more than a small fraction of a bit from any
user. These examples show the role that quantum technologies can play in the
security of ML and vice versa. This illustrates that quantum computing can
provide useful advantages to machine learning apart from speedups."),
Nathan Wiebe, Ram Shankar Siva Kumar,
arXiv: [1711.06652](http://arxiv.org/abs/1711.06652v1),
11/2017

- ["An efficient quantum algorithm for generative machine learning"](
http://arxiv.org/abs/1711.02038v1
"A central task in the field of quantum computing is to find applications
where quantum computer could provide exponential speedup over any classical
computer. Machine learning represents an important field with broad
applications where quantum computer may offer significant speedup. Several
quantum algorithms for discriminative machine learning have been found based on
efficient solving of linear algebraic problems, with potential exponential
speedup in runtime under the assumption of effective input from a quantum
random access memory. In machine learning, generative models represent another
large class which is widely used for both supervised and unsupervised learning.
Here, we propose an efficient quantum algorithm for machine learning based on a
quantum generative model. We prove that our proposed model is exponentially
more powerful to represent probability distributions compared with classical
generative models and has exponential speedup in training and inference at
least for some instances under a reasonable assumption in computational
complexity theory. Our result opens a new direction for quantum machine
learning and offers a remarkable example in which a quantum algorithm shows
exponential improvement over any classical algorithm in an important
application field."),
Xun Gao, Zhengyu Zhang, Luming Duan,
arXiv: [1711.02038](http://arxiv.org/abs/1711.02038v1),
11/2017

- ["Learning Hidden Quantum Markov Models"](
http://arxiv.org/abs/1710.09016v1
"Hidden Quantum Markov Models (HQMMs) can be thought of as quantum
probabilistic graphical models that can model sequential data. We extend
previous work on HQMMs with three contributions: (1) we show how classical
hidden Markov models (HMMs) can be simulated on a quantum circuit, (2) we
reformulate HQMMs by relaxing the constraints for modeling HMMs on quantum
circuits, and (3) we present a learning algorithm to estimate the parameters of
an HQMM from data. While our algorithm requires further optimization to handle
larger datasets, we are able to evaluate our algorithm using several synthetic
datasets. We show that on HQMM generated data, our algorithm learns HQMMs with
the same number of hidden states and predictive accuracy as the true HQMMs,
while HMMs learned with the Baum-Welch algorithm require more states to match
the predictive accuracy."),
Siddarth Srinivasan, Geoff Gordon, Byron Boots,
arXiv: [1710.09016](http://arxiv.org/abs/1710.09016v1),
10/2017

- ["Enhanced Quantum Synchronization via Quantum Machine Learning"](
http://arxiv.org/abs/1709.08519v1
"We study the quantum synchronization between a pair of two-level systems
inside two coupledcavities. Using a digital-analog decomposition of the master
equation that rules the system dynamics, we show that this approach leads to
quantum synchronization between both two-level systems. Moreover, we can
identify in this digital-analog block decomposition the fundamental elements of
a quantum machine learning protocol, in which the agent and the environment
(learning units) interact through a mediating system, namely, the register. If
we can additionally equip this algorithm with a classical feedback mechanism,
which consists of projective measurements in the register, reinitialization of
the register state and local conditional operations on the agent and register
subspace, a powerful and flexible quantum machine learning protocol emerges.
Indeed, numerical simulations show that this protocol enhances the
synchronization process, even when every subsystem experience different
loss/decoherence mechanisms, and give us flexibility to choose the
synchronization state. Finally, we propose an implementation based on current
technologies in superconducting circuits."),
F. A. Cárdenas-López, M. Sanz, J. C. Retamal, E. Solano,
arXiv: [1709.08519](http://arxiv.org/abs/1709.08519v1),
9/2017

- ["Generalized Quantum Reinforcement Learning with Quantum Technologies"](
http://arxiv.org/abs/1709.07848v1
"We propose a protocol to perform generalized quantum reinforcement learning
with quantum technologies. At variance with recent results on quantum
reinforcement learning with superconducting circuits [L. Lamata, Sci. Rep. 7,
1609 (2017)], in our current protocol coherent feedback during the learning
process is not required, enabling its implementation in a wide variety of
quantum systems. We consider diverse possible scenarios for an agent, an
environment, and a register that connects them, involving multiqubit and
multilevel systems, as well as open-system dynamics. We finally propose
possible implementations of this protocol in trapped ions and superconducting
circuits. The field of quantum reinforcement learning with quantum technologies
will enable enhanced quantum control, as well as more efficient machine
learning calculations."),
F. A. Cárdenas-López, L. Lamata, J. C. Retamal, E. Solano,
arXiv: [1709.07848](http://arxiv.org/abs/1709.07848v1),
9/2017

- ["Quantum Autoencoders via Quantum Adders with Genetic Algorithms"](
http://arxiv.org/abs/1709.07409v1
"The quantum autoencoder is a recent paradigm in the field of quantum machine
learning, which may enable an enhanced use of resources in quantum
technologies. To this end, quantum neural networks with less nodes in the inner
than in the outer layers were considered. Here, we propose a useful connection
between approximate quantum adders and quantum autoencoders. Specifically, this
link allows us to employ optimized approximate quantum adders, obtained with
genetic algorithms, for the implementation of quantum autoencoders for a
variety of initial states. Furthermore, we can also directly optimize the
quantum autoencoders via genetic algorithms. Our approach opens a different
path for the design of quantum autoencoders in controllable quantum platforms."),
L. Lamata, U. Alvarez-Rodriguez, J. D. Martín-Guerrero, M. Sanz, E. Solano,
arXiv: [1709.07409](http://arxiv.org/abs/1709.07409v1),
9/2017

- ["Quantum machine learning: a classical perspective"](
http://arxiv.org/abs/1707.08561v3
"Recently, increased computational power and data availability, as well as
algorithmic advances, have led machine learning techniques to impressive
results in regression, classification, data-generation and reinforcement
learning tasks. Despite these successes, the proximity to the physical limits
of chip fabrication alongside the increasing size of datasets are motivating a
growing number of researchers to explore the possibility of harnessing the
power of quantum computation to speed-up classical machine learning algorithms.
Here we review the literature in quantum machine learning and discuss
perspectives for a mixed readership of classical machine learning and quantum
computation experts. Particular emphasis will be placed on clarifying the
limitations of quantum algorithms, how they compare with their best classical
counterparts and why quantum resources are expected to provide advantages for
learning problems. Learning in the presence of noise and certain
computationally hard problems in machine learning are identified as promising
directions for the field. Practical questions, like how to upload classical
data into quantum form, will also be addressed."),
Carlo Ciliberto, Mark Herbster, Alessandro Davide Ialongo, Massimiliano Pontil, Andrea Rocchetto, Simone Severini, Leonard Wossnig,
arXiv: [1707.08561](http://arxiv.org/abs/1707.08561v3),
7/2017



- ["Experimental Quantum Hamiltonian Learning"](
http://arxiv.org/abs/1703.05402v1
"Efficiently characterising quantum systems, verifying operations of quantum
devices and validating underpinning physical models, are central challenges for
the development of quantum technologies and for our continued understanding of
foundational physics. Machine-learning enhanced by quantum simulators has been
proposed as a route to improve the computational cost of performing these
studies. Here we interface two different quantum systems through a classical
channel - a silicon-photonics quantum simulator and an electron spin in a
diamond nitrogen-vacancy centre - and use the former to learn the latter's
Hamiltonian via Bayesian inference. We learn the salient Hamiltonian parameter
with an uncertainty of approximately $10^{-5}$. Furthermore, an observed
saturation in the learning algorithm suggests deficiencies in the underlying
Hamiltonian model, which we exploit to further improve the model itself. We go
on to implement an interactive version of the protocol and experimentally show
its ability to characterise the operation of the quantum photonic device. This
work demonstrates powerful new quantum-enhanced techniques for investigating
foundational physical models and characterising quantum technologies."),
Jianwei Wang, Stefano Paesani, Raffaele Santagati, Sebastian Knauer, Antonio A. Gentile, Nathan Wiebe, Maurangelo Petruzzella, Jeremy L. O'Brien, John G. Rarity, Anthony Laing, Mark G. Thompson,
arXiv: [1703.05402](http://arxiv.org/abs/1703.05402v1),
3/2017

- ["Tomography and Generative Data Modeling via Quantum Boltzmann Training"](
http://arxiv.org/abs/1612.05204v1
"The promise of quantum neural nets, which utilize quantum effects to model
complex data sets, has made their development an aspirational goal for quantum
machine learning and quantum computing in general. Here we provide new methods
of training quantum Boltzmann machines, which are a class of recurrent quantum
neural network. Our work generalizes existing methods and provides new
approaches for training quantum neural networks that compare favorably to
existing methods. We further demonstrate that quantum Boltzmann machines enable
a form of quantum state tomography that not only estimates a state but provides
a perscription for generating copies of the reconstructed state. Classical
Boltzmann machines are incapable of this. Finally we compare small
non-stoquastic quantum Boltzmann machines to traditional Boltzmann machines for
generative tasks and observe evidence that quantum models outperform their
classical counterparts."),
Maria Kieferova, Nathan Wiebe,
arXiv: [1612.05204](http://arxiv.org/abs/1612.05204v1),
12/2016

- ["Quantum Machine Learning"](
http://arxiv.org/abs/1611.09347v1
"Recent progress implies that a crossover between machine learning and quantum
information processing benefits both fields. Traditional machine learning has
dramatically improved the benchmarking and control of experimental quantum
computing systems, including adaptive quantum phase estimation and designing
quantum computing gates. On the other hand, quantum mechanics offers
tantalizing prospects to enhance machine learning, ranging from reduced
computational complexity to improved generalization performance. The most
notable examples include quantum enhanced algorithms for principal component
analysis, quantum support vector machines, and quantum Boltzmann machines.
Progress has been rapid, fostered by demonstrations of midsized quantum
optimizers which are predicted to soon outperform their classical counterparts.
Further, we are witnessing the emergence of a physical theory pinpointing the
fundamental and natural limitations of learning. Here we survey the cutting
edge of this merger and list several open problems."),
Jacob Biamonte, Peter Wittek, Nicola Pancotti, Patrick Rebentrost, Nathan Wiebe, Seth Lloyd,
arXiv: [1611.09347](http://arxiv.org/abs/1611.09347v1),
11/2016

- ["Quantum algorithms for supervised and unsupervised machine learning"](
http://arxiv.org/abs/1307.0411v2
"Machine-learning tasks frequently involve problems of manipulating and
classifying large numbers of vectors in high-dimensional spaces. Classical
algorithms for solving such problems typically take time polynomial in the
number of vectors and the dimension of the space. Quantum computers are good at
manipulating high-dimensional vectors in large tensor product spaces. This
paper provides supervised and unsupervised quantum machine learning algorithms
for cluster assignment and cluster finding. Quantum machine learning can take
time logarithmic in both the number of vectors and their dimension, an
exponential speed-up over classical algorithms."),
Seth Lloyd, Masoud Mohseni, Patrick Rebentrost,
arXiv: [1307.0411](http://arxiv.org/abs/1307.0411v2),
7/2013

- ["Improved Bounds on Quantum Learning Algorithms"](
http://arxiv.org/abs/quant-ph/0411140v2
"In this article we give several new results on the complexity of algorithms
that learn Boolean functions from quantum queries and quantum examples.
  Hunziker et al. conjectured that for any class C of Boolean functions, the
number of quantum black-box queries which are required to exactly identify an
unknown function from C is $O(\frac{\log |C|}{\sqrt{{\hat{\gamma}}^{C}}})$,
where $\hat{\gamma}^{C}$ is a combinatorial parameter of the class C. We
essentially resolve this conjecture in the affirmative by giving a quantum
algorithm that, for any class C, identifies any unknown function from C using
$O(\frac{\log |C| \log \log |C|}{\sqrt{{\hat{\gamma}}^{C}}})$ quantum black-box
queries.
  We consider a range of natural problems intermediate between the exact
learning problem (in which the learner must obtain all bits of information
about the black-box function) and the usual problem of computing a predicate
(in which the learner must obtain only one bit of information about the
black-box function). We give positive and negative results on when the quantum
and classical query complexities of these intermediate problems are
polynomially related to each other.
  Finally, we improve the known lower bounds on the number of quantum examples
(as opposed to quantum black-box queries) required for $(\epsilon,\delta)$-PAC
learning any concept class of Vapnik-Chervonenkis dimension d over the domain
$\{0,1\}^n$ from $\Omega(\frac{d}{n})$ to $\Omega(\frac{1}{\epsilon}\log
\frac{1}{\delta}+d+\frac{\sqrt{d}}{\epsilon})$. This new lower bound comes
closer to matching known upper bounds for classical PAC learning."),
Alp Atici, Rocco A. Servedio,
arXiv: [quant-ph/0411140](http://arxiv.org/abs/quant-ph/0411140v2),
11/2004

- ["The geometry of quantum learning"](
http://arxiv.org/abs/quant-ph/0309059v1
"Concept learning provides a natural framework in which to place the problems
solved by the quantum algorithms of Bernstein-Vazirani and Grover. By combining
the tools used in these algorithms--quantum fast transforms and amplitude
amplification--with a novel (in this context) tool--a solution method for
geometrical optimization problems--we derive a general technique for quantum
concept learning. We name this technique "Amplified Impatient Learning" and
apply it to construct quantum algorithms solving two new problems: BATTLESHIP
and MAJORITY, more efficiently than is possible classically."),
Markus Hunziker, David A. Meyer, Jihun Park, James Pommersheim, Mitch Rothstein,
arXiv: [quant-ph/0309059](http://arxiv.org/abs/quant-ph/0309059v1),
9/2003

