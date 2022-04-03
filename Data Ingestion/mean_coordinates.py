# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:24:09 2021

@author: Kostas-Geosystems
"""


import statistics
import geojson
from datetime import date

def mean_coordinates():
    with open('AOI_manual_%s.geojson' % str(date.today())) as f:
        gj = geojson.load(f)
    
    latitude1 = gj['features'][0]['geometry']['coordinates'][0][0][0]
    latitude3 = gj['features'][0]['geometry']['coordinates'][0][3][0]

    mean_latitude = statistics.mean([latitude1,latitude3])


    longitude1 = gj['features'][0]['geometry']['coordinates'][0][0][1]
    longitude3 = gj['features'][0]['geometry']['coordinates'][0][3][1]

    mean_longitude = statistics.mean([longitude1,longitude3])

    return mean_latitude, mean_longitude