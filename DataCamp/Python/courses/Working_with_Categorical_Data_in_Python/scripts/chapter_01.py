# exercise 01

"""
Exploring a target variable

You have been asked to build a machine learning model to predict whether or not a person makes over $50,000 in a year. 
To understand the target variable, Above/Below 50k, you decide to explore the variable in more detail.

The Python package pandas will be used throughout this course and will be loaded as pd throughout. 
The adult census income dataset, adult, has also been preloaded for you.
"""

# steps

"""
Explore the Above/Below 50k variable by printing out a description of the variable's contents.
---
Explore the Above/Below 50k variable by printing out a frequency table of the values found in this column.
---
Rerun .value_counts(), but this time print out the relative frequency values instead of the counts.
---
Question

    Given the output from the previous steps, do more people make more or less than $50,000?

Possible Answers

    More than $50,000
    Less than $50,000 (Answer)
"""

# solution

# Explore the Above/Below 50k variable
print(adult['Above/Below 50k'].describe())

#----------------------------------#

# Explore the Above/Below 50k variable
print(adult["Above/Below 50k"].describe())

# Print a frequency table of "Above/Below 50k"
print(adult["Above/Below 50k"].value_counts())

#----------------------------------#

# Explore the Above/Below 50k variable
print(adult["Above/Below 50k"].describe())

# Print a frequency table of "Above/Below 50k"
print(adult["Above/Below 50k"].value_counts())

# Print relative frequency values
print(adult["Above/Below 50k"].value_counts(normalize = True))

#----------------------------------#

# exercise 02

"""
Setting dtypes and saving memory

A colleague of yours is exploring a list of occupations and how they relate to salary. 
She has given you a list of these occupations, list_of_occupations, 
and has a few simple questions such as "How many different titles are there?" and "Which position is the most common?".
"""

# steps

"""
Create a pandas Series, series1, using the list_of_occupations (do not set the dtype).
---
Print both the data type and number of bytes used of this new Series.
---
Create a second pandas Series, series2, using the list_of_occupations and set the dtype to "category".
---
Print both the data type and number of bytes used of this new Series.
"""

# solution

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

#----------------------------------#

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

#----------------------------------#

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype='category')

#----------------------------------#

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype="category")

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)

#----------------------------------#

# exercise 03

"""
Creating a categorical pandas Series

Another colleague at work has collected information on the number of "Gold", "Silver", and "Bronze" medals won by the USA 
at the Summer & Winter Olympics since 1896. She has provided this as a list, medals_won. 
Before taking a look at the total number of each medal won, you want to create a categorical pandas Series. 
However, you know that these medals have a specific order to them and that Gold is better than Silver, 
but Silver is better than Bronze. Use the object, medals_won, to help.
"""

# steps

"""
Create a categorical pandas Series without using pd.Series().
Specify the three known medal categories such that "Bronze" < "Silver" < "Gold".
Specify that the order of the categories is important when creating this Series.
"""

# solution

# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories = ['Bronze', 'Silver', 'Gold'], ordered = True)
print(medals)

#----------------------------------#

# exercise 04

"""
Setting dtype when reading data

You are preparing to create a machine learning model to predict a person's income category using the adult census income dataset. 
You don't have access to any cloud resources and you want to make sure that your laptop will be able to load the full dataset 
and process its contents. 
You have read in the first five rows of the dataset adult to help you understand what kind of columns are available.
"""

# steps

"""
Call the correct attribute on the adult DataFrame to review the data types.
---
Question

Based on the data types in adult, which columns are good candidates for specifying a dtype of "category" 
when reading in the adult dataset?
Possible Answers

    "Age", "Education Num", and "Race"
    "Age", "Hours/Week", and "Capital Loss"
    "Workclass", "Education Num", "Hours/Week", and "Above/Below 50k"
    "Workclass", "Education", "Relationship", "Above/Below 50k" (Answer)
---
Create a dictionary with keys: "Workclass", "Education", "Relationship", and "Above/Below 50k".
Set the value for each key to be "category".
---
Use the newly created dictionary, adult_dtypes, when reading in adult.csv
"""

# solution

# Check the dtypes
print(adult.dtypes)

#----------------------------------#

# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
  'Workclass' : 'category',
  'Education' : 'category',
  'Relationship' : 'category',
  'Above/Below 50k' : 'category'
}

#----------------------------------#

# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  "adult.csv",
  dtype = adult_dtypes
)
print(adult2.dtypes)

#----------------------------------#

# exercise 05

"""
Create lots of groups

You want to find the mean Age of adults when grouping by the following categories:

    "Workclass" (which has 9 categories)
    "Above/Below 50k" (which has 2 categories)
    "Education" (which has 16 categories).

You have developed the following bit of code:

gb = adult.groupby(by=[ "Workclass",
                        "Above/Below 50k", 
                        "Education"])

How many groups are in the gb object and what is the maximum possible number of groups that could have been created? 
The dataset adult, and the gb object have been preloaded for you.
"""

# steps

"""
Possible Answers

    2 are created out of 2 possible groups.
    2 are created out of 18 possible groups.
    288 are created out of 288 possible groups.
    208 are created out of 288 possible groups. (Answer)
"""

# solution



#----------------------------------#

# exercise 06

"""
Setting up a .groupby() statement

The gender wage gap is a hot-topic item in the United States and across the world. 
Using the adult census income dataset, loaded as adult, 
you want to check if some of the recently published data lines up with this income survey.
"""

# steps

"""
Split the adult dataset across the "Sex" and "Above/Below 50k" columns, saving this object as gb.
Print out the number of observations found in each group.
Using gb, find the average of each numerical column.
"""

# solution

# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=['Sex','Above/Below 50k'])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
print(gb.mean())

#----------------------------------#

# exercise 07

"""
Using pandas functions effectively

You are creating a Python application that will calculate summary statistics based on user-selected variables. 
The complete dataset is quite large. For now, you are setting up your code using part of the dataset, preloaded as adult. 
As you create a reusable process, make sure you are thinking through the most efficient way to setup the GroupBy object.
"""

# steps

"""
Create a list of the names for two user-selected variables: "Education" and "Above/Below 50k".
Create a GroupBy object, gb, using the user_list as the grouping variables.
Calculate the mean of "Hours/Week" across each group using the most efficient approach covered in the video.
"""

# solution

# Create a list of user-selected variables
user_list = ['Education', 'Above/Below 50k']

# Create a GroupBy object using this list
gb = adult.groupby(by = user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb['Hours/Week'].mean())

#----------------------------------#