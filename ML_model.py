#Importing all Modules Required
import pandas
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pickle

#Reading Dataframe using pandas Module
df = pandas.read_csv("cars (2).csv")
X = df[['Weight','Volume']]
y = df['CO2']

#Creating arrays of Weight, Volume and CO2 for Plotting Purpose
a = np.array(df['Weight'])
b = np.array(df['CO2'])
c = np.array(df['Volume'])

#Using Linear regression module
regr = linear_model.LinearRegression()
regr.fit(X, y)

#Training and Testing our dataset
train_x = a[:80]
train_y = b[:80]
train_z = c[:80]

test_x = a[80:]
test_y = b[80:]
test_z = c[80:]

#To find R2 Score of our dataset
mymodel1 = np.poly1d(np.polyfit(train_x, train_y, 1))
mymodel2 = np.poly1d(np.polyfit(train_z, train_y, 1))
#r1= R2 score when Weight and CO2 are considered
#r2= R2 score when Volume and CO2 are considered
r1 = r2_score(train_y, mymodel1(train_x))
r2 = r2_score(train_y, mymodel2(train_z))
print(r1,r2)

#To find slope and intercept for both parameters for plotting purpose
fit1 = np.polyfit(train_x,train_y,1)
ang_coeff1 = fit1[0]
intercept1 = fit1[1]
fit_eq1 = ang_coeff1*train_x + intercept1
fit2 = np.polyfit(train_z,train_y,1)
ang_coeff2 = fit2[0]
intercept2 = fit2[1]
fit_eq2 = ang_coeff2*train_z + intercept2

#Plotting y=mx+c and Data points
fig = plt.figure()
ax = fig.subplots()
ax.plot(train_x, fit_eq1,color = 'r', alpha = 0.9, label = 'Linear fit(Weight)')
ax.plot(train_z, fit_eq2,color = 'g', alpha = 0.9, label = 'Linear fit(Volume)')
ax.scatter(a,b,s = 10, color = 'b', label = 'Data(Weight)')
ax.scatter(c,b,s = 10, color = 'y', label = 'Data(Volume)')
ax.set_title('Weight,Volume Vs CO2')
ax.legend()
plt.xlabel('Weight and Volume')
plt.ylabel('CO2 Emission')
plt.show()

#Dumping our code using Pickle module to 'model.pkl'
pickle.dump(regr, open('model.pkl','wb'))