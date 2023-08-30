from flask import request, jsonify
from app import app, spec
from flask_pydantic_spec import (Response, Request)
from app.schemas import (
                         ExtractDTO, 
                         GetDataDTO, 
                         TransformDTO
                        )
from app.services import (
                          extract_data, 
                          transform_data, 
                          get_trasformed_data
                         )


@app.post('/extract')
@spec.validate(resp=Response(HTTP_200=ExtractDTO), tags=["ETL - Pipeline"])
def extract():
    """
    - Extract route.
    """
    id_ = extract_data()
    return jsonify(id=str(id_)), 200


@app.put('/transform')
@spec.validate(body=Request(TransformDTO),resp=Response(HTTP_200=TransformDTO), tags=["ETL - Pipeline"])
def transform():
    """
    - Transform route.
    """
    id = request.json.get('id')
    id_ = transform_data(id)
    return jsonify(id=str(id_)), 200


@app.get('/get-transformed-data/<string:id>')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"]) # HTTP_200=GetDataDTO
def get_transformed_data(id):
    """
    - Get transformed data route.
    """
    transformed_data = get_trasformed_data(id)
    return jsonify(data=transformed_data), 200