# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:01:36 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  

# Filter movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Get the number of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

print(f"The number of movies with a rating of at least 8.0 is: {num_high_rated_movies}")
