Title: The Unreasonable Effectiveness of Restricted Boltzmann Machines
Date: 2016-09-10 20:00
Category: Articles
Tags: quantum mechanics, machine learning, Boltzmann Machines
Authors: Roger Melko
Summary: The unsupervised learning tool, ambiguous in modern deep learning, has some important lessons for quantum physicists


When I first encountered a Boltzmann Machine, I did not immediately see its appeal to a condensed matter physicist.  Why would we need a learning tool to approximate distributions, when, presumably, in order to obtain data to train the machine, we must already ''know'' the distribution (or, at least, the Hamiltonian)?  I knew as a Monte Carlo practitioner, we are already in the business of sampling from perfect distributions -- a practice fraught with many difficulties as it is.  Why would we add further systematic error (on top of our statistical error) from an imperfectly-learned distribution?  The application of such a machine in the technology industry is more obvious.  There, we are trying to train a machine on say a finite-size number of pictures of cats that is itself capable of generating (or dreaming) a picture of a ``cat''.  For me, each picture of a cat is instead (say) a spin configuration, each pixel and up or down spin state, sampled from (say) the Boltzmann distribution at finite temperature.  This sampling is done with a Markov Chain Monte Carlo procedure, an efficient algorithm honed by scientists since the end of Word-War 2.  It seems, we already have the distribution, and we already know how to sample it very efficiently.  Why would we use these samples to train an imperfect machine, the sampling of which may be less efficient than our existing algorithms, honed for the past 65 years?

([Andy Rubin][4] among them) 
[4]: http://www.theverge.com/2016/6/14/11939310/andy-rubin-google-android-playground-ai-robotics "Andy Rubin AI Robotics"
