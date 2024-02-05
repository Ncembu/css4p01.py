# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:28:25 2024

@author: onken
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  # Replace 'movie_dataset.csv' with the actual file name

# Drop rows with missing revenue values
df_cleaned = df.dropna(subset=['Revenue(Millions)'])

# Calculate the average revenue
average_revenue = df_cleaned['Revenue(Millions)'].mean()

print(f"The average revenue of all movies in the dataset is between ${average_revenue:.2f} (minimum) and ${average_revenue:.2f} (maximum).")
