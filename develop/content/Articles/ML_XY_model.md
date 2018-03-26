Title: Machine Learning Topological Defects in the XY Model
Date: 2018-03-14 19:00
Tags: quantum mechanics, topological phase transitions, machine learning, supervised learning
Author: Matthew Beach
Summary: Machine learning can detect classical topological defects in materials
Slug: ML-in-XY

One of the discoveries that earned the [2016 Nobel Prize](https://www.nobelprize.org/nobel_prizes/physics/laureates/2016/) was that topological effects play an important role in certain classical phase transitions. The work of David J. Thouless and J. Michael Kosterlitz explained how two-dimensional materials, like thin films, can have phase transitions despite lacking a true ordered phase. Their key insight was that small topological objects called vortices are bound tightly together at low temperatures, and yet at high temperature, they become unbound and proliferate. This sharp change in behavior turns out to be universal and explains many unconventional phase transitions such as those found in superfluid helium and superconductors.

It took over three decades for physicists to recognize that topological defects are responsible for the superfluid helium transition, but what if there was another way to detect these objects?

In the last few years, we have seen the remarkable success of algorithms that are capable of finding meaningful structures and patterns in massive datasets. Machine learning techniques, in particular, deep neural networks, have had tremendous success in achieving state-of-the-art results on image recognition tasks. By breaking down an image into it's most important properties, neural networks are able to successfully identify complex objects.

Machine learning has already found many uses in physics; from detecting particle collisions at [CERN](http://openlab.cern/news/identification-complex-dynamical-systems-neural-networks) to identifying [quantum phases of matter](https://www.nature.com/articles/nphys4035), and even [classifying galaxies](Deep Galaxy: Classification of Galaxies based on Deep Convolutional Neural Networks) from satellite images. Can machine learning also tell us something about topological defects?


## What is a vortex?

A topological defect is a group of spins that have a different topology than spins that point in only one direction (Figure 1 (a)). Because of this, a spin configuration with defects cannot be smoothly transformed into the ferromagnetic ground state where all spins are aligned. A vortex is a special type of topological defect defined by having a non-zero [*winding number*](https://en.wikipedia.org/wiki/Winding_number). Intuitively, the winding number, $w$, measures the total rotation that the spins undergo along the closed curve. For a square lattice, a vortex is just four neighboring spins which undergo a clockwise rotation about their center as shown in Figure 1 (b). A positive winding number indicates a vortex, and a negative number corresponds to an antivortex. Higher winding numbers like that shown in Figure 1 (d) are extremely rare so they can effectively be neglected.

To get some intuition, try placing a pen on the bottom-left spin of any circle in Figure 1. As you move the pen clockwise along the circle, adjust the pen to point in the direction indicated by each spin vector. Arriving back at the first spin, if the pen has done a full clockwise rotation, then that configuration is a vortex. Likewise, if the pen rotates counterclockwise, then it is an antivortex.

<figure>
    <img
    style="float: center; width: 90%; margin-right: 1%; margin-bottom: 0.0em;"
    src="/images/windings.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 1.</b> Illustration of how the winding number counts the number of times the spins rotate around the origin. In (a), the spins are mostly aligned so they have zero winding number, whereas in (b) the spins form a vortex because they complete one clockwise rotation while transversing the circular path. The antivortex in (c) completes one counterclockwise rotation along the path, and the higher-order vortex in (d) completes two full clockwise rotations.
    </figcaption>
</figure>
<br/>

The simplest physical model with vortices is the two-dimensional classical XY model which consists of unit spins that can point in any direction, $\theta_i\in[0,2\pi)$, and interact only with their nearest neighbors. At low temperatures, the spins generally align like an Ising ferromagnet. However, because the spins take on continuous values $\theta$, spin-wave excitations become very strong and prevent any true [long-range order](https://en.wikipedia.org/wiki/Mermin%E2%80%93Wagner_theorem). Unlike the ferromagnet, in this regime, the correlations between spins decay polynomially with their separation. This is called a quasi-long-range ordered phase.

At the temperature $T_{\text{KT}} \approx 0.8935$ [1], the XY model exhibits a Kosterlitz–Thouless transition. In contrast with conventional phase transitions, the KT transition displays no discontinuity in any observable such as the magnetization or energy. Instead, the transition is caused by the unbinding of vortex-antivortex pairs above $T_{\text{KT}}$. Below this temperature, it takes infinite energy to excite a single vortex; however, thermal fluctuations can create vortex-antivortex *pairs* so long as they remain bound together (Figure 2).  Above $T_{\text{KT}}$, it is entropically favorable for vortices to separate. This balancing act between energy and entropy is responsible for the vortex-unbinding transition.


<figure>
    <img
    style="float: center; width: 35%; margin-left: 5%;margin-right: 5%;"
    src="/images/below.png"
    />
    <img
    style="float: center; width: 35%; margin-left: 5%;margin-right: 5%;"
    src="/images/above.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 2.</b> <b>Left:</b> A configuration of the spins in the XY model for a temperature below the KT temperature. Notice that it contains one vortex-antivortex pair that is bound together. <b>Right:</b> A configuration above the KT temperature contains one bound pair but also some free vortices.
    </figcaption>
</figure>
<br/>

## Can neural networks recognize vortices?

Training a neural network to recognize vortices is different than training one to classify cats and dogs. Instead of a single number (or word) labeling the image, we have an entire array of numbers $w$, where each number corresponds to one square of the lattice.

<!-- The network must learn to compute the winding number for each square of neighboring spins. -->

We will train a supervised convolutional neural network implemented in [TensorFlow](https://www.tensorflow.org/) to recognize vortices. The input to the network is spin configurations on a square lattice generated by Monte Carlo sampling and the labels are created by explicitly calculating the winding numbers for each square of spins. The label is not one number, but rather a two-dimensional array of numbers, with values of $+1$ (vortex), $-1$ (antivortex), and $0$ otherwise.

Instead of training directly on the vorticity, it helps to split the label into three channels. This is the equivalent of one-hot encoding vectors into binary vectors, except applied to matrices. Instead of the vorticity $w\in[0,\pm1]$, we rewrite this as three binary arrays containing only $0$'s and $1$'s. To revert back to the ordinary 'one-channel' vorticity, we simply subtract the $w=-1$ channel from the $w=+1$ channel.

The full network architecture is displayed in Figure 3. The motivation for this structure is that the first convolutional layer with 2x2 filters might learn local angle differences as in [2]. The three-channel output is activated with a softmax function which forces the network to choose only one value for the vorticity of each plaquette.


<figure>
    <img
    style="float: center; width: 90%; margin-right: 1%; margin-bottom: 0.0em;"
    src="/images/CNN.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 3.</b> Network architecture for supervised learning of vortices. On the input spins we apply 128 convolution filters of size 2×2 to capture interactions between spins. After applying ReLu activation functions, the next layer is 64 filters of size 1×1, again with ReLu activations. The network outputs three binary channels with a softmax activation function to ensure only one label is associated to each square in the lattice. Each channels represents ones of the possible values of the winding number.
    </figcaption>
</figure>
<br/>

In Figure 3, the loss function during training is shown for different lattice sizes. Each network was trained using the Adam optimizer and early stopping with a patience of ten epochs to prevent overfitting. It turns out that this network architecture readily achieves over $99\%$ accuracy in identifying vortices!

Adding $L_2$ regularization had no effect on the performance of the network; however, ReLu units were substantially better than tanh or sigmoid functions. Likewise, a single-layer fully-connected network did not perform well, yet convolutions layers worked perfectly. Increasing the number of layers or neurons resulted in faster convergence.

<figure>
    <img
    style="float: center; width: 70%; margin-left: 10%; margin-bottom: 0.0em;"
    src="/images/loss.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 4.</b> Training and cross-validation loss function for system sizes from 8×8 up to 32×32. Training is stopped once the loss on the cross-validation set fails to decrease after ten epochs.
    </figcaption>
</figure>
<br/>


Extending this to the quantum realm has already been done for 1D topological band insulators [3]. In this case, the label is not an array, but rather a single number (the global winding number), which describes the topological sector of a Hamiltonian. With a network similar to Figure 3., the authors achieve very high accuracy and can even detect higher-order winding numbers not included in the training data.

## Could a network discover vortex-unbinding?

Another question is whether it's possible for supervised learning to identify vortices for the purpose of phase classification. Given the experimental evidence of a phase transition, could a network have learned that vortex-unbinding drives the transition?

One method to address this would be to just add an additional layer to the end of the architecture which classifies the phase as either below or above $T_{\text{KT}}$. Hopefully, the network would learn vortices in an intermediate layer (the softmax layer) before classifying the phases. For a given spin configuration, if the softmax layer outputs the correct three-channel winding number, than the network will have learned that vortices are responsible for the phase transition. Unfortunately, this network (nor that studied in [4]) was able to learn about vortex-unbinding without additional information.

Turns out neural networks could not earn the Nobel Prize... at least not yet.

## Conclusions

We have demonstrated that a neural network can easily learn to recognize vortices when trained on label data, yet it remains unclear if an unsupervised method could achieve similar results. So far, the results from PCA and variational autoencoders both suffer from learning the energy or magnetization instead of vorticity [5-8]. This is perhaps not surprising since, while in the thermodynamic limit the 2D XY model has no magnetization, a finite-size system has a very large magnetization in the low-temperature region. Even a lattice the [size of Texas](http://discovery.ucl.ac.uk/1466258/) would have a significant magnetization! While theorists can take the continuum limit to avoid these finite-size effects, machine learning algorithms don't have this privilege and must work with only the data they are given.

Still, neural networks exhibit a remarkable ability to recognize patterns, including the identification of vortices in the XY model. While historically it can take decades to understand which microscopic objects influence the macroscopic properties of materials, one can't help but wonder; will the process of discovery be accelerated by the adaption of machine learning algorithms in physics?


## References

[1] Y. D. Hsieh, Y.J. Kao, A. W. Sandvik. *Finite-size scaling method for the Berezinskii–Kosterlitz–Thouless transition* [J. Stat. Mech.: Theory and Experiment (09), P09001 (2013)](http://iopscience.iop.org/article/10.1088/1742-5468/2013/09/P09001/meta)

[2] P. Suchsland, S. Wessel, *Parameter diagnostics of phases and phase transition learning by neural networks* [arXiv: 802.09876 (2018)](https://arxiv.org/abs/1802.09876)

[3] P. Zhang, H. Shen, H. Zhai, *Machine Learning Topological Invariants with Neural Networks* [Phys. Rev. Lett. 120, 066401 (2018)](https://journals.aps.org/prl/abstract/10.1103/
PhysRevLett.120.066401)

[4] M. J. S. Beach, A. Golubeva, R. G. Melko, *Machine learning vortices at the Kosterlitz-Thouless transition* [Phys. Rev. B 97.045207 (2018)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.97.045207)

[5] W. Hu, R. R. P. Singh, R. T. Scalettar, *Discovering phases, phase transitions, and crossovers through unsupervised machine learning: A critical examination* [Phys. Rev. E 95.062122 (2017)](https://link.aps.org/doi/10.1103/PhysRevE.95.062122)

[6] C. Wang, H. Zhai, *Machine learning of frustrated classical spin models. I. Principal component analysis* [Phys. Rev. B 96.144432 (2017)](https://link.aps.org/doi/10.1103/PhysRevB.96.144432)

[7] C. Wang, H. Zhai, *Machine Learning of Frustrated Classical Spin Models. II. Kernel Principal Component Analysis* [https://arxiv.org/abs/1803.01205 (2018)](https://arxiv.org/abs/1803.01205)

[8] M. Cristoforetti, G. Jurman, A. I. Nardelli, C. Furlanello, *Towards meaningful physics from generative models* [arXiv:1705.09524 (2017)](https://arxiv.org/abs/1705.09524)

