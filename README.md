# Sentiment Analysis Project

This project involves loading multiple datasets containing product reviews for e-commerce applications, combining them, calculating sentiment polarity, assigning sentiment labels, and plotting the sentiment distribution. This `README.md` file provides clear instructions on what the project does, how to set it up, and how to run it. It also includes the necessary code snippets for reference.


## Files

- `dataset1.csv`: First dataset of reviews.
- `dataset2.csv`: Second dataset of reviews.
- `dataset3.csv`: Third dataset of reviews.
- `Sentiment_Analysis.py`: Python script to perform sentiment analysis.
- `README.md`: Documentation for the project.

## Dependencies 

- pandas
- textblob
- matplotlib

You can install these dependencies using `pip`:

```python3
pip install pandas textblob matplotlib
```

## Data Loading
The script starts by loading three CSV datasets using pandas:
```python3
import pandas as pd

# Load datasets
data_set1 = pd.read_csv('dataset1.csv')
data_set2 = pd.read_csv('dataset2.csv')
data_set3 = pd.read_csv('dataset3.csv')
```
## Combining Datasets
The datasets are combined into a single DataFrame:
```python3
# Combine datasets
combined_data = pd.concat([data_set1, data_set2, data_set3])
```
## Sentiment Analysis
Sentiment polarity is calculated for each review using TextBlob, and sentiment labels are assigned based on the polarity:
```python3
from textblob import TextBlob

# Calculate sentiment polarity
combined_data['Sentiment_Polarity'] = combined_data['Review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Assign sentiment labels
combined_data['Sentiment_Label'] = combined_data['Sentiment_Polarity'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')
```
## Displaying Results
The combined dataset with sentiment polarity and labels is displayed:
```python3
# Display combined data with sentiment polarity and labels
print(combined_data)
```

## Running the Script
To run the sentiment analysis script, you can use Python IDLE or execute it from the command line.
### Using Python IDLE
Open Python IDLE.  
Open the sentiment_analysis.py file by navigating to File > Open and selecting the file.  
Run the script by navigating to Run > Run Module or by pressing F5.  

### Using the Command Line
To run the sentiment analysis script from the command line, execute:
```cmd
python sentiment_analysis.py
```
