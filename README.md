# Sentinel_1-2_Water_Mapping
<p>In this repository I am sharing a pipeline I have created to ingest, preprocess and finaly create an analysis ready products based on Sentinel 1 and Sentinel 2 images.
The repo is consited of 2 folders. The first one contains a jupyter notebook and a set of custom functions in order to create a list of available Sentinel 1 and Sentinel 2 images and then download them on our local machine. The second folder contains a jupyter noteboon as the main body and the output is a new image processed and cleaned indicating where water is appears on the image. The result is a binary image seperating water from background, while it also can be used to create a probability water map in case a long time series of images is available. The project has been build in python environment making use of modules like Snappy, GDAL, SentinelSat and Folium.</p>

This project experiments in water mapping using Sentinel 2 and Sentinel 1 data either separately or synergistically. <b> OnGoing Project </b>

<h2> Data Ingestion </h2>
This folder contains four files with the Jupyter notebook <b>"Data_Ingestion.ipynb"</b> being the main body.
<ul>
  <li><b>Data Ingestion.ipynb</b> - This is the main body from which data ingestion process is running.</li>
  <li><b>basemaps.py</b> - This file contains some necessary funcntions fro rendering google maps</li>
  <li><b>credential.ini</b> - In this file you need to write your credentials for Copernicus open access hub (https://scihub.copernicus.eu/)</li>
  <li><b>sentinel.py</b> - This file contains some custom made functions</li>
</ul>


![image](https://user-images.githubusercontent.com/23013328/162620579-0863768a-5781-4352-80df-44b209f171c6.png)


<h2> Data Processing </h2>
<b>Step 1: Pre-Process</b>

Sentinel 2 images are cropped within the area of interest and spectral bands are resampled to 10 meters spatial resolution. For Sentinel 1 images a geometric correction is neccesary using orbit file and terrain correction using a digital elevation model. Additionally, Sentinel 1 images get calibrated, filtered for speckles, converted to decibel units and cropped within the area of interest.

![image](https://user-images.githubusercontent.com/23013328/162620202-17ff4828-fe37-4593-85ac-7d0ffcf74ed0.png)


The NDVI index for Sentinel 2 spectral channels is defined as follows:
  - NDVI∶=(NIR - RED)/(NIR + RED)
  - NDVI∶= (B8 - B4)/(B8 +  B4)

The mNDWI water index for Sentinel 2 spectral channels is defined as follows:
  - mNDWI∶= (Green - Middle Infrared)/(Green + Middle Infrared)
  - mNDWI∶= (B3 - B12)/(B3 + B12)



<h3> Acknowledgements </h3> 

<cite>Serco Italia SPA (2020). Sentinel-1 processing using snappy (version 1.1). Retrieved from RUS
Lectures at https://rus-copernicus.eu/portal/the-rus-library/learn-by-yourself/ </cite>


