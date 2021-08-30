#Importing all Modules required
import pandas
import numpy as np
import pickle

#Reading Dataframe using pandas module
df2 = pandas.read_csv("CO2 list.csv")

#Creating array of CO2 in float type
b2 = np.array(df2['CO2'].astype(float))

#Creating arrays for plotting purpose
audi=np.nanmean(b2[:36])
bmw=np.nanmean(b2[36:91])
ford=np.nanmean(b2[91:128])
honda=np.nanmean(b2[128:147])
mercedes=np.nanmean(b2[147:215])
toyota=np.nanmean(b2[215:])
array=[audi,bmw,ford,honda,mercedes,toyota]

#Dumping our array using pickle module to 'co2_compare.pkl'
pickle.dump(array,open('co2_compare.pkl','wb'))