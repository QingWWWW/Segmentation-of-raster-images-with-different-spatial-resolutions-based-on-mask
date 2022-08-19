# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 19:27:01 2022

@author: Qing Wang
"""

from osgeo import gdal
import os
import numpy as np

raster_path='./data_raw/r1/'
raster_files=os.listdir(raster_path)

raster_savepath='./mask_file/raster_background_s/'
if not os.path.exists(raster_savepath):
    os.makedirs(raster_savepath)
    
for f in raster_files:
    #name=os.path.splitext(f)[0]
    input_raster = gdal.Open(raster_path+f)  
    prj = input_raster.GetProjection()
    trans = input_raster.GetGeoTransform()
    
    inband = input_raster.GetRasterBand(1)  
    in_band_array=inband.ReadAsArray()
    #Set threshold to split background (None data) and foreground (pix value after normalization)
    delta=np.max(in_band_array)-np.min(in_band_array)
    in_band_array_new=(in_band_array-np.min(in_band_array))/delta
    re=np.where(in_band_array_new<=0.12,np.nan,in_band_array_new)
    
    #Save as raster image
    driver = gdal.GetDriverByName('GTiff')
    dst_ds = driver.Create(raster_savepath+f, re.shape[1], re.shape[0], 1, 7)
 
    if prj:
        dst_ds.SetProjection(prj)
    if trans:
        dst_ds.SetGeoTransform(trans)
 
    
    dst_ds.GetRasterBand(1).WriteArray(re)
 
    dst_ds.FlushCache()
    del dst_ds