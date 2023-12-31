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
                         )


@app.post('/extract')
@spec.validate(resp=Response(HTTP_200=ExtractDTO), tags=["ETL - Pipeline"])
def extract():
    """
    - Extract route.
    """
    id_ = extract_data()
    return jsonify(id=str(id_)), 200


@app.get('/transform/<string:id>')
@spec.validate(resp=Response(), tags=["ETL - Pipeline"])
def transform(id):
    """
    - Transform route.
    """
    transformed_data = transform_data(id)
    
    return jsonify(posts=transformed_data), 200