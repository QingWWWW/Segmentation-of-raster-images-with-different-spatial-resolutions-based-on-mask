# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:26:50 2022

@author: Qing Wang
"""

from osgeo import gdal, ogr, osr
import os
import numpy as np

raster_path='./mask_file/raster_background_s/'

raster_files=os.listdir(raster_path)

mask_savepath='./mask_file/mask_shp_file/'
if not os.path.exists(mask_savepath):
    os.makedirs(mask_savepath)

for f in raster_files:
    name=os.path.splitext(f)[0]
    data=gdal.Open(raster_path+f) 
    band = data.GetRasterBand(1) 
    
    
    
    prj = osr.SpatialReference()
    prj.ImportFromWkt(data.GetProjection())  
    
    outshp = mask_savepath+ name+ ".shp"  # name of the output vector
    drv = ogr.GetDriverByName("ESRI Shapefile")
    Polygon = drv.CreateDataSource(outshp)  # creat target file
    Poly_layer = Polygon.CreateLayer(name, srs=prj, geom_type=ogr.wkbMultiPolygon)  # Create a layer for the shp file
    newField = ogr.FieldDefn('pix_value', ogr.OFTReal)  # Adds a field to the target shp file to store the Pixel value of the original raster，
    Poly_layer.CreateField(newField)
    
   
    gdal.FPolygonize(band, None, Poly_layer, 0)  
    Polygon.SyncToDisk()
    Polygon.Destroy()    