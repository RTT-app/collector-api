import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def clean_text(comment):
    comment_ = re.sub('http[s]?://\S+', ' ',comment)
    comment_ = re.sub('\d+', ' ', comment_)
    comment_ = re.sub('[^a-zA-Z\s]', ' ',comment_)
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


def remove_emojis(text):
    # This pattern matches emojis based on Unicode code points
    emoji_pattern = re.compile('[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FAB0-\U0001FABF\U0001FAC0-\U0001FAFF\U0001F200-\U0001F251\u2000-\u3300\u0080-\u00FF]+')
    
    # Remove emojis by replacing them with an empty string
    text_without_emojis = re.sub(emoji_pattern,'', text)
    
    return text_without_emojis