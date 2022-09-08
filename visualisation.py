import pandas as pd 
import matplotlib.pyplot as plt

my_csv = pd.read_csv("Data/part_data/non-coop/Part10/Part10_Task3_otpitrack.csv", usecols=['x', 'y', 'z'])

column_x = my_csv["x"]
column_y = my_csv["y"]
column_z = my_csv["z"]

fig = plt.figure()

k=13362
l=18980
ax3 = plt.axes(projection='3d')
ax3.plot3D(column_z.loc[k:l], column_x.loc[k:l], column_y.loc[k:l], 'blue')

