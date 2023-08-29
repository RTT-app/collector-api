import praw
import uuid
from app import data_base
from config import (CLIENT_ID, 
                    SECRET_TOKEN, 
                    USER_AGENT, 
                    SUBREDDIT, 
                    N_POSTS)

"""
Redis use example:
    r.set('hello', 'world') # True

    value = r.get('hello')
    print(value) # b'world'

    r.delete('hello') # True
    print(r.get('hello')) # None
"""

def extract_data():
    client = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret= SECRET_TOKEN,
            user_agent= USER_AGENT
            )
    
    subreddit = client.subreddit(SUBREDDIT)

    top_posts = subreddit.new(limit=N_POSTS) # jogar isso pra dentro do while

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
    
    id_ = uuid.uuid4()

    if data_base.get(id_):
        raise Exception('Error on commit data.')
    
    data_base.set(id_, data)

    return id_

def transform_data():
    pass

def get_trasformed_data():
    pass