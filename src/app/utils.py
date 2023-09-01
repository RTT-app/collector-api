import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def clean_text(comment):
    comment_ = re.sub('\d+', ' ', comment)
    comment_ = re.sub('#',' ',comment_)
    comment_ = comment_.lower()

    return comment_


def stemm_comments(words):
    words = words.split()
    stemmed_comment = []

    ps = PorterStemmer()
    
    for word in words:
        stemmed_word = ps.stem(word)
        stemmed_comment.append(stemmed_word)

    stemmed_comment = ' '.join(stemmed_comment)

    return stemmed_comment