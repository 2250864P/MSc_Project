import pandas as pd
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



df = pd.read_csv("D:/PhD/emotional behaviors/code/svm/ecg1.csv",header=None)
np.array(df)
#2.划分数据与标签
x,y=np.split(df,indices_or_sections=(8,),axis=1) 




train_data,test_data,train_label,test_label =train_test_split(x,y, random_state=1, train_size=0.5,test_size=0.5)



#3.训练svm分类器



#classifier=svm.SVC(C=1,kernel='rbf',gamma="auto",decision_function_shape='ovo')
classifier=svm.SVC(C=1,kernel='linear',gamma=4,probability=True,decision_function_shape='ovr') # ovr:一对多策略
classifier.fit(train_data,train_label.values.ravel()) #ravel函数在降维时默认是行序优先



print("训练集：",classifier.score(train_data,train_label))
print("测试集：",classifier.score(test_data,test_label))
#print(test_label)
#print("测试集：",classifier.predict_proba(test_data))