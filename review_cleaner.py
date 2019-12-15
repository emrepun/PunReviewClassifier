import pandas as pd
import numpy as np
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

reviews_df = pd.read_csv("reviews.csv")

def clean_review(review):
    review = review.lower()
    review = review.split()

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review
                if not word in set(stopwords.words('english'))]

    review = ' '.join(review)

    return review

for index, row in reviews_df.iterrows():
    cleared_review = clean_review(row['review'])
    reviews_df.at[index, 'review'] = cleared_review



#reviews_df.loc[reviews_df['review'], 'review'] = clean_review()

most_common_100_words = Counter(" ".join(reviews_df["review"]).split()).most_common(100)

print(most_common_100_words)

#reviews_cleared
