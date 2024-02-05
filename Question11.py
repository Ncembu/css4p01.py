# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:13:35 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  

# Split the "Genre" column into a list of genres
all_genres = df['Genre'].str.split(', ').explode().dropna()

# Get the number of unique genres
num_unique_genres = all_genres.nunique()

print(f"There are {num_unique_genres} unique genres in the dataset.")
