Title: The Unreasonable Effectiveness of Restricted Boltzmann Machines
Date: 2017-01-17 20:00
Category: Articles
Tags: quantum mechanics, machine learning, Boltzmann Machines
Authors: Roger Melko
Summary: The unsupervised learning tool, ambiguous in modern deep learning, has some important lessons for quantum physicists
Status: draft


When I first encountered a Boltzmann Machine, I did not immediately see its appeal to a quantum many-body physicist.  A Boltzmann Machine is a stochastic neural network used to (approximately) learn probability distributions, and to generate samples from the learned distribution.  It is a common tool in feature extraction, classification, and other tasks in the modern machine learning community.

But, why would we physicists need a learning tool to approximate distributions, when, presumably, in order to obtain data to train the machine, we must already ''know'' the distribution (or, at least, the Hamiltonian)?  I knew as a Monte Carlo practitioner, we are already in the business of sampling from perfect distributions -- a practice fraught with many difficulties as it is.  Why would we add further systematic error (on top of our statistical error) by sampling from an imperfect distribution, which presumably takes considerable computational effort to learn? The application of such a machine in the technology industry is more obvious.  There, we are trying to train a machine on (say) a finite-size number of cat pictures, so that the machine itself is capable of generating (dreaming) a picture of a ``cat''.  For me, each picture of a cat is instead (say) a spin configuration, each pixel and up or down spin state, sampled e.g. from the Boltzmann distribution at finite temperature.  This sampling is done with a Markov Chain Monte Carlo procedure, an efficient algorithm honed by scientists since the end of Word-War 2.  It seems, we already have the distribution, and we already know how to sample it very efficiently.  Why would we use these samples to train an imperfect machine, the sampling of which may be less efficient than our existing algorithms, honed by scientists for the past 65 years?

Needless to say, I'm now a convert to the myriad possibilities that Boltzmann Machines present to the physicist.  Over the last year, I've been watching the field develop with excitement.  One variant, the `Restricted' Boltzmann Machine (RBM), seems to hold particular promise as a tool for representing and sampling classical and quantum states (wavefunctions).  Below, I've outlined some of the promise inherent in RBMs for the field of condensed matter and quantum many-body physics.

## Representation of wavefunctions, and the inverse problem

## Ancillary support for Monte Carlo simulations

([Andy Rubin][4] among them) 
[4]: http://www.theverge.com/2016/6/14/11939310/andy-rubin-google-android-playground-ai-robotics "Andy Rubin AI Robotics"
