Title: The Theory of Deep Learning - Part I
Date: 2018-05-16
Tags: machine learning, deep learning, theory of deep learning
Author: Anna Go
Slug: DL-theory


 > Why do modern deep neural networks (DNNs) perform so well on 
    previously unseen test data, even when their number of weights 
    is much larger than the number of data points in the training set?

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
unseen test data will be poorer (cf. figure 1). To sum up, the larger the 
number of parameters in a model, the more prone it is to overfitting.

This is known as the **bias-variance tradeoff**, a central concept of 
statistical learning theory. In this context, the variance refers to 
the amount by which the fit function changes if estimated on a different 
training set, and the bias measures how much the chosen ansatz for the 
fit function is off from reality. Generally, when the model flexibitliy 
is increased, the variance will increase and the bias will decrease (cf. 
figure 1a). 
Consider the plots presented in figure 1 below: 1.b shows three models 
of different flexibility fitting the given data (open circles), which was 
sampled from the true target function (black curve) with noise. 1.c shows 
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
decreases (cf. figure 1a). The test error, however, exhibits a local minimum 
at a certain flexibility, and grows rapidly as the flexibility increases further. 
The discrepancy between the training and the test error is called the **generalization 
gap** (GG) and is used as a measure for the generalization ability of a model.


<figure>
    <img
    style="float: center; width: 100%; margin-right: 0%;"
    src="/images/bias_variance.png"
    />
    <p style="clear: both;">
    <figcaption>
    <b>Figure 1.</b> Illustration of the bias-variance tradeoff. 
    <b>(a):</b> Prediction error on the training (blue) or test (red) sample,
    as a function of model complexity. 
    <b>(b):</b> Example of different fits: Open circles is data simulated 
    from the true target function shown in black. Orange, blue and green 
    curves are three estimates of the target, with increasing model complexity 
    (flexibility).
    <b>(c)</b> Training (grey) and test (red) errors, relative 
    to the minimum possible test error over all methods (dashed line). 
    Squares represent the values for the three fits shown on the left. 
    Figures from: <a href="https://web.stanford.edu/~hastie/ElemStatLearn/">Hastie, Tibshirani, Friedman - The Elements of Statistical Learning</a>
    </figcaption>
</figure>
<br/>


In statistical learning theory, models are typically characterized through a **bound 
on GG**, which is derived based on some notion of model complexity. The latter is not 
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
a somewhat diffuse piece of common knowledge. Recently, [Zhang et al. (2017)](https://arxiv.org/abs/1611.03530) 
brought this topic into focus of attention by making a concrete statement about 
the DDNs' complexity in terms of their capacity:

  > Modern DNNs have enough capacity to fit random noise.

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
the conventional view of statistical learning theory, which establishes bounds 
on the GG based on some model features, while fully disregarding the dataset. 
This is essentially the reason why standard notions of model complexity, such 
as, for example, the [Rademacher complexity](https://en.wikipedia.org/wiki/Rademacher_complexity) 
and the [VC dimension](https://epubs.siam.org/doi/10.1137/1116025), are not useful in 
the DL setting. Looking deeper into classical learning theory, one finds that, 
in fact, many fundamental concepts are not applicable to DNNs, and thus building 
a theory of DL requires rethinking some of the established frameworks.

Is there a way to tackle the puzzle posed by DL outside the paradigm of classical 
statistical learning theory, or can the classical frameworks be reconciled with 
the modern learning machines? - Stay tuned for part II in this series!

