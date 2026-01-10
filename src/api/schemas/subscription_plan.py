from marshmallow import Schema, fields

class SubscriptionPlanRequestSchema(Schema):
    name = fields.Str(required=True)
    user_id = fields.Int(required=True)
    billing_cycle = fields.Str(required=False)
    price = fields.Raw(required=False)
    description = fields.Str(required=False)
    status = fields.Str(required=True)


class SubscriptionPlanResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    user_id = fields.Int(required=True)
    billing_cycle = fields.Str(required=False)
    price = fields.Raw(required=False)
    description = fields.Str(required=False)
    status = fields.Str(required=True)
    created_by = fields.Str(required=False)
    updated_by = fields.Str(required=False)
    created_at = fields.Raw(required=True)
    updated_at = fields.Raw(required=True)
