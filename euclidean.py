import pandas as pd
import numpy

directory = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_1_otpitrack.csv'
directory1 = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_2_otpitrack.csv'
directory2 = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_3_otpitrack.csv'
directory3 = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_4_otpitrack.csv'
directory4 = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_5_otpitrack.csv'
#directory5 = 'MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_6_otpitrack.csv'

df = pd.read_csv(directory)
df1 = pd.read_csv(directory1)
df2 = pd.read_csv(directory2)
df3 = pd.read_csv(directory3)
df4 = pd.read_csv(directory4)
#df5 = pd.read_csv(directory5)



a = df.iloc[:,[1,2,3]].values
b = df1.iloc[:,[1,2,3]].values
c = df2.iloc[:,[1,2,3]].values
d = df3.iloc[:,[1,2,3]].values
e = df4.iloc[:,[1,2,3]].values
#f = df5.iloc[:,[1,2,3]].values

dist = numpy.linalg.norm(a)
print(dist)
dist = numpy.linalg.norm(b)
print(dist)
dist = numpy.linalg.norm(c)
print(dist)
dist = numpy.linalg.norm(d)
print(dist)
dist = numpy.linalg.norm(e)
print(dist)
#dist = numpy.linalg.norm(f)
#print(dist)