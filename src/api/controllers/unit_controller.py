from flask import Blueprint, request, g, jsonify
from services.unit_service import UnitService
from infrastructure.repositories.unit_repository import UnitRepository
from api.decorators.auth_decorators import require_permission

# ================= OWNER – F105 =================

owner_bp = Blueprint(
    "owner_units",
    __name__,
    url_prefix="/api/owner/units"
)

# ================= EMPLOYEE – F204 (READ ONLY) =================

employee_bp = Blueprint(
    "employee_units",
    __name__,
    url_prefix="/api/employee/units"
)

unit_service = UnitService(UnitRepository())

# =====================================================
# OWNER
# =====================================================

@owner_bp.route("", methods=["GET"])
@require_permission("F105", ["GET"])
def owner_list_units():
    """
    List units (Owner only)
    ---
    get:
      summary: List units
      tags: [Owner Units]
      security:
        - Bearer: []
      responses:
        200:
          description: List of units
    """
    return jsonify(unit_service.list_units(g.household_id)), 200


@owner_bp.route("", methods=["POST"])
@require_permission("F105", ["POST"])
def owner_create_unit():
    """
    Create unit (Owner only)
    ---
    post:
      summary: Create unit
      tags: [Owner Units]
      security:
        - Bearer: []
      parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            required:
              - name
            properties:
              name:
                type: string
              description:
                type: string
              status:
                type: string
                enum: [ACTIVE, INACTIVE]
      responses:
        201:
          description: Unit created
    """
    data = request.get_json()

    unit = unit_service.create_unit(
        household_id=g.household_id,
        name=data["name"],
        description=data.get("description"),
        status=data.get("status", "ACTIVE")
    )
    return jsonify(unit), 201


@owner_bp.route("/<int:unit_id>", methods=["GET"])
@require_permission("F105", ["GET"])
def owner_get_unit(unit_id):
    """
    Get unit by id (Owner only)
    ---
    get:
      summary: Get unit
      tags: [Owner Units]
      security:
        - Bearer: []
      parameters:
        - name: unit_id
          in: path
          required: true
          type: integer
      responses:
        200:
          description: Unit detail
        404:
          description: Not found
    """
    unit = unit_service.get_unit(unit_id, g.household_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404
    return jsonify(unit), 200


@owner_bp.route("/<int:unit_id>", methods=["PUT"])
@require_permission("F105", ["PUT"])
def owner_update_unit(unit_id):
    """
    Update unit (Owner only)
    ---
    put:
      summary: Update unit
      tags: [Owner Units]
      security:
        - Bearer: []
      parameters:
        - name: unit_id
          in: path
          required: true
          type: integer
        - in: body
          name: body
          schema:
            type: object
            properties:
              name:
                type: string
              description:
                type: string
              status:
                type: string
                enum: [ACTIVE, INACTIVE]
      responses:
        200:
          description: Unit updated
    """
    data = request.get_json()

    unit = unit_service.update_unit(
        unit_id=unit_id,
        household_id=g.household_id,
        name=data.get("name"),
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(unit), 200


@owner_bp.route("/<int:unit_id>", methods=["DELETE"])
@require_permission("F105", ["DELETE"])
def owner_delete_unit(unit_id):
    """
    Delete unit (Owner only)
    ---
    delete:
      summary: Delete unit
      tags: [Owner Units]
      security:
        - Bearer: []
      parameters:
        - name: unit_id
          in: path
          required: true
          type: integer
      responses:
        204:
          description: Deleted
    """
    unit_service.delete_unit(unit_id, g.household_id)
    return "", 204


# =====================================================
# EMPLOYEE – READ ONLY
# =====================================================

@employee_bp.route("", methods=["GET"])
@require_permission("F204", ["GET"])
def employee_list_units():
    """
    List units (Employee – read only)
    ---
    get:
      summary: List units
      tags: [Employee Units]
      security:
        - Bearer: []
      responses:
        200:
          description: List of units
    """
    return jsonify(unit_service.list_units(g.household_id)), 200


@employee_bp.route("/<int:unit_id>", methods=["GET"])
@require_permission("F204", ["GET"])
def employee_get_unit(unit_id):
    """
    Get unit by id (Employee – read only)
    ---
    get:
      summary: Get unit
      tags: [Employee Units]
      security:
        - Bearer: []
      parameters:
        - name: unit_id
          in: path
          required: true
          type: integer
      responses:
        200:
          description: Unit detail
        404:
          description: Not found
    """
    unit = unit_service.get_unit(unit_id, g.household_id)
    if not unit:
        return jsonify({"error": "Unit not found"}), 404
    return jsonify(unit), 200
