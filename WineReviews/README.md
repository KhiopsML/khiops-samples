# "WineReviews" Dataset
Regression problem, where the goal is to predict the rating of the wine review (target variable `points`)

The dataset contains several text variables

Source: https://www.kaggle.com/datasets/zynicide/wine-reviews

## Preprocessing
- File: `winemag-data-130k-v2.csv`
- Preprocessing
  - Remove the index column
  - Recode multi-line records using single-line text values to comply with Khiops format (three impacted records)
  - Export to `WineReviews.txt` using tabulation field separator
```
import pandas as pd

def preprocess_wine_reviews():
    """Preprocess wine reviews data to remove the index column and
    to replace multi-line values by single-line text values"""
    # Source: https://www.kaggle.com/datasets/zynicide/wine-reviews
    df = pd.read_csv("winemag-data-130k-v2.csv", index_col=[0])
    # Replace end of lines by blanks in order to obtain single-line text fields, to comply with Khiops format
    df = df.replace(['\r', '\n'],' ', regex=True)
    # Export using the tab separator
    df.to_csv("WineReviews.txt", index=False, sep = '\t')

preprocess_wine_reviews()
```
- Create the `WineReviews.kdic` dictionary with Khiops
  - Set `designation` type as `Text`
