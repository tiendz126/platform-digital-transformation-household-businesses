from flask import Blueprint, request, jsonify
from services.household_service import HouseholdService
from infrastructure.repositories.household_repository import HouseholdRepository
from api.schemas.household import HouseholdRequestSchema, HouseholdResponseSchema
from infrastructure.databases.mssql import session
from datetime import datetime

bp = Blueprint('admin_household', __name__, url_prefix='/api/admin/households')
owner_bp = Blueprint('owner_household', __name__, url_prefix='/api/owner/households')

household_service = HouseholdService(HouseholdRepository(session=session))
request_schema = HouseholdRequestSchema()
response_schema = HouseholdResponseSchema()


# ---------------- Admin Routes ----------------
@bp.route('', methods=['GET'])
def list_households():
    """
    List all households (Admin only)
    ---
    get:
      summary: Get all households
      tags:
        - Households
      responses:
        200:
          description: List of households
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
                    name:
                      type: string
                      example: "Household A"
                    address:
                      type: string
                      example: "123 Main St"
                    created_at:
                      type: string
                      example: "2026-01-09T17:00:00Z"
                    updated_at:
                      type: string
                      example: "2026-01-09T17:00:00Z"
    """
    households = household_service.list_households()
    return jsonify(response_schema.dump(households, many=True)), 200


@bp.route('', methods=['POST'])
def create_household():
    """
    Create a new household (Admin only)
    ---
    post:
      summary: Create a household
      tags:
        - Households
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Household A"
                address:
                  type: string
                  example: "123 Main St"
                status:
                  type: string
                  example: "active"
                phone:
                  type: string
                  example: "555-1234"
                
                description:
                  type: string
                  example: "This is a sample household."
      responses:
        201:
          description: Household created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Household A"
                  address:
                    type: string
                    example: "123 Main St"
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
    household = household_service.create_household(
        name=data['name'],
        address=data['address'],
        status=data['status']
    )
    return jsonify(response_schema.dump(household)), 201


@bp.route('/<int:id>', methods=['GET'])
def get_household(id):
    """
    Get household by ID (Admin only)
    ---
    get:
      summary: Get a household by ID
      tags:
        - Households
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: Household ID
      responses:
        200:
          description: Household object
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Household A"
                  address:
                    type: string
                    example: "123 Main St"
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
        404:
          description: Household not found
    """
    household = household_service.get_household(id)
    if not household:
        return jsonify({'message': 'Household not found'}), 404
    return jsonify(response_schema.dump(household)), 200


@bp.route('/<int:id>', methods=['PUT'])
def update_household(id):
    """
    Update household by ID (Admin only)
    ---
    put:
      summary: Update a household
      tags:
        - Households
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Household A Updated"
                address:
                  type: string
                  example: "456 Main St"
      responses:
        200:
          description: Updated household
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Household A Updated"
                  address:
                    type: string
                    example: "456 Main St"
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T18:00:00Z"
        400:
          description: Invalid input
        404:
          description: Household not found
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    household = household_service.update_household(
        household_id=id,
        tax_code=data.get('tax_code'),
        name=data.get('name'),
        phone=data.get('phone'),
        address=data.get('address'),
        description=data.get('description'),
        status=data.get('status'),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(household)), 200


@bp.route('/<int:id>', methods=['DELETE'])
def delete_household(id):
    """
    Delete household by ID (Admin only)
    ---
    delete:
      summary: Delete a household
      tags:
        - Households
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        204:
          description: Household deleted successfully
        404:
          description: Household not found
    """
    household_service.delete_household(id)
    return '', 204


# ---------------- Owner Routes ----------------
@owner_bp.route('', methods=['GET'])
def get_own_household():
    """
    Get own household (Owner only)
    ---
    get:
      summary: Get the household of the current owner
      tags:
        - Households
      responses:
        200:
          description: Household object
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Owner Household"
                  address:
                    type: string
                    example: "789 Owner St"
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T18:00:00Z"
        404:
          description: Household not found
    """
    household = household_service.get_own_household()
    if not household:
        return jsonify({'message': 'Household not found'}), 404
    return jsonify(response_schema.dump(household)), 200


@owner_bp.route('', methods=['PUT'])
def update_own_household():
    """
    Update own household (Owner only)
    ---
    put:
      summary: Update the household of the current owner
      tags:
        - Households
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Owner Household Updated"
                address:
                  type: string
                  example: "987 Owner St"
      responses:
        200:
          description: Updated household
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Owner Household Updated"
                  address:
                    type: string
                    example: "987 Owner St"
                  created_at:
                    type: string
                    example: "2026-01-09T17:00:00Z"
                  updated_at:
                    type: string
                    example: "2026-01-09T18:00:00Z"
        400:
          description: Invalid input
        404:
          description: Household not found
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    household = household_service.update_own_household(
        name=data.get('name'),
        address=data.get('address')
    )
    return jsonify(response_schema.dump(household)), 200
