# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:46:42 2022

@author: zhu_wei@cqu.edu.cn
read the dataset from the csv file
"""
from matplotlib import pyplot as plt

def list_float(list_str):#for the list with elements in str type, translate it into a list with elements in float type
    list_float=[]
    for element in list_str:
        list_float.append(float(element))
    return(list_float)
def list_int(list_str):#for the list with elements in str type, translate it into a list with elements in int type
    list_int=[]
    for element in list_str:
        list_int.append(int(element))
    return(list_int)
class hierarchy_dataset_2nd:#class of sub-type 
    def __init__(self,num):
        self.num=num
        self.function_x=[]
        self.function_y=[]
    def read(self,num):
        filename='hierarchy_dataset_2nd_'+str(self.num)+'.csv'
        with open(filename, "r") as f:
            temp_file=f.readlines()
        for line in  temp_file:
            temp_line_split=line.split(',')
            if temp_line_split[0]=='group_number':
                self.num=int(temp_line_split[1])
            elif temp_line_split[0]=='total_num_in_group':
                self.total_num_in_group=int(temp_line_split[1])
            elif temp_line_split[0]=='center_num':
                self.center=int(temp_line_split[1])
            elif temp_line_split[0]=='E1E2v1v2_mean_value':
                self.M_E1=float(temp_line_split[1])
                self.M_E2=float(temp_line_split[2])
                self.M_v1=float(temp_line_split[3])
                self.M_v2=float(temp_line_split[4])
            elif temp_line_split[0]=='E1E2v1v2_Std':
                self.Std_E1=float(temp_line_split[1])
                self.Std_E2=float(temp_line_split[2])
                self.Std_v1=float(temp_line_split[3])
                self.Std_v2=float(temp_line_split[4])
            elif temp_line_split[0]=='lab':
                self.num_1=int(temp_line_split[1])
                self.num_2=int(temp_line_split[2])
            elif temp_line_split[0]=='curve_lenth':
                self.curve_lenth=list_float(temp_line_split[1:])
            elif temp_line_split[0]=='E1_group':
                self.E1_group=list_float(temp_line_split[1:])
            elif temp_line_split[0]=='E2_group':
                self.E2_group=list_float(temp_line_split[1:])
            elif temp_line_split[0]=='v1_group':
                self.v1_group=list_float(temp_line_split[1:])
            elif temp_line_split[0]=='v2_group':
                self.v2_group=list_float(temp_line_split[1:])
            elif temp_line_split[0][:10]=='function_x':
                for mm in range(self.total_num_in_group):    
                    if int(temp_line_split[0][10:])==mm:
                        self.function_x.append(list_float(temp_line_split[1:]))
            elif temp_line_split[0][:10]=='function_y':
                for mm in range(self.total_num_in_group):
                   if int(temp_line_split[0][10:])==mm:
                       self.function_y.append(list_float(temp_line_split[1:]))
            else:
                print("error in reading")
                print(temp_line_split)

hierarchy_dataset=[]
set_num=184#total number of the subtypes
for num in range(set_num):
    new_hierarchy_dataset=hierarchy_dataset_2nd(num)
    new_hierarchy_dataset.read(num)
    total_len=len(hierarchy_dataset)
    flg_ii=total_len
    for ii in range(total_len):#sort
        if hierarchy_dataset[ii].num_1<new_hierarchy_dataset.num_1 or (hierarchy_dataset[ii].num_1==new_hierarchy_dataset.num_1 and hierarchy_dataset[ii].num_2<new_hierarchy_dataset.num_2):
            flg_ii=ii
            break
    hierarchy_dataset=hierarchy_dataset[:flg_ii]+[new_hierarchy_dataset]+hierarchy_dataset[flg_ii:]
hierarchy_dataset=list(reversed(hierarchy_dataset))    

       
