from flask import Blueprint, request, g, jsonify
from services.warehouse_service import WarehouseService
from infrastructure.repositories.warehouse_repository import WarehouseRepository
from api.schemas.warehouse import (
    WarehouseRequestSchema,
    WarehouseUpdateSchema,
    WarehouseResponseSchema
)
from api.decorators.auth_decorators import require_permission


# ================= OWNER – F107 =================

owner_bp = Blueprint(
    "owner_warehouses",
    __name__,
    url_prefix="/api/owner/warehouses"
)

# ================= EMPLOYEE – F207 (READ ONLY) =================

employee_bp = Blueprint(
    "employee_warehouses",
    __name__,
    url_prefix="/api/employee/warehouses"
)

warehouse_service = WarehouseService(WarehouseRepository())

request_schema = WarehouseRequestSchema()
update_schema = WarehouseUpdateSchema()
response_schema = WarehouseResponseSchema()


@owner_bp.route("", methods=["GET"])
@require_permission(function_code="F107", methods=["GET"])
def owner_list_warehouses():
    """
    List warehouses (Owner only)
    ---
    get:
      summary: List warehouses
      security:
        - Bearer: []
      tags:
        - Owner Warehouses
      responses:
        200:
          description: List of warehouses
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/WarehouseResponse'
    """
    warehouses = warehouse_service.list_warehouses(g.household_id)
    return jsonify(response_schema.dump(warehouses, many=True)), 200


@owner_bp.route("", methods=["POST"])
@require_permission(function_code="F107", methods=["POST"])
def owner_create_warehouse():
    """
    Create warehouse (Owner only)
    ---
    post:
      summary: Create warehouse
      security:
        - Bearer: []
      tags:
        - Owner Warehouses
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WarehouseRequest'
      responses:
        201:
          description: Warehouse created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WarehouseResponse'
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    warehouse = warehouse_service.create_warehouse(
        household_id=g.household_id,
        name=data["name"],
        address=data["address"],
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(warehouse)), 201


@owner_bp.route("/<int:warehouse_id>", methods=["GET"])
@require_permission(function_code="F107", methods=["GET"])
def owner_get_warehouse(warehouse_id):
    """
    Get warehouse by id (Owner only)
    ---
    get:
      summary: Get warehouse detail
      security:
        - Bearer: []
      tags:
        - Owner Warehouses
      parameters:
        - name: warehouse_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Warehouse detail
        404:
          description: Warehouse not found
    """
    warehouse = warehouse_service.get_warehouse(warehouse_id, g.household_id)
    if not warehouse:
        return jsonify({"message": "Warehouse not found"}), 404

    return jsonify(response_schema.dump(warehouse)), 200


@owner_bp.route("/<int:warehouse_id>", methods=["PUT"])
@require_permission(function_code="F107", methods=["PUT"])
def owner_update_warehouse(warehouse_id):
    """
    Update warehouse (Owner only)
    ---
    put:
      summary: Update warehouse
      security:
        - Bearer: []
      tags:
        - Owner Warehouses
      parameters:
        - name: warehouse_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WarehouseUpdate'
      responses:
        200:
          description: Warehouse updated successfully
        404:
          description: Warehouse not found
    """
    data = request.get_json()
    errors = update_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    warehouse = warehouse_service.update_warehouse(
        warehouse_id=warehouse_id,
        household_id=g.household_id,
        name=data.get("name"),
        address=data.get("address"),
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(warehouse)), 200


@owner_bp.route("/<int:warehouse_id>", methods=["DELETE"])
@require_permission(function_code="F107", methods=["DELETE"])
def owner_delete_warehouse(warehouse_id):
    """
    Delete warehouse (Owner only)
    ---
    delete:
      summary: Delete warehouse
      security:
        - Bearer: []
      tags:
        - Owner Warehouses
      parameters:
        - name: warehouse_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        204:
          description: Warehouse deleted successfully
    """
    warehouse_service.delete_warehouse(warehouse_id, g.household_id)
    return "", 204


# ================= EMPLOYEE – READ ONLY =================

@employee_bp.route("", methods=["GET"])
@require_permission(function_code="F207", methods=["GET"])
def employee_list_warehouses():
    """
    List warehouses (Employee – read only)
    ---
    get:
      summary: List warehouses
      security:
        - Bearer: []
      tags:
        - Employee Warehouses
      responses:
        200:
          description: List of warehouses
    """
    warehouses = warehouse_service.list_warehouses(g.household_id)
    return jsonify(response_schema.dump(warehouses, many=True)), 200


@employee_bp.route("/<int:warehouse_id>", methods=["GET"])
@require_permission(function_code="F207", methods=["GET"])
def employee_get_warehouse(warehouse_id):
    """
    Get warehouse by id (Employee – read only)
    ---
    get:
      summary: Get warehouse detail
      security:
        - Bearer: []
      tags:
        - Employee Warehouses
      parameters:
        - name: warehouse_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Warehouse detail
        404:
          description: Warehouse not found
    """
    warehouse = warehouse_service.get_warehouse(warehouse_id, g.household_id)
    if not warehouse:
        return jsonify({"message": "Warehouse not found"}), 404

    return jsonify(response_schema.dump(warehouse)), 200
