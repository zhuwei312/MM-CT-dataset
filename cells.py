# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:12:37 2021

@author: Administrator
"""

class cells():
    def __init__(self,par_fourier,par_c,curvepoint,function,geo):
        self.par_fourier=par_fourier
        self.function=function
        self.par_c=par_c
        self.curvepoint=curvepoint
        self.geo="normal triangle"