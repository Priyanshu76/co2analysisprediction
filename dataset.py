#Importing all Modules Required
import pandas
import numpy as np
import pickle

#Reading dataframe using pandas module
df = pandas.read_csv("cars (2).csv")
X = df[['Weight','Volume']]
y = df['CO2']

#Creating arrays for plotting purpose
a = np.array(df['Weight'])
b = np.array(df['CO2'])
c = np.array(df['Volume'])

#Zipping weight-co2 array and volume-co2 array
res1 = list(zip(a,b))
res2 = list(zip(c,b))

#Dumping both the zipped lists
pickle.dump(res1, open('array1.pkl','wb'))
pickle.dump(res2, open('array2.pkl','wb'))