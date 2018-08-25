#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:32:37 2018

@author: fai
"""

import matplotlib.pyplot as plt
import datetime
import matplotlib
from floodsystem.analysis import polyfit


'''Task 2E - a function that plots a graph of water level against time for a given station'''
def plot_water_levels(station, dates, levels):
    
    #plot data points
    plt.plot(dates,levels,label='water level')
    
    #extract the values of the typical range
    typical_lower, typical_higher =station.typical_range[0],station.typical_range[1]

    #plot the typical values as horizontal lines
    plt.axhline(y=typical_lower, color='b',label='typical low')
    plt.axhline(y=typical_higher, color='r', label='typical high')


    #labels
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(str(station.name))
    plt.legend()
    
    # Display plot
    plt.tight_layout()
    plt.show()

'''Task 2F - a function that plots the orginal data points and the best fit line
 of water level against time for a given station'''
def plot_water_level_with_fit(station, dates, levels, p):
    
    x = matplotlib.dates.date2num(dates) #changing the dates to floats
    y = levels
    
    #plot original data points
    plt.plot(dates,y,label='water level')

    
    typical_lower, typical_higher =station.typical_range[0],station.typical_range[1]
    plt.axhline(y=typical_lower, color='b',label='typical low')
    plt.axhline(y=typical_higher, color='r', label='typical high')
    
    #call ployfit to generate the best fit line and the shift of the x values
    poly, d0 = polyfit(dates, y, p)
    
    #Plot the best fit line
    plt.plot(dates, poly(x - d0),label='best fit')

    #labels
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(str(station.name))
    plt.legend()
    
    # Display plot
    plt.tight_layout()
    plt.show()
