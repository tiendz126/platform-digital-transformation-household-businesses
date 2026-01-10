from flask import Blueprint, request, g, jsonify
from services.unit_service import UnitService
from infrastructure.repositories.unit_repository import UnitRepository
from api.schemas.unit import (
    UnitRequestSchema,
    UnitUpdateSchema,
    UnitResponseSchema
)
from api.decorators.auth_decorators import require_permission

# ================= BLUEPRINT =================

owner_bp = Blueprint(
    "owner_units",
    __name__,
    url_prefix="/api/owner/units"
)

employee_bp = Blueprint(
    "employee_units",
    __name__,
    url_prefix="/api/employee/units"
)

unit_service = UnitService(UnitRepository())

request_schema = UnitRequestSchema()
update_schema = UnitUpdateSchema()
response_schema = UnitResponseSchema()

# ================= OWNER – F105 =================

@owner_bp.route("", methods=["GET"])
@require_permission(function_code="F105", methods=["GET"])
def owner_list_units():
    """
    Get list of units (Owner only)
    ---
    get:
      summary: List units
      tags:
        - Owner Units
      responses:
        200:
          description: List of units
    """
    units = unit_service.list_units(g.household_id)
    return jsonify(response_schema.dump(units, many=True)), 200


@owner_bp.route("", methods=["POST"])
@require_permission(function_code="F105", methods=["POST"])
def owner_create_unit():
    """
    Create unit (Owner only)
    ---
    post:
      summary: Create new unit
      tags:
        - Owner Units
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UnitRequest'
      responses:
        201:
          description: Unit created successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    unit = unit_service.create_unit(
        household_id=g.household_id,
        name=data["name"],
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(unit)), 201


@owner_bp.route("/<int:unit_id>", methods=["GET"])
@require_permission(function_code="F105", methods=["GET"])
def owner_get_unit(unit_id):
    """
    Get unit by id (Owner only)
    ---
    get:
      summary: Get unit detail
      tags:
        - Owner Units
      parameters:
        - name: unit_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Unit detail
        404:
          description: Unit not found
    """
    unit = unit_service.get_unit(unit_id, g.household_id)
    if not unit:
        return jsonify({"message": "Unit not found"}), 404

    return jsonify(response_schema.dump(unit)), 200


@owner_bp.route("/<int:unit_id>", methods=["PUT"])
@require_permission(function_code="F105", methods=["PUT"])
def owner_update_unit(unit_id):
    """
    Update unit (Owner only)
    ---
    put:
      summary: Update unit
      tags:
        - Owner Units
      parameters:
        - name: unit_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UnitUpdate'
      responses:
        200:
          description: Unit updated successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = update_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    unit = unit_service.update_unit(
        unit_id=unit_id,
        household_id=g.household_id,
        name=data.get("name"),
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(unit)), 200


@owner_bp.route("/<int:unit_id>", methods=["DELETE"])
@require_permission(function_code="F105", methods=["DELETE"])
def owner_delete_unit(unit_id):
    """
    Delete unit (Owner only)
    ---
    delete:
      summary: Delete unit
      tags:
        - Owner Units
      parameters:
        - name: unit_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        204:
          description: Unit deleted successfully
    """
    unit_service.delete_unit(unit_id, g.household_id)
    return "", 204


# ================= EMPLOYEE – F204 (READ ONLY) =================

@employee_bp.route("", methods=["GET"])
@require_permission(function_code="F204", methods=["GET"])
def employee_list_units():
    """
    List units (Employee only – read only)
    ---
    get:
      summary: List units (Employee)
      tags:
        - Employee Units
      responses:
        200:
          description: List of units
    """
    units = unit_service.list_units(g.household_id)
    return jsonify(response_schema.dump(units, many=True)), 200
