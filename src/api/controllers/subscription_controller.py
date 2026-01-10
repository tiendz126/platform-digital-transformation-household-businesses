from flask import Blueprint, request, jsonify
from services.subscription_service import SubscriptionService
from infrastructure.repositories.subscription_repository import SubscriptionRepository
from api.schemas.subscription import SubscriptionRequestSchema, SubscriptionResponseSchema
from infrastructure.databases.mssql import session
from datetime import datetime

bp = Blueprint('admin_subscription', __name__, url_prefix='/api/admin/subscriptions')

service = SubscriptionService(SubscriptionRepository(session=session))
request_schema = SubscriptionRequestSchema()
response_schema = SubscriptionResponseSchema()


@bp.route('', methods=['GET'])
def list_subscriptions():
    """
    List all subscriptions
    ---
    get:
      summary: Get all subscriptions
      tags:
        - Subscriptions
      responses:
        200:
          description: List of subscriptions
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1
                    plan_id:
                      type: integer
                      example: 2
                    household_id:
                      type: integer
                      example: 3
                    start_date:
                      type: string
                      example: "2026-01-09T17:00:00Z"
                    end_date:
                      type: string
                      example: "2026-02-09T17:00:00Z"
                    is_active:
                      type: boolean
                      example: true
                    created_at:
                      type: string
                      example: "2026-01-09T17:00:00Z"
                    updated_at:
                      type: string
                      example: "2026-01-09T17:00:00Z"
    """
    subs = service.list_subscriptions()
    return jsonify(response_schema.dump(subs, many=True)), 200


@bp.route('', methods=['POST'])
def create_subscription():
    """
    Create a new subscription
    ---
    post:
      summary: Create a subscription
      tags:
        - Subscriptions
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                plan_id:
                  type: integer
                  example: 2
                household_id:
                  type: integer
                  example: 3
                start_date:
                  type: string
                  example: "2026-01-09T17:00:00Z"
                end_date:
                  type: string
                  example: "2026-02-09T17:00:00Z"
                is_active:
                  type: boolean
                  example: true
      responses:
        201:
          description: Subscription created
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  plan_id:
                    type: integer
                    example: 2
                  household_id:
                    type: integer
                    example: 3
                  start_date:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  end_date:
                    type: string
                    example: "2026-02-09T17:00:00Z"
                  is_active:
                    type: boolean
                    example: true
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    now = datetime.utcnow()
    sub = service.create_subscription(
        plan_id=data['plan_id'],
        household_id=data['household_id'],
        start_date=data.get('start_date', now),
        end_date=data.get('end_date'),
        is_active=data.get('is_active', True),
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(sub)), 201


@bp.route('/<int:id>', methods=['GET'])
def get_subscription(id):
    """
    Get subscription by ID
    ---
    get:
      summary: Get a subscription by ID
      tags:
        - Subscriptions
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: Subscription ID
      responses:
        200:
          description: Subscription object
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  plan_id:
                    type: integer
                    example: 2
                  household_id:
                    type: integer
                    example: 3
                  start_date:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  end_date:
                    type: string
                    example: "2026-02-09T17:00:00Z"
                  is_active:
                    type: boolean
                    example: true
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
        404:
          description: Subscription not found
    """
    sub = service.get_subscription(id)
    if not sub:
        return jsonify({'message': 'Subscription not found'}), 404
    return jsonify(response_schema.dump(sub)), 200


@bp.route('/<int:id>', methods=['PUT'])
def update_subscription(id):
    """
    Update subscription by ID
    ---
    put:
      summary: Update a subscription
      tags:
        - Subscriptions
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: Subscription ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                plan_id:
                  type: integer
                  example: 2
                household_id:
                  type: integer
                  example: 3
                start_date:
                  type: string
                  example: "2026-01-09T17:00:00Z"
                end_date:
                  type: string
                  example: "2026-02-09T17:00:00Z"
                is_active:
                  type: boolean
                  example: true
      responses:
        200:
          description: Updated subscription
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  plan_id:
                    type: integer
                    example: 2
                  household_id:
                    type: integer
                    example: 3
                  start_date:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  end_date:
                    type: string
                    example: "2026-02-09T17:00:00Z"
                  is_active:
                    type: boolean
                    example: true
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
        400:
          description: Invalid input
        404:
          description: Subscription not found
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    sub = service.update_subscription(
        subscription_id=id,
        plan_id=data.get('plan_id'),
        household_id=data.get('household_id'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        is_active=data.get('is_active'),
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(sub)), 200


@bp.route('/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    """
    Delete subscription by ID
    ---
    delete:
      summary: Delete a subscription
      tags:
        - Subscriptions
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: Subscription ID
      responses:
        204:
          description: Subscription deleted successfully
        404:
          description: Subscription not found
    """
    service.delete_subscription(id)
    return '', 204
