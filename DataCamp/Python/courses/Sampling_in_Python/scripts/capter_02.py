# exercise 01

"""
Simple random sampling

The simplest method of sampling a population is the one you've seen already. 
It is known as simple random sampling (sometimes abbreviated to "SRS"), and involves picking rows at random, one at a time, where each row has the same chance of being picked as any other.

In this chapter, you'll apply sampling methods to a synthetic (fictional) employee attrition dataset from IBM, where "attrition" in this context means leaving the company.

attrition_pop is available; pandas as pd is loaded.
"""

# steps

"""

    Sample 70 rows from attrition_pop using simple random sampling, setting the random seed to 18900217.
    Print the sample dataset, attrition_samp. What do you notice about the indices?

"""

# solution

# Sample 70 rows using simple random sampling and set the seed
attrition_samp = attrition_pop.sample(n = 70, random_state = 18900217)

# Print the sample
print(attrition_samp)

#----------------------------------#

# exercise 02

"""
Systematic sampling

One sampling method that avoids randomness is called systematic sampling. Here, you pick rows from the population at regular intervals.

For example, if the population dataset had one thousand rows, and you wanted a sample size of five, you could pick rows 0, 200, 400, 600, and 800.

attrition_pop is available; pandas has been pre-loaded as pd.
"""

# steps

"""

    Set the sample size to 70.
    Calculate the population size from attrition_pop.
    Calculate the interval between the rows to be sampled.
---
Systematically sample attrition_pop to get the rows of the population at each interval, starting at 0; assign the rows to attrition_sys_samp.
"""

# solution

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

#----------------------------------#

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop[:: interval]

# Print the sample
print(attrition_sys_samp)

#----------------------------------#

# exercise 03

"""
Is systematic sampling OK?

Systematic sampling has a problem: 
if the data has been sorted, or there is some sort of pattern or meaning behind the row order, then the resulting sample may not be representative of the whole population. 
The problem can be solved by shuffling the rows, but then systematic sampling is equivalent to simple random sampling.

Here you'll look at how to determine whether or not there is a problem.

attrition_pop is available; pandas is loaded as pd, and matplotlib.pyplot as plt.
"""

# steps

"""

    Add an index column to attrition_pop, assigning the result to attrition_pop_id.
    Create a scatter plot of YearsAtCompany versus index for attrition_pop_id using pandas .plot().
---

    Randomly shuffle the rows of attrition_pop.
    Reset the row indexes, and add an index column to attrition_pop.
    Repeat the scatter plot of YearsAtCompany versus index, this time using attrition_shuffled.
---
Question

Does a systematic sample always produce a sample similar to a simple random sample?
Possible Answers

    Yes. All sampling (random or non-random) methods will lead us to similar results.
    Yes. We should always expect a representative sample for both systematic and simple random sampling.
    No. This only holds if a seed has been set for both processes.
    No. This is not true if the data is sorted in some way. (Answer)
"""

# solution

# Add an index column to attrition_pop
attrition_pop_id = attrition_pop.reset_index()
# Plot YearsAtCompany vs. index for attrition_pop_id
attrition_pop_id.plot(y = 'YearsAtCompany', x = 'index', kind = 'scatter')
plt.show()

#----------------------------------#

# Shuffle the rows of attrition_pop
attrition_shuffled = attrition_pop.sample(frac=1)

# Reset the row indexes and create an index column
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

# Plot YearsAtCompany vs. index for attrition_shuffled
attrition_shuffled.plot(y = 'YearsAtCompany', x = 'index', kind = 'scatter')
plt.show()

#----------------------------------#

# exercise 04

"""
Proportional stratified sampling

If you are interested in subgroups within the population, then you may need to carefully control the counts of each subgroup within the population. 
Proportional stratified sampling results in subgroup sizes within the sample that are representative of the subgroup sizes within the population. 
It is equivalent to performing a simple random sample on each subgroup.

attrition_pop is available; pandas is loaded with its usual alias.
"""

# steps

"""
Get the proportion of employees by Education level from attrition_pop.
---
Use proportional stratified sampling on attrition_pop to sample 40% of each Education group, setting the seed to 2022.
---
Get the proportion of employees by Education level from attrition_strat.
"""

# solution

# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize = True)

# Print education_counts_pop
print(education_counts_pop)

#----------------------------------#

# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
.sample(frac = 0.4, random_state=2022)


# Print the sample
print(attrition_strat)

#----------------------------------#

# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
	.sample(frac=0.4, random_state=2022)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat['Education'].value_counts(normalize = True)

# Print education_counts_strat
print(education_counts_strat)

#----------------------------------#

# exercise 05

"""
Equal counts stratified sampling

If one subgroup is larger than another subgroup in the population, but you don't want to reflect that difference in your analysis, 
then you can use equal counts stratified sampling to generate samples where each subgroup has the same amount of data. 
For example, if you are analyzing blood types, O is the most common blood type worldwide, but you may wish to have equal amounts of O, A, B, and AB in your sample.

attrition_pop is available; pandas is loaded with its usual alias.
"""

# steps

"""
Use equal counts stratified sampling on attrition_pop to get 30 employees from each Education group, setting the seed to 2022.
---
Get the proportion of employees by Education level from attrition_eq.
"""

# solution

# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education').sample(n = 30, random_state = 2022)


# Print the sample
print(attrition_eq)

#----------------------------------#


# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
	.sample(n=30, random_state=2022)      

# Get the proportions from attrition_eq
education_counts_eq = attrition_eq['Education'].value_counts(normalize = True)

# Print the results
print(education_counts_eq)

#----------------------------------#

# exercise 06

"""
Weighted sampling

Stratified sampling provides rules about the probability of picking rows from your dataset at the subgroup level. 
A generalization of this is weighted sampling, which lets you specify rules about the probability of picking rows at the row level. 
The probability of picking any given row is proportional to the weight value for that row.

attrition_pop is available; pandas, matplotlib.pyplot, and numpy are loaded with their usual aliases.
"""

# steps

"""
Plot YearsAtCompany from attrition_pop as a histogram with bins of width 1 from 0 to 40.
---
Sample 400 employees from attrition_pop weighted by YearsAtCompany.
---
Plot YearsAtCompany from attrition_weight as a histogram with bins of width 1 from 0 to 40.
---
Question

Which is higher? The mean YearsAtCompany from attrition_pop or the mean YearsAtCompany from attrition_weight?
Possible Answers

    Population mean.
    Both means are identical.
    Sample mean. (Answer)
    It is impossible to calculate the two means.
"""

# solution

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins = np.arange(0, 41, 1))
plt.show()

#----------------------------------#

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n = 400, weights = 'YearsAtCompany')

# Print the sample
print(attrition_weight)

#----------------------------------#

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight['YearsAtCompany'].hist(bins = np.arange(0, 41, 1))
plt.show()

#----------------------------------#

# exercise 07

"""
Performing cluster sampling

Now that you know when to use cluster sampling, it's time to put it into action. 
In this exercise, you'll explore the JobRole column of the attrition dataset. You can think of each job role as a subgroup of the whole population of employees.

attrition_pop is available; pandas is loaded with its usual alias, and the random package is available. A seed of 19790801 has also been set with random.seed().
"""

# steps

"""
    Create a list of unique JobRole values from attrition_pop, and assign to job_roles_pop.
    Randomly sample four JobRole values from job_roles_pop.
---
Subset attrition_pop for the sampled job roles by filtering for rows where JobRole is in job_roles_samp.
---

    Remove any unused categories from JobRole.
    For each job role in the filtered dataset, take a random sample of ten rows, setting the seed to 2022.

"""

# solution

# Create a list of unique JobRole values
job_roles_pop = list(attrition_pop['JobRole'].unique())

# Randomly sample four JobRole values
job_roles_samp = random.sample(job_roles_pop, k = 4)

# Print the result
print(job_roles_samp)

#----------------------------------#

# Create a list of unique JobRole values
job_roles_pop = list(attrition_pop['JobRole'].unique())

# Randomly sample four JobRole values
job_roles_samp = random.sample(job_roles_pop, k=4)

# Filter for rows where JobRole is in job_roles_samp
jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition]

# Print the result
print(attrition_filtered)

#----------------------------------#

# Create a list of unique JobRole values
job_roles_pop = list(attrition_pop['JobRole'].unique())

# Randomly sample four JobRole values
job_roles_samp = random.sample(job_roles_pop, k=4)

# Filter for rows where JobRole is in job_roles_samp
jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition]

# Remove categories with no rows
attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()

# Randomly sample 10 employees from each sampled job role
attrition_clust = attrition_filtered.groupby('JobRole').sample(n = 10, random_state = 2022)


# Print the sample
print(attrition_clust)

#----------------------------------#

# exercise 08

"""
3 kinds of sampling

You're going to compare the performance of point estimates using simple, stratified, and cluster sampling. Before doing that, you'll have to set up the samples.

You'll use the RelationshipSatisfaction column of the attrition_pop dataset, which categorizes the employee's relationship with the company. 
It has four levels: Low, Medium, High, and Very_High. 
pandas has been loaded with its usual alias, and the random package has been loaded.
"""

# steps

"""
Perform simple random sampling on attrition_pop to get one-quarter of the population, setting the seed to 2022.
---
Perform stratified sampling on attrition_pop to sample one-quarter of each RelationshipSatisfaction group, setting the seed to 2022.
---

    Create a list of unique values from attrition_pop's RelationshipSatisfaction column.
    Randomly sample satisfaction_unique to get two values.
    Subset the population for rows where RelationshipSatisfaction is in satisfaction_samp and clear any unused categories from RelationshipSatisfaction; assign to attrition_clust_prep.
    Perform cluster sampling on the selected satisfaction groups, sampling one quarter of the population and setting the seed to 2022.

"""

# solution

# Perform simple random sampling to get 0.25 of the population
attrition_srs = attrition_pop.sample(frac = 0.25, random_state = 2022)

#----------------------------------#

# Perform stratified sampling to get 0.25 of each relationship group
attrition_strat = attrition_pop.groupby('RelationshipSatisfaction').sample(frac = 0.25, random_state = 2022)


#----------------------------------#

# Create a list of unique RelationshipSatisfaction values
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())

# Randomly sample 2 unique satisfaction values
satisfaction_samp = random.sample(satisfaction_unique, k =2)

# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()

# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop
attrition_clust = attrition_clust_prep.groupby('RelationshipSatisfaction').sample(n = len(attrition_pop)//4, random_state = 2022)


#----------------------------------#

# exercise 09

"""
Comparing point estimates

Now that you have three types of sample (simple, stratified, and cluster), you can compare point estimates from each sample to the population parameter. 
That is, you can calculate the same summary statistic on each sample and see how it compares to the summary statistic for the population.

Here, we'll look at how satisfaction with the company affects whether or not the employee leaves the company. 
That is, you'll calculate the proportion of employees who left the company (they have an Attrition value of 1) for each value of RelationshipSatisfaction.

attrition_pop, attrition_srs, attrition_strat, and attrition_clust are available; pandas is loaded with its usual alias.
"""

# steps

"""
Group attrition_pop by RelationshipSatisfaction levels and calculate the mean of Attrition for each level.
---
Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the simple random sample, attrition_srs.
---
Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the stratified sample, attrition_strat.
---
Calculate the proportion of employee attrition for each relationship satisfaction group, this time on the cluster sample, attrition_clust.
---
"""

# solution

# Mean Attrition by RelationshipSatisfaction group
mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_pop)

#----------------------------------#

# Calculate the same thing for the simple random sample 
mean_attrition_srs = attrition_srs.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_srs)

#----------------------------------#

# Calculate the same thing for the stratified sample 
mean_attrition_strat = attrition_strat.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_strat)

#----------------------------------#

# Calculate the same thing for the cluster sample 
mean_attrition_clust = attrition_clust.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_clust)

#----------------------------------#