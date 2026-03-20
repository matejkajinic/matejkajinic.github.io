---
layout: article
title: 'Predict Breast Cancer'
description: 'Demonstration project for breast cancer prediction.'
github_repo: 'matejkajinic/predict-breast-cancer'
github_url: 'https://github.com/matejkajinic/predict-breast-cancer'
source_path: 'breast_cancer_notebook.ipynb'
last_commit_sha: '4e9c9ea770c2430a6d6d7f772de288c70eef4201'
last_commit_date: '2019-04-09T12:00:00Z'
---

<!-- Generated at 2026-03-20T22:08:20Z by scripts/sync_writing.py -->

# Predict Breast Cancer with Tensorflow

<a href="https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)">Data from Wisconsin</a>.

Train and test data (X), results Y = 0 is benign and Y = 1 is malignant tumor.

```python
import pandas as pd

from google.colab import files
file = files.upload()
X_train = pd.read_csv("xtrain.csv", header=None)
Y_train = pd.read_csv("ytrain.csv", header=None)
X_test = pd.read_csv("xtest.csv", header=None)
Y_test = pd.read_csv("ytest.csv", header=None)
```

30 -> 16 -> 8 -> 6 -> 1

```python
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units = 16, activation = 'relu', input_dim = 30))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
```

```python
classifier.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy')
```

```python
classifier.fit(X_train, Y_train, batch_size = 1, epochs = 100)
```

```python
Y_pred = classifier.predict(X_test)
Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred ]
```

```python
total = 0
correct = 0
wrong = 0
for i in range(len(Y_pred)):
  total=total+1
  if(Y_test.at[i,0] == Y_pred[i]):
    correct=correct+1
  else:
    wrong=wrong+1

print("Total " + str(total))
print("Correct " + str(correct))
print("Wrong " + str(wrong))
print ((correct)/(total)*100)
```

<a href="https://www.kaggle.com/arturogro/predict-breast-cancer-with-tensorflow">Kaggle - Predict Breast Cancer with Tensorflow</a>

