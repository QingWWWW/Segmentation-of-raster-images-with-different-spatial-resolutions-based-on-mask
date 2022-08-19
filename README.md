# Segmentation-of-raster-images-with-different-spatial-resolutions-based-on-mask
Background segmentation of raster images with different spatial resolutions based on mask

precondition：Raster images with the same geospatial size

gdal==3.2.3 numpy==1.22.3

Multiple raster images with multiple different spatial resolutions. The example data shown here are r1 and r2 with two different spatial resolutions raster images from different sensors in the folder data_raw.

Assuming that one of the spatial resolution raster images is sensitive to the background information, a mask can be built based on this raster image to remove the background of raster images with different spatial resolution. Here the raster image of R1 is sensitive to the background。

Steps: First, use' background segmentation based on background sensitive image.py' to separate background information from r1-based raster image (Here, the threshold method was adopted), and export a raster file (\mask_file\raster_background_s) without background information. Secondly,' create _ mask _ shp.py' is used to generate the mask in shp format (\mask_file\mask_shp_file) based on the r1 raster image with the background removed. Finally,' segmentation to different resolution image.py' is used to segment the background (\result) of raster images with different resolutions based on the .shp file.
