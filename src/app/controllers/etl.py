from flask import jsonify
from app import app, spec
from flask_pydantic_spec import (Response, Request)
from app.services import (
                          extract_data, 
                          transform_data, 
                          get_trasformed_data
                         )


@app.post('/extract')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def extract():
    """
    - Extract route.
    """
    id_ = extract_data()
    return jsonify(raw_data_id=str(id_)), 200


@app.put('/transform')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def transform():
    """
    - Transform route.
    """
    id_ = transform_data()
    return jsonify(transformed_data_id=str(id_)), 200


@app.get('/get-transformed-data/<int:id>')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def get_transformed_data(id):
    """
    - Get transformed data route.
    """
    transformed_data = get_trasformed_data(id)
    return jsonify(data=transformed_data), 200