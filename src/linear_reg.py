from src.projet_python import CsvDataframe
from src.support.constants import *
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

Data = CsvDataframe(nrows=10000)
df = Data.df
X = np.array(df[Distance]).reshape(-1,1)
Y = df[Fare_amount]

LR = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, Y)
LR.fit(X_train, y_train)
LR.predict(X_test)

score = r2_score(y_test,LR.predict(X_test))
print(score) #0.747302



# #Croisement avec le jour de la semaine
# df['week_day'].value_counts().plot.pie() #Répartition apparemment équitable
# for k in df['week_day'].unique():
#     print(k)
#     print(df['fare_amount'][df['week_day']==k].describe())
