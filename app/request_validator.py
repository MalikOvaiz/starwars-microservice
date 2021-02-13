from marshmallow import Schema, fields, validate, ValidationError


# https://github.com/marshmallow-code/marshmallow

class StarshipAPISchema(Schema):
    sort_id = fields.Int(required=True, validate=validate.Range(min=0, max=2))
