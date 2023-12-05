# exercise 01

"""
Simple sampling with pandas

Throughout this chapter, you'll be exploring song data from Spotify. 
Each row of this population dataset represents a song, and there are over 40,000 rows. 
Columns include the song name, the artists who performed it, the release year, and attributes of the song like its duration, tempo, and danceability. 
You'll start by looking at the durations.

Your first task is to sample the Spotify dataset and compare the mean duration of the population with the sample.

spotify_population is available and pandas is loaded as pd.
"""

# steps

"""
Sample 1000 rows from spotify_population, assigning to spotify_sample.
---

    Calculate the mean duration in minutes from spotify_population using pandas.
    Calculate the mean duration in minutes from spotify_sample using pandas.

"""

# solution

# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(1000)

# Print the sample
print(spotify_sample)

#----------------------------------#

# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

# Calculate the mean duration in mins from spotify_population
mean_dur_pop = spotify_population['duration_minutes'].mean()

# Calculate the mean duration in mins from spotify_sample
mean_dur_samp = spotify_sample['duration_minutes'].mean()

# Print the means
print(mean_dur_pop)
print(mean_dur_samp)

#----------------------------------#

# exercise 02

"""
Simple sampling and calculating with NumPy

You can also use numpy to calculate parameters or statistics from a list or pandas Series.

You'll be turning it up to eleven and looking at the loudness property of each song.

spotify_population is available and numpy is loaded as np.
"""

# steps

"""

    Subset the loudness column from spotify_population to create the pandas Series, loudness_pop.
    Sample loudness_pop to get 100 random values, assigning to loudness_samp.
---

    Calculate the mean of loudness_pop using numpy.
    Calculate the mean of loudness_samp using numpy.

"""

# solution

# Subset the loudness column of spotify_population
loudness_pop = spotify_population['loudness']

# Sample 100 values of loudness_pop
loudness_samp = loudness_pop.sample(100)

# Print the sample
print(loudness_samp)

#----------------------------------#

# Create a pandas Series from the loudness column of spotify_population
loudness_pop = spotify_population['loudness']

# Sample 100 values of loudness_pop
loudness_samp = loudness_pop.sample(n=100)

# Calculate the mean of loudness_pop
mean_loudness_pop = np.mean(loudness_pop)

# Calculate the mean of loudness_samp
mean_loudness_samp = np.mean(loudness_samp)

# Print the means
print(mean_loudness_pop)
print(mean_loudness_samp)

#----------------------------------#

# exercise 03

"""
Are findings from the sample generalizable?

You just saw how convenience sampling—collecting data using the easiest method—can result in samples that aren't representative of the population. 
Equivalently, this means findings from the sample are not generalizable to the population. 
Visualizing the distributions of the population and the sample can help determine whether or not the sample is representative of the population.

The Spotify dataset contains an acousticness column, which is a confidence measure from zero to one of whether the track was made with instruments that aren't plugged in. 
You'll compare the acousticness distribution of the total population of songs with a sample of those songs.

spotify_population and spotify_mysterious_sample are available; pandas as pd, matplotlib.pyplot as plt, and numpy as np are loaded.
"""

# steps

"""
Plot a histogram of the acousticness from spotify_population with bins of width 0.01 from 0 to 1 using pandas .hist().
---
Update the histogram code to use the spotify_mysterious_sample dataset.
---
Question

Compare the two histograms you drew. Are the acousticness values in the sample generalizable to the general population?
Possible Answers

    Yes. Any sample should lead to a generalizable result about the population.
    Yes. The sample selected is likely a random sample of all songs in our population.
    No. Samples can never lead to generalizable results about the population.
    No. The acousticness samples are consistently higher than those in the general population. (Answer)
    No. The acousticness samples are consistently lower than those in the general population.
"""

# solution

# Visualize the distribution of acousticness with a histogram
spotify_population['acousticness'].hist(bins = np.arange(0, 1.01, 0.01))
plt.show()

#----------------------------------#

# Update the histogram to use spotify_mysterious_sample
spotify_mysterious_sample['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
plt.show()

#----------------------------------#

# exercise 04

"""
Are these findings generalizable?

Let's look at another sample to see if it is representative of the population. 
This time, you'll look at the duration_minutes column of the Spotify dataset, which contains the length of the song in minutes.

spotify_population and spotify_mysterious_sample2 are available; pandas, matplotlib.pyplot, and numpy are loaded using their standard aliases.
"""

# steps

"""
Plot a histogram of duration_minutes from spotify_population with bins of width 0.5 from 0 to 15 using pandas .hist().
---
Update the histogram code to use the spotify_mysterious_sample2 dataset.
---
Question

Compare the two histograms you drew. Are the duration values in the sample generalizable to the general population?
Possible Answers

    Yes. Any sample should lead to a generalizable result about the population.
    Yes. The sample selected is likely a random sample of all songs in the population. (Answer)
    No. Samples can never lead to generalizable results about the population.
    No. The duration samples are consistently higher than those in the general population.
    No. The duration samples are consistently lower than those in the general population.
"""

# solution

# Visualize the distribution of duration_minutes as a histogram
spotify_population['duration_minutes'].hist(bins = np.arange(0, 15.5, 0.5))
plt.show()

#----------------------------------#

# Update the histogram to use spotify_mysterious_sample2
spotify_mysterious_sample2['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))
plt.show()

#----------------------------------#

# exercise 05

"""
Generating random numbers

You've used .sample() to generate pseudo-random numbers from a set of values in a DataFrame. 
A related task is to generate random numbers that follow a statistical distribution, like the uniform distribution or the normal distribution.

Each random number generation function has distribution-specific arguments and an argument for specifying the number of random numbers to generate.

matplotlib.pyplot is loaded as plt, and numpy is loaded as np.
"""

# steps

"""
Generate 5000 numbers from a uniform distribution, setting the parameters low to -3 and high to 3.
---
Generate 5000 numbers from a normal distribution, setting the parameters loc to 5 and scale to 2.
---
Plot a histogram of uniforms with bins of width of 0.25 from -3 to 3 using plt.hist().
---
Plot a histogram of normals with bins of width of 0.5 from -2 to 13 using plt.hist().
"""

# solution

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low = -3, high = 3, size = 5000)

# Print uniforms
print(uniforms)

#----------------------------------#

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc = 5, scale = 2, size = 5000)

# Print normals
print(normals)

#----------------------------------#

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Plot a histogram of uniform values, binwidth 0.25
plt.hist(uniforms, bins = np.arange(-3, 3.25, 0.25))
plt.show()

#----------------------------------#

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Plot a histogram of normal values, binwidth 0.5
plt.hist(normals, bins = np.arange(-2, 13.5 , 0.5))
plt.show()

#----------------------------------#

# exercise 06

"""
Understanding random seeds

While random numbers are important for many analyses, they create a problem: the results you get can vary slightly. 
This can cause awkward conversations with your boss when your script for calculating the sales forecast gives different answers each time.

Setting the seed for numpy's random number generator helps avoid such problems by making the random number generation reproducible.
"""

# steps

"""
Question

Which statement about x and y is true?

import numpy as np
np.random.seed(123)
x = np.random.normal(size=5)
y = np.random.normal(size=5)

Possible Answers

    x and y have identical values.
    The first value of x is identical to the first value of y, but other values are different.
    The values of x are different from those of y. (Answer)
---
Question

Which statement about x and y is true?

import numpy as np
np.random.seed(123)
x = np.random.normal(size=5)
np.random.seed(123)
y = np.random.normal(size=5)

Possible Answers

    x and y have identical values. (Answer)
    The first value of x is identical to the first value of y, but other values are different.
    The values of x are different from those of y.
---
Question

Which statement about x and y is true?

import numpy as np
np.random.seed(123)
x = np.random.normal(size=5)
np.random.seed(456)
y = np.random.normal(size=5)

Possible Answers

    x and y have identical values.
    The first value of x is identical to the first value of y, but other values are different.
    The values of x are different from those of y. (Answer)
"""

# solution



#----------------------------------#