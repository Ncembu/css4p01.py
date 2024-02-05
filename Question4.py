# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:53:12 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv') 

# Filter movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]

# Get the number of movies released in 2016
num_movies_2016 = len(movies_2016)

print(f"The number of movies released in 2016 is: {num_movies_2016}")
