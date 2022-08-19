# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:38:37 2022

@author: Qing Wang
"""

from osgeo import gdal
import os
import shapefile


path_raster='./data_raw/r2/'
path_shp='./mask_file/mask_shp_file/'

savepath_raster= './result/r2_segmentation/'

if not os.path.exists(savepath_raster):
    os.makedirs(savepath_raster)

def get_file_name(path,file_type):
    file_name=[]
    files=os.listdir(path)
    for f in files:
        if f.split('.')[1]==file_type:                           
            file_name.append(f)
    return file_name
        


raster_files= get_file_name(path_raster,'tif')
shp_files= get_file_name(path_shp,'shp')

#Import the raster and the corresponding shp file
for r ,s in zip(raster_files,shp_files):#
    
    input_raster= gdal.Open(path_raster+r)
    inshape=path_shp+s
    b= shapefile.Reader(inshape)
    output_raster= savepath_raster+r
    ds=gdal.Warp(output_raster,
                    input_raster,
                    format = 'GTiff',
                    outputBounds=b.bbox,
                    cutlineDSName = inshape,#layer name
                    cutlineWhere='pix_value>0', #Keep the foreground
                    dstNodata = -1000)
    ds=None


