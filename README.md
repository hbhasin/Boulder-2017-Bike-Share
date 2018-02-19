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


### Basic Ridership Statistics 
#### Number of Rides 
The B-cycle data, as downloaded, contained 122,331 rows of trips data. Under normal circumstances this would mean that 122,331 B-cycle trips were taken in 2017. However, the [2017 Boulder B-cycle annual report](https://cdn01.bcycle.com/libraries/docs/librariesprovider35/default-document-library/2017-annual-report-final_web.pdf?sfvrsn=996021c5_2) acknowledged 103,568 total trips for the year. The breakdown, totaling 101,146 trips, was as follows:

Membership Type | Number of Trips
--------------- | -------------
Annual (Republic Rider) | 63,262
24-hour (Day Tripper) | 21,900
Monthly (People’s Pedaler) | 13,817
Pay-per-trip (Casual Cruiser) | 2,167
**Total Trips**	 | **101,146**

The Trips dataset reported 39 rows with NaN (Not A Number) entries. Removal of these 39 rows resulted in 122,292 rows with the following breakdown:

Membership Type | Number of Trips
--------------- | -------------
Annual (Republic Rider) | 67,092
24-hour (Day Tripper) | 23,082
Maintenance | 15,393
Monthly | 14,426
Pay-per-trip | 2,293
7-day | 6
**Total Trips** | **122,292**

Removing “Maintenance” entries brought the number of rows down to 106,899. Removing entries with a Trip Duration = 0 resulted in 104,985 rows.
Over 1.4% of the Boulder B-cycle rides (1284 rides) had the same checkout station as return station with a trip duration of only 1 minute (Figure 1). These trips were removed from Again, Tyler’s explanation of why these trips should be removed from the dataset makes sense - “I believe these should be filtered out because I believe the majority of these “rides” are likely people checking out a bike, and then deciding after a very short time that this particular bike doesn’t work for them. I believe that most of the same-kiosk rides under 5 minutes or so likely shouldn’t count, but only culled the ones that were one minute long”.

![](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/figures/Figure%201.PNG)

<p align="center">
FIGURE 1: TRIP DURATION WHEN CHECKOUT AND RETURN KIOSKS ARE THE SAME
</p>
