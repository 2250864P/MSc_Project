import csv
import pandas as pd
import numpy
directory = 'MSc_Project/Data/robot_data/Part10_Task3_ur3e.csv'
df = pd.read_csv(directory)
#df=df.iloc[:,:].values
print(df.shape)



c=df[~( df['z'].isin([0])|df['y'].isin([0])|df['x'].isin([0]))]  
print(c.shape)

numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/robot_data/non_coop/Part10/P10_T3_ur3e.csv", c, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(c)