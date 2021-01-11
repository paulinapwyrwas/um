import pandas as pd
import numpy as np


df = pd.read_csv("task.csv", delimiter=';', header=None)
print(df.head)
data = np.random.randint(0,5,size=len(df))
df[[3]] = data
print(df.head)
df.to_csv("submission.csv", sep=';', index=False)