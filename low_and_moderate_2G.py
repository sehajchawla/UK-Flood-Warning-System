#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:56:33 2018

@author: Sehaj
"""
from floodsystem.utils import sorted_by_key

def low_and_moderate_staions(stations):
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
    return("The list of stations that have a low risk are: " + str(output_list_low) + "....................................................... The list of stations that have a moderate risk are: " + str(output_list_moderate))


    
    
    
    
    
    
    
    
    
    