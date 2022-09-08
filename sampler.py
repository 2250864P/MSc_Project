import pandas as pd
import numpy
directory = 'MSc_Project/Data/part_data/non-coop/Part10/Part10_Task3_otpitrack.csv'
df = pd.read_csv(directory)
#df=df.iloc[:,:].values
print(df.shape)


k=2
l=3182
m=3183
n=5634
o=5635
p=10846
q=10847
r=13361
s=17669
t=21252
#u=21252
#v=

a= df.loc[k:l]  
print(a.shape)
b= df.loc[m:n]
print(b.shape)
c= df.loc[o:p]
print(c.shape)
d= df.loc[q:r]
print(d.shape)
e= df.loc[s:t]
print(e.shape)
#f= df.loc[u:v]
#print(f.shape)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_1_otpitrack.csv", a, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(a)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_2_otpitrack.csv", b, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(b)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_3_otpitrack.csv", c, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(c)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_4_otpitrack.csv", d, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(d)
numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_5_otpitrack.csv", e, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
print(e)
#numpy.savetxt("C:/Users/Dougie Price/Robot_analysis/MSc_Project/Data/part_data/non-coop/Part10/P10_T3_Sample_6_otpitrack.csv", f, delimiter=",", header="time,x,y,z,qx,qy,qz,qw,gripper_stat", comments='')
#print(f)
