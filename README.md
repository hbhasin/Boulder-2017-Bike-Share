# Boulder 2017 B-cycle Ridership Data Exploration and Predictive Analysis

## Project Summary
This study explores the Boulder 2017 Bike Share Trips dataset and follows up with regression analytics deploying several popular machine learning algorithms.

## Project Files
The following project files are located in this project directory:

[README.md](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/README.md) -- This document, with project description.

[Boulder 2017 Bike Share Data Exploration and Predictive Analysis](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_2017_Bike_share_Data_Exploration_and_Predictive_Analysis.md) - Final Report.

[Boulder 2017 Excel to CSV File Conversion](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_2017_Excel_to_CSV_File_Conversion.ipynb) -- Converts the Trips dataset Excel spreadsheet from a 8MB file size to a reasonable 1.8MB compressed file.

[Boulder 2017 Bike Share Distance Duration Submit](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_2017_Bike_Share_Distance_Duration_Submit.py) - Python 3.6 script to retrieve distances between checkout and return kiosks from [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/).

[Boulder 2017 Daily Weather Forecast](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_2017_Daily_Weather_Forecast.py) - Python 2.7 script used to retrieve daily weather attributes from [Dark Sky API](https://darksky.net/dev/).

[Boulder 2017 Hourly Weather Forecast](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_Hourly_Weather_Forecast.py) - Python 2.7 script used to retrieve hourly weather attributes from [Dark Sky API](https://darksky.net/dev/).

[Boulder 2017 Bike Share Weather Data Consolidation](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/Boulder_2017_Bike_Share_Weather_Data_Consolidation.ipynb) - Merges the daily and hourly weather attributes from [Dark Sky API](https://darksky.net/dev/) into the Trips dataset.

[Boulder 2017 Bike Share Data Exploration](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/Boulder%202016%20Bike%20Share%20Data%20Exploration.ipynb) - Jupyter notebook containing Python code used to explore and visualize the information contained in the Boulder 2017 Trips dataset. 

[Boulder 2017 Bike Share Regression Modeling](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/Boulder%202016%20Bike%20Share%20Regression%20Modeling.ipynb) - Jupyter notebook containing Python code used to deploy a variety of regression models to train and test the Trips dataset followed by a predcition on 20 unseen samples. The regression models include Linear, Lasso, Ridge, Bayesian Ridge, Decision Tree, Random Forest, Extra Trees and Nearest Neighbors. 

[./data](https://github.com/hbhasin/Boulder-2017-Bike-Share/tree/master/data) - Folder containing data files used in the Python scripts and in the notebooks.

[./figures](https://github.com/hbhasin/Boulder-2017-Bike-Share/tree/master/figures) - Folder containing figures used in the Python notebooks.


## Data Sources
[Boulder B-cycle](https://boulder.bcycle.com/) - The Trips dataset was retrieved from [Data and Reports](https://boulder.bcycle.com/data-reports).

Distances between Checkout and Return Kiosks: Distances were retrieved from [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/) using Python 3.6 script.

Weather Data: Retrieved from [Dark Sky API](https://darksky.net/dev/) using Python 2.7 scripts.

Geo-spatial Mapping: [Tableau](https://public.tableau.com/) was used to map the number of bike checkouts and returns by kiosks.

## Analysis Software
All data analyses were done in Python and with publicly available libraries using Jupyter Notebook and IDLE except for the geo-spatial mapping of the number of bike checkouts and returns by kiosks which was done using Tableau.
