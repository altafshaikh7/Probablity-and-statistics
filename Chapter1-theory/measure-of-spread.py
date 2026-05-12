# Measures of Spread (Dispersion) – Full Information

# Measures of Spread or Dispersion tell us how much the data values are scattered around the central value (mean, median, or mode).

# If the data values are close together → spread is small.
# If the data values are far apart → spread is large.

# Why Measures of Spread are Important

# Measures of spread help to:

# Understand variability in data
# Compare two datasets
# Measure consistency
# Detect outliers
# Analyze risk and uncertainty

# They are widely used in:

# Data Science
# Machine Learning
# Business analytics
# Finance
# Research
# Engineering
# Main Types of Measures of Spread
# Range
# Quartiles and Interquartile Range (IQR)
# Mean Deviation
# Variance
# Standard Deviation
# Coefficient of Variation
# 1. Range

# Range is the difference between the maximum and minimum value in a dataset.

# Range=Maximum Value−Minimum Value

# Example

# Data: 3, 7, 9, 15, 20

# Maximum value = 20
# Minimum value = 3

# Range = 20 − 3 = 17

# Merits of Range
# Very easy to calculate
# Quick understanding of spread
# Demerits of Range
# Uses only two values
# Affected by extreme values (outliers)
# 2. Quartiles and Interquartile Range (IQR)

# Quartiles divide data into four equal parts.

# Q₁ → First Quartile
# Q₂ → Median
# Q₃ → Third Quartile

# Interquartile Range measures the spread of the middle 50% data.

# IQR=Q
# 3
# 	​

# −Q
# 1
# 	​


# Example

# Data: 1, 3, 5, 7, 9, 11, 13

# Q₁ = 3
# Q₃ = 11

# IQR = 11 − 3 = 8

# Merits of IQR
# Not affected by outliers
# Good for skewed data
# Demerits of IQR
# Ignores extreme values
# 3. Mean Deviation

# Mean deviation is the average of absolute deviations from the mean.

# Mean Deviation=
# n
# ∑∣x−
# x
# ˉ
# ∣
# 	​


# Example

# Data: 2, 4, 6

# Mean = 4

# |2−4| = 2
# |4−4| = 0
# |6−4| = 2

# Mean deviation = (2 + 0 + 2)/3 = 4/3

# Merits
# Uses all observations
# Simple understanding
# Demerits
# Absolute values make calculations harder
# 4. Variance

# Variance measures the average squared deviation from the mean.

# Variance=
# n
# ∑(x−
# x
# ˉ
# )
# 2
# 	​


# Steps to Find Variance
# Find mean
# Subtract mean from each value
# Square each deviation
# Add squared deviations
# Divide by total observations
# Example


# Data: 2, 4, 6

# Mean = 4

# | x | x − x̄ | (x − x̄)² |
# | - | ------ | --------- |
# | 2 | -2     | 4         |
# | 4 | 0      | 0         |
# | 6 | 2      | 4         |

# Sum = 8
# Variance = 8/3