#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:28:09 2018

@author: Sehaj
"""
import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    stations = build_station_list()
    assert stations
    update_water_levels(stations)
    assert stations_highest_rel_level(stations, 10)
    