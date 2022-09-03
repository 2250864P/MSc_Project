import csv
import pandas as pd
import numpy
directory = 'MSc_Project\Data\part_data\coop\Part1\Part1_Task2_otpitrack.csv'
df = pd.read_csv(directory)
#df=df.iloc[:,:].values
print(df.shape)

k= 9471
l= 11313

c= df.loc[k:l]  
print(c.shape)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/coop/Part1/P1_T2_Sample_6_ur3e.csv", c, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(c)