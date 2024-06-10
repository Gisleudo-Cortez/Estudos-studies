# Excercise 01

# Loading the gapminder and dplyr packages

# Before you can work with the gapminder dataset, you'll need to load two R packages that contain the tools for working with it, then display the gapminder dataset so that you can see what it contains.

# To your right, you'll see two windows inside which you can enter code: The script.R window, and the R Console. All of your code to solve each exercise must go inside script.R.

# If you hit Submit Answer, your R script is executed and the output is shown in the R Console. DataCamp checks whether your submission is correct and gives you feedback. You can hit Submit Answer as often as you want. If you're stuck, you can ask for a hint or a solution.

# You can use the R Console interactively by simply typing R code and hitting Enter. When you work in the console directly, your code will not be checked for correctness so it is a great way to experiment and explore.

# This course introduces a lot of new concepts, so if you ever need a quick refresher, download the Tidyverse For Beginners Cheat Sheet and keep it handy!

# Instructions
#
# Use the library() function to load the dplyr package, just like we've loaded the gapminder package for you.
# Type gapminder, on its own line, to look at the gapminder dataset.

# Load the gapminder package
library(gapminder)

# Load the dplyr package
library(dplyr)

# Look at the gapminder dataset
print(gapminder)

#####

# Excercise 02

# Understanding a data frame

# Now that you've loaded the gapminder dataset, you can start examining and understanding it.

# We've already loaded the gapminder and dplyr packages. Type gapminder in the console, to display the object.

# How many observations (rows) are in the dataset?

# Possible answers
# 1704 {Answer}
# 6
# 1694
# 1952

#####

# Exercise 03

# Filtering for one year

# The filter verb extracts particular observations based on a condition. In this exercise you'll filter for observations from a particular year.

# Instructions

#     Add a filter() line after the pipe (%>%) to extract only the observations from the year 1957. Remember that you use == to compare two values.

library(gapminder)
library(dplyr)

# Filter the gapminder dataset for the year 1957
print(gapminder %>%
    filter(year == 1957))

#####

# Exercise 04

# Filtering for one country and one year

# You can also use the filter() verb to set two conditions, which could retrieve a single observation.

# Just like in the last exercise, you can do this in two lines of code, starting with gapminder %>% and having the filter() on the second line. Keeping one verb on each line helps keep the code readable. Note that each time, you'll put the pipe %>% at the end of the first line (like gapminder %>%); putting the pipe at the beginning of the second line will throw an error.

# Instructions

#     Filter the gapminder data to retrieve only the observation from China in the year 2002.

library(gapminder)
library(dplyr)

# Filter for China in 2002
print(gapminder %>%
    filter(country == "China", year == 2002))

#####

# Exercise 05

# Arranging observations by life expectancy

# You use arrange() to sort observations in ascending or descending order of a particular variable. In this case, you'll sort the dataset based on the lifeExp variable.

# Instructions

#    Sort the gapminder dataset in ascending order of life expectancy (lifeExp).
#    Sort the gapminder dataset in descending order of life expectancy.

library(gapminder)
library(dplyr)

# Sort in ascending order of lifeExp
print(gapminder %>%
    arrange(lifeExp))


# Sort in descending order of lifeExp
print(gapminder %>%
    arrange(desc(lifeExp)))

#####

# Exercise 06

# Filtering and arranging

# You'll often need to use the pipe operator (%>%) to combine multiple dplyr verbs in a row. In this case, you'll combine a filter() with an arrange() to find the highest population countries in a particular year.
# Instructions

#    Use filter() to extract observations from just the year 1957, then use arrange() to sort in descending order of population (pop).

library(gapminder)
library(dplyr)

# Filter for the year 1957, then arrange in descending order of population


print(gapminder %>%
    filter(year == 1957) %>%
    arrange(desc(pop)))

#####

# Exercise 07

# Using mutate to change or create a column

#Suppose we want life expectancy to be measured in months instead of years: you'd have to multiply the existing value by 12. You can use the mutate() verb to change this column, or to create a new column that's calculated this way.

#Instructions


#    Use mutate() to change the existing lifeExp column, by multiplying it by 12: 12 * lifeExp.
#    Use mutate() to add a new column, called lifeExpMonths, calculated as 12 * lifeExp.

library(gapminder)
library(dplyr)

# Use mutate to change lifeExp to be in months
print(gapminder %>%
    mutate(lifeExp = lifeExp * 12))

# Use mutate to create a new column called lifeExpMonths
print(gapminder %>%
    mutate(lifeExpMonths = lifeExp * 12))

#####

# Exercise 08

# Combining filter, mutate, and arrange

# In this exercise, you'll combine all three of the verbs you've learned in this chapter, to find the countries with the highest life expectancy, in months, in the year 2007.
# Instructions

#    In one sequence of pipes on the gapminder dataset:
#    filter() for observations from the year 2007,
#    mutate() to create a column lifeExpMonths, calculated as 12 * lifeExp, and
#    arrange() in descending order of that new column

library(gapminder)
library(dplyr)

# Filter, mutate, and arrange the gapminder dataset
print(gapminder %>%
    filter(year == 2007) %>%
    mutate(lifeExpMonths = lifeExp * 12) %>%
    arrange(desc(lifeExpMonths)))