import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t_coop = []
t_noncoop = []
coop_n = []
noncoop_n = []
g_coop = []
g_noncoop = []
v_coop = []
v_noncoop = []
a_coop = []
a_noncoop = []
j_coop = []
j_noncoop = []


for j in range(10):

    vel1 = [[], []]
    acc1 = [[], []]
    jerk1 = [[], []]
    vel2 = [[], []]
    acc2 = [[], []]
    jerk2 = [[], []]
    fileheader = 'MSc_Project/Data/part_data/'
    # _coop = input('Coop(1) or non-Coop(0)?')
    # _coop = int(_coop)
    filename = ''
    # part_number = input('Which participant?(1-10)')
    part_number = j + 1
    filename1 = fileheader + 'coop/' + 'Part' + str(part_number) + '/Part' + str(part_number) + '_Task2_otpitrack.csv'
    filename2 = fileheader + 'non-coop/' + 'Part' + str(part_number) + '/Part' + str(part_number) + '_Task3_otpitrack.csv'

    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)
    gripper_times1 = 0 
    gripper_times2 = 0

    time1 = df1.iloc[:,[0]].values
    time2 = df2.iloc[:,[0]].values
    x1 = df1.iloc[:,[1]].values
    x2 = df2.iloc[:,[1]].values
    y1 = df1.iloc[:,[2]].values
    y2 = df2.iloc[:,[2]].values
    z1 = df1.iloc[:,[3]].values
    z2 = df2.iloc[:,[3]].values
    gripper1 = df1.iloc[:,[8]].values
    gripper2 = df2.iloc[:,[8]].values

    for i in range(len(x1)):
        if i >= 1:
            temp_time1 = (time1[i] + time1[i-1])/2
            vel1[0].append(temp_time1)
            distance1 = np.sqrt((x1[i]-x1[i-1])**2 + (y1[i]-y1[i-1])**2 + (z1[i]-z1[i-1])**2)
            time_used1 = (time1[i] - time1[i-1])/2
            velocity = distance1 / time_used1
            vel1[1].append(velocity)

    for i in range(len(x2)):
        if i >= 1:
            
            temp_time2 = (time2[i] + time2[i-1])/2
            vel2[0].append(temp_time2)
            distance2 = np.sqrt((x2[i]-x2[i-1])**2 + (y2[i]-y2[i-1])**2 + (z2[i]-z2[i-1])**2)
            time_used2 = (time2[i] - time2[i-1])/2
            velocity2 = distance2 / time_used2
            vel2[1].append(velocity2)

    for i in range(len(gripper1)):
        if gripper1[i] - gripper1[i-1] != 0:
            gripper_times1 += 1
    gripper_times1 /= 2
    coop_n.append(gripper_times1)

    for i in range(len(gripper2)):
        if gripper2[i] - gripper2[i-1] != 0:
            gripper_times2 += 1
    gripper_times2 /= 2
    g_coop.append(gripper1)
    g_noncoop.append(gripper2)
    t_coop.append(time1)
    t_noncoop.append(time2)
    noncoop_n.append(gripper_times2)
    v_coop.append(vel1)
    v_noncoop.append(vel2)
    

p = 5
plt.plot(v_coop[p][0], v_coop[p][1])
plt.plot(t_coop[p], g_coop[p])
plt.show()

plt.plot(v_noncoop[p][0], v_noncoop[p][1])
plt.plot(t_noncoop[p], g_noncoop[p])
plt.show()