# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:40:02 2021

@author: Kostas-Geosystems
"""
import matplotlib.colors as colors
import matplotlib.image as mpimg
import matplotlib. pyplot as plt
import snappy
from zipfile import ZipFile
from os.path import join
from glob import glob
import pandas as pd
import numpy as np
import subprocess
import pprint
import os
import glob
from snappy import ProductIO
import jpy
System = jpy.get_type('java.lang.System')
System.gc()
import gc

import re
from geomet import wkt
from snappy import GPF
from snappy import ProductIO
from snappy import HashMap
from snappy import jpy
HashMap = snappy.jpy.get_type('java.util.HashMap')
import time
import glob
import os



###################################____Sentinel 2____###########################################################################################


# Subset
def subset_s2(product):
    # Subset Operator - snappy
    region =  'POLYGON ((25.928734321793883 40.86922448639907, 26.186724235597396 40.8646204407358, 26.18206442358473 40.722504195022196, 25.9246233910673 40.72708535938524, 25.928734321793883 40.86922448639907))'
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    image = product
    parameters = snappy.HashMap()
    parameters.put('copyMetadata', True)
    parameters.put('geoRegion', region)
    parameters.put('sourceBands', 'B2,B3,B4,B5,B8,B9,B12')
    subset = snappy.GPF.createProduct('Subset', parameters, image)
    print('Subseting the product....')
    
    return subset

def resample_s2(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    image = product
    parameters = snappy.HashMap()
#     parameters.put('targetHeight', 5490) # 10980
#     parameters.put('targetWidth', 5490) #10980
    parameters.put('downsampling', 'Median') 
    parameters.put('referenceBand', 'B2')
#     parameters.put('targetResolution', 20)
    
    resampled_n = snappy.GPF.createProduct('Resample', parameters, image)
    print('Resampling the product....')
    
    return resampled_n

def pca_s2(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('componentCount', 1)
    parameters.put('PsourceBandNames', 'B2,B3,B4,B5,B8,B9,B12')
    component = snappy.GPF.createProduct('pca', parameters, product)
    print('Applying PCA.....')
    
    return component

def createstack(path, name):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    #collection of preprocessed files
    f1 = path+name+str('_PCA.tif')
    f2 = path+name+str('_ndvi.tif')
    f3 = path+name+str('_ndwi.tif')
    
    processed_files = [f1,f2,f3]

    product_set=[]
    
    for f in processed_files:
        product_set.append(ProductIO.readProduct(f))
        
    #define the stack parameters
    params = HashMap()
    params.put('resamplingType', None)
    params.put('initialOffsetMethod', 'Product Geolocation')
    params.put('extent', 'Master')
    
    #make the stack    
    create_stack = GPF.createProduct('CreateStack', params, product_set)
    
    return create_stack


def stack(pca, ndvi, mndvi):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = HashMap()
    parameters.put('resamplingType', None)
    parameters.put('initialOffsetMethod', 'Product Geolocation')
    parameters.put('extent', 'Master')
    
    stack = GPF.createProduct('CreateStack', parameters, pca, ndvi, mndvi)
    print('Stacking the images....')
    
    return stack

def ndvi_ndwi(resampled):
    # Calculate ndvi
    parameters = snappy.HashMap()
    parameters.put('PredSourceBand', 'B4')
    parameters.put('PnirSourceBand', 'B8')
    ndvi = snappy.GPF.createProduct('NDVIOp', parameters, resampled)
    
    # Calculate mndwi
    parameters = snappy.HashMap()
    parameters.put('PgreenSourceBand', 'B3')
    parameters.put('PmirSourceBand', 'B12')
    mndwi = snappy.GPF.createProduct('mNdwiOp', parameters, resampled)
    print('Calculating NDVI and mNDWI....')
    
    return ndvi, mndwi


def kmeans_s2(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('clusterCount', 2)
    parameters.put('iterationCount', 300)
    bands = list(product.getBandNames())
    
    parameters.put('sourceBandNames', str(bands[1])+str(',')+str(bands[5]) +str(',')+str(bands[7]))
    
    cluster = snappy.GPF.createProduct('KMeansClusterAnalysis', parameters, product)
    print('Implementing Kmeans....')
    
    #reprojected = reproject(cluster)
    
    return cluster


def reproject(product_name):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('crs', 'EPSG:2100')
    parameters.put('noDataValue', -9.999)
    
    reprojected = snappy.GPF.createProduct('Reproject', parameters, product_name)
    
    return reprojected



##########################################################################################################################

##########################################____Sentinel_1________#########################################################

# Subset
def subset_s1(product):
    # Subset Operator - snappy
    region =  'POLYGON ((25.928734321793883 40.86922448639907, 26.186724235597396 40.8646204407358, 26.18206442358473 40.722504195022196, 25.9246233910673 40.72708535938524, 25.928734321793883 40.86922448639907))'
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    image = product
    parameters = snappy.HashMap()
    parameters.put('copyMetadata', True)
    parameters.put('geoRegion', region)

    subset = snappy.GPF.createProduct('Subset', parameters, image)
    print('Subset implemented succesfully')
    return subset

# Apply Orbit File Operator - snappy
def applyorbitfile(product):
    
    parameters = snappy.HashMap()
    parameters.put ('Apply-Orbit-File', True)
    apply_orbit = snappy.GPF.createProduct('Apply-Orbit-File', parameters, product)
    print('Orbit updated succesfully')
    
    return apply_orbit


# Calibration Operator - snappy
def s1_calibration(product):
    
    parameters = snappy.HashMap()
    parameters.put('outputSigmaBand', True)
    parameters.put('sourceBands', 'Intensity_VH,Intensity_VV')
    parameters.put('selectedPolarizations', 'VH,VV')
    parameters.put('outputImageScalInDb', True)
    calibrated = snappy.GPF.createProduct("Calibration", parameters, product)
    print("Calibration implemented succesfully")
    
    return calibrated


# Speckle Filter operator - snappy
def specklefilter(product):
    
    parameters = snappy.HashMap()
    parameters.put('filters', 'Lee')
    parameters.put('filterSizeX', 5)
    parameters.put('filterSizeY', 5)
    speckle = snappy.GPF.createProduct('Speckle-Filter', parameters, product)
    print('Speckle Filtering applied succesfully')
    
    return speckle


# Apply Terrain Correction
def terrain_correction(product):
    
    # Define the EGSA87 wkt
    proj = '''PROJCS["GGRS87 / Greek Grid",
        GEOGCS["GGRS87",
            DATUM["Greek_Geodetic_Reference_System_1987",
                SPHEROID["GRS 1980",6378137,298.257222101,
                    AUTHORITY["EPSG","7019"]],
                TOWGS84[-199.87,74.79,246.62,0,0,0,0],
                AUTHORITY["EPSG","6121"]],
            PRIMEM["Greenwich",0,
                AUTHORITY["EPSG","8901"]],
            UNIT["degree",0.0174532925199433,
                AUTHORITY["EPSG","9122"]],
            AUTHORITY["EPSG","4121"]],
        PROJECTION["Transverse_Mercator"],
        PARAMETER["latitude_of_origin",0],
        PARAMETER["central_meridian",24],
        PARAMETER["scale_factor",0.9996],
        PARAMETER["false_easting",500000],
        PARAMETER["false_northing",0],
        UNIT["metre",1,
            AUTHORITY["EPSG","9001"]],
        AXIS["Easting",EAST],
        AXIS["Northing",NORTH],
        AUTHORITY["EPSG","2100"]]'''
    
    
    # Define the EPSG:32635
    proj2 = '''PROJCS["WGS 84 / UTM zone 35N",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",27],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH],
    AUTHORITY["EPSG","32635"]]'''
    
    proj3 = '''GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]'''

    parameters = snappy.HashMap()
    parameters.put('demName', 'SRTM 1Sec HGT')
    parameters.put('imageResamplingMethod', 'BILINEAR_INTERPOLATION')
    parameters.put('pixelSpacingInMeter', 10.0)
    parameters.put('mapProjection', proj2)
    parameters.put('noDataValueAtSea', False)
    parameters.put('saveSelectedSourceBand', True)
    parameters.put('nodataValueAtSea', False)
    terrain_correction = snappy.GPF.createProduct('Terrain-Correction', parameters, product)
    print('Terrain Correction and Reprojection applied successfully')
    
    return terrain_correction

# Applying Kmeans Classification
def kmeans_s1(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('clusterCount', 2)
    parameters.put('iterationCount', 300)
    bands = list(product.getBandNames())
    print(str(bands[0])+str(',')+str(bands[1]))
    
    parameters.put('sourceBandNames', str(bands[0])+str(',')+str(bands[1]))
    
    cluster = snappy.GPF.createProduct('KMeansClusterAnalysis', parameters, product)
    print(f'Applying K-means has finished')
    
    return cluster

def lineartodB(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    bands = list(product.getBandNames())
    parameters = snappy.HashMap()
    parameters.put('sourceBands', str(bands[0])+str(',')+str(bands[1]))
    
    db = snappy.GPF.createProduct('LinearToFromdB', parameters, product)
    print(f'Applying Linear to dB...')
    
    return db


def resample_s1(product):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    image = product
    parameters = snappy.HashMap()
    parameters.put('targetHeight', 10980) # 10980
    parameters.put('targetWidth', 10980) #10980
    parameters.put('downsampling', 'Median') 


    resampled_n = snappy.GPF.createProduct('Resample', parameters, image)
    print('Resampling the product....')
    
    return resampled_n










