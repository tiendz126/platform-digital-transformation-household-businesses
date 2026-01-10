from marshmallow import Schema, fields

class HouseholdRequestSchema(Schema):
    tax_code = fields.Str(required=False)
    name = fields.Str(required=True)
    phone = fields.Str(required=False)
    address = fields.Str(required=False)
    description = fields.Str(required=False)
    status = fields.Str(required=True)

class HouseholdResponseSchema(Schema):
    id = fields.Int(required=True)
    tax_code = fields.Str(required=False)
    name = fields.Str(required=False)
    phone = fields.Str(required=False)
    address = fields.Str(required=False)
    description = fields.Str(required=False)
    status = fields.Str(required=True)
    created_by = fields.Str(required=False)
    updated_by = fields.Str(required=False)
    created_at = fields.Raw(required=True)
    updated_at = fields.Raw(required=True)