# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:47:53 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  

# Filter movies released from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue
average_revenue = filtered_df['Revenue(Millions)'].mean()

print(f"The average revenue of movies from 2015 to 2017 is: ${average_revenue:.2f}")
