# exercise 01

"""
Testing sample size

In order to conduct a hypothesis test and be sure that the result is fair, a sample must meet three requirements: 
it is a random sample of the population, the observations are independent, and there are enough observations. 
Of these, only the last condition is easily testable with code.

The minimum sample size depends on the type of hypothesis tests you want to perform. You'll now test some scenarios on the late_shipments dataset.

Note that the .all() method from pandas can be used to check if all elements are true. 
For example, given a DataFrame df with numeric entries, you check to see if all its elements are less than 5, using (df < 5).all().

late_shipments is available, and pandas is loaded as pd.
"""

# steps

"""

    Get the count of each value in the freight_cost_group column of late_shipments.
    Insert a suitable number to inspect whether the counts are "big enough" for a two sample t-test.
---

    Get the count of each value in the late column of late_shipments.
    Insert a suitable number to inspect whether the counts are "big enough" for a one sample proportion test.
---

    Get the count of each value in the freight_cost_group column of late_shipments grouped by vendor_inco_term.
    Insert a suitable number to inspect whether the counts are "big enough" for a chi-square independence test.
---

    Get the count of each value in the shipment_mode column of late_shipments.
    Insert a suitable number to inspect whether the counts are "big enough" for an ANOVA test.

"""

# solution

# Count the freight_cost_group values
counts = late_shipments['freight_cost_group'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())

#----------------------------------#

# Count the late values
counts = late_shipments['late'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 10).all())

#----------------------------------#

# Count the values of freight_cost_group grouped by vendor_inco_term
counts = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 5).all())

#----------------------------------#

# Count the shipment_mode values
counts = late_shipments['shipment_mode'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())

#----------------------------------#

# exercise 02

"""
Wilcoxon signed-rank test

You'll explore the difference between the proportion of county-level votes for the Democratic candidate in 2012 and 2016 to identify if the difference is significant.

sample_dem_data is available, and has columns dem_percent_12 and dem_percent_16 in addition to state and county names. 
The following packages have also been loaded: pingouin and pandas as pd.
"""

# steps

"""
Conduct a paired t-test on the percentage columns using an appropriate alternative hypothesis.
---
Conduct a Wilcoxon-signed rank test on the same columns.
"""

# solution

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results =  pingouin.ttest(x = sample_dem_data['dem_percent_12'], y = sample_dem_data['dem_percent_16'], paired = True, alternative = 'two-sided')




# Print paired t-test results
print(paired_test_results)

#----------------------------------#

# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(x = sample_dem_data['dem_percent_12'], y = sample_dem_data['dem_percent_16'], alternative = 'two-sided')



# Print Wilcoxon test results
print(wilcoxon_test_results)

#----------------------------------#

# exercise 03

"""
Wilcoxon-Mann-Whitney

Another class of non-parametric hypothesis tests are called rank sum tests. 
Ranks are the positions of numeric values from smallest to largest. 
Think of them as positions in running events: whoever has the fastest (smallest) time is rank 1, second fastest is rank 2, and so on.

By calculating on the ranks of data instead of the actual values, you can avoid making assumptions about the distribution of the test statistic. 
It's more robust in the same way that a median is more robust than a mean.

One common rank-based test is the Wilcoxon-Mann-Whitney test, which is like a non-parametric t-test.

late_shipments is available, and the following packages have been loaded: pingouin and pandas as pd.
"""

# steps

"""

    Select weight_kilograms and late from late_shipments, assigning the name weight_vs_late.
    Convert weight_vs_late from long-to-wide format, setting columns to 'late'.
    Run a Wilcoxon-Mann-Whitney test for a difference in weight_kilograms when the shipment was late and on-time.

"""

# solution

# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[['weight_kilograms', 'late']]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(columns='late', 
                                           values='weight_kilograms')


# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(x = weight_vs_late_wide['No'], y = weight_vs_late_wide['Yes'], alternative = 'two-sided')



# Print the test results
print(wmw_test)

#----------------------------------#

# exercise 04

"""
Kruskal-Wallis

Recall that the Kruskal-Wallis test is a non-parametric version of an ANOVA test, comparing the means across multiple groups.

late_shipments is available, and the following packages have been loaded: pingouin and pandas as pd.
"""

# steps

"""
Run a Kruskal-Wallis test on weight_kilograms between the different shipment modes in late_shipments.
"""

# solution

# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(data = late_shipments, dv = 'weight_kilograms', between = 'shipment_mode')



# Print the results
print(kw_test)

#----------------------------------#