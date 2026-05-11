# Outliers in Statistics

# An outlier is a data value that is very different from the other values in a dataset.

# It may be:

# Much larger than other values
# Much smaller than other values

# Outliers can affect statistical calculations like mean, variance, and standard deviation.

# Example of Outlier

# Data: 2, 4, 5, 6, 7, 50

# Here, 50 is an outlier because it is far away from the other values.

# Causes of Outliers

# Outliers may occur because of:

# Measurement errors
# Data entry mistakes
# Experimental errors
# Natural variation
# Rare events
# Types of Outliers
# 1. Low Outlier

# A value much smaller than others.

# Example:
# 1, 20, 22, 24, 25

# Here, 1 is a low outlier.

# 2. High Outlier

# A value much larger than others.

# Example:
# 10, 12, 14, 16, 100

# Here, 100 is a high outlier.

# Effects of Outliers

# Outliers can:

# Increase or decrease the mean
# Increase range
# Increase variance
# Increase standard deviation
# Mislead data analysis
# Detecting Outliers
# 1. Using Interquartile Range (IQR) Method

# First calculate:

# IQR=Q
# 3
# 	​

# −Q
# 1
# 	​


# Then find limits:

# Lower Limit

# Q
# 1
# 	​

# −1.5(IQR)

# Upper Limit

# Q
# 3
# 	​

# +1.5(IQR)

# Any value outside these limits is an outlier.

# Example Using IQR

# Data: 1, 2, 3, 4, 5, 20

# Q₁ = 2
# Q₃ = 5

# IQR = 5 − 2 = 3

# Lower Limit = 2 − 1.5(3) = -2.5
# Upper Limit = 5 + 1.5(3) = 9.5

# Since 20 > 9.5, 20 is an outlier.

# 2. Using Z-Score Method

# Z-score shows how far a value is from the mean.

# z=
# σ
# x−
# x
# ˉ
# 	​


# Where:

# x = observation
# x
# ˉ
#  = mean
# σ = standard deviation
# Rule
# If |z| > 3, the value is usually considered an outlier.
# Graphical Methods to Detect Outliers
# Box plot
# Histogram
# Scatter plot
# Handling Outliers
# 1. Remove Outliers

# Used when data is incorrect.

# 2. Keep Outliers

# Used when outlier is meaningful.

# 3. Replace Outliers

# Replace with:

# Mean
# Median
# Mode
# Advantages of Detecting Outliers
# Improves accuracy
# Better statistical analysis
# Helps identify errors
# Disadvantages
# Removing true data may reduce accuracy
# Sometimes difficult to identify correctly