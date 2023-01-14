## Impersonator
Impersonator is a series of machine-learning algorithms to continue on a list of strings and impersonate the same style.
This is based on Andrej Karpathy's make more. The test example is to continue to make artificial names from names.txt (32K names).

It currently includes the following models:
- Bigram

### Training loss
The goal with training loss is to get a value to determine model performance. 
Goal: Maximize likelihood of the data w.r.t. model parameters (statistical modeling).
Equivalent to maximizing the log likelihood (log is monotonic)
Equivalent to minimizing the negative log likelihood
Equivalent to minimizing the average negative log likelihood


#### Bigram

The first 10 names from the Bigram is:

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
