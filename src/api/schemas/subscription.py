from marshmallow import Schema, fields

class SubscriptionRequestSchema(Schema):
    plan_id = fields.Int(required=True)
    household_id = fields.Int(required=True)
    start_date = fields.Raw(required=False)
    end_date = fields.Raw(required=False)
    is_active = fields.Bool(required=False)

class SubscriptionResponseSchema(Schema):
    id = fields.Int(required=True)
    plan_id = fields.Int(required=True)
    household_id = fields.Int(required=True)
    start_date = fields.Raw(required=False)
    end_date = fields.Raw(required=False)
    is_active = fields.Bool(required=False)
    created_at = fields.Raw(required=True)
    updated_at = fields.Raw(required=True)
