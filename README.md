# Sentinel_1-2_Water_Mapping
<p>In this repository I am sharing a pipeline I have created to ingest, preprocess and finaly create an analysis ready products based on Sentinel 1 and Sentinel 2 images.
The repo is consited of 2 folders. 
<ul>
  <li>The first folder <b>"Data Ingestion"</b> contains a jupyter notebook and a set of custom functions in order to create a list of available Sentinel 1 and Sentinel 2 images and then download them on our local machine.</li>
  <li>The second folder <b>"Data Processing"</b> contains a jupyter noteboon as the main body and the output is a new image processed and cleaned indicating where water is appears on the image.</li>
</ul>
The result is a binary image seperating water from background, while it also can be used to create a probability water map in case of using time series of images. The project has been build in python environment making use of modules like Snappy, GDAL, SentinelSat and Folium.</p>

This project is experimenting in water mapping using Sentinel 2 and Sentinel 1 data either separately or synergistically. <b> OnGoing Project </b>

<h2> Data Ingestion </h2>
This folder contains four files with the Jupyter notebook <b>"Data_Ingestion.ipynb"</b> being the main body.
<ul>
  <li><b>Data Ingestion.ipynb</b> - This is the main body from which data ingestion process is running.</li>
  <li><b>basemaps.py</b> - This file contains some necessary funcntions for rendering google maps.</li>
  <li><b>credential.ini</b> - In this file you need to write your credentials for Copernicus open access hub (https://scihub.copernicus.eu/).</li>
  <li><b>sentinel.py</b> - This file contains some custom made functions.</li>
</ul>


![image](https://user-images.githubusercontent.com/23013328/162620579-0863768a-5781-4352-80df-44b209f171c6.png)


<h2> Data Processing </h2>
Inside the folder data processing the user will find the following files:
<ul>
  <li><b>Probability_Map_S1_S2.ipynb</b> - This jupyter notebook is the main body of code which reads Sentinel images calculates the water masks aligns them and then creates a probability layer.</li>
  <li><b>evros.py</b> - In this python file some custom made functions are placed.</li>
  <li><b>sentinels.ini</b> - In this file write the path where the sentinel products can be found on the local machine.</li>
</ul>
<b>Step 1: Pre-Process</b>

<p>Sentinel 2 images are cropped within the area of interest and spectral bands are resampled to 10 meters spatial resolution. For Sentinel 1 images a geometric correction is neccesary using orbit file and terrain correction using a digital elevation model. Additionally, Sentinel 1 images get calibrated, filtered for speckles, converted to decibel units and cropped within the area of interest.</p>

![image](https://user-images.githubusercontent.com/23013328/162620202-17ff4828-fe37-4593-85ac-7d0ffcf74ed0.png)


The NDVI index for Sentinel 2 spectral channels is defined as follows:
  - NDVI∶=(NIR - RED)/(NIR + RED)
  - NDVI∶= (B8 - B4)/(B8 +  B4)

The mNDWI water index for Sentinel 2 spectral channels is defined as follows:
  - mNDWI∶= (Green - Middle Infrared)/(Green + Middle Infrared)
  - mNDWI∶= (B3 - B12)/(B3 + B12)

Sentinel 2
Read Products
Produce Classification Maps from Sentinel 2
-subset the product
- resample the product to 10m spatial resolution
- calculate the first principal component
- calculate the NDVI and mNDVI
- stack the pca , ndvi and mndvi into a single product
- implement Kmeans unsupervised classification
- Wite the classification map on the local disk

Sentinel 1
Read Products
Produce Classification Maps using Sentinel 1
- Apply orbit file
- Callibration
- Speckle Filtering
- Linear to dB
- Terrain Correction
- Subset
- Applying Kmeans
- Saving the product on local disk

- Align Classification Maps
- Create the Final Probability Map


# <h3> Validation </h3>
JRC (European Commission Joint Research Center) surface water dataset

<p>The European Commission's Joint Research Center initiated the development of a water database within the framework of the Copernicus Programme. The database covers the temporal distribution of water surfaces at a global scale for almost the entire last 4 decades, providing significant statistics on the extent and change of water bodies. The observations produced from Landsat imagery, supporting applications like water resources management, climate modeling and vital information for decision making. For every area of interest the user can download a set of geotiffs raster products covering six layers of information illustrated in the table below:</p>
<ol>
  <li>Occurrence: 
The Global Surface Water Occurrence shows where surface water occurred between 1984 and 2015 and provides information concerning overall water dynamics. This product captures both the intra and inter-annual variability and changes.</li>
  <li>Occurrence change intensity: The Global Surface Water Occurrence Change Intensity map provides information on where surface water occurrence increased, decreased or remained the same between 1984-1999 and 2000-2020. Both the direction of change and its intensity are documented.</li>
  <li>Seasonality: The Global Surface Water Seasonality map provides information concerning the intra-annual behaviour of water surfaces for a single year (2020) and shows permanent and seasonal water and the number of months water was present.</li>
  <li> Recurrence: The Global Surface Water Recurrence provides information concerning the inter-annual behaviour of water surfaces and captures the frequency with which water returns from year to year. </li>
  <li> Transitions: The Global Surface Water Transitions map provides information on the change in surface water seasonality between the first and last years (between 1984 and 2020) and captures changes between the three classes of not water, seasonal water and permanent water. </li>
  <li> Maximum water extent: The Global Surface Water Maximum Water Extent shows all the locations ever detected as water over a 35-year period (1984-2019).</li>
</ol>

# <h3> Acknowledgements </h3> 

<cite> [1]Serco Italia SPA (2020). Sentinel-1 processing using snappy (version 1.1). Retrieved from RUS
Lectures at https://rus-copernicus.eu/portal/the-rus-library/learn-by-yourself/ </cite>

<cite> [2] Copernicus Snap Software https://step.esa.int/main/download/snap-download/ </cite
