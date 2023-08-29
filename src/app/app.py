from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('ETL - REST API')
spec.register(app)

from app.controller import etl