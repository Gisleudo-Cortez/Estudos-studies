# exercise 01

"""
Two sample mean test statistic

The hypothesis test for determining if there is a difference between the means of two populations uses a different type of test statistic to the z-scores you saw in Chapter 1. 
It's called "t", and it can be calculated from three values from each sample using this equation.

While trying to determine why some shipments are late, you may wonder if the weight of the shipments that were on time is less than the weight of the shipments that were late. 
The late_shipments dataset has been split into a "yes" group, where late == "Yes" and a "no" group where late == "No". 
The weight of the shipment is given in the weight_kilograms variable.
The sample means for the two groups are available as xbar_no and xbar_yes. 
The sample standard deviations are s_no and s_yes. The sample sizes are n_no and n_yes. numpy is also loaded as np.
"""

# steps

"""
Calculate the numerator of the t test statistic.
Calculate the denominator of the t test statistic.
Use those two numbers to calculate the t test statistic.
"""

# solution

# Calculate the numerator of the test statistic
numerator = (xbar_yes - xbar_no)

# Calculate the denominator of the test statistic
denominator = np.sqrt((s_yes ** 2 / n_yes) + (s_no ** 2 / n_no))

# Calculate the test statistic
t_stat = numerator / denominator

# Print the test statistic
print(t_stat)

#----------------------------------#

# exercise 02

"""
The t-distribution

The t-distribution is used to calculate the p-value from the t test statistic, and having a sense of how the PDF and CDF look can help you understand this calculation. 
It has two parameters: the degrees of freedom, and the non-centrality parameter.

The plots show the PDF and CDF for a t-distribution (solid black line), and for comparison show a standard normal distribution with mean 0 and variance 1 (gray dotted line).

Which statement about the the t-distribution is true?
"""

# steps

"""
Like the normal distribution, the PDF of a central t-distribution is always symmetric.
As you increase the degrees of freedom, the tails of the t-distribution get fatter.
As you increase the degrees of freedom, the t-distribution PDF and CDF curves get closer to those of a normal distribution. (Answer)
As you increase the non-centrality, the t-distribution PDF and CDF curves get closer to those of a normal distribution.
"""

# solution



#----------------------------------#

# exercise 03

"""
From t to p

Previously, you calculated the test statistic for the two-sample problem of whether the mean weight of shipments is smaller for shipments that weren't late (late == "No") 
compared to shipments that were late (late == "Yes"). 
In order to make decisions about it, you need to transform the test statistic with a cumulative distribution function to get a p-value.

Recall the hypotheses:

H0: The mean weight of shipments that weren't late is the same as the mean weight of shipments that were late.

HA: The mean weight of shipments that weren't late is less than the mean weight of shipments that were late.

The test statistic, t_stat, is available, as are the samples sizes for each group, n_no and n_yes. Use a significance level of alpha = 0.05.

t has also been imported from scipy.stats.
"""

# steps

"""
Question

What type of test does the alternative hypothesis indicate that we need?
Possible Answers

    Two-tailed
    Left-tailed (Answer)
    Right-tailed
---

    Calculate the degrees of freedom for the test.
    Compute the p-value using the test statistic, t_stat.
---
Question

What decision should you make based on the results of the hypothesis test?
Possible Answers

    Fail to reject the null hypothesis.
    Reject the null hypothesis. (Answer)
    You can't conclude anything from this hypothesis test.
"""

# solution

# Calculate the degrees of freedom
degrees_of_freedom = (n_no + n_yes) - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, df = degrees_of_freedom)

# Print the p_value
print(p_value)

#----------------------------------#

# exercise 04

"""
Visualizing the difference

Before you start running hypothesis tests, it's a great idea to perform some exploratory data analysis; that is, calculating summary statistics and visualizing distributions.

Here, you'll look at the proportion of county-level votes for the Democratic candidate in 2012 and 2016, sample_dem_data. 
Since the counties are the same in both years, these samples are paired. The columns containing the samples are dem_percent_12 and dem_percent_16.

dem_votes_potus_12_16 is available as sample_dem_data. pandas and matplotlib.pyplot are loaded with their usual aliases.
"""

# steps

"""
Create a new diff column containing the percentage of votes for the democratic candidate in 2012 minus the percentage of votes for the democratic candidate in 2016.
---

    Calculate the mean of the diff column as xbar_diff.
---
Calculate the standard deviation of the diff column as s_diff.
---

    Plot a histogram of the diff column with 20 bins.

"""

# solution

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Print sample_dem_data
print(sample_dem_data)

#----------------------------------#

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Print xbar_diff
print(xbar_diff)

#----------------------------------#

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std(ddof = 1)

# Print s_diff
print(s_diff)

#----------------------------------#

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins = 20)
plt.show()

#----------------------------------#

# exercise 05

"""
Using ttest()

Manually calculating test statistics and transforming them with a CDF to get a p-value is a lot of effort to compare two sample means. 
The comparison of two sample means is called a t-test, and the pingouin Python package has a .ttest() method to accomplish it. 
This method provides some flexibility in how you perform the test.

As in the previous exercise, you'll explore the difference between the proportion of county-level votes for the Democratic candidate in 2012 and 2016 
to identify if the difference is significant. The hypotheses are as follows:

H0: The proportion of democratic votes in 2012 and 2016 were the same.

HA: The proportion of democratic votes in 2012 and 2016 were different.

sample_dem_data is available and has the columns diff, dem_percent_12, and dem_percent_16 in addition to the state and county names. 
pingouin and has been loaded along with pandas as pd.
"""

# steps

"""
Conduct a t-test on the sample differences (the diff column of sample_dem_data), using an appropriate alternative hypothesis chosen from "two-sided", "less", and "greater".
---
Question

What's the correct decision from the t-test, assuming a = 0.01 ?

Possible Answers

    Fail to reject the null hypothesis.
    Reject the null hypothesis. (Answer)
    You can't conclude anything from this hypothesis test.
---
Conduct a paired test on the democratic votes in 2012 and 2016 (the dem_percent_12 and dem_percent_16 columns of sample_dem_data), using an appropriate alternative hypothesis.
---
Question

Compare the paired t-test to an (inappropriate) unpaired test on the same data. How does the p-value change?

pingouin.ttest(x=sample_dem_data['dem_percent_12'], 
               y=sample_dem_data['dem_percent_16'], 
               alternative="two-sided")

Possible Answers

    The p-value from the unpaired test is smaller than the p-value from the paired test.
    The p-value from the unpaired test is equal to the p-value from the paired test.
    The p-value from the unpaired test is greater than than the p-value from the paired test. (Answer)
"""

# solution

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'],
y=0,
alternative="two-sided")


                              
# Print the test results
print(test_results)

#----------------------------------#

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], 
                              y=0, 
                              alternative="two-sided")

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x = sample_dem_data['dem_percent_12'], y = sample_dem_data['dem_percent_16'], paired = True, alternative = 'two-sided')



                              
# Print the paired test results
print(paired_test_results)

#----------------------------------#

# exercise 06

"""
Visualizing many categories

So far in this chapter, we've only considered the case of differences in a numeric variable between two categories. 
Of course, many datasets contain more categories. 
Before you get to conducting tests on many categories, it's often helpful to perform exploratory data analysis (EDA), 
calculating summary statistics for each group and visualizing the distributions of the numeric variable for each category using box plots.

Here, we'll return to the late shipments data, and how the price of each package (pack_price) varies between the three shipment modes (shipment_mode): "Air", "Air Charter", and "Ocean".

late_shipments is available; pandas and matplotlib.pyplot are loaded with their standard aliases, and seaborn is loaded as sns.
"""

# steps

"""
Group late_shipments by shipment_mode and calculate the mean pack_price for each group, storing the result in xbar_pack_by_mode.
---
Group late_shipments by shipment_mode and calculate the standard deviation pack_price for each group, storing the result in s_pack_by_mode.
---
Create a boxplot from late_shipments with "pack_price" as x and "shipment_mode" as y.
"""

# solution

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].mean()

# Print the grouped means
print(xbar_pack_by_mode)

#----------------------------------#

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].std(ddof = 1)

# Print the grouped standard deviations
print(s_pack_by_mode)

#----------------------------------#

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x = 'pack_price', y = 'shipment_mode', data = late_shipments)
plt.show()

#----------------------------------#

# exercise 07

"""
Conducting an ANOVA test

The box plots made it look like the distribution of pack price was different for each of the three shipment modes. 
However, it didn't tell us whether the mean pack price was different in each category. 
To determine that, we can use an ANOVA test. The null and alternative hypotheses can be written as follows.

H0: Pack prices for every category of shipment mode are the same.

HA: Pack prices for some categories of shipment mode are different.

Use a significance level of 0.1.

late_shipments is available and pingouin has been loaded.
"""

# steps

"""
Run an ANOVA on late_shipments investigating 'pack_price' (the dependent variable) between the groups of 'shipment_mode'.
---
Assuming a significance level of 0.1, should you reject the null hypothesis that there is no difference in pack prices between shipment modes?
Possible Answers

    Yes. The p-value is greater than or equal to the significance level, so the null hypothesis should be rejected.
    Yes. The p-value is less than or equal to the significance level, so the null hypothesis should be rejected. (Answer)
    No. The p-value is greater than or equal to the significance level, so the null hypothesis should fail to be rejected.
    No. The p-value is less than or equal to the significance level, so the null hypothesis should fail to be rejected.
"""

# solution

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data = late_shipments, dv = 'pack_price', between = 'shipment_mode')



# Print anova_results
print(anova_results)

#----------------------------------#

# exercise 08

"""
Pairwise t-tests

The ANOVA test didn't tell you which categories of shipment mode had significant differences in pack prices. 
To pinpoint which categories had differences, you could instead use pairwise t-tests.

late_shipments is available and pingouin has been loaded.
"""

# steps

"""
Perform pairwise t-tests on late_shipments's pack_price variable, grouped by shipment_mode, without doing any p-value adjustment.
---
Modify the pairwise t-tests to use the Bonferroni p-value adjustment.
---
Question

Using the Bonferroni correction results and assuming a significance level of 0.1, for which pairs of shipment modes should you reject the null hypothesis that the pack prices are equal?
Possible Answers

    "Ocean" and "Air Charter"; "Ocean" and "Air"; "Air Charter" and "Air". (Answer)
    "Ocean" and "Air" and also "Air Charter" and "Air".
    "Ocean" and "Air" only.
    "Ocean" and "Air Charter" only.
"""

# solution

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_tests(data=late_shipments,
dv="pack_price",
between="shipment_mode",
padjust="none") 




# Print pairwise_results
print(pairwise_results)

#----------------------------------#

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(pairwise_results)

#----------------------------------#