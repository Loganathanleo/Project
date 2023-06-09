# -*- coding: utf-8 -*-
"""Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rLgdRL6AERiMdYN6Lg7ZBlxrqvrMMHZk
"""

import pandas as pd
data = pd.read_csv('water_potability.csv')

# Identify missing values
missing_values = data.isnull().sum()
print(missing_values)

# Convert data types
data['ph'] = data['ph'].astype(float)

# Normalize the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data['Hardness'] = scaler.fit_transform(data[['Hardness']])

# One-hot encode categorical data
encoded_data = pd.get_dummies(data, columns=['Chloramines'])

# Remove outliers using IQR method
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
data = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]

# Calculate summary statistics
summary_stats = data.describe()
print(summary_stats)

# Create a histogram of a numerical column
import matplotlib.pyplot as plt
plt.hist(data['Hardness'], bins=10)
plt.xlabel('Hardness')
plt.ylabel('Frequency')
plt.show()

# Calculate correlations between variables
correlations = data.corr()
print(correlations)

# Conduct a t-test
from scipy.stats import ttest_ind
group1 = data[data['Turbidity'] == 'A']['Turbidity']
group2 = data[data['Turbidity'] == 'B']['Turbidity']
t_stat, p_value = ttest_ind(group1, group2)
print('T-Statistic:', t_stat)
print('P-Value:', p_value)

# Split data into training and testing sets
from sklearn.model_selection import train_test_split

# Drop samples with missing values
data.dropna(inplace=True)

X_train, X_test, y_train, y_test = train_test_split(data.drop('Organic_carbon', axis=1), data['Trihalomethanes'], test_size=0.2, random_state=42)

# Train a machine learning model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, max_depth=5)
rf.fit(X_train, y_train)

# Evaluate the model
from sklearn.metrics import mean_squared_error
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('MSE:', mse)

# Load the dataset
import pandas as pd
water_data = pd.read_csv('water_potability.csv')

# Explore the dataset
print(water_data.head())
print(water_data.info())
print(water_data.describe())