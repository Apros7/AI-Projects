import torch
import torch.nn as nn
import torch.optim as optim
import tensorflow as tf
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(len(x_train), len(x_test))


num_samples = 10000
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]

x_train = torch.tensor(x_train, dtype=torch.float32)
y_train = torch.LongTensor(y_train)

x_train = x_train / 255.0
x_train = x_train.reshape(num_samples, -1)

x_test_len = len(x_test)
x_test = (torch.tensor(x_test, dtype=torch.float32) / 255).reshape(len(x_test), -1)
y_test = torch.LongTensor(y_test)

class ClassifierModule(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.l1 = nn.Linear(input_size, output_size)

    def forward(self, X):
        return self.l1(X)


input_size = 784
output_size = 10
model = ClassifierModule(input_size, output_size)

learning_rate = 0.01
num_epochs = 100
batch_size = 32
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

train_dataset = TensorDataset(x_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Training loop
for epoch in tqdm(range(num_epochs)):
    total_loss = 0.0
    for i, (inputs, labels) in enumerate(train_loader):
        optimizer.zero_grad()  # Zero the gradients
        outputs = model(inputs)  # Forward pass
        loss = criterion(outputs, labels)  # Compute the loss
        loss.backward()  # Backpropagation
        optimizer.step()  # Update model parameters

        total_loss += loss.item()
    
    # print(f"Epoch [{epoch + 1}/{num_epochs}] Loss: {total_loss / len(train_loader)}")

print("Training complete.")

# Optionally, evaluate the model on the test set
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for inputs, labels in zip(x_test, y_test):
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 0)
        total += 1
        correct += (predicted == labels).item()

    accuracy = correct / total
    print(f"Test Accuracy: {100 * accuracy:.2f}%")