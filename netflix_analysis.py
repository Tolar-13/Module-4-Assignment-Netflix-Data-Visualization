# Renaming the file to "Netflix_shows_movies"

import pandas as pd
import os

# Define the old and new file names
old_file_name = 'netflix_data.csv'
new_file_name = 'Netflix_shows_movies.csv'

# Read the csv file
df = pd.read_csv(old_file_name)

# Rename the file
os.rename(old_file_name, new_file_name)

# Load the dataset
netflix_data = pd.read_csv(new_file_name)

# Display the first few rows of the dataset
netflix_data.head()

# Data Cleaning

# Check for missing values
print(netflix_data.isnull().sum())

# Handle missing values by dropping rows with missing values
netflix_cleaned = netflix_data.dropna()

# Verify missing values have been addressed
print(netflix_cleaned.isnull().sum())

# Display the first few rows of the cleaned dataset
netflix_cleaned.head()

# Data Exploration

# Describe the data
print(netflix_cleaned.describe())

# Statistical analysis

# Count the number of shows and movies
num_shows = netflix_cleaned[netflix_cleaned['type'] == 'TV Show'].shape[0]
num_movies = netflix_cleaned[netflix_cleaned['type'] == 'Movie'].shape[0]

print(f"Number of TV Shows: {num_shows}")
print(f"Number of Movies: {num_movies}")

# Analyze the release year distribution
release_years = netflix_cleaned['release_year'].value_counts()

print("Release Year Distribution:\n", release_years.head())

# Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns

# Most watched genres
plt.figure(figsize=(12, 6))
genre_counts = netflix_cleaned['listed_in'].value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title('Top 10 Most Watched Genres')
plt.xlabel('Number of Titles')
plt.ylabel('Genres')
plt.xticks(range(0, max(genre_counts) + 50, 50))
plt.tight_layout()
plt.show()

# Calculate frequency of each rating and sort in descending order
rating_counts = netflix_cleaned['rating'].value_counts().sort_values(ascending=False)

# Plot the distribution of ratings
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.title('Distribution of Ratings on Netflix')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.yticks(range(0, max(rating_counts) + 200, 200))
plt.show()


# Save the cleaned dataset to a CSV file for R visualisation
netflix_cleaned.to_csv('Netflix_cleaned.csv', index=False)
