# exercise 01

"""
Setting the default style

For these exercises, we will be looking at fair market rent values calculated by the US Housing and Urban Development Department. 
This data is used to calculate guidelines for several federal programs. 
The actual values for rents vary greatly across the US. 
We can use this data to get some experience with configuring Seaborn plots.

All of the necessary imports for seaborn, pandas and matplotlib have been completed. 
The data is stored in the pandas DataFrame df.

By the way, if you haven't downloaded it already, check out the Seaborn Cheat Sheet. 
It includes an overview of the most important concepts, 
functions and methods and might come in handy if you ever need a quick refresher!
"""

# steps

"""
Plot a pandas histogram without adjusting the style.
Set Seaborn's default style.
Create another pandas histogram of the fmr_2 column which represents fair market rent for a 2-bedroom apartment.
"""

# solution

# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

#----------------------------------#

# exercise 02

"""
Comparing styles

Seaborn supports setting different styles that can control the aesthetics of the final plot. 
In this exercise, you will plot the same data in two different styles in order to see how the styles change the output.
"""

# steps

"""
Create a displot() of the fmr_2 column in df using a dark style. Use plt.clf() to clear the figure.
---
Create the same displot() of fmr_2 using a whitegrid style. Clear the plot after showing it.
"""

# solution

sns.set_style('dark')
sns.displot(data = df['fmr_2'], kind = 'hist')
plt.show()
plt.clf()

#----------------------------------#

sns.set_style('whitegrid')
sns.displot(data = df['fmr_2'], kind = 'hist')
plt.show()
plt.clf()

#----------------------------------#

# exercise 03

"""
Removing spines

In general, visualizations should minimize extraneous markings so that the data speaks for itself. 
Seaborn allows you to remove the lines on the top, bottom, left and right axis, which are often called spines.
"""

# steps

"""
Use a white style for the plot.
Create a lmplot() comparing the pop2010 and the fmr_2 columns.
Remove the top and right spines using despine().
"""

# solution

# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine(top=True, right=True)

# Show the plot and clear the figure
plt.show()
plt.clf()

#----------------------------------#

# exercise 04

"""
Matplotlib color codes

Seaborn offers several options for modifying the colors of your visualizations. 
The simplest approach is to explicitly state the color of the plot. 
A quick way to change colors is to use the standard matplotlib color codes.
"""

# steps

"""
Set the default Seaborn style and enable the matplotlib color codes.
Create a displot for the fmr_3 column using matplotlib's magenta (m) color code.
"""

# solution

# Set style, enable color code, and create a magenta displot
sns.set(color_codes=True)
sns.displot(df['fmr_3'], color='m')

# Show the plot
plt.show()

#----------------------------------#

# exercise 05

"""
Using default palettes

Seaborn includes several default palettes that can be easily applied to your plots. 
In this example, we will look at the impact of two different palettes on the same displot.
"""

# steps

"""
Create a for loop to show the difference between the bright and colorblind palette.
Set the palette using the set_palette() function.
Use a displot of the fmr_3 column.
"""

# solution

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.displot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()

#----------------------------------#

# exercise 06

"""
Creating Custom Palettes

Choosing a cohesive palette that works for your data can be time consuming. 
Fortunately, Seaborn provides the color_palette() function to create your own custom sequential, categorical, or diverging palettes.
Seaborn also makes it easy to view your palettes by using the palplot() function.

In this exercise, you can experiment with creating different palettes.
"""

# steps

"""
Create and display a Purples sequential palette containing 8 colors.
---
Create and display a palette with 10 colors using the husl system
---
Create and display a diverging palette with 6 colors coolwarm
"""

# solution

sns.palplot(sns.color_palette("Purples", 8))
sns.palplot(sns.color_palette())
plt.show()

#----------------------------------#

sns.palplot(sns.color_palette("husl", 10))
sns.palplot(sns.color_palette())
plt.show()

#----------------------------------#

sns.palplot(sns.color_palette("coolwarm", 6))
sns.palplot(sns.color_palette())
plt.show()

#----------------------------------#

# exercise 07

"""
Using matplotlib axes

Seaborn uses matplotlib as the underlying library for creating plots. 
Most of the time, you can use the Seaborn API to modify your visualizations but sometimes it is helpful to use matplotlib's 
functions to customize your plots. 
The most important object in this case is matplotlib's axes.

Once you have an axes object, you can perform a lot of customization of your plot.

In these examples, the US HUD data is loaded in the dataframe df and all libraries are imported.
"""

# steps

"""
Use plt.subplots() to create a axes and figure objects.
Plot a histplot of column fmr_3 on the axes.
Set a more useful label on the x axis of "3 Bedroom Fair Market Rent".
"""

# solution

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of data
sns.histplot(df['fmr_3'], ax=ax)

# Create a more descriptive x axis label
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()

#----------------------------------#

# exercise 08

"""
Additional plot customizations

The matplotlib API supports many common customizations such as labeling axes, adding titles, and setting limits. 
Let's complete another customization exercise.
"""

# steps

"""
Create a histplot of the fmr_1 column.
Modify the x axis label to say "1 Bedroom Fair Market Rent".
Change the x axis limits to be between 100 and 1500.
Add a descriptive title of "US Rent" to the plot.
"""

# solution

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.histplot(df['fmr_1'], ax=ax)

# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")

# Display the plot
plt.show()

#----------------------------------#

# exercise 09

"""
Adding annotations

Each of the enhancements we have covered can be combined together. 
In the next exercise, we can annotate our distribution plot to include lines that show the mean and median rent prices.

For this example, the palette has been changed to bright using sns.set_palette()
"""

# steps

"""
Create a figure and axes.
Plot the fmr_1 column distribution.
Add a vertical line using axvline for the median and mean of the values which are already defined.
"""

# solution

# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.histplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=median, color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=mean, color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()

#----------------------------------#

# exercise 10

"""
Multiple plots

For the final exercise we will plot a comparison of the fair market rents for 1-bedroom and 2-bedroom apartments.
"""

# steps

"""
Create two axes objects, ax0 and ax1.
Plot fmr_1 on ax0 and fmr_2 on ax1.
Display the plots side by side.
"""

# solution

# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.histplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.histplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))

# Display the plot
plt.show()

#----------------------------------#

