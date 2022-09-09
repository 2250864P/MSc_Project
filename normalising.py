import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split

def csv_writeline(filename, filecontent):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(filecontent)

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
    if j == 2:
        pass 
    else:
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

        ### Normalising
        x1 = x1 / max(x1)
        x2 = x2 / max(x1)
        y1 = y1 / max(y1)
        y2 = y2 / max(y2)
        z1 = z1 / max(z1)
        z2 = z2 / max(z2)

        for i in range(len(x1)):
            if i >= 1:
                temp_time1 = (time1[i] + time1[i-1])/2
                vel1[0].append(temp_time1)
                distance1 = np.sqrt((x1[i]-x1[i-1])**2 + (y1[i]-y1[i-1])**2 + (z1[i]-z1[i-1])**2)
                time_used1 = (time1[i] - time1[i-1])
                velocity = distance1 / time_used1
                vel1[1].append(velocity)

        for i in range(len(x2)):
            if i >= 1:
                
                temp_time2 = (time2[i] + time2[i-1])/2
                vel2[0].append(temp_time2)
                distance2 = np.sqrt((x2[i]-x2[i-1])**2 + (y2[i]-y2[i-1])**2 + (z2[i]-z2[i-1])**2)
                time_used2 = (time2[i] - time2[i-1])
                velocity2 = distance2 / time_used2
                vel2[1].append(velocity2)

        for i in range(len(vel1[0])):
            if i > 1:
                acc_time_used1 = vel1[0][i] - vel1[0][i-1] 
                acc_temp_time1 = (vel1[0][i] + vel1[0][i-1])/2
                acc_vel_diff1 = vel1[1][i] - vel1[1][i-1]
                acc_temp1 = acc_vel_diff1/acc_time_used1
                acc1[0].append(acc_temp_time1)
                acc1[1].append(acc_temp1)
        
        for i in range(len(vel2[0])):
            if i > 1:
                acc_time_used2 = vel2[0][i] - vel2[0][i-1] 
                acc_temp_time2 = (vel2[0][i] + vel2[0][i-1])/2 
                acc_vel_diff2 = vel2[1][i] - vel2[1][i-1]
                acc_temp2 = acc_vel_diff2 / acc_time_used2
                acc2[0].append(acc_temp_time2)
                acc2[1].append(acc_temp2)

        for i in range(len(acc1[0])):
            if i > 1:
                jerk_time_used1 = acc1[0][i] - acc1[0][i-1] 
                jerk_temp_time1 = (acc1[0][i] + acc1[0][i-1])/2
                jerk_acc_diff1 = acc1[1][i] - acc1[1][i-1]
                jerk_temp1 = jerk_acc_diff1 / jerk_time_used1
                jerk1[0].append(jerk_temp_time1)
                jerk1[1].append(jerk_temp1)
        
        for i in range(len(acc2[0])):
            if i > 1:
                jerk_time_used2 = acc2[0][i] - acc2[0][i-1] 
                jerk_temp_time2 = (acc2[0][i] + acc2[0][i-1])/2
                jerk_acc_diff2 = acc2[1][i] - acc2[1][i-1]
                jerk_temp2 = jerk_acc_diff2 / jerk_time_used2
                jerk2[0].append(jerk_temp_time2)
                jerk2[1].append(jerk_temp2)

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
        noncoop_n.append(gripper_times2)
        v_coop.append(vel1)
        v_noncoop.append(vel2)
        a_coop.append(acc1)
        a_noncoop.append(acc2)
        j_coop.append(jerk1)
        j_noncoop.append(jerk2)
        t_coop.append(float(time1[len(time1)-1] - time1[0]))
        t_noncoop.append(float(time2[len(time2)-1] - time2[0]))
p = 8

### Plot

# plt.figure()
# plt.subplot(3, 1, 1)
# plt.plot(v_coop[p][0], v_coop[p][1])
# # # plt.plot(t_coop[p], g_coop[p])
# plt.subplot(3, 1, 2)
# plt.plot(a_coop[p][0], a_coop[p][1], color = 'red')
# plt.subplot(3, 1, 3)
# plt.plot(j_coop[p][0], j_coop[p][1], color = 'green')
# plt.show()


### SVM

mean_vel_coop = []
mean_vel_noncoop = []
mean_acc_coop = []
mean_acc_noncoop = []
mean_jerk_coop = []
mean_jerk_noncoop = []

for i in range(len(v_coop)):
    sum = 0
    for j in range(len(v_coop[i][1])):
        sum += float(v_coop[i][1][j])
    mean_vel_coop.append(sum/len(v_coop[i][1]))

for i in range(len(v_noncoop)):
    sum = 0
    for j in range(len(v_noncoop[i][1])):
        sum += float(v_noncoop[i][1][j])
    mean_vel_noncoop.append(sum/len(v_noncoop[i][1]))

for i in range(len(a_coop)):
    sum = 0
    for j in range(len(a_coop[i][1])):
        sum += float(a_coop[i][1][j])
    mean_acc_coop.append(sum/len(a_coop[i][1]))

for i in range(len(a_noncoop)):
    sum = 0
    for j in range(len(a_noncoop[i][1])):
        sum += float(a_noncoop[i][1][j])
    mean_acc_noncoop.append(sum/len(a_noncoop[i][1]))

for i in range(len(j_coop)):
    sum = 0
    for j in range(len(j_coop[i][1])):
        sum += float(j_coop[i][1][j])
    mean_jerk_coop.append(sum/len(j_coop[i][1]))

for i in range(len(j_noncoop)):
    sum = 0
    for j in range(len(j_noncoop[i][1])):
        sum += float(j_noncoop[i][1][j])
    mean_jerk_noncoop.append(sum/len(j_noncoop[i][1]))

# print(mean_vel_coop)
# print(mean_vel_noncoop)
# print(mean_acc_coop)
# print(mean_acc_noncoop)
# print(mean_jerk_coop)
# print(mean_jerk_noncoop)
# print(coop_n)

# for i in range(len(mean_vel_coop)):
#     content = [mean_vel_coop[i], mean_acc_coop[i], mean_jerk_coop[i], coop_n[i], t_coop[i], 1]
#     csv_writeline(filename, content)
# for i in range(len(mean_vel_noncoop)):
#     content = [mean_vel_noncoop[i], mean_acc_noncoop[i], mean_jerk_noncoop[i], noncoop_n[i], t_noncoop[i], 2]
#     csv_writeline(filename, content)

# filename = 'data_without_time.csv'
# for i in range(len(mean_vel_coop)):
#     content = [mean_vel_coop[i], mean_acc_coop[i], mean_jerk_coop[i], coop_n[i], 1]
#     csv_writeline(filename, content)
# for i in range(len(mean_vel_noncoop)):
#     content = [mean_vel_noncoop[i], mean_acc_noncoop[i], mean_jerk_noncoop[i], noncoop_n[i], 2]
#     csv_writeline(filename, content)  

# filename = 'normalised_with_time.csv'
# for i in range(len(mean_vel_coop)):
#     content = [mean_vel_coop[i], mean_acc_coop[i], mean_jerk_coop[i], coop_n[i], t_coop[i], 1]
#     csv_writeline(filename, content)
# for i in range(len(mean_vel_noncoop)):
#     content = [mean_vel_noncoop[i], mean_acc_noncoop[i], mean_jerk_noncoop[i], noncoop_n[i], t_noncoop[i], 2]
#     csv_writeline(filename, content)


# filename = 'normalised_without_time.csv'
# for i in range(len(mean_vel_coop)):
#     content = [mean_vel_coop[i], mean_acc_coop[i], mean_jerk_coop[i], coop_n[i], 1]
#     csv_writeline(filename, content)
# for i in range(len(mean_vel_noncoop)):
#     content = [mean_vel_noncoop[i], mean_acc_noncoop[i], mean_jerk_noncoop[i], noncoop_n[i], 2]
#     csv_writeline(filename, content)  

### KNN and DTW

# filename = 'velocity.csv'
# content = []
# for i in range(len(v_coop)):
#     content = []
#     for j in range(40000):
#         if j < len(v_coop[i][0]):
#             content.append(float(v_coop[i][1][j]))
#         else:
#             content.append(0)
#     content.append(1)
#     csv_writeline(filename, content)

# for i in range(len(v_noncoop)):
#     content = []
#     for j in range(40000):
#         if j < len(v_noncoop[i][0]):
#             content.append(float(v_noncoop[i][1][j]))
#         else:
#             content.append(0)
#     content.append(2)
#     csv_writeline(filename, content)

### Data splitting

df = pd.read_csv("./velocity.csv",header=None)
np.array(df)
x,y = np.split(df,indices_or_sections=(40000,),axis=1)
train_data,test_data,train_label,test_label = train_test_split(x,y, random_state=1, train_size=0.7,test_size=0.3)
np.savetxt('train_data.txt', train_data, delimiter=" ") 
np.savetxt('test_data.txt', test_data, delimiter=" ") 
np.savetxt('train_label.txt', train_label, delimiter=" ")
np.savetxt('test_label.txt', test_label, delimiter=" ")
