# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:15:47 2021

@author: zhu_wei@cqu.edu.cn
creat a curved triangle
"""
from Curves_ed import Curves
import math
from cells import cells
#from matplotlib import pyplot as plt

def Cross(temp1,temp2,r):#Cross function is used to assess the interesection of the two curve
    for i in range(len(temp1[0])):
        if (temp1[0][i]-temp1[0][0])**2+(temp1[1][i]-temp1[1][0])**2>4*r**2:#距端点处2r内相交不考虑不考虑
            if (temp1[0][i]-temp1[0][-1])**2+(temp1[1][i]-temp1[1][-1])**2>4*r**2:
                for j in range(len(temp2[0])):
                    if (temp1[0][i]-temp2[0][j])**2+(temp1[1][i]-temp2[1][j])**2<r**2:#节点接近r视为相交
                        return 0
    return 1

def check(cu):#check function is used to assess the interesection of the triangles and the adjecent triangles
    temp1=cu.out    
    temp2=cu.Rotation(cu.out,[cu.out[0][0],cu.out[1][0]],2*math.pi/3)
    temp3=cu.Rotation(cu.out,[cu.out[0][0],cu.out[1][0]],-2*math.pi/3)
    temp2=cu.Toform(temp2,1,[1,0])
    temp3=cu.Toform(temp3,1,[0.5,math.sqrt(3)/2])
    temp1_2=cu.Toform(temp1,1,[-1,0])
    temp2_1=cu.Toform(temp2,1,[0.5,-math.sqrt(3)/2])
    temp3_1=cu.Toform(temp3,1,[0,0])
    temp3_2=cu.Toform(temp3,1,[-0.5,math.sqrt(3)/2])

    if Cross(temp1,temp2,0.05)==0:
        return 0, 0
        #plt.text(0,0,"1")
    elif Cross(temp1,temp2_1,0.05)==0:
        return 0, 0
        #plt.text(0,0,"2")
    elif Cross(temp1_2,temp3_1,0.05)==0:
        return 0, 0
        #plt.text(0,0,"3")
    elif Cross(temp3,temp2_1,0.05)==0:
        return 0, 0
        #plt.text(0,0,"3")
    elif Cross(temp3_2,temp3,0.05)==0:
        return 0, 0
        #plt.text(0,0,"4")
    else:
        cell=cells(cu.par_fourier,cu.par_c,cu.out,[temp1[0]+temp2[0][1:]+temp3[0][1:-1],temp1[1]+temp2[1][1:]+temp3[1][1:-1]],"normal triangle")
        return cu,cell

def triangle_creator(max_curve_number):#creat max_curve_number curves
    cellset=[]
    jishu=0
    errors=0
    while jishu<max_curve_number:
        cu=Curves()
        cu,cell=check(cu)
        if cu==0:
           errors=errors+1
        else:
            jishu=jishu+1
            cellset.append(cell)
    return cellset




