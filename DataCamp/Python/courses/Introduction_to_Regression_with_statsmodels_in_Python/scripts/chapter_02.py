# exercise 01

"""
Predicting house prices

Perhaps the most useful feature of statistical models like linear regression is that you can make predictions. That is, you specify values for each of the explanatory variables, feed them to the model, and get a prediction for the corresponding response variable. The code flow is as follows.

explanatory_data = pd.DataFrame({"explanatory_var": list_of_values})
predictions = model.predict(explanatory_data)
prediction_data = explanatory_data.assign(response_var=predictions)

Here, you'll make predictions for the house prices in the Taiwan real estate dataset.

taiwan_real_estate is available. The fitted linear regression model of house price versus number of convenience stores is available as mdl_price_vs_conv. For future exercises, when a model is available, it will also be fitted.
"""

# steps

"""

    Import the numpy package using the alias np.
    Create a DataFrame of explanatory data, where the number of convenience stores, n_convenience, takes the integer values from zero to ten.
    Print explanatory_data.
---

    Use the model mdl_price_vs_conv to make predictions from explanatory_data and store it as price_twd_msq.
    Print the predictions.
---
Create a DataFrame of predictions named prediction_data. Start with explanatory_data, then add an extra column, price_twd_msq, containing the predictions you created in the previous step.
"""

# solution

# Import numpy with alias np
import numpy as np

# Create the explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0,11)})

# Print it
print(explanatory_data)

#----------------------------------#

# Import numpy with alias np
import numpy as np

# Create explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)

# Print it
print(price_twd_msq)

#----------------------------------#

# Import numpy with alias np
import numpy as np

# Create explanatory_data 
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)

# Create prediction_data
prediction_data = explanatory_data.assign(
    price_twd_msq = price_twd_msq)

# Print the result
print(prediction_data)

#----------------------------------#

# Conclusion

"""
Premium predicting! Having the predictions in a DataFrame will make it easier to visualize them.
"""

# exercise 02

"""
Visualizing predictions

The prediction DataFrame you created contains a column of explanatory variable values and a column of response variable values. That means you can plot it on the same scatter plot of response versus explanatory data values.

prediction_data is available. The code for the plot you created using sns.regplot() in Chapter 1 is shown.
"""

# steps

"""

    Create a new figure to plot multiple layers.
    Extend the plotting code to add points for the predictions in prediction_data. Color the points red.
    Display the layered plot.

"""

# solution

# Create a new figure, fig
fig = plt.figure()

sns.regplot(x="n_convenience",
            y="price_twd_msq",
            data=taiwan_real_estate,
            ci=None)
# Add a scatter plot layer to the regplot
sns.scatterplot(x = 'n_convenience', y = 'price_twd_msq', data = prediction_data, color="red")

# Show the layered plot
plt.show()

#----------------------------------#

# Conclusion

"""
Perfect prediction plotting! Naturally, the predicted points lie on the trend line.
"""

# exercise 03

"""
The limits of prediction

In the last exercise, you made predictions on some sensible, could-happen-in-real-life, situations. That is, the cases when the number of nearby convenience stores were between zero and ten. To test the limits of the model's ability to predict, try some impossible situations.

Use the console to try predicting house prices from mdl_price_vs_conv when there are -1 convenience stores. Do the same for 2.5 convenience stores. What happens in each case?

mdl_price_vs_conv is available.
"""

# steps

"""
Create some impossible explanatory data. Define a DataFrame impossible with one column, n_convenience, set to -1 in the first row, and 2.5 in the second row.
---
Question

Try making predictions on your two impossible cases. What happens?
Possible Answers

    The model throws an error because these cases are impossible in real life.

    The model throws a warning because these cases are impossible in real life.

    The model successfully gives a prediction about cases that are impossible in real life. (Answer)

    The model throws an error for -1 stores because it violates the assumptions of a linear regression. 2.5 stores gives a successful prediction.

    The model throws an error for 2.5 stores because it violates the assumptions of a linear regression. -1 stores gives a successful prediction.
"""

# solution

# Define a DataFrame impossible
impossible = pd.DataFrame({'n_convenience' : [-1,2.5]})

#----------------------------------#

# Conclusion

"""
Legendary limit detection! Linear models don't know what is possible or not in real life. That means that they can give you predictions that don't make any sense when applied to your data. You need to understand what your data means in order to determine whether a prediction is nonsense or not.
"""

# exercise 04

"""
Extracting model elements

The model object created by ols() contains many elements. In order to perform further analysis on the model results, you need to extract its useful bits. The model coefficients, the fitted values, and the residuals are perhaps the most important pieces of the linear model object.

mdl_price_vs_conv is available.
"""

# steps

"""

 Print the parameters of mdl_price_vs_conv.
---
 Print the fitted values of mdl_price_vs_conv.
---
 Print the residuals of mdl_price_vs_conv.
---
Print a summary of mdl_price_vs_conv.
"""

# solution

# Print the model parameters of mdl_price_vs_conv
print(mdl_price_vs_conv.params)

#----------------------------------#

# Print the fitted values of mdl_price_vs_conv
print(mdl_price_vs_conv.fittedvalues)

#----------------------------------#

# Print the residuals of mdl_price_vs_conv
print(mdl_price_vs_conv.resid)

#----------------------------------#

# Print a summary of mdl_price_vs_conv
print(mdl_price_vs_conv.summary())

#----------------------------------#

# Conclusion

"""
Marvelous model manipulation! Working with individual pieces of the model is often more useful than working with the whole model object at once.
"""

# exercise 05

"""
Manually predicting house prices

You can manually calculate the predictions from the model coefficients. When making predictions in real life, it is better to use .predict(), but doing this manually is helpful to reassure yourself that predictions aren't magic - they are simply arithmetic.

In fact, for a simple linear regression, the predicted value is just the intercept plus the slope times the explanatory variable.

response = intercept + slope * explanatory

mdl_price_vs_conv and explanatory_data are available.
"""

# steps

"""
Get the coefficients/parameters of mdl_price_vs_conv, assigning to coeffs.
---
Get the intercept, which is the first element of coeffs, assigning to intercept.
---
Get the slope, which is the second element of coeffs, assigning to slope.
---
Manually predict price_twd_msq using the formula, specifying the intercept, slope, and explanatory_data.
---
Run the code to compare your manually calculated predictions to the results from .predict().
"""

# solution

# Get the coefficients of mdl_price_vs_conv
coeffs = mdl_price_vs_conv.params

# Get the intercept
intercept = coeffs[0]

# Get the slope
slope = coeffs[1]

# Manually calculate the predictions
price_twd_msq = intercept + slope * explanatory_data
print(price_twd_msq)

# Compare to the results from .predict()
print(price_twd_msq.assign(predictions_auto=mdl_price_vs_conv.predict(explanatory_data)))

#----------------------------------#

# Conclusion

"""
Magic manual prediction! For simple linear regression, the prediction just involves one addition and one multiplication.
"""

# exercise 06

"""
Home run!

Regression to the mean is an important concept in many areas, including sports.

Here you can see a dataset of baseball batting data in 2017 and 2018. Each point represents a player, and more home runs are better. A naive prediction might be that the performance in 2018 is the same as the performance in 2017. That is, a linear regression would lie on the "y equals x" line.

Explore the plot and make predictions. What does regression to the mean say about the number of home runs in 2018 for a player who was very successful in 2017?
"""

# steps

"""
Someone who hit 40 home runs in 2017 is predicted to hit the same number of home runs the next year because regression to the mean states that performance is consistent over time.
---
If someone hit 40 home runs in 2017, we can't predict the number of home runs the next year because regression to the mean states that extremely high values are unpredictable.
---
Someone who hit 40 home runs in 2017 is predicted to hit 10 fewer home runs the next year because regression to the mean states that, on average, extremely high values are not sustained. (Answer)
---
Someone who hit 40 home runs in 2017 is predicted to hit 10 more home runs the next year because regression to the mean states that, on average, extremely high values are amplified over time.
"""

# solution



#----------------------------------#

# Conclusion

"""
Magnificent regression to the mean! Due to regression to the mean, it's common that one player or team that does really well one year, doesn't do as well the next. Likewise players or teams that perform very badly one year do better the next year.
"""

# exercise 07

"""
Plotting consecutive portfolio returns

Regression to the mean is also an important concept in investing. Here you'll look at the annual returns from investing in companies in the Standard and Poor 500 index (S&P 500), in 2018 and 2019.

The sp500_yearly_returns dataset contains three columns:
variable 	meaning
symbol 	Stock ticker symbol uniquely identifying the company.
return_2018 	A measure of investment performance in 2018.
return_2019 	A measure of investment performance in 2019.

A positive number for the return means the investment increased in value; negative means it lost value.

Just as with baseball home runs, a naive prediction might be that the investment performance stays the same from year to year, lying on the y equals x line.

sp500_yearly_returns is available as a pandas DataFrame.
"""

# steps

"""
Create a new figure, fig, to enable plot layering.
---
Generate a line at y equals x. This has been done for you.
---
Using sp500_yearly_returns, draw a scatter plot of return_2019 vs. return_2018 with a linear regression trend line, without a standard error ribbon.
---
Set the axes so that the distances along the x and y axes look the same.
"""

# solution

# Create a new figure, fig
fig = plt.figure()

# Plot the first layer: y = x
plt.axline(xy1=(0,0), slope=1, linewidth=2, color="green")

# Add scatter plot with linear regression trend line
sns.regplot(x = 'return_2018', y = 'return_2019', data = sp500_yearly_returns, ci = None)

# Set the axes so that the distances along the x and y axes look the same
plt.axis('equal')

# Show the plot
plt.show()

#----------------------------------#

# Conclusion

"""
Super scatter plotting! The regression trend line looks very different to the y equals x line. As the financial advisors say, "Past performance is no guarantee of future results."
"""

# exercise 08

"""
Modeling consecutive returns

Let's quantify the relationship between returns in 2019 and 2018 by running a linear regression and making predictions. By looking at companies with extremely high or extremely low returns in 2018, we can see if their performance was similar in 2019.

sp500_yearly_returns is available and ols() is loaded.
"""

# steps

"""

    Run a linear regression on return_2019 versus return_2018 using sp500_yearly_returns and fit the model. Assign to mdl_returns.
    Print the parameters of the model.
---

    Create a DataFrame named explanatory_data. Give it one column (return_2018) with 2018 returns set to a list containing -1, 0, and 1.
    Use mdl_returns to predict with explanatory_data in a print() call.

"""

# solution

# Run a linear regression on return_2019 vs. return_2018 using sp500_yearly_returns
mdl_returns = ols('return_2019 ~ return_2018', data = sp500_yearly_returns).fit()

# Print the parameters
print(mdl_returns.params)

#----------------------------------#

mdl_returns = ols("return_2019 ~ return_2018", data=sp500_yearly_returns).fit()

# Create a DataFrame with return_2018 at -1, 0, and 1 
explanatory_data = pd.DataFrame({'return_2018': [-1,0,1]})

# Use mdl_returns to predict with explanatory_data
print(mdl_returns.predict(explanatory_data))

#----------------------------------#

# Conclusion

"""
Incredible investment predictions! Investments that gained a lot in value in 2018 on average gained only a small amount in 2019. Similarly, investments that lost a lot of value in 2018 on average also gained a small amount in 2019.
"""

# exercise 09

"""
Transforming the explanatory variable

If there is no straight-line relationship between the response variable and the explanatory variable, it is sometimes possible to create one by transforming one or both of the variables. Here, you'll look at transforming the explanatory variable.

You'll take another look at the Taiwan real estate dataset, this time using the distance to the nearest MRT (metro) station as the explanatory variable. You'll use code to make every commuter's dream come true: shortening the distance to the metro station by taking the square root. Take that, geography!

taiwan_real_estate is available.
"""

# steps

"""

    Look at the plot.
    Add a new column to taiwan_real_estate called sqrt_dist_to_mrt_m that contains the square root of dist_to_mrt_m.
    Create the same scatter plot as the first one, but use the new transformed variable on the x-axis instead.
    Look at the new plot. Notice how the numbers on the x-axis have changed. This is a different line to what was shown before. Do the points track the line more closely?
---

    Run a linear regression of price_twd_msq versus the square root of dist_to_mrt_m using taiwan_real_estate.
    Print the parameters.
---

    Create a DataFrame of predictions named prediction_data by adding a column of predictions called price_twd_msq to explanatory_data. Predict using mdl_price_vs_dist and explanatory_data.
    Print the predictions.
---
    Add a layer to your plot containing points from prediction_data, colored "red".
"""

# solution

# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

plt.figure()

# Plot using the transformed variable
sns.regplot(x = 'sqrt_dist_to_mrt_m', y = 'price_twd_msq', data = taiwan_real_estate, ci = None)
plt.show()

#----------------------------------#

# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. square root of dist_to_mrt_m using taiwan_real_estate
mdl_price_vs_dist = ols('price_twd_msq ~ sqrt_dist_to_mrt_m', data = taiwan_real_estate).fit()

# Print the parameters
print(mdl_price_vs_dist.params)

#----------------------------------#

# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. sqrt_dist_to_mrt_m
mdl_price_vs_dist = ols("price_twd_msq ~ sqrt_dist_to_mrt_m", data=taiwan_real_estate).fit()

explanatory_data = pd.DataFrame({"sqrt_dist_to_mrt_m": np.sqrt(np.arange(0, 81, 10) ** 2),
                                "dist_to_mrt_m": np.arange(0, 81, 10) ** 2})

# Create prediction_data by adding a column of predictions to explantory_data
prediction_data = explanatory_data.assign(
    price_twd_msq = mdl_price_vs_dist.predict(explanatory_data)
)

# Print the result
print(prediction_data)

#----------------------------------#

# Create sqrt_dist_to_mrt_m
taiwan_real_estate["sqrt_dist_to_mrt_m"] = np.sqrt(taiwan_real_estate["dist_to_mrt_m"])

# Run a linear regression of price_twd_msq vs. sqrt_dist_to_mrt_m
mdl_price_vs_dist = ols("price_twd_msq ~ sqrt_dist_to_mrt_m", data=taiwan_real_estate).fit()

# Use this explanatory data
explanatory_data = pd.DataFrame({"sqrt_dist_to_mrt_m": np.sqrt(np.arange(0, 81, 10) ** 2),
                                "dist_to_mrt_m": np.arange(0, 81, 10) ** 2})

# Use mdl_price_vs_dist to predict explanatory_data
prediction_data = explanatory_data.assign(
    price_twd_msq = mdl_price_vs_dist.predict(explanatory_data)
)

fig = plt.figure()
sns.regplot(x="sqrt_dist_to_mrt_m", y="price_twd_msq", data=taiwan_real_estate, ci=None)

# Add a layer of your prediction points
sns.scatterplot(x = 'sqrt_dist_to_mrt_m', y = 'price_twd_msq', data = prediction_data, color='red')
plt.show()

#----------------------------------#

# Conclusion

"""
You transform like a robot in disguise! By transforming the explanatory variable, the relationship with the response variable became linear, and so a linear regression became an appropriate model.
"""

# exercise 10

"""
Transforming the response variable too

The response variable can be transformed too, but this means you need an extra step at the end to undo that transformation. That is, you "back transform" the predictions.

In the video, you saw the first step of the digital advertising workflow: spending money to buy ads, and counting how many people see them (the "impressions"). The next step is determining how many people click on the advert after seeing it.

ad_conversion is available as a pandas DataFrame.
"""

# steps

"""

    Look at the plot.
    Create a qdrt_n_impressions column using n_impressions raised to the power of 0.25.
    Create a qdrt_n_clicks column using n_clicks raised to the power of 0.25.
    Create a regression plot using the transformed variables. Do the points track the line more closely?
---
    Run a linear regression of qdrt_n_clicks versus qdrt_n_impressions using ad_conversion and assign it to mdl_click_vs_impression.
---

    Complete the code to create the prediction data.

"""

# solution

# Create qdrt_n_impressions and qdrt_n_clicks
ad_conversion["qdrt_n_impressions"] = ad_conversion['n_impressions'] ** 0.25
ad_conversion["qdrt_n_clicks"] = ad_conversion['n_clicks'] ** 0.25

plt.figure()

# Plot using the transformed variables
sns.regplot(x = 'qdrt_n_impressions', y = 'qdrt_n_clicks', data = ad_conversion, ci = None)
plt.show()

#----------------------------------#

ad_conversion["qdrt_n_impressions"] = ad_conversion["n_impressions"] ** 0.25
ad_conversion["qdrt_n_clicks"] = ad_conversion["n_clicks"] ** 0.25

# Run a linear regression of your transformed variables
mdl_click_vs_impression = ols('qdrt_n_clicks ~ qdrt_n_impressions', data = ad_conversion).fit()

#----------------------------------#

ad_conversion["qdrt_n_impressions"] = ad_conversion["n_impressions"] ** 0.25
ad_conversion["qdrt_n_clicks"] = ad_conversion["n_clicks"] ** 0.25

mdl_click_vs_impression = ols("qdrt_n_clicks ~ qdrt_n_impressions", data=ad_conversion, ci=None).fit()

explanatory_data = pd.DataFrame({"qdrt_n_impressions": np.arange(0, 3e6+1, 5e5) ** .25,
                                 "n_impressions": np.arange(0, 3e6+1, 5e5)})

# Complete prediction_data
prediction_data = explanatory_data.assign(
    qdrt_n_clicks = mdl_click_vs_impression.predict(explanatory_data)
)

# Print the result
print(prediction_data)

#----------------------------------#

# Conclusion

"""
Terrific transformation! Since the response variable has been transformed, you'll now need to back-transform the predictions to correctly interpret your results.
"""

# exercise 11

"""
Back transformation

In the previous exercise, you transformed the response variable, ran a regression, and made predictions. But you're not done yet! In order to correctly interpret and visualize your predictions, you'll need to do a back-transformation.

prediction_data, which you created in the previous exercise, is available.
"""

# steps

"""
Back transform the response variable in prediction_data by raising qdrt_n_clicks to the power 4 to get n_clicks
---
Edit the plot to add a layer of points from prediction_data, colored "red"
"""

# solution

# Back transform qdrt_n_clicks
prediction_data["n_clicks"] = prediction_data['qdrt_n_clicks'] ** 4
print(prediction_data)

#----------------------------------#

# Back transform qdrt_n_clicks
prediction_data["n_clicks"] = prediction_data["qdrt_n_clicks"] ** 4

# Plot the transformed variables
fig = plt.figure()
sns.regplot(x="qdrt_n_impressions", y="qdrt_n_clicks", data=ad_conversion, ci=None)

# Add a layer of your prediction points
sns.scatterplot(x = 'qdrt_n_impressions', y = 'qdrt_n_clicks', data = prediction_data, color='red')
plt.show()

#----------------------------------#

# Conclusion

"""
Brilliant back transformation! Notice that your back-transformed predictions nicely follow the trend line and allow you to make more accurate predictions.
"""