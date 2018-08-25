#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:26:29 2018

@author: fai
"""

import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()

update_water_levels(stations)
    
dt=2
Number_of_stations=5

#Set the degree of the polynomial to p
p=4

station_names =[]
for i in stations_highest_rel_level(stations, Number_of_stations)[:Number_of_stations]:
    station_names.append(i[0])

greatest_relative_water_level_stations=[]
for station in stations:
    if station.name in station_names:
            greatest_relative_water_level_stations.append(station)

#call the function to plot the data and the best fit
for station in greatest_relative_water_level_stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(station,dates,levels,p)