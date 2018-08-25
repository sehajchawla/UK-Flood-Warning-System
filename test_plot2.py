#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:05:04 2018

@author: fai
"""

from datetime import datetime, timedelta
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list


stations = build_station_list()


t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]
station=stations[0]

plot_water_level_with_fit(station,t,level,3)