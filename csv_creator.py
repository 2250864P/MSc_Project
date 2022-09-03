import csv
import pandas as pd 
import numpy as np

f1=pd.read_csv("data\part1_sample_positions.csv")
f2=pd.read_csv("data\Part1_Task2_ur3e_test.csv")
f1=f1.iloc[:,:].values
f2=f2.iloc[:,:].values
sample=[]
for i in range (5):

    onesample=f2[f1[i,0]:f1[i,1],0:1]
    sample.append(onesample)

print(sample)