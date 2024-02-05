# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:10:25 2024

@author: onken
"""

import pandas as pd
from collections import Counter

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')
# Split the "Actors" column into a list of actor names
all_actors = df['Actors'].str.split(', ').explode().dropna()

# Find the most common actor
most_common_actor, most_common_count = Counter(all_actors).most_common(1)[0]

print(f"The most common actor in all movies is: {most_common_actor} with {most_common_count} appearances.")
