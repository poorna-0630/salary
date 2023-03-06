import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_excel("data.xlsx")
print(df.tail())
y=df.iloc[:,2].values
print(y)