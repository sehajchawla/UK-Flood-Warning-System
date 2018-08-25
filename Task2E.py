#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:58:38 2018

@author: fai
"""
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels



stations = build_station_list()

update_water_levels(stations)

#The number of days before today
dt=10

#The number of stations at which the current relative water level is greatest.
Number_of_stations=5
    
#An empty list for the names of the required stations
station_names =[]

#call the function to find the greatest relative water level stations
for i in stations_highest_rel_level(stations, Number_of_stations)[:Number_of_stations]:
    station_names.append(i[0])

#An empty list for the required stations as monitoring station objects
greatest_relative_water_level_stations=[]

#convert the names to the objects and add to the list
for station in stations:
    if station.name in station_names:
            greatest_relative_water_level_stations.append(station)

#call the plot function 
for station in greatest_relative_water_level_stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station,dates,levels)