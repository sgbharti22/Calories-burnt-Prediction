import pandas as pd   #used to make a data frame which is easy for processing the data
import numpy as np  
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor
import pickle

calories=pd.read_csv("calories.csv")

exercise=pd.read_csv("exercise.csv")

dataset=pd.concat([exercise,calories["Calories"]] ,axis=1)

X=dataset.iloc[:,1:-1].values

Y=dataset.iloc[:,-1].values


ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


model=XGBRegressor()
model.fit(X_train,Y_train)


pickle.dump(model,open("modelfile.pkl","wb"))


# male -   0 1
# female -  1 0
# check=[]

# gen=input("asdf:")
# if(gen=="male"):
#   check.append(0)
#   check.append(1)
# if(gen=="female"):
#   check.append(1)
#   check.append(0)

# for i in range(6):
#   check.append(float(input()))

# print(check)

# print("Predicted value : ",model.predict([check]))

# print("type: ",float(model.predict([check])))
