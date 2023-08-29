from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

dotenv_path = find_dotenv(filename='.env')

if not Path(dotenv_path).exists():
    os.system("touch .env")

load_dotenv(dotenv_path)

# Redis vars
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_HOST = os.getenv('REDIS_HOST')

# Reddit praw client config vars
CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
USER_AGENT = os.getenv('USER_AGENT')
SUBREDDIT = os.getenv('SUBREDDIT')
N_POSTS = os.getenv('N_POSTS')