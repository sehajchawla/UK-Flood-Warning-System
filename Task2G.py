#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:30:30 2018

@author: Sehaj
"""

from low_and_moderate_2G import low_and_moderate_staions 
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels



stations = build_station_list()
update_water_levels(stations)


print(low_and_moderate_staions(stations))