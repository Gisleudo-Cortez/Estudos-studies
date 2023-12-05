# exercise 01

"""
Overcoming pitfalls: string issues

Being able to effectively use categorical pandas Series is an important skill to have in your toolbelt. Unfortunately, there are several common problems that you may run into when using these Series.

In this exercise, you will work through code from a previous exercise on updating a categorical Series. Follow the instructions to make sure everything goes smoothly. The used cars dataset, used_cars, is loaded for you.
"""

# steps

"""
Print the frequency table of the "body_type" column for used_cars and include NaN values.
---
Update the .loc statement so that all NaN values in "body_type" are set to "other".
---
Convert the "body_type" column to title case.
---
Check the dtype of the "body_type" column.
"""

# solution

# Print the frequency table of body_type and include NaN values
print(used_cars['body_type'].value_counts(dropna=False))

#----------------------------------#

# Print the frequency table of body_type and include NaN values
print(used_cars["body_type"].value_counts(dropna=False))

# Update NaN values
used_cars.loc[used_cars['body_type'].isna(), 'body_type'] = 'other'

#----------------------------------#

# Print the frequency table of body_type and include NaN values
print(used_cars["body_type"].value_counts(dropna=False))

# Update NaN values
used_cars.loc[used_cars["body_type"].isna(), "body_type"] = "other"

# Convert body_type to title case
used_cars["body_type"] = used_cars["body_type"].str.title()

#----------------------------------#

# Print the frequency table of body_type and include NaN values
print(used_cars["body_type"].value_counts(dropna=False))

# Update NaN values
used_cars.loc[used_cars["body_type"].isna(), "body_type"] = "other"

# Convert body_type to title case
used_cars["body_type"] = used_cars["body_type"].str.title()

# Check the dtype
print(used_cars["body_type"].dtype)

#----------------------------------#

# exercise 02

"""
Overcoming pitfalls: using NumPy arrays

A local used car company manually appraises each car that they add to their inventory. When a new car comes in, they select from a drop-down menu, giving the car a rating between 1 and 5. A 1 means that the car probably won't sell as is, but a 5 indicates the car will definitely sell without a problem.

With over 38,000 cars in their inventory, the company has asked you to give them an average "sellability" of their cars. For this exercise, use the used_cars dataset. The column of interest is called "Sale Rating" and it is currently a categorical column.
"""

# steps

"""
Print the frequency table of the "Sale Rating" column of the used_cars dataset.
---
Question

Now on to the key question: what is the average "saleability" of the used cars? What happens if you try the following code:

average_score = used_cars["Sale Rating"].mean()

Try it out in the console and then choose the best answer.
Possible Answers

    It will automatically convert the column to an integer type and return the mean.
    A type error, because numpy doesn't understand the categorical dtype. (Answer)
    A value error, because numpy doesn't expect categorical columns to be numeric.
---
Correct the second statement by converting the column to type int before calling .mean().
"""

# solution

# Print the frequency table of Sale Rating
print(used_cars['Sale Rating'].value_counts())

#----------------------------------#

# Print the frequency table of Sale Rating
print(used_cars["Sale Rating"].value_counts())

# Find the average score
average_score = used_cars["Sale Rating"].astype(int).mean()

# Print the average
print(average_score)

#----------------------------------#

# exercise 03

"""
Create a label encoding and map

A used car company believes that they can predict a car's sales price reasonably well using their used_cars dataset. One of the variables they want to use, "color", needs to be converted to codes. The company believes that a car's color will be important when predicting sales price.
"""

# steps

"""
Convert the color column to a categorical Series.
---
Create a new column, "color_code", by creating a label encoding for the variable "color".
---
Before you forget which codes belong to which categories, create a color map using the codes and categories objects.
---
Print the new color map to see which codes map to which categories.
"""

# solution

# Convert to categorical and print the frequency table
used_cars["color"] = used_cars['color'].astype('category')
print(used_cars["color"].value_counts())

#----------------------------------#

# Convert to categorical and print the frequency table
used_cars["color"] = used_cars["color"].astype("category")
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars['color'].cat.codes

#----------------------------------#

# Convert to categorical and print the frequency table
used_cars["color"] = used_cars["color"].astype("category")
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars["color"].cat.codes

# Create codes and categories objects
codes = used_cars['color_code']
categories = used_cars["color"]
color_map = dict(zip(codes, categories))

#----------------------------------#

# Convert to categorical and print the frequency table
used_cars["color"] = used_cars["color"].astype("category")
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars["color"].cat.codes

# Create codes and categories objects
codes = used_cars["color"].cat.codes
categories = used_cars["color"]
color_map = dict(zip(codes, categories))

# Print the map
print(color_map)

#----------------------------------#

# exercise 04

"""
Using saved mappings

You are using a subset of a dataset and have been asked to create visualizations summarizing the output. As the dataset currently stands, all you see are numbers! Luckily, you had created and saved dictionaries (color_map, fuel_map, and transmission_map) that will map these columns back to their original categorical names. The dataset used_cars_updated has been preloaded. A preview of the dataset is shown. Check out the console to view the column data types.

       engine_fuel  color  transmission  price_usd
0                3      8             0   10900.00
1                3      1             0    5000.00
2                3      7             0    2800.00

"""

# steps

"""
Update the "color" column back to its original values using the color_map dictionary.
Update the "engine_fuel" column back to its original values using the fuel_map dictionary.
Update the "transmission" column back to its original values using the transmission_map dictionary.
Use .info() on the dataset to see if the dtypes have changed.
"""

# solution

# Update the color column using the color_map
used_cars_updated["color"] = used_cars_updated['color'].map(color_map)
# Update the engine fuel column using the fuel_map
used_cars_updated["engine_fuel"] = used_cars_updated['engine_fuel'].map(fuel_map)
# Update the transmission column using the transmission_map
used_cars_updated["transmission"] = used_cars_updated['transmission'].map(transmission_map)

# Print the info statement
print(used_cars_updated.info())

#----------------------------------#

# exercise 05

"""
Creating a Boolean encoding

In preparation for running machine learning models to estimate the sale price of used cars, you are starting to analyze the available columns of the used_cars dataset and want to create columns that can be used in training. One of the managers of a used car dealership has said that the manufacturer of the car is the most important aspect he considers when setting prices. You will begin by exploring the manufacturer_name column.
"""

# steps

"""
Print the frequency table of the "manufacturer_name" column.
---
Create a column, "is_volkswagen", that is True when "manufacturer_name" contains "Volkswagen" and False otherwise.
---
Update the code so that a 1 is used instead of True and a 0 is used instead of False so Python can use this column in algorithms.
---
Print out a frequency table for the newly created column.
"""

# solution

# Print the manufacturer name frequency table
print(used_cars['manufacturer_name'].value_counts())

#----------------------------------#

# Print the manufacturer name frequency table
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column based on if the manufacturer name that contain Volkswagen
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains('Volkswagen', regex=False), True, False
)

#----------------------------------#

# Print the manufacturer name frequency table
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column based on if the manufacturer name that contain Volkswagen: using 0s an 1s
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)

#----------------------------------#

# Print the "manufacturer_name" frequency table.
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column for the most common manufacturer name
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)
  
# Check the final frequency table
print(used_cars['is_volkswagen'].value_counts())

#----------------------------------#
# exercise 06

"""
One-hot encoding specific columns

A local used car dealership wants your help in predicting the sale price of their vehicles. If you use one-hot encoding on the entire used_cars dataset, the new dataset has over 1,200 columns. You are worried that this might lead to problems when training your machine learning models to predict price. You have decided to try a simpler approach and only use one-hot encoding on a few columns.
"""

# steps

"""
# Create one-hot encoding for just two columns
used_cars_simple = pd.get_dummies(
  used_cars,
  # Specify the columns from the instructions
  columns = ['manufacturer_name', 'transmission'],
  # Set the prefix
  prefix='dummy'
)

# Print the shape of the new dataset
print(used_cars_simple.shape)
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

# exercise 0

"""

"""

# steps

"""

"""

# solution



#----------------------------------#