#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 00:17:45 2018

@author: fai
"""
from low_and_moderate_2G import low_and_moderate_staions
import datetime
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from analysis import polyfit,maxima,slope_at_end_point


def high_and_severe_staions(moderate):
    p=6
    dt=5
    high_name=[]
    severe_name=[]
    moderate_name=[]
    for station in moderate:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        x = matplotlib.dates.date2num(dates) #changing the dates to floats
        poly, d0 = polyfit(dates, levels, p)
        y1=poly(x - d0)
        
        increasing_local_maxima=None
        max_values=maxima(y1)
        
        if max_values[-1]>max_values[-2] and max_values[-2]>max_values[-3]:
            increasing_local_maxima=True
        else:
                increasing_local_maxima=False
        
        
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
    
    return high_name,severe_name,moderate_name
        
    
    
        
