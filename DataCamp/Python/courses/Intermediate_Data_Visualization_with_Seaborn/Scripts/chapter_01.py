# exercise 01

"""
Reading a csv file

Before you analyze data, you will need to read the data into a pandas DataFrame. 
In this exercise, you will be looking at data from US School Improvement Grants in 2010. 
This program gave nearly $4B to schools to help them renovate or improve their programs.

This first step in most data analysis is to import pandas and seaborn and read a data file in order to analyze it further.

This course introduces a lot of new concepts, so if you ever need a quick refresher, 
download the Seaborn Cheat Sheet and keep it handy!
"""

# steps

"""
Import pandas and seaborn using the standard naming conventions.
The path to the csv file is stored in the grant_file variable.
Use pandas to read the file.
Store the resulting DataFrame in the variable df.
"""

# solution

# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv(grant_file)

#----------------------------------#

# exercise 02

"""
Comparing a histogram and displot

The pandas library supports simple plotting of data, 
which is very convenient when data is already likely to be in a pandas DataFrame.

Seaborn generally does more statistical analysis on data and can provide more sophisticated insight into the data. 
In this exercise, we will compare a pandas histogram vs the seaborn displot.
"""

# steps

"""
Use the pandas' plot.hist() function to plot a histogram of the Award_Amount column.
---
Use Seaborn's displot() function to plot a distribution plot of the same column.
"""

# solution

# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

#----------------------------------#

# Display a Seaborn displot
sns.displot(df['Award_Amount'])
plt.show()

# Clear the displot
plt.clf()

#----------------------------------#

# exercise 03

"""
Plot a histogram

The displot() function will return a histogram by default. 
The displot() can also create a KDE or rug plot which are useful ways to look at the data. 
Seaborn can also combine these plots so you can perform more meaningful analysis.
"""

# steps

"""
Create a displot for the data.
Explicitly pass in the number 20 for the number of bins in the histogram.
Display the plot using plt.show().
"""

# solution

# Create a displot
sns.displot(df['Award_Amount'],
             bins=20)

# Display the plot
plt.show()

#----------------------------------#

# exercise 04

"""
Rug plot and kde shading

Now that you understand some function arguments for displot(), we can continue further refining the output. 
This process of creating a visualization and updating it in an incremental fashion is a useful and common approach to look at data
from multiple perspectives.

Seaborn excels at making this process simple.
"""

# steps

"""
Create a displot of the Award_Amount column in the df.
Configure it to show a shaded kde plot (using the kind and fill parameters).
Add a rug plot above the x axis (using the rug parameter).
Display the plot.
"""

# solution

# Create a displot of the Award Amount
sns.displot(df['Award_Amount'],
             kind='kde',
             rug=True,
             fill=True)

# Plot the results
plt.show()

#----------------------------------#

# exercise 05

"""
Create a regression plot

For this set of exercises, we will be looking at FiveThirtyEight's data on which US State has the worst drivers. 
The data set includes summary level information about fatal accidents as well as insurance premiums for each state as of 2010.

In this exercise, we will look at the difference between the regression plotting functions.
"""

# steps

"""
The data is available in the dataframe called df.
Create a regression plot using regplot() with "insurance_losses" on the x axis and "premiums" on the y axis.
---
Create a regression plot of "premiums" versus "insurance_losses" using lmplot().
Display the plot.
"""

# solution

# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data = df, x = 'insurance_losses', y = 'premiums')



# Display the plot
plt.show()

#----------------------------------#

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data = df, x = 'insurance_losses', y = 'premiums')



# Display the second plot
plt.show()

#----------------------------------#

# exercise 06

"""
Plotting multiple variables

Since we are using lmplot() now, we can look at the more complex interactions of data. 
This data set includes geographic information by state and area. 
It might be interesting to see if there is a difference in relationships based on the Region of the country.
"""

# steps

"""
Use lmplot() to look at the relationship between insurance_losses and premiums.
Plot a regression line for each Region of the country.
"""

# solution

# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()

#----------------------------------#

# exercise 07

"""
Facetting multiple regressions

lmplot() allows us to facet the data across multiple rows and columns. 
In the previous plot, the multiple lines were difficult to read in one plot. 
We can try creating multiple plots by Region to see if that is a more useful visualization.
"""

# steps

"""
Use lmplot() to look at the relationship between insurance_losses and premiums.
Create a plot for each Region of the country.
Display the plots across multiple rows.
"""

# solution

# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()

#----------------------------------#