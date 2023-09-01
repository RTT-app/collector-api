import praw
import uuid
import json
from app import data_base
from config import (CLIENT_ID, 
                    SECRET_TOKEN, 
                    USER_AGENT, 
                    SUBREDDIT, 
                    N_POSTS)
from app.utils import (
                       clean_text, 
                       stemm_comments
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
    
    id_ = str(uuid.uuid4())

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

    json_data["comment"] = [clean_text(comment) for comment in json_data["comment"]]
    json_data["comment"] = [stemm_comments(comment) for comment in json_data["comment"]]

    id_ = str(uuid.uuid4())

    if data_base.get(id_):
        raise Exception('Error to commit transformed data.')
    
    json_data = str(json_data)
    data_base.set(id_, json_data)

    return id_


def get_trasformed_data(id_):
    data = data_base.get(id_)

    return data