# exercise 01

"""
Coefficient of determination

The coefficient of determination is a measure of how well the linear regression line fits the observed values. For simple linear regression, it is equal to the square of the correlation between the explanatory and response variables.

Here, you'll take another look at the second stage of the advertising pipeline: modeling the click response to impressions. Two models are available: mdl_click_vs_impression_orig models n_clicks versus n_impressions. mdl_click_vs_impression_trans is the transformed model you saw in Chapter 2. It models n_clicks to the power of 0.25 versus n_impressions to the power of 0.25.
"""

# Instructions

"""
Print the summary of mdl_click_vs_impression_orig.
Do the same for mdl_click_vs_impression_trans.
---
Print the coefficient of determination for mdl_click_vs_impression_orig.
Do the same for mdl_click_vs_impression_trans.
---
Question

mdl_click_vs_impression_orig has a coefficient of determination of 0.89. Which statement about the model is true?
Possible Answers

    The number of clicks explains 89% of the variability in the number of impressions.
    ---
    The number of impressions explains 89% of the variability in the number of clicks. (Answer)
    ---
    The model is correct 89% of the time.
    ---
    The correlation between the number of impressions and the number of clicks is 0.89.
---
Question

Which model does the coefficient of determination suggest gives a better fit?
Possible Answers

    The original model, mdl_click_vs_impression_orig.
    ---
    The transformed model, mdl_click_vs_impression_trans. (Answer)
    ---
    Both models are equally good.
    ---
    Coefficient of determination doesn't measure the goodness of fit of a regression model.
"""

# solution

# Print a summary of mdl_click_vs_impression_orig
print(mdl_click_vs_impression_orig.summary())

# Print a summary of mdl_click_vs_impression_trans
print(mdl_click_vs_impression_trans.summary())

#----------------------------------#

# Print the coeff of determination for mdl_click_vs_impression_orig
print(mdl_click_vs_impression_orig.rsquared)

# Print the coeff of determination for mdl_click_vs_impression_trans
print(mdl_click_vs_impression_trans.rsquared)

#----------------------------------#

# Conclusion

"""
Cool coefficient of determination calculating! The transformed model has a higher coefficient of determination than the original model, suggesting that it gives a better fit to the data.
"""

# exercise 02

"""
Residual standard error

Residual standard error (RSE) is a measure of the typical size of the residuals. Equivalently, it's a measure of how wrong you can expect predictions to be. Smaller numbers are better, with zero being a perfect fit to the data.

Again, you'll look at the models from the advertising pipeline, mdl_click_vs_impression_orig and mdl_click_vs_impression_trans.
"""

# Instructions

"""

    Calculate the MSE of mdl_click_vs_impression_orig, assigning to mse_orig.
    Using mse_orig, calculate and print the RSE of mdl_click_vs_impression_orig.
    Do the same for mdl_click_vs_impression_trans.
---
Question

mdl_click_vs_impression_orig has an RSE of about 20. Which statement is true?
Possible Answers

    The model explains 20% of the variability in the number of clicks.
    
    20% of the residuals are typically greater than the observed values.
    
    The typical difference between observed number of clicks and predicted number of clicks is 20.
    
    The typical difference between observed number of impressions and predicted number of impressions is 20. (Answer)
    
    The model predicts that you get one click for every 20 observed impressions.
---
Question

Which model does the RSE suggest gives more accurate predictions? mdl_click_vs_impression_orig has an RSE of about 20, mdl_click_vs_impression_trans has an RSE of about 0.2.
Possible Answers

    The original model, mdl_click_vs_impression_orig.
    
    The transformed model, mdl_click_vs_impression_trans. (Answer)
    
    Both models are equally good.
    
    RSE doesn't measure the accuracy of a regression model.
"""

# solution

# Calculate mse_orig for mdl_click_vs_impression_orig
mse_orig = mdl_click_vs_impression_orig.mse_resid

# Calculate rse_orig for mdl_click_vs_impression_orig and print it
rse_orig = np.sqrt(mse_orig)
print("RSE of original model: ", rse_orig)

# Calculate mse_trans for mdl_click_vs_impression_trans
mse_trans = mdl_click_vs_impression_trans.mse_resid

# Calculate rse_trans for mdl_click_vs_impression_trans and print it
rse_trans = np.sqrt(mse_trans)
print("RSE of transformed model: ", rse_trans)

#----------------------------------#

# Conclusion

"""
Rapid RSE wrangling! RSE is a measure of accuracy for regression models. It even works on other other statistical model types like regression trees, so you can compare accuracy across different classes of models.
"""

# exercise 03

"""
Drawing diagnostic plots

It's time for you to draw these diagnostic plots yourself using the Taiwan real estate dataset and the model of house prices versus number of convenience stores.

taiwan_real_estate is available as a pandas DataFrame and mdl_price_vs_conv is available.
"""

# Instructions

"""
    Create the residuals versus fitted values plot. Add a lowess argument to visualize the trend of the residuals.
---
    Import qqplot() from statsmodels.api.
    Create the Q-Q plot of the residuals.
---
    Create the scale-location plot.

"""

# solution

# Plot the residuals vs. fitted values
sns.residplot(x='n_convenience', y='price_twd_msq', data=taiwan_real_estate, lowess = True)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")

# Show the plot
plt.show()

#----------------------------------#

# Import qqplot
from statsmodels.api import qqplot

# Create the Q-Q plot of the residuals
qqplot(data=mdl_price_vs_conv.resid, fit=True, line="45")

# Show the plot
plt.show()

#----------------------------------#

# Preprocessing steps
model_norm_residuals = mdl_price_vs_conv.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))

# Create the scale-location plot
sns.regplot(x=mdl_price_vs_conv.fittedvalues, y=model_norm_residuals_abs_sqrt, ci=None, lowess=True)
plt.xlabel("Fitted values")
plt.ylabel("Sqrt of abs val of stdized residuals")

# Show the plot
plt.show()

#----------------------------------#

# Conclusion

"""
Perfect plotting! These three diagnostic plots are excellent for sanity-checking the quality of your models.
"""

# exercise 04

"""
Leverage

Leverage measures how unusual or extreme the explanatory variables are for each observation. Very roughly, high leverage means that the explanatory variable has values that are different from other points in the dataset. In the case of simple linear regression, where there is only one explanatory value, this typically means values with a very high or very low explanatory value.

Here, you'll look at highly leveraged values in the model of house price versus the square root of distance from the nearest MRT station in the Taiwan real estate dataset.

Guess which observations you think will have a high leverage, then move the slider to find out.

Which statement is true?
"""

# Instructions

"""
Observations with a large distance to the nearest MRT station have the highest leverage, because these points are furthest away from the linear regression trend line.

Observations with a large distance to the nearest MRT station have the highest leverage, because leverage is proportional to the explanatory variable.

Observations with a large distance to the nearest MRT station have the highest leverage, because most of the observations have a short distance, so long distances are more extreme. (Answer)

Observations with a high price have the highest leverage, because most of the observations have a low price, so high prices are most extreme.
"""

# solution




#----------------------------------#

# Conclusion

"""
Lovely leveraging! Highly leveraged points are the ones with explanatory variables that are furthest away from the others.
"""

# exercise 05

"""
Influence

Influence measures how much a model would change if each observation was left out of the model calculations, one at a time. That is, it measures how different the prediction line would look if you would run a linear regression on all data points except that point, compared to running a linear regression on the whole dataset.

The standard metric for influence is Cook's distance, which calculates influence based on the residual size and the leverage of the point.

You can see the same model as last time: house price versus the square root of distance from the nearest MRT station in the Taiwan real estate dataset.

Guess which observations you think will have a high influence, then move the slider to find out.
"""

# Instructions

"""
Observations far away from the trend line have high influence, because they have large residuals and are far away from other observations. (Answer)

Observations with high prices have high influence, because influence is proportional to the response variable.

Observations far away from the trend line have high influence, because the slope of the trend is negative.

Observations far away from the trend line have high influence, because that increases the leverage of those points.
"""

# solution



#----------------------------------#

# Conclusion

"""
Impressive influence interpretation! The majority of the influential houses were those with prices that were much higher than the model predicted (and one with a price that was much lower).
"""

# exercise 06

"""
Extracting leverage and influence

In the last few exercises, you explored which observations had the highest leverage and influence. Now you'll extract those values from the model.

mdl_price_vs_dist and taiwan_real_estate are available.
"""

# Instructions

"""
Get the summary frame from mdl_price_vs_dist and save as summary_info.
---

    Add the hat_diag column of summary_info to taiwan_real_estate as the leverage column.
    Sort taiwan_real_estate by leverage in descending order and print the head.
---

    Add the cooks_d column from summary_info to taiwan_real_estate as the cooks_dist column.
    Sort taiwan_real_estate by cooks_dist in descending order and print the head.

"""

# solution

# Create summary_info
summary_info = mdl_price_vs_dist.get_influence().summary_frame()

#----------------------------------#

# Create summary_info
summary_info = mdl_price_vs_dist.get_influence().summary_frame()

# Add the hat_diag column to taiwan_real_estate, name it leverage
taiwan_real_estate["leverage"] = summary_info['hat_diag']

# Sort taiwan_real_estate by leverage in descending order and print the head
print(taiwan_real_estate.sort_values('leverage', ascending = False).head())

#----------------------------------#

# Create summary_info
summary_info = mdl_price_vs_dist.get_influence().summary_frame()

# Add the hat_diag column to taiwan_real_estate, name it leverage
taiwan_real_estate["leverage"] = summary_info["hat_diag"]

# Add the cooks_d column to taiwan_real_estate, name it cooks_dist
taiwan_real_estate['cooks_dist'] = summary_info['cooks_d']

# Sort taiwan_real_estate by cooks_dist in descending order and print the head.
print(taiwan_real_estate.sort_values('cooks_dist', ascending = False).head())

#----------------------------------#

# Conclusion

"""

"""