import pandas as pd 
import matplotlib.pyplot as plt

my_csv = pd.read_csv("data/Part9_Task3_ur3e.csv", usecols=['x', 'y', 'z'])

column_x = my_csv["x"]
column_y = my_csv["y"]
column_z = my_csv["z"]

fig = plt.figure()

k= 2
l= 500
ax3 = plt.axes(projection='3d')
ax3.plot3D(column_z.loc[k:l], column_x.loc[k:l], column_y.loc[k:l], 'blue')

