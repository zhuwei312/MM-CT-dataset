# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 19:37:11 2022

@author: Administrator
"""
from keras.models import load_model
from triangle_creator import triangle_creator
import pandas as pd
import numpy as np

def int_r(array):#return the location of the max value in array
    maxvalue=max(array)
    for iii in range(len(array)):
        if array[iii]==maxvalue:
           return iii
def up_dim(list_i):#transfrom [1,2,3...] to [[1],[2],[3],...]
    result=[]    
    for ii in list_i:
        result.append([ii])
    return result
def trans_curve_to_in_or_de(curve):#将curve的y坐标数组转换为单调性编码
    in_or_de=[]#单调性list
    for i in range(len(curve)-1):
        if curve[i+1]-curve[i]>0:
            in_or_de.append(1)
        elif curve[i+1]-curve[i]<0:
            in_or_de.append(-1)
        else:
            in_or_de.append(0)
    sim_in_or_de=[in_or_de[0]]
    for i in range(len(in_or_de)-1):
        if in_or_de[i+1]!=in_or_de[i]:
            sim_in_or_de.append(in_or_de[i+1])
    if len(sim_in_or_de)>8:
        print("error in sim_in_or_de")
        print(sim_in_or_de)
        print("...")
    while len(sim_in_or_de)<10:
        sim_in_or_de.append(0)
    return sim_in_or_de
def clsssfier(model,Xtest,Plist):#clsssfier,model represent the trained model
    #Xtest is a x*100*1 np array representing x curves
    Ypredict1,Ypredict2=model.predict(Xtest)
    int_Ypredict1_group=[]
    int_Ypredict2_group=[]
    in_con=0
    for ii in range(len(Ypredict1)):
        int_Ypredict1=int_r(Ypredict1[ii])
        int_Ypredict2=int_r(Ypredict2[ii])
        int_Ypredict2_group.append(int_Ypredict2)
        if Plist[int_Ypredict1]==int_Ypredict2:
            int_Ypredict1_group.append(int_Ypredict1)
        else:
            int_Ypredict1_group.append(-1)
            in_con=in_con+1
    return int_Ypredict1_group,int_Ypredict2_group,in_con/len(Xtest)
model=load_model("model.h5")
Plist1=pd.read_csv('Plist.csv',header=None)
Plist1=np.array(Plist1.T).tolist()[0]
n=10
triangles=triangle_creator(n)#creat n triangles
curve_set=[]
in_or_de_set=[]
for triangle in triangles:
    temp=triangle.curvepoint[1]
    in_or_de_set.append(trans_curve_to_in_or_de(temp))
    curve_set.append(up_dim(temp))
    
X_train5=np.array(curve_set).astype('float32')
X_train6=np.array(in_or_de_set).astype('float32')
Ypredict1,Ypredict2,in_con_ratio=clsssfier(model,[X_train5,X_train6],Plist1)
#Ypredict1=0~183 represent 184 different subtypes(-1 means can't classify,
#with the ratio of in_con_ratio)
#Ypredict2=0~7 represent 8 different types
print("The sub-types of the creator curved triangles are"+str(Ypredict1))
print("The types of the creator curved triangles are"+str(Ypredict2))
