## MNIST Synthetic Data
Here I have experimented with two different approaches to creating synthetic data from scratch.
* simple_NN: A simple neural network with batch_norm, dropout, 3 hidden layers and relu activation.
* Probability_model: A simple probability model that makes a new picture from a label. The overall shape of the label can be seen, but the picture is of very bad quality.
* GAN: A simple generator and discriminator architecture as proposed in Goodfellow et al. (2014). This GAN does not used convolutional layers, which could increase the performance. Maybe I will make another model with conv layers later :-).

### GAN:
##### After 0 epochs
![Examples of pictures created with GAN](images/GAN_epoch_0_sample.png)
##### After 1 epochs
![Examples of pictures created with GAN](images/GAN_epoch_1_sample.png)
##### After 10 epochs
![Examples of pictures created with GAN](images/GAN_epoch_10_sample.png)
##### After 50 epochs
![Examples of pictures created with GAN](images/GAN_epoch_50_sample.png)
##### Loss over time
![GAN loss over time](images/GAN_loss.png)

### Simple NN:
![Examples of pictures created with simple NN](images/simple_nn_sample.png)
### Probability model:
![Examples of pictures created with probability model](images/probability_model_sample.png)
