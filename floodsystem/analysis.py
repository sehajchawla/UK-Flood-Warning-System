#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:43:30 2018

@author: fai
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime


'''Task 2F - create a polynomial that is the best fit to the data points'''

def polyfit(dates, levels, p):
    #Convert the dates to floats
    x = matplotlib.dates.date2num(dates)
    
    y=levels
    
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)
    
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    
    return poly, x[0]

def maxima(y):
    
    maxima=[]
    
    for i in range(1,len(y)-1):
        if y[i]>y[i-1] and y[i]>y[i+1]:
            maxima.append(y[i])
    
    return maxima

def slope_at_end_point(x,y):
    slope=(y[-1]-y[-2])
    return slope