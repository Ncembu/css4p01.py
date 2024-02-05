# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:15:59 2024

@author: onken
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('movie_dataset_cleaned1.csv')  

# Select only numerical columns for correlation analysis
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# Calculate correlation matrix
correlation_matrix = numerical_columns.corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.show()

# Insights:

#1. A subtle negative correlation exists between 'Rank' and 'Rating', suggesting that a higher rank does not necessarily result in higher ratings.

#2. A subtle negative correlation is noted between 'Rank' and 'Votes', indicating highly ranked movies don't necessarily get more votes.

#3. There is a negative correlation between 'Revenue' and 'Rank', suggesting that movies with higher rank do not necessarily yield higher revenue.

#4. A positive correlation exists between 'Revenue' and 'votes', indicating that movies with a greater number of votes tend to have higher revenues.

#5. A modest positive correlation is observed between 'Revenue' and 'runtime', implying that longer movies might contribute slightly to higher revenue.

#Advice for Directors:
    
#1. Concentrate on developing compelling and high-quality content that resonates with the audience, aiming to increase votes and potentially enhance revenue.

#2. Consider the optimal runtime for your movie, as both excessively short and excessively long movies might impact audience satisfaction.

#3. Make use of audience feedback and ratings to continually enhance and refine your filmmaking skills.
