

import pandas as pd
import numpy
directory = 'MSc_Project/Data/part_data/coop/Part1/Part1_Task2_otpitrack.csv'
df = pd.read_csv(directory)

n = 0 
row_count = sum(1 for row in df)
y = df.iloc[:,[8]].values

for i in range(row_count):
    if y(i+1) - y(i) != 0:
        n = n +1
        print(n)


import pandas as pd
import numpy as np
df = pd.read_csv("MSc_Project/Data/part_data/coop/Part1/P1_T2_Sample_ur3e.csv")
from sklearn import preprocessing
x_array = np.array(df['time'])
a = preprocessing.normalize([x_array])
np.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/coop/Part1/P1T2_S1_otpitrack.csv", a, delimiter=",")
print(a)
