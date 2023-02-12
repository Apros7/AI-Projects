## Impersonator
Impersonator is a series of machine-learning algorithms to continue on a list of strings and impersonate the same style.
This is based on Andrej Karpathy's make more. The test example is to continue to make artificial names from names.txt (32K names).

It currently includes the following models:
- Bigram 
- Single Layer NN 
- MLP, using the explination from [Bengio et al. 2003](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
- CNN, using the explination from [Mikolov et al. 2010](https://arxiv.org/abs/1609.03499)

### Training loss
The goal with training loss is to get a value to determine model performance: Maximize likelihood of the data w.r.t. model parameters.(statistical modeling).
- Equivalent to maximizing the log likelihood (log is monotonic)
- Equivalent to minimizing the negative log likelihood
- Equivalent to minimizing the average negative log likelihood


#### Bigram

The first 10 names from the Bigram are:

```
mor
axx
minaymoryles
kondlaisah
anchshizarie
odaren
iaddash
h
jhinatien
egushl
```

Bigram loss is:
```
2.4543561935424805
```

Hopefully other models perform better :/!

#### Single Layer NN with softmax

The first 10 names from this NN are:
```
mor
axx
minaymoryles
kondlaisah
anchthizarie
odaren
iaddash
h
jionatien
egvonn
```

Funnily enough, as the Bigram and NN is trained completely alike, the output is nearly exactly the same. The loss is (on training set):
```
2.481842279434204
```
after 300 epochs

#### Multilayer NN
The first 10 names from this NN are:
```
carpah.
amille.
khi.
mili.
tatyannah.
sae.
rahnen.
deliah.
jareen.
neziah.
```

The loss is:
```
Training: 2.0520
Validation: 2.1502
```

with the neural network having a total of 22K params and after 300000 total steps (processed batches).
