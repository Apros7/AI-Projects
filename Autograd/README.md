
A deep dive into backpropagation to make sure I have it all figured out.

See intro.ipynb or mnist.ipynb for usage.

Inspired by Andrej's Karpathy micrograd and George Hotz' tinygrad

Is it computationally expensive? Definitely so. Is it practical to use? Heck no. Should it ever be used in real scenarios? That's a big no. Does it even work? So far :-). 

mnist.ipynb shows that a NN can be fitted to MNIST, although with high computation time (36 training minutes) and low accuracy (67 %) with a working batch (size = 32). This is due to python being the computation backend, which is definitely not ideal. This is not impressive, but this shows that the module works as expected.

![Loss over time](lossplot.png)

![MNIST results](mnist.png)
