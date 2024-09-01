import sys
sys.path.append("/Users/lucasvilsen/Desktop")
from MLPapers.Autoencoder.autoencoders import AutoEncoder, AutoEncoderLoss
import tiktoken
import numpy as np
from tinygrad import Tensor
from tinygrad.nn import optim
import matplotlib.pyplot as plt
from tqdm import tqdm

# Get some text 
text = None
encoding = tiktoken.get_encoding("gpt2")
encoded_text = encoding.encode(text)
# run through autoencoder
# Now see the compression in text
autoencoder_result = None
original_text = encoding.decode(autoencoder_result)

# Construct X_train, X_test from encoded_text

nsteps = 50000
batch_size = 32

steps = []
losses = []
evals = []

autoencoder = AutoEncoder([784, 128, 10])
opt = optim.SGD([layer.weight for layer in autoencoder.encoder.layers] + [layer.weight for layer in autoencoder.decoder.layers], lr=1e-4)

def sparse_categorical_crossentropy(x, y):
    z = ((x - y)**2).sum(axis=1).sum(axis=0)
    return z

def eval(autoencoder, X_test):
    losses = []
    for _ in range(20):
        samp = np.random.randint(0, X_train.shape[0], size=(batch_size))
        batch = Tensor(X_train[samp], requires_grad=False)
        labels = Tensor(X_train[samp])

        out = autoencoder(batch)
        losses.append(sparse_categorical_crossentropy(out, labels))
    return (sum(losses) / len(losses)).numpy()

with Tensor.train():
  for step in tqdm(range(nsteps)):
    # random sample a batch
    samp = np.random.randint(0, X_train.shape[0], size=(batch_size))
    batch = Tensor(X_train[samp], requires_grad=False)
    labels = Tensor(X_train[samp])

    out = autoencoder(batch)
    loss = sparse_categorical_crossentropy(out, labels)

    opt.zero_grad()
    loss.backward()
    opt.step()

    if step % 100 == 0:
      steps.append(step)
      losses.append(loss.numpy())
      evals.append(eval(autoencoder, X_test))

print("Equivalent number of epochs trained for: ", nsteps * batch_size / X_train.shape[0])

plt.semilogy(steps, losses, label="train loss")
plt.semilogy(steps, evals, label="eval loss")
plt.legend()

# Now test autoencoder
# Save autoencoder object