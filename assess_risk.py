#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:56:33 2018

@author: Sehaj
"""
from floodsystem.utils import sorted_by_key

import datetime
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit,maxima,slope_at_end_point


def assess_the_risk(stations):
    output_list = []
    output_list_low = []
    output_list_moderate = []
    stations_that_are_flooding = []
    relative_water_level = []
    for i in stations:
        if i.relative_water_level() != None:
            """adding all things  that are low"""
            if i.relative_water_level()>0 and i.relative_water_level()<1:
                stations_that_are_flooding.append(i.name)
                relative_water_level.append(i.relative_water_level())
    for j in range(1,len(stations_that_are_flooding)):
        """putting them in one tuple"""
        output_list.append((stations_that_are_flooding[j],relative_water_level[j]))
    """sorting stuff out"""
    output_list = sorted_by_key(output_list,1)
    output_list = output_list[::-1]
    output_list_low = output_list
    
    output_list = []
    moderate_list = []
    stations_that_are_flooding = []
    relative_water_level = []
    for i in stations:
        if i.relative_water_level() != None:
            """adding all things  that are moderate"""
            if i.relative_water_level()>1:
                stations_that_are_flooding.append(i.name)
                relative_water_level.append(i.relative_water_level())
                """FOR YOU TO USE"""
                moderate_list.append(i)
    for j in range(1,len(stations_that_are_flooding)):
        """putting them in one tuple"""
        output_list.append((stations_that_are_flooding[j],relative_water_level[j]))
    """sorting stuff out"""
    output_list = sorted_by_key(output_list,1)
    output_list = output_list[::-1]
    output_list_moderate = output_list
    
    '''take in the stations that qualify as moderate risks to evaluate if they have high/severe risk'''

    p=12
    dt=3
    #create lists of different risks
    high_name=[]
    severe_name=[]
    moderate_name=[]
    
    for station in moderate_list:
        #get the water levels over the last dt days
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        x = matplotlib.dates.date2num(dates) #changing the dates to floats
        poly, d0 = polyfit(dates, levels, p) #create a line of best fit
        y1=poly(x - d0)
        
        #call the function to put the maxima of the best fit line in a list
        increasing_local_maxima=None
        max_values=maxima(y1)
        
        #Check if the station has increasing maxima
        if max_values[-1]>max_values[-2] and max_values[-2]>max_values[-3]:
            increasing_local_maxima=True
        else:
                increasing_local_maxima=False
        
        #Call the slope funciton to see if the water level is rising rapidly
        rapid_increase_in_water_level= None
        
        if slope_at_end_point(y1)>0.1:
            rapid_increase_in_water_level=True
        else:
            rapid_increase_in_water_level=False
        
        if increasing_local_maxima and rapid_increase_in_water_level:
            severe_name.append(station.name)
        elif increasing_local_maxima or rapid_increase_in_water_level:
            high_name.append(station.name)
        else:
            moderate_name.append(station.name)
    
    return output_list_low,moderate_name,high_name,severe_name
    

    
    
    
    
    
    
    
    
    
    