# An Analysis on the Weather Data in Oahu

## Overview of the analysis
The purpose of this analysis is to determine the sustainability of the surf and ice cream shop through-out the year by extracting and comparing the weather data in June and December.

## Results
![June_data](/Resources/June_data.png)
![Dec_data](/Resources/Dec_data.png)

 - The number of temperature data collected in was 1700 and 1517 in June and December respectively. 183 more data were collected in June.
 - The mean temperature in June was 74.9 degree and was 71.0 degree in December. The 50% quartile temperatures were 75 degree and 71 degree respectively. 
 - The standard deviation of temperature in June and December were 3.26 and 3.75 respectively.


## Summary
Since the mean and 50% quartile temperatures were both higher in June, the average temperature is higher for June than that for December. A lower standard deviation of temperature in June showed that the distribution of temperature is closer to the mean, so the temperature in June might fluctuate less than December.

Two additional queries to perform to gather more weather data for June and December:
 1) A query that filters the Measurement table to retrieve the Precipitation for the month of June.

	'''
	session.query(Measurement.date, Measurement.prcp).\
	filter(func.strftime("%m", Measurement.date) == June_str).all()
	'''

 2) A query that filters the Measurement table to retrieve the Precipitation for the month of June

	session.query(Measurement.date, Measurement.prcp).\
	filter(func.strftime("%m", Measurement.date) == Dec_str).all()
