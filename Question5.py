# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:57:35 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Get the number of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")
