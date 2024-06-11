# Excercise 01

# Variable assignment

# Throughout the exercises in this chapter, you'll be visualizing a subset of the gapminder data from the year 1952. First, you'll have to load the ggplot2 package, and create a gapminder_1952 dataset to visualize.

# By the way, if you haven't downloaded it already, check out the Tidyverse For Beginners Cheat Sheet. It includes an overview of the most important concepts, functions and methods and might come in handy if you ever need a quick refresher!

# Instructions

#     Load the ggplot2 package after the gapminder and dplyr packages.
#     Filter gapminder for observations from the year 1952, and assign it to a new dataset gapminder_1952 using the assignment operator (<-).

# Load the ggplot2 package as well
library(gapminder)
library(dplyr)
library(ggplot2)

# Create gapminder_1952
gapminder_1952 <- gapminder %>%
 filter(year == 1952)

print(gapminder_1952, n=10)

#####

# Excercise 02

# Comparing population and GDP per capita

# In the video you learned to create a scatter plot with GDP per capita on the x-axis and life expectancy on the y-axis (the code for that graph has been provided in the exercise code). When you're exploring data visually, you'll often need to try different combinations of variables and aesthetics.

# Instructions

    # Change the scatter plot of gapminder_1952 so that (pop) is on the x-axis and GDP per capita (gdpPercap) is on the y-axis.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Change to put pop on the x-axis and gdpPercap on the y-axis
ggplot(gapminder_1952, aes(x = pop, y = gdpPercap)) +
  geom_point()

#####

# Exercise 03

# Comparing population and life expectancy

# In this exercise, you'll use ggplot2 to create a scatter plot from scratch, to compare each country's population with its life expectancy in the year 1952.

# Instructions


#     Create a scatter plot of gapminder_1952 with population (pop) is on the x-axis and life expectancy (lifeExp) on the y-axis.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Create a scatter plot with pop on the x-axis and lifeExp on the y-axis
ggplot(gapminder_1952, aes(x = pop, y = lifeExp)) +
 geom_point()

#####

# Exercise 04

# Putting the x-axis on a log scale

# You previously created a scatter plot with population on the x-axis and life expectancy on the y-axis. Since population is spread over several orders of magnitude, with some countries having a much higher population than others, it's a good idea to put the x-axis on a log scale.
# Instructions


#     Change the existing scatter plot (code provided) to put the x-axis (representing population) on a log scale.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Change this plot to put the x-axis on a log scale
ggplot(gapminder_1952, aes(x = pop, y = lifeExp)) +
  geom_point() +
  scale_x_log10()

#####

# Exercise 05

# Putting the x- and y- axes on a log scale

# Suppose you want to create a scatter plot with population on the x-axis and GDP per capita on the y-axis. Both population and GDP per-capita are better represented with log scales, since they vary over many orders of magnitude.
# Instructions


#     Create a scatter plot with population (pop) on the x-axis and GDP per capita (gdpPercap) on the y-axis. Put both the x- and y- axes on a log scale.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Scatter plot comparing pop and gdpPercap, with both axes on a log scale
ggplot(gapminder_1952, aes(x = pop, y = gdpPercap)) + 
 geom_point() +
 scale_x_log10()+
 scale_y_log10()

#####

# Exercise 06

# Adding color to a scatter plot

# In this lesson you learned how to use the color aesthetic, which can be used to show which continent each point in a scatter plot represents.
# Instructions

#     Create a scatter plot with population (pop) on the x-axis, life expectancy (lifeExp) on the y-axis, and with continent (continent) represented by the color of the points. Put the x-axis on a log scale.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Scatter plot comparing pop and lifeExp, with color representing continent
ggplot(gapminder_1952, aes(x=pop, y=lifeExp, colot=continent)) + 
 geom_point() + 
 scale_x_log10()

#####

# Exercise 07

# Adding size and color to a plot

# In the last exercise, you created a scatter plot communicating information about each country's population, life expectancy, and continent. Now you'll use the size of the points to communicate even more.
# Instructions

#     Modify the scatter plot so that the size of the points represents each country's GDP per capita (gdpPercap).

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Add the size aesthetic to represent a country's gdpPercap
ggplot(gapminder_1952, aes(x = pop, y = lifeExp, color = continent, size = gdpPercap)) +
  geom_point() +
  scale_x_log10()

#####

# Exercise 08

# Creating a subgraph for each continent

# You've learned to use faceting to divide a graph into subplots based on one of its variables, such as the continent.
# Instructions

#     Create a scatter plot of gapminder_1952 with the x-axis representing population (pop), the y-axis representing life expectancy (lifeExp), and faceted to have one subplot per continent (continent). Put the x-axis on a log scale.

library(gapminder)
library(dplyr)
library(ggplot2)

gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Scatter plot comparing pop and lifeExp, faceted by continent
ggplot(gapminder_1952, aes(x=pop, y=lifeExp)) +
 geom_point() + 
 scale_x_log10() +
 facet_wrap(~ continent)

#####

# Exercise 09

# Faceting by year

# All of the graphs in this chapter have been visualizing statistics within one year. Now that you're able to use faceting, however, you can create a graph showing all the country-level data from 1952 to 2007, to understand how global statistics have changed over time.
# Instructions

#     Create a scatter plot of the gapminder data:
#     Put GDP per capita (gdpPercap) on the x-axis and life expectancy (lifeExp) on the y-axis, with continent (continent) represented by color and population (pop) represented by size.
#     Put the x-axis on a log scale
#     Facet by the year variable

library(gapminder)
library(dplyr)
library(ggplot2)

# Scatter plot comparing gdpPercap and lifeExp, with color representing continent
# and size representing population, faceted by year
ggplot(gapminder, aes(x=gdpPercap, y=lifeExp, color=continent, size=pop))+
 geom_point() + 
 scale_x_log10() + 
 facet_wrap(~ year)