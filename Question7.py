# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:03:25 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv') 

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_nolan_rating = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_nolan_rating:.2f}")
