
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

data = pd.read_csv('bank_train(1).csv')

data_cp = data.copy(deep=True)

print(data.info())

print(data['age'].corr(data['balance']))


