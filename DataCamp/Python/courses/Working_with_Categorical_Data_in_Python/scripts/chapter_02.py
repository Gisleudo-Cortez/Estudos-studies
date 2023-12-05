# exercise 01

"""
Adding categories

The owner of a local dog adoption agency has listings for almost 3,000 dogs. 
One of the most common questions they have been receiving lately is: 
"What type of area was the dog previously kept in?". 
You are setting up a pipeline to do some analysis and want to look into what information is available regarding the "keep_in" 
variable. Both pandas, as pd, and the dogs dataset have been preloaded.
"""

# steps

"""
Print the frequency of the responses in the "keep_in" variable and make sure the count of NaN values are shown.
---
Convert the "keep_in" variable to a categorical Series.
---
Add the list of new categories provided by the adoption agency, new_categories, to the "keep_in" column.
---
Print the frequency counts of the keep_in column and do not drop NaN values.
"""

# solution

# Check frequency counts while also printing the NaN count
print(dogs['keep_in'].value_counts(dropna=False))

#----------------------------------#

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs['keep_in'].astype('category')

#----------------------------------#

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs['keep_in'].cat.add_categories(new_categories=new_categories)

#----------------------------------#

# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories)

# Check frequency counts one more time
print(dogs['keep_in'].value_counts(dropna=False))

#----------------------------------#

# exercise 02

"""
Removing categories

Before adopting dogs, parents might want to know whether or not a new dog likes children. 
When looking at the adoptable dogs dataset, dogs, 
you notice that the frequency of responses for the categorical Series "likes_children" looks like this:

maybe     1718
yes       1172
no          47

The owner of the data wants to convert all "maybe" responses to "no", 
as it would be unsafe to let a family adapt a dog if it doesn't like children. 
The code to convert all "maybe" to "no" is provided in Step 1. 
However, the option for "maybe" still remains as a category.
"""

# steps

"""
Print out the categories of the categorical Series dogs["likes_children"].
---
Print out the frequency table for "likes_children" to see if any "maybe" responses remain.
---
Remove the "maybe" category from the Series.
---
Print out the categories of "likes_children" one more time.
"""

# solution

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

#----------------------------------#

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs['likes_children'].value_counts(dropna=False))

#----------------------------------#

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the "maybe" category
dogs["likes_children"] = dogs['likes_children'].cat.remove_categories(removals=["maybe"])
print(dogs["likes_children"].value_counts())

#----------------------------------#

# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the `"maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(["maybe"])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(dogs["likes_children"].cat.categories)

#----------------------------------#

# exercise 03

"""
Renaming categories

The likes_children column of the adoptable dogs dataset needs an update. Here are the current frequency counts:

Maybe?    1718
yes       1172
no          47

Two things that stick out are the differences in capitalization and the ? found in the Maybe? category. 
The data should be cleaner than this and you are being asked to make a few changes.
"""

# steps

"""
Create a dictionary called my_changes that will update the Maybe? category to Maybe.
Rename the categories in likes_children using the my_changes dictionary.
Update the categories one more time so that all categories are uppercase using the .upper() method.
Print out the categories of the updated likes_children Series.
"""

# solution

# Create the my_changes dictionary
my_changes = {
    'Maybe?' : 'Maybe'
}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs['likes_children'].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs['likes_children'].cat.categories)

#----------------------------------#

# exercise 04

"""
Collapsing categories

One problem that users of a local dog adoption website have voiced is that there are too many options. 
As they look through the different types of dogs, they are getting lost in the overwhelming amount of choice. 
To simplify some of the data, you are going through each column and collapsing data if appropriate. 
To preserve the original data, you are going to make new updated columns in the dogs dataset. 
You will start with the coat column. The frequency table is listed here:

short          1969
medium          565
wirehaired      220
long            180
medium-long       3

"""

# steps

"""
Create a dictionary named update_coats to map both wirehaired and medium-long to medium.
Collapse the categories listed in this new dictionary and save this as a new column, coat_collapsed.
Convert this new column into a categorical Series.
Print the frequency table of this new Series.
"""

# solution

# Create the update_coats dictionary
update_coats = {
    'wirehaired' : 'medium',
    'medium-long' : 'medium'
}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs['coat'].replace(update_coats)

# Convert the column to categorical
dogs['coat_collapsed'] = dogs['coat_collapsed'].astype('category')

# Print the frequency table
print(dogs['coat_collapsed'].value_counts(dropna=False))

#----------------------------------#

# exercise 05

"""
Reordering categories in a Series

The owner of a local dog adoption agency has asked you take a look at her data on adoptable dogs. 
She is specifically interested in the size of the dogs in her dataset and wants to know if there are differences in other variables,
given a dog's size. 
The adoptable dogs dataset has been loaded as dogs and the "size" variable has already been saved as a categorical column.
"""

# steps

"""
Print out the current categories of the "size" pandas Series.
---
Reorder categories in the "size" column using the categories "small", "medium", "large", do not set the ordered parameter.
---
Update the reorder_categories() method so that pandas knows the variable has a natural order.
---
Add a argument to the method so that the "size" column is updated without needing to save it to itself.
"""

# solution

# Print out the current categories of the size variable
print(dogs['size'].cat.categories)

#----------------------------------#

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories using the list provided
dogs["size"] = dogs['size'].cat.reorder_categories(new_categories = ['small', 'medium', 'large'])

#----------------------------------#

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal
dogs["size"] = dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered = True
)

#----------------------------------#

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal, and overwriting the original series
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace = True
)

#----------------------------------#

# exercise 06

"""
Using .groupby() after reordering

It is now time to run some analyses on the adoptable dogs dataset that is focused on the "size" of the dog. 
You have already developed some code to reorder the categories. 
In this exercise, you will develop two similar .groupby() statements to help better understand the effect of "size" 
on other variables. dogs has been preloaded for you.
"""

# steps

"""
Print out the frequency table of "sex" for each category of the "size" column.
Print out the frequency table of "keep_in" for each category of the "size" column.
"""

# solution

# Previous code
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby('size')['sex'].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby('size')['keep_in'].value_counts())

#----------------------------------#

# exercise 07

"""
Cleaning variables

Users of an online entry system used to have the ability to freely type in responses to questions. 
This is causing issues when trying to analyze the adoptable dogs dataset, dogs. 
Here is the current frequency table of the "sex" column:

male      1672
female    1249
 MALE        10
 FEMALE       5
Malez        1

Now that the system only takes responses of "female" and "male", you want this variable to match the updated system.
"""

# steps

"""
Update the misspelled response "Malez" to be "male" by creating the replacement map, replace_map.
---
Replace all occurrences of "Malez" with "male" by using replace_map.
---
Remove the leading spaces of the " MALE" and " FEMALE" responses.
---
Convert all responses to be strictly lowercase.
"""

# solution

# Fix the misspelled word 
replace_map = {
    'Malez' : 'male'
}

#----------------------------------#

# Fix the misspelled word 
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs['sex'].replace(replace_map)

print(dogs["sex"].value_counts())

#----------------------------------#

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs['sex'].str.strip()

print(dogs["sex"].value_counts())

#----------------------------------#

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

print(dogs["sex"].value_counts())

#----------------------------------#

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

# Convert to a categorical Series
dogs["sex"] = dogs["sex"].astype('category')

print(dogs["sex"].value_counts())

#----------------------------------#

# exercise 08

"""
Accessing and filtering data

You are working on a Python application to display information about the dogs available for adoption at your local animal shelter. 
Some of the variables of interest, such as "breed", "size", and "coat", are saved as categorical variables. 
In order for this application to work properly, you need to be able to access and filter data using these columns.

The ID variable has been set as the index of the pandas DataFrame dogs.
"""

# steps

"""
Print the "coat" value for the dog with an ID of 23807.
---
For dogs with a long "coat", print the number of each "sex".
---
Print the average age of dogs with a "breed" of "English Cocker Spaniel".
---
Filter to the dogs with "English" in their "breed" name using the .contains() method.
"""

# solution

# Print the category of the coat for ID 23807
print(dogs.loc[dogs.index == 23807, 'coat'])

#----------------------------------#

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs['coat'] == 'long', 'sex'].value_counts())

#----------------------------------#

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs['breed'] == 'English Cocker Spaniel', 'age'].mean())

#----------------------------------#

# Count the number of dogs that have "English" in their breed name
print(dogs[dogs["breed"].str.contains('English', regex=False)].shape[0])

#----------------------------------#

# exercise 0

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 0

"""

"""

# steps

"""

"""

# solution



#----------------------------------#