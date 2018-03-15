Title: Machine Learning Topological Defects in the XY Model
Date: 2018-03-14 19:00
Tags: quantum mechanics, topological phase transitions, machine learning, supervised learning
Author: Matt Beach
Summary: catchy two-sentence summary to appear here 
Slug: ML-in-XY

One of the discoveries that earned the 2016 Nobel Prize was that topological effects play an important role in classical phase transitions. The work of David J. Thouless and J. Michael Kosterlitz explained how two-dimensional materials, like thin films, can have phase transitions despite lacking a true ordered phase. They showed that small distortions of the field called vortices are bound tightly together at low temperatures, and yet at high temperature, they become unbound and proliferate. This sharp change in behavior turns out to be universal and explains many unconventional phase transitions such as those found in superfluid helium and superconductors.

It took over 30 years for physicists to recognize that topological defects are responsible for the superfluid helium transition, but what if there was another way to detect these objects?

In the last few years, we have seen remarkable success of novel algorithms that are capable of finding meaningful structures and patterns in massive datasets. Machine learning - in particular deep neural networks - have had tremendous success in achieving state-of-the-art results on image recognition tasks. These networks are capable of finding common features between images which lets them differentiate between distinct objects like cats and dogs. 

Machine learning has already found many uses in physics - from detecting particle collisions to identifying quantum phases of matter, and even classifying galaxies from satellite images. Can machine learning also tell us something about topological defects?

## What is a vortex?

The simplest model that allows to study vortices is the two-dimensional classical XY model. It describes spins on a two-dimensional lattice that can rotate in the plane, such that the state of each spin can be specified by a single angle @@\theta\in[0,2\pi)@@, and the Hamiltonian reads

$$H = -J\sum_{\langle i,j \rangle }\cos(\theta_i - \theta_j)\,.$$

The coupling @@J@@ is positive, such that the ground state at @@T=0@@ is an Ising ferromagnet. However, the spin-wave excitations at low temperatures @@T\gt 0@@ prevent any true long-range order. Unlike in the ferromagnet, one finds that in this regime the correlations between spins decay polynomially with their separation.

The vortex in the XY model is a topological spin configuration that cannot be transformed into the ground state where all spins are aligned by a continuous rotation of the spins.

In the continuum, a vortex is defined through a finite value of vorticity

$$ w = \frac{1}{2\pi}\oint_{C} d\mathbb{r}\cdot \nabla\theta(\mathbb{r}), $$

where @@C@@ is any curve enclosing the center of the vortex. Since the integral measures the total rotation of the spin vector along the curve, @@w@@ is simply the number of full turns it makes when circling the vortex, also referred to as the winding number.

Analogously, on a square lattice, a vortex is defined as four spins on a plaquette which undergo a clockwise rotation about the plaquette center as shown in Figure 1. The explicit formula for the vorticity of each plaquette @@\mathcal{P}@@ is 

$$ w = \frac{1}{2\pi}\sum_{[i,j]\in \mathcal{P}}\Delta\theta_{ij} $$

with @@\Delta\theta_{ij} = (\theta_i - \theta_j) \mod 2\pi@@ such that @@\Delta\theta_{ij}\in [-\pi, \pi)@@. A positive winding number @@w@@ indicates a vortex, and a negative @@w@@ corresponds to an antivortex. Winding numbers higher than @@|w|=1@@ occur rarely. Some examples of different @@w@@'s are shown in Figure 1.

<figure>
<img style="width:400px;" src="/images/windings.png"/>
<figcaption>Illustration of how @@w@@ counts the number of times the vectors rotate around the origin.</figcaption>
</figure>

A single vortex introduces a field distortion that propagates through the entire system. In fact, it can be shown that the energy of a vortex diverges logarithmically with the linear system size @@L@@, and hence a single vortex can not be excited by thermal fluctuations. The combination of a vortex with an antivortex, however, introduces only a local field distortion, and the associated energy of the pair scales logarithmically with their separation distance. This kind of excitations can be induced thermally and are therefore found in the low-temperature regime of the XY model.

At the temperature @@T_{\text{BKT}} \approx 0.892@@, the XY model exhibits the Berezinskii–Kosterlitz–Thouless transition. Unlike conventional phase transitions, the BKT transition displays no discontinuity in any observable. Instead, it is caused by the unbinding of vortex-antivortex pairs above @@T_{\text{BKT}}@@, as shown in Figure 2. The reason why pairs can unbind despite the logarithmically divergent energy of the individual (anti)vortices is their high entropy which scales logarithmically with the quadratic system size @@L^2@@. Above @@T_{\text{BKT}}@@ the entropic contribution to the free energy outweights the energetic one, and the pairs can unbind. There is also a finite peak in the specific heat near @@T=1.1@@ which indicates where the number of vortices increases most rapidly.


<figure>
<img style="width:400px;" src="/images/below.png"/>
<img style="width:400px;" src="/images/above.png"/>
<figcaption>Spin configuration below  @@T_{\text{BKT}}@@ (left) and above @@T_{\text{BKT}}@@ (right).</figcaption>
</figure>


## Can neural networks learn to recognize vortices?

Training a neural network to recognize vortices is different than training it to classify cats and dogs. Instead of a single number (or word) labeling the image, we have an entire array of numbers @@w@@ - one for each plaquette of the lattice. The network must learn to distinguish between spin configurations based on the location and vorticity of each plaquette.

The input to our network is the spin configurations of the 2D XY model on a square lattice generated by Monte Carlo sampling. Now we want the network to output the vorticity of each plaquette (the circles in Figure 2), so we create labels to all spin configurations by applying formula (1). The result is a two-dimensional array of numbers, with value +1/-1 for vortex/antivortex, and 0 otherwise. 

Instead of training directly on the vorticity, we split the output of the network into three channels, for @@w=0,\pm 1@@ respectively. This is the equivalent of one-hot encoding vectors into binary vectors. We encode the vorticity @@w\in[0,\pm1]@@ into three binary arrays.  We could also add more channels for higher winding numbers, but these are extremely rare and can be neglected here. To revert back to the ordinary 'one-channel' vorticity, we simply take the "@@+1@@" channel minus the "@@-1@@" channel.

<figure>
<img style="width:500px;" src="/images/CNN.png"/>
<figcaption>Network architecture for learning vortices in the XY model.</figcaption>
</figure>

The network architecture used is displayed in Figure 2. The first convolutional layer with 2x2 filters can learn local angle differences. The second layer, we expect, learns that certain difference are equivalent, i.e. @@\Delta \theta = 2\pi \equiv \Delta \theta = 0@@. This performs the @@\text{mod } 2\pi@@ from the definition of @@w@@. Lastly, the three-channel output is activated with a @@\text{Softmax}@@ function. This forces the network to choose only one value for the vorticity of each plaquette. Adding more neurons or increasing the depth usually results in faster convergence, but we prefer to keep the network minimal here.

It turns out that this network architecture readily achieves over 99% accuracy. In Figure 3, the loss function on the training and cross-validation set using the Adam optimizer. Early stopping was used with a patience of 10 epochs to prevent overfitting. The final test accuracy for a @@16\times 16@@ lattice was 99.6%. 

<figure>
<img style="width:400px;" src="/images/loss.png"/>
<figcaption>Training and cross-validation loss function for system sizes from @@8\times 8@@ up to @@64\times 64@@.</figcaption>
</figure>

So far, we have demonstrated that a neural network can easily learn to recognize vortices when trained directly on the vorticity, yet it remains to be seen if an unsupervised method could achieve similar results. So far, the results from PCA and variational autoencoders both suffer from learning the energy or magnetization instead of vorticity [2,3,4,5]. This is perhaps not surprising since (while in the thermodynamic limit the 2D XY model has no magnetization) a finite-size system has a very large magnetization in the low-temperature region.

Another question proposed in [6] is whether it's possible for supervised learning to identify vortices for the purpose of phase classification. Basically, one can just add an additional layer to the end of the architecture which classifies the phase as either below or above @@T_{\text{BKT}}@@. Hopefully, the network would learn vortices in an intermediate layer (the @@\text{Softmax}@@ layer) before classifying the phases. Unfortunately, this was not possible with our network nor that studied in [6]. It seems that it is in general not beneficial to learn vortices and very difficult given the nature of the BKT transition. Turns out neural networks may be more like experimentalists than theoreticians - they observe the transition in the magnetization.

* In [6] it was shown that the unsupervised "confusion" method predicts @@T=1.1@@ as the critical temperature instead of the true @@T_{\text{BKT}}@@. This corresponds to the peak in the specific heat.

## References

[1] P. Zhang, H. Shen, and H. Zhai, *Machine Learning Topological Invariants with Neural Networks* [Phys. Rev. Lett. 120, 066401 (2018)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.066401)

[2] W. Hu, R. R. P. Singh, and R. T. Scalettar, *Discovering phases, phase transitions, and crossovers through unsupervised machine learning: A critical examination* [Phys. Rev. E 95.062122 (2017)](https://link.aps.org/doi/10.1103/PhysRevE.95.062122)

[3] C. Wang, and H. Zhai, *Machine learning of frustrated classical spin models. I. Principal component analysis* [Phys. Rev. B 96.144432 (2017)](https://link.aps.org/doi/10.1103/PhysRevB.96.144432)

[4] C. Wang, and H. Zhai, *Machine Learning of Frustrated Classical Spin Models. II. Kernel Principal Component Analysis* [https://arxiv.org/abs/1803.01205 (2018)](https://arxiv.org/abs/1803.01205)

[5] M. Cristoforetti, G. Jurman, A. I. Nardelli, and C. Furlanello, *Towards meaningful physics from generative models* [arXiv:1705.09524 (2017)](https://arxiv.org/abs/1705.09524)

[6] Matthew J. S. Beach, Anna Golubeva, and Roger G. Melko, *Machine learning vortices at the Kosterlitz-Thouless transition* [Phys. Rev. B 97.045207 (2018)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.97.045207)
