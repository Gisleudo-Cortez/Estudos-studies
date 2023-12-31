# exercise 01

"""
The cutoff point

In this exercise, and throughout this chapter, you'll be working with the restaurants DataFrame which has data on various restaurants. Your ultimate goal is to create a restaurant recommendation engine, but you need to first clean your data.

This version of restaurants has been collected from many sources, where the cuisine_type column is riddled with typos, and should contain only italian, american and asian cuisine types. There are so many unique categories that remapping them manually isn't scalable, and it's best to use string similarity instead.

Before doing so, you want to establish the cutoff point for the similarity score using the thefuzz's process.extract() function by finding the similarity score of the most distant typo of each category.
"""

# steps

"""
Import process from thefuzz.
Store the unique cuisine_types into unique_types.
Calculate the similarity of 'asian', 'american', and 'italian' to all possible cuisine_types using process.extract(), while returning all possible matches.
---
Question

Take a look at the output, what do you think should be the similarity cutoff point when remapping categories?
Possible Answers

    80 (Answer)
    70
    60
"""

# solution

# Import process from thefuzz
from thefuzz import process

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))

#----------------------------------#

# exercise 02

"""
Remapping categories II

In the last exercise, you determined that the distance cutoff point for remapping typos of 'american', 'asian', and 'italian' cuisine types stored in the cuisine_type column should be 80.

In this exercise, you're going to put it all together by finding matches with similarity scores equal to or higher than 80 by using fuzywuzzy.process's extract() function, for each correct cuisine type, and replacing these matches with it. Remember, when comparing a string with an array of strings using process.extract(), the output is a list of tuples where each is formatted like:

(closest match, similarity score, index of match)

The restaurants DataFrame is in your environment, and you have access to a categories list containing the correct cuisine types ('italian', 'asian', and 'american').
"""

# steps

"""
Return all of the unique values in the cuisine_type column of restaurants.
---
Okay! Looks like you will need to use some string matching to correct these misspellings!

    As a first step, create a list of all possible matches, comparing 'italian' with the restaurant types listed in the cuisine_type column.
---
Now you're getting somewhere! Now you can iterate through matches to reassign similar entries.

    Within the for loop, use an if statement to check whether the similarity score in each match is greater than or equal to 80.
    If it is, use .loc to select rows where cuisine_type in restaurants is equal to the current match (which is the first element of match), and reassign them to be 'italian'.
---
Finally, you'll adapt your code to work with every restaurant type in categories.

    Using the variable cuisine to iterate through categories, embed your code from the previous step in an outer for loop.
    Inspect the final result. This has been done for you.

"""

# solution

# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())

#----------------------------------#

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit = len(restaurants['cuisine_type']))

# Inspect the first 5 matches
print(matches[0:5])

#----------------------------------#

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] > 80:
    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
    restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = 'italian'

#----------------------------------#

# Iterate through categories
for cuisine in categories:  
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine
      
# Inspect the final result
print(restaurants['cuisine_type'].unique())

#----------------------------------#

# exercise 03

"""
Pairs of restaurants

In the last lesson, you cleaned the restaurants dataset to make it ready for building a restaurants recommendation engine. You have a new DataFrame named restaurants_new with new restaurants to train your model on, that's been scraped from a new data source.

You've already cleaned the cuisine_type and city columns using the techniques learned throughout the course. However you saw duplicates with typos in restaurants names that require record linkage instead of joins with restaurants.

In this exercise, you will perform the first step in record linkage and generate possible pairs of rows between restaurants and restaurants_new. Both DataFrames, pandas and recordlinkage are in your environment.
"""

# steps

"""
Instantiate an indexing object by using the Index() function from recordlinkage.
Block your pairing on cuisine_type by using indexer's' .block() method.
Generate pairs by indexing restaurants and restaurants_new in that order.
---
Question

Now that you've generated your pairs, you've achieved the first step of record linkage. What are the steps remaining to link both restaurants DataFrames, and in what order?
Possible Answers

    Compare between columns, score the comparison, then link the DataFrames. (Answer)
    Clean the data, compare between columns, link the DataFrames, then score the comparison.
    Clean the data, compare between columns, score the comparison, then link the DataFrames.
"""

# solution

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

#----------------------------------#

# exercise 04

"""
Similar restaurants

In the last exercise, you generated pairs between restaurants and restaurants_new in an effort to cleanly merge both DataFrames using record linkage.

When performing record linkage, there are different types of matching you can perform between different columns of your DataFrames, including exact matches, string similarities, and more.

Now that your pairs have been generated and stored in pairs, you will find exact matches in the city and cuisine_type columns between each pair, and similar strings for each pair in the rest_name column. Both DataFrames, pandas and recordlinkage are in your environment.
"""

# steps

"""
Instantiate a comparison object using the recordlinkage.Compare() function.
---
Use the appropriate comp_cl method to find exact matches between the city and cuisine_type columns of both DataFrames.
Use the appropriate comp_cl method to find similar strings with a 0.8 similarity threshold in the rest_name column of both DataFrames.
---
Compute the comparison of the pairs by using the .compute() method of comp_cl
---
Question

Print out potential_matches, the columns are the columns being compared, with values being 1 for a match, and 0 for not a match for each pair of rows in your DataFrames. To find potential matches, you need to find rows with more than matching value in a column. You can find them with

potential_matches[potential_matches.sum(axis = 1) >= n]

Where n is the minimum number of columns you want matching to ensure a proper duplicate find, what do you think should the value of n be?
Possible Answers

    3 because I need to have matches in all my columns. (Answer)
    2 because matching on any of the 2 columns or more is enough to find potential duplicates.
    1 because matching on just 1 column like the restaurant name is enough to find potential duplicates.
"""

# solution

# Create a comparison object
comp_cl = recordlinkage.Compare()

#----------------------------------#

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label = 'cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 

#----------------------------------#

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types - 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

#----------------------------------#

# exercise 05

"""
Getting the right index

Here's a DataFrame named matches containing potential matches between two DataFrames, users_1 and users_2. Each DataFrame's row indices is stored in uid_1 and uid_2 respectively.

             first_name  address_1  address_2  marriage_status  date_of_birth
uid_1 uid_2                                                                  
0     3              1          1          1                1              0
     ...            ...         ...        ...              ...            ...
     ...            ...         ...        ...              ...            ...
1     3              1          1          1                1              0
     ...            ...         ...        ...              ...            ...
     ...            ...         ...        ...              ...            ...

How do you extract all values of the uid_1 index column?
Answer the question
50XP
Possible Answers

    matches.index.get_level_values(0)
    press
    1
    matches.index.get_level_values(1)
    press
    2
    matches.index.get_level_values('uid_1')
    press
    3
    Both 1 and 3 are correct. (Answer)
"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 06

"""
Linking them together!

In the last lesson, you've finished the bulk of the work on your effort to link restaurants and restaurants_new. You've generated the different pairs of potentially matching rows, searched for exact matches between the cuisine_type and city columns, but compared for similar strings in the rest_name column. You stored the DataFrame containing the scores in potential_matches.

Now it's finally time to link both DataFrames. You will do so by first extracting all row indices of restaurants_new that are matching across the columns mentioned above from potential_matches. Then you will subset restaurants_new on these indices, then append the non-duplicate values to restaurants. All DataFrames are in your environment, alongside pandas imported as pd.
"""

# steps

"""
Isolate instances of potential_matches where the row sum is above or equal to 3 by using the .sum() method.
Extract the second column index from matches, which represents row indices of matching record from restaurants_new by using the .get_level_values() method.
Subset restaurants_new for rows that are not in matching_indices.
Append non_dup to restaurants.
"""

# solution

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)

#----------------------------------#

# exercise 07

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 08

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 09

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 10

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 11

"""

"""

# steps

"""

"""

# solution



#----------------------------------#