# Sentinel_1-2_Water_Mapping
In this repository I am sharing a pipeline I have created to ingest, preprocess and finaly create an analysis ready products based on Sentinel 1 and Sentinel 2 images.
The repo is consited of 2 folders. The first one contains a jupyter notebook and a set of custom functions in order to create a list of available Sentinel 1 and Sentinel 2 images and then download them on our local machine. The second folder contains a jupyter noteboon as the main body and the output is a new image processed and cleaned indicating where water is appears on the image. The result is a binary image seperating water from background, while it also can be used to create a probability water map in case a long time series of images is available. The project has been build in python environment making use of modules like Snappy, GDAL, SentinelSat and Folium.

This project experiments in water mapping using Sentinel 2 and Sentinel 1 data either separately or synergistically. <b> OnGoing Project </b>

<h2> Data Ingestion </h2>
This folder contains four files with the Jupyter notebook <b>"Data_Ingestion.ipynb"</b> being the main body.
- Data Ingestion.ipynb
- basemaps.py
- credential.ini
- sentinel.py

<h2> Data Processing </h2>



<h3> Acknowledgements </h3> 

