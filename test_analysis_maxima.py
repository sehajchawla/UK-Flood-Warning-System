#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:51:47 2018

@author: fai
"""

import pytest
from floodsystem.analysis import maxima



y=[10,9,1,3,1,5,1,7,1,8,10]

    
maxima(y)
    
assert maxima(y)==[3,5,7]
