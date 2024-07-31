# Load necessary libraries
library(ggplot2)
library(dplyr)

# Read the dataset
netflix_data <- read.csv('Netflix_cleaned.csv')

# Calculate the frequency of each rating and sort in descending order
rating_counts <- netflix_cleaned %>%
  count(rating) %>%
  arrange(desc(n))

# Convert the 'rating' column to a factor with levels ordered by frequency
rating_counts$rating <- factor(rating_counts$rating, levels = rating_counts$rating)


# Plot the distribution of ratings
ggplot(rating_counts, aes(x = rating, y = n)) +
  geom_bar(stat = "identity", fill = "skyblue", color = "black") +
  labs(title = "Distribution of Ratings on Netflix",
       x = "Ratings",
       y = "Frequency") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  scale_y_continuous(limits = c(0, 1200), breaks = seq(0, 1200, by = 200)) # Increase y-axis limit

