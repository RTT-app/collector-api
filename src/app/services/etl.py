import praw
import json
from app import data_base
from datetime import datetime
from config import (CLIENT_ID, 
                    SECRET_TOKEN, 
                    USER_AGENT, 
                    SUBREDDIT, 
                    N_POSTS)
from app.utils import (
                       clean_text, 
                       stemm_comments,
                       remove_emojis,
                       remove_stopwords
                       )

def extract_data():
    client = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= SECRET_TOKEN,
            user_agent= USER_AGENT
            )
    
    subreddit = client.subreddit(SUBREDDIT)

    top_posts = subreddit.new(limit=N_POSTS)

    data = {
            "title":[],
            "self_text":[],
            "comment":[],
            "score":[]
            }

    for post in top_posts:
        for comment in post.comments:
            data["title"].append(post.title)
            data["self_text"].append(post.selftext)
            data["comment"].append(comment.body)
            data["score"].append(comment.score)

    current_datetime = datetime.now()
    id_ = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    if data_base.get(id_):
        raise Exception('Error to commit data.')
    
    json_data = json.dumps(data)
    data_base.set(id_, json_data)

    return id_


def transform_data(id_):
    data = data_base.get(id_)
    json_data = json.loads(data)

    json_data["self_text"] = [clean_text(title) for title in json_data["self_text"]]
    json_data["self_text"] = [stemm_comments(title) for title in json_data["self_text"]]
    json_data["self_text"] = [remove_emojis(title) for title in json_data["self_text"]]

    json_data["comment"] = [clean_text(comment) for comment in json_data["comment"]]
    json_data["comment"] = [stemm_comments(comment) for comment in json_data["comment"]]
    json_data["comment"] = [remove_emojis(comment) for comment in json_data["comment"]]
    json_data["comment"] = [remove_stopwords(comment) for comment in json_data["comment"]]
    
    return json_data