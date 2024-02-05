# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:08:29 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv') 

# Filter movies released in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Calculate the number of movies in each year
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")
