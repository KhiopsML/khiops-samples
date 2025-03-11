# "NegativeAirlineTweets" Dataset
Text classification problem, where the goal is to predict the reason of a tweet with a negative sentiment (target variable `negativereason`)

Source: https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment

## Preprocessing
- File: `Tweets.csv`
- Preprocessing
  - Keep only the negative reason and text columns
  - Filter records with negative sentiment and annotated reason, keeping the top five reasons
  - Recode multi-line records using single-line text values to comply with Khiops format (hundreds of records concerned)
  - Export to `NegativeAirlineTweets.txt` using a tab field separator
```
import pandas as pd

def preprocess_airline_tweets():
    """Preprocess airline tweets data:
     - keep only the reason and text columns
     - filter negative tweets with a top five reason
     - replace multi-line values by single-line text values"""
    # Source: https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment
    df = pd.read_csv("Tweets.csv")
    # Keep only two columns
    df = df.filter(items=['negativereason', 'text'])
    # Keep tweets with negative sentiment among the top five reasons
    top_reasons = ['Bad Flight', 'Cancelled Flight', 'Customer Service Issue', 'Late Flight', 'Lost Luggage']
    df = df[df['negativereason'].isin(top_reasons)]
    # Replace end of lines by blanks in order to obtain single-line text fields, to comply with Khiops format
    df = df.replace(['\r', '\n'],' ', regex=True)
    # Export using the tab separator
    df.to_csv("Tweets.txt", index=False, sep = '\t')

preprocess_airline_tweets()
```
- Create the `NegativeAirlineTweets.kdic` dictionary with Khiops
