# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:04:47 2024

@author: onken
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")

#remove spaces from column names
file.columns = file.columns.str.replace(" ", "")

#Replacing nan values using fillna
x=file["Revenue(Millions)"].mean()
file["Revenue(Millions)"].fillna(x, inplace = True)

y=file["Metascore"].mean()
file["Metascore"].fillna(y, inplace = True)

#Removing any duplicates
duplicate_rows = file.duplicated()
print("Number of duplicate rows:", duplicate_rows.sum())

#file.to_csv('Cleaned_movie_dataset.csv', index=False)
file.to_csv('movie_dataset_cleaned1.csv', index=False)