# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:05:42 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')

# Calculate the average rating for each year
average_ratings_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_avg_rating = average_ratings_by_year.idxmax()
highest_avg_rating = average_ratings_by_year.max()

print(f"The year with the highest average rating is {year_highest_avg_rating} with an average rating of {highest_avg_rating:.2f}")
