import pandas as pd
data={
  "name":["sai","sree","meg"],
  "marks":[100,200,300]
}
dt=pd.DataFrame(data)
dt['marks'].fillna(dt['marks'].mean(),inplace=True)
print(dt)



                              ***************



import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 2, 3])

mean = np.mean(X, axis=0)
print("Mean of features:", mean)
