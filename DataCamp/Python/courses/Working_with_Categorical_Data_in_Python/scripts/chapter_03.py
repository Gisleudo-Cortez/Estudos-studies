# exercise 01

"""
Creating a box plot

When people leave reviews for products, services, or destinations, 
people reading those reviews can sometimes mark the original review as helpful. 
If enough people mark the review as helpful, 
future readers of these reviews might be more likely to trust the content of the original review.

Using the reviews dataset, 
explore the continuous variable "Helpful votes" across the different categories found in the "Traveler type" variable.

Note that for the remainder of this chapter, seaborn as sns and matplotlib.pyplot as plt will be preloaded for you.
"""

# steps

"""
Set the font size of your graphic to be 1.25.
Set the background of the graphic to be "darkgrid".
Create a boxplot using catplot() with "Helpful votes" as the continuous variable split across each "Traveler type". 
Make sure that you are using the reviews dataset.
"""

# solution

# Set the font size to 1.25
sns.set(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(data = reviews, x = 'Traveler type', y = 'Helpful votes', kind = 'box')

plt.show()

#----------------------------------#

# exercise 02

"""
Creating a bar plot

Las Vegas hotels are seeing large variations in how helpful reviews appear to other people. 
The owners of these hotels are curious if there are times of the year when reviews have been more helpful to their potential guests.
Help the owners understand their reviews better by creating a bar plot of the average number of helpful votes 
per review across the categorical variable "Period of stay". The dataset reviews has been preloaded for you.
"""

# steps

"""
Print out the frequency counts of the variable "Period of stay" to make sure each category has data.
Create a bar plot using catplot().
Split the reviews dataset on "Period of stay" across the x-axis.
Specify the numerical variable to aggregate on as "Helpful votes".
"""

# solution

# Print the frequency counts of "Period of stay"
print(reviews['Period of stay'].value_counts())

sns.set(font_scale=1.4)
sns.set_style("whitegrid")

# Create a bar plot of "Helpful votes" by "Period of stay"
sns.catplot(data = reviews, x = 'Period of stay', y = 'Helpful votes', kind = 'bar')
plt.show()

#----------------------------------#

# exercise 03

"""
Ordering categories

Not all categories are created equal. In the hotel review dataset, reviews, 
hotel owners know that most of their customers are from North America. 
When visualizing data broken out by "User continent" they might want North America to appear first. 
An ordered list of user continents has been provided as continent_categories. 
In this exercise, you will work through preparing a visualization that is ordered by the frequency counts of a Series.
"""

# steps

"""
Create a bar chart with "User continent" along the x-axis and "Score" along the y-axis.
---
Print out the frequency counts of "User continent".
---
Convert the "User continent" Series to a categorical and create a bar plot with "User continent" along the x-axis.
---
Reorder the "User continent" Series using the ordered list, continent_categories, and rerun the graphic.
"""

# solution

# Create a bar chart
sns.set(font_scale=.9)
sns.set_style("whitegrid")
sns.catplot(x = 'User continent', y = 'Score', data=reviews, kind='bar')
plt.show()

#----------------------------------#

# Create a bar chart
sns.set(font_scale=.9)
sns.set_style("whitegrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")

# Print the frequency counts for "User continent"
print(reviews['User continent'].value_counts())

#----------------------------------#

# Set style
sns.set(font_scale=.9)
sns.set_style("whitegrid")

# Print the frequency counts for "User continent"
print(reviews["User continent"].value_counts())

# Convert "User continent" to a categorical variable
reviews["User continent"] = reviews['User continent'].astype('category')
sns.catplot(x = 'User continent', y="Score", data=reviews, kind="bar")
plt.show()

#----------------------------------#

# Set style
sns.set(font_scale=.9)
sns.set_style("whitegrid")

# Print the frequency counts for "User continent"
print(reviews["User continent"].value_counts())

# Convert "User continent" to a categorical variable
reviews["User continent"] = reviews["User continent"].astype("category")

# Reorder "User continent" using continent_categories and rerun the graphic
continent_categories = list(reviews["User continent"].value_counts().index)
reviews["User continent"] = reviews["User continent"].cat.reorder_categories(new_categories = continent_categories)
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()

#----------------------------------#

# exercise 04

"""
Bar plot using hue

Aggregating information across multiple categories is often necessary to help stakeholders better understand their data. 
In preparation for building a dashboard that will allow users to select up to two variables when creating visualizations, 
you want to test visualizations that use different combinations of categorical variables using a bar plot.
"""

# steps

"""
Update the plot so that "Casino" (along the x-axis) and "Free internet" (to color the bars) are used to split the data.
---
Switch the categories so that "Free internet" is on the x-axis and "Casino" is in the legend.
---
Update the x parameter to be "User continent".
---
The font was too large for the last visualization - change the font size to 1.0.
"""

# solution

# Add a second category to split the data on: "Free internet"
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='Casino', y="Score", data=reviews, kind="bar", hue = 'Free internet')
plt.show()

#----------------------------------#

# Switch the x and hue categories
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='Free internet', y="Score", data=reviews, kind="bar", hue='Casino')
plt.show()

#----------------------------------#

# Update x to be "User continent"
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x='User continent', y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

#----------------------------------#

# Lower the font size so that all text fits on the screen.
sns.set(font_scale=1.0)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

#----------------------------------#

# exercise 05

"""
Creating a point plot

Creating helpful visualizations sometimes requires a lot of testing. 
You have been asked to create a visualization that shows the number of reviews, 
"Nr. reviews", which is the number of reviews a reviewer has previously written, 
across a hotel's star rating, "Hotel stars". Since the number of reviews is numerical, 
you have decided to use a point plot to show the mean of the data across the categories.
"""

# steps

"""
Using the catplot() function, create a point plot.
Split the data across the x-axis using "Hotel stars".
Specify the numerical variable to visualize to "Nr. reviews".
Update the arguments so that any lines that appear do not overlap.
"""

# solution

# Create a point plot with catplot using "Hotel stars" and "Nr. reviews"
sns.catplot(
  # Split the data across Hotel stars and summarize Nr. reviews
  x='Hotel stars',
  y='Nr. reviews',
  data=reviews,
  # Specify a point plot
  kind = 'point',
  hue="Pool",
  # Make sure the lines and points don't overlap
  dodge=True
)
plt.show()

#----------------------------------#

# exercise 06

"""
Creating a count plot

When creating quick analysis of frequency counts, you have been using .value_counts(). 
This is a great way for you to see the counts and get an idea of which categories are present in the data. 
However, sending frequency tables to clients or coworkers may not always be a good idea. 
For this exercise, you will visualize the number of reviews by their "Score". 
Although "Score" has been used as a numerical variable in the past, 
it can be used as a categorical variable given that it has five unique values that are ordered from worst to best. 
The reviews dataset has been preloaded.
"""

# steps

"""
Use the catplot() function to display count frequencies using the reviews dataset.
Count the frequencies for the "Score" variable across the x-axis.
When counting the frequencies, color the bars using the "Traveler type" column.
"""

# solution

sns.set(font_scale=1.4)
sns.set_style("darkgrid")

# Create a catplot that will count the frequency of "Score" across "Traveler type"
sns.catplot(
  data = reviews,
  x='Score',
  kind='count',
  hue='Traveler type'
)
plt.show()

#----------------------------------#

# exercise 07

"""
One visualization per group

While working on a data exploration project, 
you have been asked to visualize the number of reviews of hotels by "Period of stay" and by the day of the week, 
"Review weekday". 
The goal of this visualization is to see what day of the week has the most reviews for each of the four periods of stay. 
The reviews dataset has been preloaded for you, as well as both seaborn, as sns, and matplotlib.pyplot as plt.
"""

# steps

"""
Create a catplot() using "count" as the type of graphic.
Count the number of reviews by "Review weekday".
Create individual plots for each "Period of stay".
Wrap the plots after every 2nd graphic.
"""

# solution

# Create a catplot for each "Period of stay" broken down by "Review weekday"
ax = sns.catplot(
  # Make sure Review weekday is along the x-axis
  x='Review weekday',
  # Specify Period of stay as the column to create individual graphics for
  col='Period of stay',
  # Specify that a count plot should be created
  kind='count',
  # Wrap the plots after every 2nd graphic.
  col_wrap=2,
  data=reviews
)
plt.show()

#----------------------------------#

# exercise 08

"""
Updating categorical plots

Hotels are constantly working to get better reviews from their customers. 
A hotel chain has asked you to create visualizations to help the company understand why people might provide various ratings 
after staying at their hotels. A manager has asked if hotels with "Free internet" receive higher reviews given the "Traveler type".

Creating visualizations is an iterative process. 
In this exercise, you will start with a basic graphic and iteratively add features until you have a finished product. 
The reviews dataset has been preloaded for you, as well as both seaborn, as sns, and matplotlib.pyplot as plt.
"""

# steps

"""
Adjust the color of the plot to be seaborn's "Set2" palette.
---
Add the title "Hotel Score by Traveler Type and Free Internet Access".
---
Update the axis labels to be "Free Internet" for the x-axis and "Average Review Rating" for the y-axis.
---
Adjust the starting height of the graphic to be 93% of the full visualization height.
"""

# solution

# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette("Set2")
)

#----------------------------------#

# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette("Set2")
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")

#----------------------------------#

# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette("Set2")
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")

# Update the axis labels
ax.set_axis_labels("Free Internet", "Average Review Rating")

#----------------------------------#

# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette("Set2")
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")
# Update the axis labels
ax.set_axis_labels("Free Internet", "Average Review Rating")

# Adjust the starting height of the graphic
plt.subplots_adjust(top=.93)
plt.show()

#----------------------------------#