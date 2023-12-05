# exercise 01

"""
Dealing with missing data

It is important to deal with missing data before starting your analysis.

One approach is to drop missing values if they account for a small proportion, typically five percent, of your data.

Working with a dataset on plane ticket prices, stored as a pandas DataFrame called planes, 
you'll need to count the number of missing values across all columns, 
calculate five percent of all values, use this threshold to remove observations, 
and check how many missing values remain in the dataset.
"""

# steps

"""
Print the number of missing values in each column of the DataFrame.
---
Calculate how many observations five percent of the planes DataFrame is equal to.
---
Create cols_to_drop by applying boolean indexing to columns of the DataFrame 
with missing values less than or equal to the threshold.
Use this filter to remove missing values and save the updated DataFrame.
"""

# solution

# Count the number of missing values in each column
print(planes.isna().sum())

#----------------------------------#

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

#----------------------------------#

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

#----------------------------------#

# exercise 02

"""
Strategies for remaining missing data

The five percent rule has worked nicely for your planes dataset, eliminating missing values from nine out of 11 columns!

Now, you need to decide what to do with the "Additional_Info" and "Price" columns, 
which are missing 300 and 368 values respectively.

You'll first take a look at what "Additional_Info" contains, then visualize the price of plane tickets by different airlines.

The following imports have been made for you:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""

# steps

"""
Print the values and frequencies of "Additional_Info".
---
Create a boxplot of "Price" by "Airline".
---
Question

    How should you deal with the missing values in "Additional_Info" and "Price"?

Possible Answers

    Remove the "Additional_Info" column and impute the mean for missing values of "Price".
    Remove "No info" values from "Additional_Info" and impute the median for missing values of "Price".
    Remove the "Additional_Info" column and impute the mean by "Airline" for missing values of "Price".
    Remove the "Additional_Info" column and impute the median by "Airline" for missing values of "Price". (Answer)
"""

# solution

# Check the values of the Additional_Info column
print(planes['Additional_Info'].value_counts())

#----------------------------------#

# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airline
sns.boxplot(data=planes, x='Airline', y='Price')

plt.show()

#----------------------------------#

# exercise 03

"""
Imputing missing plane prices

Now there's just one column with missing values left!

You've removed the "Additional_Info" column from planes—the last step 
is to impute the missing data in the "Price" column of the dataset.

As a reminder, you generated this boxplot, 
which suggested that imputing the median price based on the "Airline" is a solid approach!
"""

# steps

"""
Group planes by airline and calculate the median price.
---
Convert the grouped median prices to a dictionary.
---
Conditionally impute missing values for "Price" by mapping values in the "Airline column" based on prices_dict.
Check for remaining missing values.
"""

# solution

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

#----------------------------------#

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

#----------------------------------#

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(airline_prices))

# Check for missing values
print(planes.isna().sum())

#----------------------------------#

# exercise 04

"""
Finding the number of unique values

You would like to practice some of the categorical data manipulation and analysis skills that you've just seen. 
To help identify which data could be reformatted to extract value, 
you are going to find out which non-numeric columns in the planes dataset have a large number of unique values.

pandas has been imported for you as pd, and the dataset has been stored as planes.
"""

# steps

"""
Filter planes for columns that are of "object" data type.
Loop through the columns in the dataset.
Add the column iterator to the print statement, then call the function to return the number of unique values in the column.
"""

# solution

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for n in non_numeric.columns:
  
  # Print the number of unique values
  print(f"Number of unique values in {n} column: ", non_numeric[n].nunique())

#----------------------------------#

# exercise 05

"""
Flight duration categories

As you saw, there are 362 unique values in the "Duration" column of planes. 
Calling planes["Duration"].head(), we see the following values:

0        19h
1     5h 25m
2     4h 45m
3     2h 25m
4    15h 30m
Name: Duration, dtype: object

Looks like this won't be simple to convert to numbers. 
However, you could categorize flights by duration and examine the frequency of different flight lengths!

You'll create a "Duration_Category" column in the planes DataFrame. 
Before you can do this you'll need to create a list of the values you would like to insert into the DataFrame, 
followed by the existing values that these should be created from.
"""

# steps

"""
Create a list of categories containing "Short-haul", "Medium", and "Long-haul".
---

    Create short_flights, a string to capture values of "0h", "1h", "2h", "3h", or "4h".
    Create medium_flights to capture any values between five and nine hours.
    Create long_flights to capture any values from 10 hours to 16 hours inclusive.

"""

# solution

# Create a list of categories
flight_categories = ['Short-haul', 'Medium', 'Long-haul']

#----------------------------------#

# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short-haul values
short_flights = "0h|1h|2h|3h|4h"

# Create medium-haul values
medium_flights = "5h|6h|7h|8h|9h"

# Create long-haul values
long_flights = "10h|11h|12h|13h|14h|15h|16h"

#----------------------------------#    

# exercise 06

"""
Adding duration categories

Now that you've set up the categories and values you want to capture, 
it's time to build a new column to analyze the frequency of flights by duration!

The variables flight_categories, short_flights, medium_flights, and long_flights that you previously created are available to you.

Additionally, the following packages have been imported: pandas as pd, numpy as np, seaborn as sns, and matplotlib.pyplot as plt.
"""

# steps

"""
Create conditions, a list containing subsets of planes["Duration"] based on short_flights, medium_flights, and long_flights.
Create the "Duration_Category" column by calling a function that accepts your conditions list and flight_categories, setting values not found to "Extreme duration".
Create a plot showing the count of each category.
"""

# solution

# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()

#----------------------------------#

# exercise 07

"""
Flight duration

You would like to analyze the duration of flights, but unfortunately, 
the "Duration" column in the planes DataFrame currently contains string values.

You'll need to clean the column and convert it to the correct data type for analysis.
"""

# steps

"""
Print the first five values of the "Duration" column.
---
Remove "h" from the column.
---
Convert the column to float data type.
---
Plot a histogram of "Duration" values.
"""

# solution

# Preview the column
print(planes['Duration'].head())

#----------------------------------#

# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes['Duration'].str.replace('h','')

#----------------------------------#

# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)

#----------------------------------#

# Preview the column
print(planes["Duration"].head())

# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")

# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)

# Plot a histogram
sns.histplot(data = planes, x = 'Duration')
plt.show()

#----------------------------------#

# exercise 08

"""
Adding descriptive statistics

Now "Duration" and "Price" both contain numeric values in the planes DataFrame, 
you would like to calculate summary statistics for them that are conditional on values in other columns.
"""

# steps

"""
Add a column to planes containing the standard deviation of "Price" based on "Airline".
---
Calculate the median for "Duration" by "Airline", storing it as a column called "airline_median_duration".
---
Find the mean "Price" by "Destination", saving it as a column called "price_destination_mean".
"""

# solution

# Price standard deviation by Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())

print(planes[["Airline", "airline_price_st_dev"]].value_counts())

#----------------------------------#

# Median Duration by Airline
planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())

print(planes[["Airline","airline_median_duration"]].value_counts())

#----------------------------------#

# Mean Price by Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())

print(planes[["Destination","price_destination_mean"]].value_counts())

#----------------------------------#

# exercise 09

"""
Identifying outliers

You've proven that you recognize what to do when presented with outliers, but can you identify them using visualizations?

Try to figure out if there are outliers in the "Price" or "Duration" columns of the planes DataFrame.

matplotlib.pyplot and seaborn have been imported for you as plt and sns respectively.
"""

# steps

"""
Plot the distribution of "Price" column from planes.
---
Display the descriptive statistics for flight duration.
"""

# solution

# Plot a histogram of flight prices
sns.histplot(data = planes, x = 'Price')
plt.show()

#----------------------------------#

# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())

#----------------------------------#

# exercise 10

"""
Removing outliers

While removing outliers isn't always the way to go, for your analysis, 
you've decided that you will only include flights where the "Price" is not an outlier.

Therefore, you need to find the upper threshold and then use it to remove values above this from the planes DataFrame.

pandas has been imported for you as pd, along with seaborn as sns.
"""

# steps

"""
Find the 75th and 25th percentiles, saving as price_seventy_fifth and price_twenty_fifth respectively.
---
Calculate the IQR, storing it as prices_iqr.
---
Calculate the upper and lower outlier thresholds.
---
Remove the outliers from planes.
"""

# solution

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

#----------------------------------#

# Find the 75th and 25th percentiles
price_upper_perc = planes["Price"].quantile(0.75)
price_lower_perc = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_upper_perc - price_lower_perc

#----------------------------------#

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

#----------------------------------#

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(planes["Price"].describe())

#----------------------------------#