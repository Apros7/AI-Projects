import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("dataset.csv")
data = pd.concat([data[:10000], data.tail(10000)])
data = data.rename(columns={"target": "label"})
data["label"] = data["label"].replace(4,1)
max_len = max([len(sent) for sent in data.text])
print('Max length: ', max_len)

df = data[["label", "text"]].reset_index(drop=True)
x_train, x_test, y_train, y_test = train_test_split(list(df["text"]), list(df["label"]), test_size=0.2)
print(y_test)