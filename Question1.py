# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:24:41 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  # Replace 'movie_dataset.csv' with the actual file name

# Find the highest-rated movie
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

# Display relevant information about the highest-rated movie
highest_rated_movie = highest_rated_movie.iloc[0]
print("The highest-rated movie is:")
print(highest_rated_movie[['Title', 'Rating']])
