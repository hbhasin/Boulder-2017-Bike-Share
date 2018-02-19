# Boulder-2017-Bike-Share

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/splash.PNG)

[Boulder B-cycle](https://Boulder.bcycle.com/) is a nonprofit organization formed by Boulder residents to create and operate Boulder’s bike-sharing program on a not-for-profit, financially sustainable basis. Its mission is to “implement and operate a community-supported bike-share program that provides Boulder’s residents, commuters and visitors with an environmentally friendly, financially sustainable, and affordable transportation option that’s ideal for short trips resulting in fewer vehicle miles traveled, less pollution and congestion, more personal mobility and better health and wellness.”

![](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/figures/Boulder%20Header.PNG)

Boulder B-cycle posts its trips data set on its website as soon as its annual report is released. Trips data have been available since 2010. The 2017 annual report and its associated dataset for this report were obtained from [Boulder B-Cycle website](https://boulder.bcycle.com/data-reports).

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Boulder%202017%20Annual%20Report.PNG)

This study will explore the publicly available 2016 Boulder B-cycle Trip Data and perform some predictive analytics on the number of bike checkouts using calendar, clock and weather variables as the predictors. The reporting style will follow the [Boulder 2016 B-cycle Ridership Data Exploration and Predictive Analytics](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/Boulder%202016%20Bike%20Share%20Data%20Exploration.md) study to provide continuity and similarity.


This study has two parts:
1.	Explore the Trips datasets and visualize the data to provide useful and interesting information.
2.	Deploy a variety of regression models to train and test the data followed by a prediction on 20 unseen samples.

# Part 1: Data Exploration

# Data Acquisition

Data for this study was downloaded from several sources and combined using the following steps:
1. Downloaded Boulder B-cycle May 2011-January 2018 Trip Data from [Boulder B-Cycle website](https://boulder.bcycle.com/data-reports).. The columns names were changed to comply with Python code best practices and only rows for 2017 were kept for this exercise.
2. Created a list of the 1892 combinations of the 44 checkout/return kiosks. Used [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/) to provide the bicycling distance and time between each checkout and return kiosk. Google only supports a maximum of 2500 requests a day, so it took two days to obtain this data.
3. Obtained daily and hourly weather data via [Dark Sky API](https://darksky.net/dev/) for all of 2017. Dark Sky supports up to 1000 requests per day.
