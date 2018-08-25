#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:56:33 2018

@author: Sehaj
"""

def low_and_moderate_staions(stations):
    output_list_low = []
    stations_that_are_flooding1 = []
    relative_water_level = []
    for i in stations:
        if i.relative_water_level() != None:
            """adding all those that are low"""
            if i.relative_water_level()>0 and i.relative_water_level()<1:
                stations_that_are_flooding1.append(i.name)
                relative_water_level.append(i.relative_water_level())
    for j in range(1,len(stations_that_are_flooding1)):
        """putting them in one tuple"""
        output_list_low.append((stations_that_are_flooding1[j],relative_water_level[j]))
    """sorting stuff out"""
    output_list_low = sorted_by_key(output_list_low,1)
    output_list_low = output_list[::-1]
    return("The list of stations that have a low risk of flooding: ")
    return(output_list_low)
    
    output_list_moderate = []
    stations_that_are_flooding2 = []
    relative_water_level = []
    for i in stations:
        if i.relative_water_level() != None:
            """adding all things  that are moderate"""
            if i.relative_water_level()>1:
                stations_that_are_flooding2.append(i)
                relative_water_level.append(i.relative_water_level())
    for j in range(1,len(stations_that_are_flooding2)):
        """putting them in one tuple"""
        output_list_moderate.append((stations_that_are_flooding2[j],relative_water_level[j]))
    """sorting stuff out"""
    output_list_moderate = sorted_by_key(output_list_moderate,1)
    output_list_moderate = output_list[::-1]
    return("The list of stations that have a moderate risk of flooding: ")
    return(output_list_moderate)
    
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels



stations = build_station_list()
update_water_levels(stations)


print(low_and_moderate_staions(stations))
    
    
    
    
    
    
    
    
    
    