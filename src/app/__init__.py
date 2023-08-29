from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec
import redis

from config import REDIS_HOST, REDIS_PORT

app = Flask(__name__)
spec = FlaskPydanticSpec('ETL-REASTful API')
spec.register(app)

data_base = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

from app.controllers import etl