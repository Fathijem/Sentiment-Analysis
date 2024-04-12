import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load datasets
data_set1 = pd.read_csv('dataset1.csv')
data_set2 = pd.read_csv('dataset2.csv')
data_set3 = pd.read_csv('dataset3.csv')

# Display loaded datasets
print("Dataset 1:\n", data_set1)
print("Dataset 2:\n", data_set2)
print("Dataset 3:\n", data_set3)

# Combine datasets
combined_data = pd.concat([data_set1, data_set2, data_set3])

# Calculate sentiment polarity
combined_data['Sentiment_Polarity'] = combined_data['Review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Assign sentiment labels
combined_data['Sentiment_Label'] = combined_data['Sentiment_Polarity'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# Display combined data with sentiment polarity and labels
print(combined_data)

# Plot sentiment distribution
plt.figure(figsize=(8, 6))
plt.hist(combined_data['Sentiment_Polarity'], bins=30, color="blue", alpha=0.7)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()
