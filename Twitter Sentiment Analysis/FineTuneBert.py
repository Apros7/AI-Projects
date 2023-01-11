from sklearn.model_selection import train_test_split
from transformers import Trainer, TrainingArguments
import torch
from datasets import load_metric
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import numpy as np
import seaborn as sns

import pandas as pd
from transformers import BertForSequenceClassification, BertTokenizer
data = pd.read_csv("dataset.csv")
data = data[:100]
data = data.rename(columns={"target": "label"})
data["label"] = data["label"].replace(4,1)
max_len = max([len(sent) for sent in data.text])
print('Max length: ', max_len)

new_data = data[["label", "text"]].reset_index()
print(new_data.head())
x_train, x_test, y_train, y_test = train_test_split(list(new_data["text"]), list(new_data["label"]), test_size=0.2)

tokenizer = BertTokenizer.from_pretrained("distilbert-base-uncased")

x_train_tokenized = tokenizer(x_train, padding=True, truncation=True, max_length=190)
x_test_tokenized = tokenizer(x_train, padding=True, truncation=True, max_length=190)
print(len(x_test))
print(len(y_test))

batch_size = 16
epochs = 2

class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels=None):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        if self.labels:
            item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.encodings["input_ids"])

train_dataset = Dataset(x_train_tokenized, y_train)
test_dataset = Dataset(x_test_tokenized, y_test)

args = TrainingArguments(
    output_dir="output",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=2,
    weight_decay = 0.01
)

model = BertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

def compute_metrics(p):
    pred, labels = p
    pred = np.argmax(pred, axis=1)

    accuracy = accuracy_score(y_true=labels, y_pred=pred)
    recall = recall_score(y_true=labels, y_pred=pred)
    precision = precision_score(y_true=labels, y_pred=pred)
    f1 = f1_score(y_true=labels, y_pred=pred)

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
    tokenizer=tokenizer)

trainer.train()

torch.save(model, './model')