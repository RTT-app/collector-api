from flask import request, jsonify

from app import app, spec, data_base

from flask_pydantic_spec import (Response, Request)
#from app.schemas import Post_DTO, Post_list_DTO


"""
Redis use example:
    r.set('hello', 'world') # True

    value = r.get('hello')
    print(value) # b'world'

    r.delete('hello') # True
    print(r.get('hello')) # None
"""


@app.post('/extract')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def extract():
    """
    - Extract route.
    """
    pass


@app.put('/transform/')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def transform(id):
    """
    - Extract route.
    """
    pass


@app.get('/get_transformed_data')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def get_transformed_data():
    """
    - Transform route.
    """
    pass