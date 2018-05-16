Title: The Theory of Deep Learning
Date: 2018-05-16
Author: Anna Go
Slug: DL-theory


"Why do modern deep neural networks (DNNs) perform so well on 
previously unseen test data, even when their number of weights 
is much larger than the number of data points in the training set?"

This question keeps puzzling many theorists and practicioners doing 
Deep Learning (DL), in particular those who are used to the rules of 
classical statistical modeling.


For example, consider the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), 
which became a benchmark for state-of-the-art DNNs. ImageNet is a database of labeled 
high-resolution images, designed for the purpose of testing visual object recognition 
software. In the annual ILSVR challenge, ever new and sophisticated DL models compete 
in classifying a dataset of 1.2 million images from 1000 categories. Among the leaders 
on the winners list we find GoogLeNet, AlexNet and VGGNet, with 4, 60 or 138 millions 
parameters, respectively.

This degree of overparametrization is insane from the point of view 
of classical learning theory, which teaches us parsimony in model size 
selection. A larger number of parameters increases the model's flexibility, 
allowing it to express more complex functions. However, a more flexible 
model will adjust to many details of the training set which are not the 
general features of the data. As a result, its performance on a previously 
unseen test data will be poorer (cf. figure X). To sum up, the larger the 
number of parameters in a model, the more prone it is to overfitting.

This is known as the *bias-variance tradeoff*, a central concept of 
statistical learning theory. In this context, the variance refers to 
the amount by which the fit function changes if estimated on a different 
training set, and the bias measures how much the chosen ansatz for the 
fit function is off from reality. Generally, when the model flexibitliy 
is increased, the variance will increase and the bias will decrease. 
Consider the plots presented in figure Y below: Y.a shows three models 
of different flexibility fitting the given data (open circles), which was 
sampled from the true target function (black curve) with noise. Y.b shows 
how these models perform on the training (grey) and test (red) dataset by 
plotting the prediction error as a function of model flexibility. The 
linear model (orange) does a rather poor job. Among all, it has the largest 
bias and the lowest variance - that is, the linear shape is too simple to 
capture the curved nature of the target, but it is therefore stable towards 
variations in the training sample. The most flexible model (green) on the 
other hand is too wiggly and fits the irregularities of the sampled data - 
it has a large variance. The model of intermediate flexibility (blue) 
performs best: it follows the shape of the target function, ignoring the 
noise in the sample.
To a large extent, the art of making a fit that generalizes well lies in 
selecting a model that is sufficiently complex to capture the reality, 
but still rigid enough to ignore the noise.

Notice that with increasing model flexibility the training error monotonically 
decreases (cf. figure Y.b). The test error, however, exhibits a local minimum 
at a certain flexibility, and grows rapidly as the flexibility increases further. 
The discrepancy between the training and the test error is called the *generalization 
gap* (GG) and is used as a measure for the generalization ability of a model.


# HASTIE-TIBSHIRANI BIAS-VARIANCE TRADEOFF -- 2 figures, 3 subplots
<figure>
    <img
    style="float: center; width: 90%; margin-right: 1%; margin-bottom: 0.0em;"
    src="/Users/annagolubeva/Desktop/physicsml.github.io/develop/content/images/bias_variance.png"
    />
    <img
    style="float: center; width: 90%; margin-right: 1%; margin-bottom: 0.0em;"
    src="/Users/annagolubeva/Desktop/physicsml.github.io/develop/content/images/bias_variance_2.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 1.</b> Illustration of the bias-variance tradeoff. 
    Left: Open circles is data simulated from the function $f$ shown 
    in black. Orange, blue and green curves are three estimates of $f$ 
    with increasing model complexity (flexibility).
    Right: Training (grey) and test (red) errors, relative to the 
    minimum possible test error over all methods (dashed line). 
    Squares represent the values for the three fits shown on the left.
    Second figure: Model complexity vs error. Maybe it should be first!
    Figure from Hastie, Tibshirani (Introduction to Statistical Learning).
    </figcaption>
</figure>
<br/>

In statistical learning theory, models are typically characterized through a bound 
on GG, which is derived based on some notion of model complexity. The latter is not 
uniquely defined, and there is a number of different suggestions, but typically it 
is proportional to the number of free parameters in the model. A classical result 
states that GG scales, in leading order, as

$$
GG \propto \sqrt{ \frac{d}{m} },
$$

where $d$ is a measure for the model complexity (~ number of free parameters), 
and $m$ is the number of examples in the training set. Thus, to put it simply, 
the model is not expected to generalize well as long as the number of parameters 
exceeds the size of the training dataset. The use of highly overparameterized 
models in DL seems to directly contradict this rule - and yet DNNs generalize 
very well in practice.


In lack of a hard definition of model complexity for DNNs, the fact that they 
are overparametrized and thus unnecessarily complex for the actual task remains 
a somewhat diffuse piece of common knowledge. Recently, Zhang et al. (2017) 
brought this topic into focus of attention by making a concrete statement about 
the DDNs complexity in terms of their capacity:

"Modern DNNs have enough capacity to fit random noise."

They demonstrate this in a series of simple and systematic experiments on 
state-of-the art DNNs for the image classification task using the ImageNet 
and CIFAR10 benchmarks. Essentially, they show that a DNN that exhibits good 
generalization ability on the original dataset will still achieve a zero 
training error when the original labels in the dataset are replaced by random 
labels, while the test error will be, of course, at the level of guessing. 
This result implies that the DNN has sufficient capacity to fit training 
data that does not exhibit any learnable structure. To take it a step further, 
they replace the true images in the original dataset by completely random 
pixels, and train again. The result: Convolutional networks still achieve zero 
training error. Adding explicit regularization (several standard techniques 
were tested) does not substantially affect the results stated above. 

The key insight provided by these experiments is that the GG of a model can 
be substantially increased by randomizing the labels alone, without changing 
the model, its size, the hyperparameters or the optimizer. This fact challenges 
the conventional view of statistical learning theory, where the bounds on the 
GG are established based on some model features, while the dataset is fully 
disregarded. This is essentially the reason why standard notions of model 
complexity, such as, for example, the Rademacher complexity and VC dimension, 
are not useful in the DL setting. Looking deeper into classical learning theory, 
one finds that, in fact, many fundamental concepts are not applicable to DL, 
and thus building a theory of DL requires a new approach.























main: SGD has a diffusion phase. this performs compression of the input. compression is how generalization works. however, there are counterexamples. the debate is not over yet.




There is work done in this direction in different fields: CS, neuroscience, maths, and recently also physics. Essentially, there are three ways approaches:
- exploring the algorithm, in particular SGD
- class of functions that can be approximated well by DNNs
- experimental approach to determine the benefit of depth



to get an insight into the inner works of the ``intelligent’’ black boxes, but thus far there is not much on the market.



One of the notable efforts in this direction is pushed forward by Prof. Naftali Tishby and collaborators, who approach DL by combining methods from statistical learning theory, information theory and statistical physics. So what’s the key to generalization? Their answer: compression.

More specifically, Tishby argues that the learning process has two distinct phases. In the first phase, the weights are adjusted to simply fit the training data. In the second phase the magic happens: DNN gradually discards details that are not relevant for output prediction, which is the essential process for generalization. In this sense, each hidden layer is a compressed representation of the input, and the deeper the layer, the coarser the representation. What allows the DNN to discard the superfluous and keep the relevant information is the stochasticity in the Stochastic Gradient Descent algorithm.

When trained for a classification, something tells the DNN what is a specific detail and what is a universal feature, relevant for all objects in the same category.

The question what netwroks learn and what allows them to pick out relevant information from the entire swamp of information they are given throughout training, remains a secret. is a goal of explainable AI. unresolved mystery. more scientist are attempting to answer. would make life with DNN so much easier and give a boost to the development and extremely widen the field of applications.



``What I can not create, I do not understand.’’
Situation with DL shows us that creating is a notwendig, but not hinreichend for understanding.
Ironically, in case of DL we encounter the situation that we can create, but we do not understand.
We can create, plenty, and with modern software packages a 5-year old can create a functioning DNN. Understanding what exactly is happening in the network, is a current very hot topic of current research and target of joint and individual efforts from researchers in industry and academia, in essentially all disciplines. I prefer to take the optimistic side and view Feynman’s quote as a premise. After all, we’ve created it — so we are be able to understand. It does, however, require some serious effort.


One of the notable efforts in this direction is pushed forward by Prof. Naftali Tishby. He approaches this question from the point of view of information theory and statistical physics and signal processing and godknowswhatelse. So what is the sercret to generalization? His answer: compression. 
More specifically, the DNN compress the input by discarding all information that is not useful for output prediction. This process happens gradually from layer to layer. Each layer is a compressed / imperfect representation of the input, and the deeper the layer, the coarser the representation. What allows the DNN to perform this smart selection of relevant information is essentially the stochasticity in the Stochastic Gradient Descent algorithm.

In handwaving: Initially, the network will capture all possible details of the input. That’s fitting of the training data. As long as the training error is large, this process is quite directed and straightforward. Once the training error reaches a small value, diffusion starts. The gross features have now been learned; what follows is the sharpening of the hypothesis. The data is fed in in minibatches.

Also, on an intuitive level it is relatable to our human experience of learning. Think of a situation when you try to understand some concept, but you can’t find a clear definition of it. Then you look at various examples and try to sort out what is . You start with some assumption about the definition of the concept from the first example you have, and then you sharpen your definition by looking at more examples and removing details that turn out to be specific. If your examples are diverse enough, this technique allows you to deduce an accurate definition of the concept.
This is exactly how I imagine the SGD process.
You keep what they have in common, and discard details that turn out to be non-universal.


In his recent work with Ravid Schwartz-Ziv they present some numerical results that stützen this hypothesis.

Moreover, they find the DNNs reach the theoretical optimum, which is defined through the IB framework.

They apply several novel analysis techniques, that help to visualize and analyze the behavior of DNN and track the learning process.

The Information Bottleneck framework applied to DL.

To me, the most intriguing part of their work is the description of the second phase of SGD as a diffusion process, in particular the implications this view has for the advantage of network depth. Stay tuned — we will elaborate on this in an upcoming post.





Why depth matters





Their work is remarkable for three reasons:

First, they go back to the roots, and suggest how to adjust classical learning theory to the case of DL. They cast the DL problem in the language of information theory. This might set a fundament for further explorations and the development of a solid theory of DL.

They apply the IB framework to quantify their hypotheses. The IB framework is an established method in information theory. This provides new analysis methods, and introduce the MI as observable that allows to track the training process. The caveat, however, is that this approach is not easy to scale to real-world problems and has limitations regarding certain types of datasets. But there are already some extensions and generalizations (paper 2017 google guy).

Third, they use concepts from statistical physics to describe the behaviour of the compresison phase of SGD - and this, of course, grabbed my attention. The exciting part is that this description has interesting implications about why the depth of the network matters. This is worth exploring, both from 





This is how you would figure out a certain concept without having a definition, but only examples. You would 
To understand how they obtained these results, we need to adapt an information-theoretic perspective on DL…

























heiß debated (openreview link).

One of the main criticized point is the calculation of the mutual information. The difficulty that is posed here is essentially the need to estimate the probability distribution from a finite sample.
There are a number of methods to estimate MI, the simplest one relying on a calculation via Shannon entropy. The layer output is binned for this purpose. The binning procedure, i.e. the choice of bin number and size, is a nontrivial question and depends  on the range of t, which is determined by the activation function of the layer units. In case of tanh, the output is bounded, and uniform binning can be chosen, but in case of ReLU, the question of appropriate binning does not have an answer everybody agrees on. 



However, the final word has not yet been spoken, and the idea keeps evolving. 







































