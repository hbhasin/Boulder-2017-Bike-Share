# Boulder-2017-Bike-Share Data Exploration and Predictive Analytics

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/splash.PNG)

[Boulder B-cycle](https://Boulder.bcycle.com/) is a nonprofit organization formed by Boulder residents to create and operate Boulder’s bike-sharing program on a not-for-profit, financially sustainable basis. Its mission is to “implement and operate a community-supported bike-share program that provides Boulder’s residents, commuters and visitors with an environmentally friendly, financially sustainable, and affordable transportation option that’s ideal for short trips resulting in fewer vehicle miles traveled, less pollution and congestion, more personal mobility and better health and wellness.”

![](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/figures/Boulder%20Header.PNG)

Boulder B-cycle posts its trips data set on its website as soon as its annual report is released. Trips data have been available since 2010. The 2017 annual report and its associated dataset for this report were obtained from [Boulder B-Cycle website](https://boulder.bcycle.com/data-reports).

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Boulder%202017%20Annual%20Report.PNG)

This study will explore the publicly available 2017 Boulder B-cycle Trip Data and perform some predictive analytics on the number of bike checkouts using calendar, clock and weather variables as the predictors. The reporting style will follow the [Boulder 2016 B-cycle Ridership Data Exploration and Predictive Analytics](https://github.com/hbhasin/Boulder-2016-Bike-Share/blob/master/Boulder%202016%20Bike%20Share%20Data%20Exploration.md) study to provide continuity and similarity.


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

Removing “Maintenance” entries brought the number of rows down to 106,899. There were 1914 entries with a Trip Duration = 0. Removing these entries resulted in 104,985 rows.
Over 1.2% of the Boulder B-cycle rides (1284 rides) had the same checkout station as return station with a trip duration of only 1 minute (Figure 1). It is very likely that the majority of these “rides” are likely people checking out a bike, and then deciding after a very short time that this particular bike doesn’t work for them.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%201.PNG)

<p align="center">
FIGURE 1: TRIP DURATION WHEN CHECKOUT AND RETURN KIOSKS ARE THE SAME
</p>

Removing entries with a Trip Duration = 1 resulted in 103,578 rows with the following breakdown:

Membership Type | Number of Trips
--------------- | -------------
Annual (Republic Rider) | 64,842
24-hour (Day Tripper) | 22,466
Monthly (People’s Pedaler) | 14,032
Pay-per-trip (Casual Cruiser) | 2,232
7-day | 6
**Total Trips** | **103,578**

This number appeared closer to the 103,568 trips reported by Boulder B-cycle although there were differences amongst the individual membership types.

There were 296 rows in the Trips dataset that had “Maintenance” entry in the Return Kiosk column. These 296 rows were removed accordingly.

Removing the 1,343 rows with a trip duration of 1 minute and 193 rows with invalid kiosk names resulted in **103,282 Boulder B-cycle rides in 2017**.

Membership Type | Number of Trips
--------------- | -------------
Annual (Republic Rider) | 64,646
24-hour (Day Tripper) | 22,409
Monthly (People’s Pedaler) | 13,996
Pay-per-trip (Casual Cruiser) | 2,225
7-day | 6
**Total Trips** | **103,282**

## Distance Traveled
To estimate the distance between checkout and return kiosks when they are the same, Tyler’s method of using the “average speed of all the other rides (nominal distance ridden divided by the duration), and then applying this average speed to the same-kiosk trip durations” was adopted. This resulted in 158,140 miles ridden in 2017 and sharply contrasted with the 242,004 miles reported by [2017 Boulder B-cycle](https://cdn01.bcycle.com/libraries/docs/librariesprovider35/default-document-library/2017-annual-report-final_web.pdf?sfvrsn=996021c5_2). 

### Most Popular and Least Popular Checkout and Return Kiosks 
### Most Popular 
The following ten kiosks were the most popular checkout kiosks by number of total bike checkouts in 2017.

Checkout Kiosk | Number of Checkouts
-------------- | -------------------
Folsom & Colorado | 4885
15th & Pearl | 4709
28th & Mapleton | 4069
Broadway & Euclid | 3854
21st & Arapahoe | 3462
13th & Spruce | 3447
Folsom & Pearl | 3416
11th & Pearl | 3348
19th @ Boulder Creek | 3185
13th & Arapahoe | 3143

The most popular Checkout Kiosk to Return Kiosk routes were as follows:

Checkout Kiosk | Return Kiosk | Number of Trips
-------------- | ------------ | ---------------
26th @ Pearl | 28th & Mapleton | 884
28th & Mapleton | 26th @ Pearl | 883
Folsom & Pearl | 15th & Pearl | 610
13th & Arapahoe | 13th & Arapahoe | 525
Settlers' Park | 11th & Pearl | 473
38th & Arapahoe | 48th & Arapahoe | 452
21st & Arapahoe | 21st & Arapahoe | 451
15th & Pearl | Folsom & Pearl | 432
15th & Pearl | 28th & Mapleton | 413
Broadway & Baseline | Williams Village | 412

The following ten kiosks were the most popular return kiosks by number of total bike checkouts in 2017.

Return Kiosk | Number of Returns
------------ | -------------------
15th & Pearl | 4692
28th & Mapleton | 4282
13th & Spruce | 4057
21st & Arapahoe | 3943
13th & Arapahoe | 3708
Folsom & Pearl | 3491
11th & Pearl | 3464
48th & Arapahoe | 3356
The Village | 3220
Twenty Ninth Street North | 3156


### Least Popular 
The following ten kiosks were the least popular checkout kiosks by number of total bike checkouts in 2017.

Checkout Kiosk | Number of Checkouts
-------------- | -------------------
UCAR Center Green | 1379
13th & College | 1317
Boulder Junction | 1251
North Boulder Recreation Center | 1012
Pearl Place | 1006
30th & Diagonal Highway | 938
Broadway & Iris | 873
Table Mesa Park-n-Ride | 506
27th Way & Broadway | 257
Gunbarrel North | 160

The following ten kiosks were the least popular return kiosks by number of total bike returns in 2017.

Return Kiosk | Number of Returns
------------ | -------------------
Broadway & University | 1210
Boulder Junction | 1146
Pearl Place | 1132
North Boulder Recreation Center | 953
13th & College | 922
30th & Diagonal Highway | 880
Broadway & Iris | 756
Table Mesa Park-n-Ride | 475
27th Way & Broadway | 257
Gunbarrel North | 166


## Map of Station Popularity
### Checkout Kiosks 

The use of Tableau aided in the creation of the following map showing the popularity of the various Checkout Kiosks (Figure 2). The size of the circle is proportional to the number of checkouts from that kiosk in 2017. 

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%202.PNG)

<p align="center">
FIGURE 2: CHECKOUT KIOSK LOCATIONS AND NUMBER OF CHECKOUTS IN 2017
</p>

### Return Kiosks 
Similarly, the use of Tableau aided in the creation of the following map showing the popularity of the various Return Kiosks (Figure 3). The size of the circle corresponds to the number of checkouts returned to that kiosk in 2017.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%203.PNG)

<p align="center">
FIGURE 3: RETURN KIOSK LOCATIONS AND NUMBER OF RETURNS IN 2017
</p>


## Checkouts per Membership Type 
With the revisions made earlier to the membership type entries, the figure below shows the breakdown:

Membership Type | Number of Checkouts
--------------- | -------------------
Annual (Republic Rider) | 64,646
24-hour (Day Tripper) | 22,409
Monthly (People’s Pedaler) | 13,996
Pay-per-trip (Casual Cruiser) | 2,225
7-day | 6




![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%204.PNG)


<p align="center">
FIGURE 4: NUMBER OF CHECKOUTS BY MEMBERSHIP TYPE IN 2017
</p>



## Ridership by Calendar and Clock Variables 
### Ridership by Hour 
Bike checkout time is probably the most important attribute in the Trips dataset. Each checkout time was converted into its integer hour. For example, 7:02 AM or 7:59 AM would be converted to an integer of 7. In this way, total number of checkouts could be aggregated for the year and plotted against their hours of the day, as shown in Figure 5.

It appears that the highest number of checkouts occurred between 4 PM and 5 PM with ridership increasing steadily from 6 AM. Number of checkouts started to decrease after 6 PM.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%205.PNG)


<p align="center">
FIGURE 5: NUMBER OF CHECKOUTS BY HOUR IN 2017
</p>



Figure 6 shows the average distance ridden by the hour of the day in 2017. Interestingly, more distance was covered during the very early hours of the morning (2 AM to 3 AM) period. The typical distance ridden ranged from 1.4 miles to 1.6 miles from 4 AM to 12 midnight.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%206.PNG)

<p align="center">
FIGURE 6: ESTIMATED AVERAGE MILES RIDDEN BY HOUR OF CHECKOUT IN 2017
</p>


## Ridership by Hour and Weekday 
Figure 7 shows that weekday ridership patterns are similar. On the other hand weekend ridership demonstrate a busy afternoon (between 12 PM and 3 PM)

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%207.PNG)

<p align="center">
FIGURE 7: CHECKOUTS BY HOUR OF DAY PER WEEKDAY IN 2017
</p>

## Ridership by Month 
Monthly checkouts, as shown in Figure 8, suggest high ridership during the summer months and low ridership during the winter months.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%208.PNG)

<p align="center">
FIGURE 8: TOTAL CHECKOUTS BY MONTH IN 2017
</p>

## Merging with Weather 

It is highly likely that weather plays a very important role in bike ridership and bike checkout times. This was shown in the previous plots on total checkouts per hour of the day, by weekday, and by month. To verify this, weather data obtained from [Dark Sky API](https://darksky.net/dev/) was merged with the Trips dataset and several graphs plotted to visualize the relationships.

### Checkouts vs. Daily Temperature 

Figure 9 shows the total number of checkouts against maximum and minimum daily temperature. It clearly suggests that ridership increased as the temperature increased and vice-versa.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%209.PNG)

<p align="center">
FIGURE 9: TOTAL CHECKOUTS BY DAILY TEMPERATURE IN 2017
</p>

Apparent temperature, as defined by Dark Sky, is “apparent (or “feels like”) temperature in degrees Fahrenheit”. It appeared to have a subtle effect on bike ridership as shown in Figure 10.


![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2010.PNG)

<p align="center">
FIGURE 10: TOTAL CHECKOUTS BY DAILY APPARENT TEMPERATURE IN 2017
</p>


## Checkouts vs. Daily Cloud Cover 
Dark Sky defines Cloud Cover as “the percentage of sky occluded by clouds, between 0 and 1, inclusive”. Figure 11 shows the total number of checkouts against daily cloud cover. It clearly suggests that ridership was highest as the cloud cover stayed at around 0.08.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2011.PNG)

<p align="center">
FIGURE 11: TOTAL CHECKOUTS BY DAILY CLOUD COVER IN 2017
</p>

## Checkouts vs. Daily Wind Speed 
Wind speed is reported in miles per hour. As shown in Figure 12, ridership did not seem to be somewhat impacted by higher wind speeds. 

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2012.PNG)

<p align="center">
FIGURE 12: TOTAL CHECKOUTS BY DAILY WIND SPEED IN 2017
</p>

## Checkouts vs. Daily Humidity 
Humidity is defined by Dark Sky as “relative humidity, between 0 and 1. Figure 13 shows decreased ridership at higher humidity levels.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2013.PNG)

<p align="center">
FIGURE 13: TOTAL CHECKOUTS BY DAILY HUMIDITY IN 2017	
</p>

## Checkouts vs. Daily Visibility 
Visibility is measured in miles and capped at 10 miles, according to Dark Sky. As Figure 14 shows, ridership peaked when visibility was at 10 miles.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2014.PNG)

<p align="center">
FIGURE 14: TOTAL CHECKOUTS BY DAILY VISIBILITY IN 2017
</p>

## Days with Highest/Lowest Ridership
Another interesting data discovery was the fact that Saturdays and Sundays had the highest and lowest ridership depending upon the weather. This may be due to “‘weekend warriors’ who rent B-cycles for pleasure and are highly affected by the weather in their decision to ride”.

### Highest Ridership

Checkout Week Day | Date of Checkout | Max Temperature | Min Temperature | Number of Checkouts
----------------- | ------------------- | --------------- | --------------- | -------------------
Sunday | 2017-09-04 | 84.980 | 55.150 | 740
Wednesday | 2017-07-27 | 80.480 | 58.020 | 574
Friday | 2017-08-05 | 77.420 | 55.600 | 568
Friday | 2017-06-24 | 69.690 | 46.940 | 560
Thursday | 2017-06-09 | 86.380 | 54.750 | 558
Tjursday | 2017-09-08 | 78.070 | 50.720 | 552
Tuesday | 2017-06-28 | 81.830 | 54.370 | 540
Thursday | 2017-07-14 | 81.440 | 55.990 | 535
Thursday | 2017-08-11 | 73.080 | 52.170 | 526
Sunday | 2017-07-24 | 89.520 | 60.770 | 511


### Lowest Ridership

Checkout Week Day | Date of Checkout | Max Temperature | Min Temperature | Number of Checkouts
----------------- | ------------------- | --------------- | --------------- | -------------------
Tuesday | 2017-01-04 | 14.590 | 5.180 | 35
Thursday | 2017-01-06 | 20.380 | -9.100 | 31
Saturday | 2017-12-24 | 26.020 | 2.390 | 29
Wednesday | 2017-12-21 | 36.420 | 10.920 | 29
Friday | 2017-01-07 | 23.870 | 2.520 | 25
Sunday | 2017-01-16 | 35.170 | 28.520 | 24
Saturday | 2017-12-31 | 25.020 | 12.470 | 19
Monday | 2017-12-26 | 15.040 | 9.420 | 18
Sunday | 2017-12-25 | 24.000 | 11.420 | 14
Wednesday | 2017-01-05 | 6.110 | -1.190 | 4


## Checkouts vs. Hourly Weather Variables
Hourly weather conditions provide better resolution than daily weather conditions. To investigate this, number of checkouts against hourly weather variables were also plotted and compared with the plots using daily weather variables.

### Checkouts vs. Hourly Temperature
The scatter plots in Figure 15 and 16 show that the relationship between the number of checkouts and the hourly temperatures were not linear.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2015.PNG)

<p align="center">
FIGURE 15: TOTAL CHECKOUTS BY HOURLY TEMPERATURE IN 2017
</p>

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2016.PNG)

<p align="center">
FIGURE 16: TOTAL CHECKOUTS BY HOURLY APPARENT TEMPERATURE IN 2017
</p>

### Checkouts vs. Hourly Humidity
Figure 17 shows that humidity affected ridership significantly.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2017.PNG)

<p align="center">
FIGURE 17: TOTAL CHECKOUTS BY HOURLY HUMIDITY IN 2017
</p>

### Checkouts vs. Hourly Cloud Cover
As shown in Figure 18 Cloud Cover certainly impacted ridership.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2018.PNG)

<p align="center">
FIGURE 18: TOTAL CHECKOUTS BY HOURLY CLOUD COVER IN 2017	
</p>

### Checkouts vs. Hourly Wind Speed
Data on wind speed indicated it was clustered heavily in 0 to 8 miles per hour range, as shown in Figure 19.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2019.PNG)

<p align="center">
FIGURE 19: TOTAL CHECKOUTS BY HOURLY WIND SPEED IN 2017
</p>

### Checkouts vs. Hourly Visibility
As shown in Figure 20 visibility at 10 miles had the greatest impact on ridership.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2020.PNG)

<p align="center">
FIGURE 20: TOTAL CHECKOUTS BY HOURLY VISIBILITY IN 2017
</p>

# Part 2: Regression Modeling 

In this section various linear and non-linear regression models were used to test and train the Trips data that was merged with the weather data to try to predict the number of checkouts based on calendar, clock and weather conditions.

The following regression models with their brief explanation were used in this study:
	
* Linear Regression
  * Most widely used statistical and machine learning technique to model relationship between two sets of variables typically using a straight line. Simple to use and fast performance but lacks high accuracy when compared to non-linear models.
	
* Lasso Regression
  * A type of linear regression that uses shrinkage to reduce data values toward the mean. Well suited for automating feature selection.

* Ridge Regression
  * Well suited for data that suffers from multicollinearity, i.e. features with high correlation.

* Bayesian Ridge Regression
  * An approach to linear regression in which the statistical analysis is undertaken using Bayesian inference.

* Decision Tree Regression
  * Uses a tree like structure to derive a final decision on the outcome of the analysis.

* Random Forest Regression
  * An ensemble learning method that operates by constructing a multitude of decision trees to arrive at the mean prediction.

* Extra Trees Regression
  * An extremely randomized tree regressor. Builds a totally random decision tree.

* Nearest Neighbors Regression
  * A simple algorithm that uses a similarity measure (e.g. distance between neighbors) to predict the outcome.

## Regression Modeling with Categorical Feature Set
The Checkout Month, Week Day and Hour numeric variables were converted to categorical features resulting in 44 total features for regression modeling.

Prior to applying the models a feature correlation was performed on all the features to see if any of the features were highly correlated to one another. As shown in Figure 21, Temperature and Apparent Temperature were highly correlated suggesting that one of them could be removed from the features in the model application.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2021.PNG)

<p align="center">
FIGURE 21: FEATURE CORRELATION
</p>

The models used for regression supported the use of several parameters that could be used to adjust or tune them for better performance. In most cases in this study, the parameters were set to default.

The dataset was randomly spilt into 70% for training and 30% for testing. For each model the training and test scores, R Squared and RMSE results were collected and summarized. In addition, the Decision Tree, Random Forest and Extra Trees models also had their Feature Importance bar charts plotted. The chart for Extra Tree model is shown in Figure 22.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2022.PNG)

<p align="center">
FIGURE 22: EXTRA TREES REGRESSION MODEL FEATURE IMPORTANCE CHART
</p>


## Regression Modeling Summary – Categorical Feature Set

Metric | Linear | Lasso | Ridge | Bayesian Ridge | Decision Tree | Random Forest | Extra Trees | Nearest Neighbors
------ | ------ | ----- | ----- | -------------- | ------------- | ------------- | ----------- | -----------------
Training Test Score | 0.702 | 0.699 | 0.699 | 0.702 | 1.000 | 0.948 | 1.000 | 0.590
Test Set Score | 0.703 | 0.699 | 0.699 | 0.702 | 0.541 | 0.732 | 0.752 | 0.499
R Squared | 0.838215 | 0.836334 | 0.836334 | 0.838118 | 0.735793 | 0.855677 | 0.867256 | 0.706641
RMSE | 48.413736 | 48.926522 | 48.926522 | 48.440353 | 74.658154 | 43.598737 | 40.350959 | 81.503647

The Extra Trees regression model achieved the highest accuracy and the lowest RMSE. The Decision Tree model had lowest accuracy and the highest RMSE.

## Regression Modeling with Numerical Feature Set

Using Checkout Month, Week Day and Hour numeric variables resulted in just 9 total features for regression modeling.

Prior to applying the models a feature correlation was performed on all the features to see if any of the features were highly correlated to one another. As shown in Figure 23, Temperature and Apparent Temperature were highly correlated suggesting that one of them could be removed from the features in the model application.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2023.PNG)

<p align="center">
FIGURE 23: FEATURE CORRELATION
</p>

For each model the training and test scores, R Squared and RMSE results were collected and summarized. In addition, the Decision Tree, Random Forest and Extra Trees models also had their Feature Importance bar charts plotted. The chart for Random Forest and the Extra Trees models are shown in Figures 24 and 25, respectively.

![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2024.PNG)

7<p align="center">
FIGURE 24: RANDOM FOREST REGRESSION MODEL FEATURE IMPORTANCE CHART
</p>


![](https://github.com/hbhasin/Boulder-2017-Bike-Share/blob/master/figures/Figure%2025.PNG)

<p align="center">
FIGURE 25: EXTRA TREES REGRESSION MODEL FEATURE IMPORTANCE CHART
</p>

## Regression Modeling Summary – Numerical Feature Set

Metric | Linear | Lasso | Ridge | Bayesian Ridge | Decision Tree | Random Forest | Extra Trees | Nearest Neighbors
------ | ------ | ----- | ----- | -------------- | ------------- | ------------- | ----------- | -----------------
Training Test Score | 0.441 | 0.435 | 0.435 | 0.441 | 1.000 | 0.958 | 1.000 | 0.884
Test Set Score | 0.451 | 0.448 | 0.448 | 0.451 | 0.531 | 0.759 | 0.769 | 0.641
R Squared | 0.671243 | 0.669656 | 0.669656 | 0.671447 | 0.728553 | 0.871173 | 0.876915 | 0.800871
RMSE | 87.618427 | 87.957784 | 87.957784 | 87.574861 | 74.825290 | 38.441564 | 36.841010 | 57.187221


### Regression Modeling Summary
* The data exploration phase of this study revealed the significance of weather variables on the ridership. The regression modeling phase confirmed this to be accurate. Looking at the feature importance graphs generated by the Extra Trees and Random Forest models, the weather attributes rank the highest.
* The non-linear regression models performed better than the linear models. In particular, even with a reduced feature set, the non-linear models such as the Extra Trees and the Random Forest were the best performers with R Squared values well above 0.87.

## Testing Regressor on unseen samples
The Extra Trees Forest Regressor with a predictive accuracy of 87.7% was used to predict 20 samples (with numerical feature set) from the dataset that had not been used neither in the training nor in the test sets. The results are tabulated below. The regressor predicted all 20 of the 20 samples accurately. 

Sample Number | Actual Number of Checkouts | Predicted Number of Checkouts | +/-
------------- | -------------------------- | ----------------------------- | ---
1 | 4 | 4 | 0
2 | 18 | 18 | 0
3 | 2 | 2 | 0
4 | 15 | 15 | 0
5 | 54 | 54 | 0
6 | 18 | 18 | 0
7 | 17 | 17 | 0
8 | 6 | 6 | 0
9 | 3 | 3 | 0
10 | 10 | 10 | 0
11 | 29 | 29 | 0
12 | 8 | 8 | 0
13 | 16 | 16 | 0
14 | 15 | 15 | 0
15 | 19 | 19 | 0
16 | 27 | 27 | 0
17 | 34 | 34 | 0
18 | 47 | 47 | 0
19 | 35 | 35 | 0
20 | 9 | 9 | 0

# Summary

This study covered two areas:

1. Explored the Boulder Trips dataset and visualized the data and provided useful and interesting information.
2. Deployed a variety of supervised machine learning regression models to predict the number of checkouts using calendar, clock and weather attributes.
