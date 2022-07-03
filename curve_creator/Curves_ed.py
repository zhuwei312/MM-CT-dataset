# -*- coding: utf-8 -*-
"""
曲线类工具

编写人:朱绍伟
"""
# -*- coding: utf-8 -*-
import math
import random
class Curves:
    def __init__(self):
        ra=[]
        for ii in range(6):
            ra.append((random.random()-0.5)*0.3)
            #ra.append((random.random()-0.5)*0.3*(ii+1)/6)
        self.point_num=100
        self.par_fourier=ra
        self.par_c=1
        self.strut_L=1
        self.cc=0.2
        self.curvepoint=self.Fourier()
        self.length=math.sqrt((self.curvepoint[0][-1]-self.curvepoint[0][0])**2+(self.curvepoint[1][-1]-self.curvepoint[1][0])**2)
        self.theita=math.atan((self.curvepoint[1][-1]-self.curvepoint[1][0])/(self.curvepoint[0][-1]-self.curvepoint[0][0]))
        temp=self.Rotation(self.curvepoint,[self.curvepoint[0][0],self.curvepoint[1][0]],-self.theita)
        temp2=self.Toform(temp,1,[0,0])
        self.out=self.YToform(temp2,self.cc)
        
    def Fourier_to_curvepoint(self,temp_par_fourier):
        self.curvepoint=self.Fourier()
        temp=self.Rotation(self.curvepoint,[self.curvepoint[0][0],self.curvepoint[1][0]],-self.theita)
        self.out=self.Toform(temp,1,[0,0])   
        
    def Fourier(self):  
    #temp为长度为奇数的list,依次代表C,a1,b1,a2,b2,a3,b3....
        temp=[self.par_c]+self.par_fourier
        x=[]
        y=[]
        len_Fourier=(len(temp)-1)//2
        for i in range(self.point_num):
            xx=i*self.strut_L/self.point_num
            yy=0
            for j in range(1,len_Fourier):
                yy=yy+temp[2*j-1]*math.sin(2*j*xx*math.pi/self.strut_L)
                yy=yy+temp[2*j]*math.cos(2*j*xx*math.pi/self.strut_L)
            x.append(xx)
            y.append(yy)
        curve=[x,y]
        return curve
    
    def Rotation(self,curves,point,theita):
    #曲线绕点旋转theita
        x=curves[0]
        y=curves[1]
        len_curve=len(x)
        #print(len_Fourier)
        x_new=[]
        y_new=[]
        for i in range(len_curve):
            rr=math.sqrt(math.pow(x[i]-point[0],2)+math.pow(y[i]-point[1],2))
            if x[i]==point[0] and y[i]>=point[1]:
                theita0=math.pi/2
            elif x[i]==point[0] and y[i]<=point[1]:
                theita0=math.pi*3/2
            else:
                theita0=math.atan((y[i]-point[1])/(x[i]-point[0]))
                if x[i]<point[0]:
                  theita0=theita0+math.pi  
            theita_new=theita0+theita
            xx_new=point[0]+rr*math.cos(theita_new)
            yy_new=point[1]+rr*math.sin(theita_new)
            x_new.append(xx_new)
            y_new.append(yy_new)
            curve=[x_new,y_new]
        return curve
    
    def Toform(self,temp,strut_L,point): 
    #将曲线的长度定制为strut_L，起点平移到point位置
        x=temp[0]
        y=temp[1]
        L_temp=math.sqrt((x[-1]-x[0])**2+(y[-1]-y[0])**2)
        len_curve=len(x)
        #print(len_Fourier)
        x_new=[]
        y_new=[]
        for i in range(len_curve):
            xx_new=x[i]*strut_L/L_temp-x[0]+point[0]
            yy_new=y[i]-y[0]++point[1]
            x_new.append(xx_new)
            y_new.append(yy_new)
            curve=[x_new,y_new]
        return curve
    
    def YToform(self,temp,cc): 
    #将曲线的高度固定为常数cc,默认temp[1][0]和temp[1][-1]相等
        x=temp[0]
        y=temp[1]
        if abs(y[0]-y[-1])>0.1:
            print("error:曲线起点终点y值不一致")
            return temp 
        else:
            kk=max(abs(min(y)),max(y))
            len_curve=len(x)
            #print(len_Fourier)
            x_new=[]
            y_new=[]
            for i in range(len_curve):
                xx_new=x[i]
                yy_new=y[i]/kk*cc
                x_new.append(xx_new)
                y_new.append(yy_new)
                curve=[x_new,y_new]
            return curve
    
    def curve_xmirror(self, xmirror): 
    #将曲线对称复制并检查是否越界，越界则返回1
        x=self.curvepoint_hen[0]
        y=self.curvepoint_hen[1]
        len_curve=len(x)
        #print(len_Fourier)
        for i in range(len_curve-2,1,-1):
            if (x[i]>=xmirror or x[i]<=0):
                return [0,0], 1
            else:
                xx_new=2*xmirror-x[i]
                yy_new=y[i]
                x.append(xx_new)
                y.append(yy_new)
        curve=[x,y]
        return curve,0



