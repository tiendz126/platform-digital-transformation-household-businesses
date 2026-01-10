from flask import Blueprint, request, g, jsonify
from services.category_service import CategoryService
from infrastructure.repositories.category_repository import CategoryRepository
from api.schemas.category import (
    CategoryRequestSchema,
    CategoryUpdateSchema,
    CategoryResponseSchema
)
from api.decorators.auth_decorators import require_permission

# ================= BLUEPRINT =================

owner_bp = Blueprint(
    "owner_categories",
    __name__,
    url_prefix="/api/owner/categories"
)

employee_bp = Blueprint(
    "employee_categories",
    __name__,
    url_prefix="/api/employee/categories"
)

category_service = CategoryService(CategoryRepository())

request_schema = CategoryRequestSchema()
update_schema = CategoryUpdateSchema()
response_schema = CategoryResponseSchema()

# ================= OWNER – F103 =================

@owner_bp.route("", methods=["GET"])
@require_permission(function_code="F103", methods=["GET"])
def owner_list_categories():
    """
    Get list of categories (Owner only)
    ---
    get:
      summary: List categories
      tags:
        - Owner Categories
      responses:
        200:
          description: List of categories
    """
    categories = category_service.list_categories(g.household_id)
    return jsonify(response_schema.dump(categories, many=True)), 200


@owner_bp.route("", methods=["POST"])
@require_permission(function_code="F103", methods=["POST"])
def owner_create_category():
    """
    Create category (Owner only)
    ---
    post:
      summary: Create new category
      tags:
        - Owner Categories
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CategoryRequest'
      responses:
        201:
          description: Category created successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    category = category_service.create_category(
        household_id=g.household_id,
        name=data["name"],
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(category)), 201


@owner_bp.route("/<int:category_id>", methods=["GET"])
@require_permission(function_code="F103", methods=["GET"])
def owner_get_category(category_id):
    """
    Get category by id (Owner only)
    ---
    get:
      summary: Get category detail
      tags:
        - Owner Categories
      parameters:
        - name: category_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Category detail
        404:
          description: Category not found
    """
    category = category_service.get_category(category_id, g.household_id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    return jsonify(response_schema.dump(category)), 200


@owner_bp.route("/<int:category_id>", methods=["PUT"])
@require_permission(function_code="F103", methods=["PUT"])
def owner_update_category(category_id):
    """
    Update category (Owner only)
    ---
    put:
      summary: Update category
      tags:
        - Owner Categories
      parameters:
        - name: category_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CategoryUpdate'
      responses:
        200:
          description: Category updated successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = update_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    category = category_service.update_category(
        category_id=category_id,
        household_id=g.household_id,
        name=data.get("name"),
        description=data.get("description"),
        status=data.get("status")
    )
    return jsonify(response_schema.dump(category)), 200


@owner_bp.route("/<int:category_id>", methods=["DELETE"])
@require_permission(function_code="F103", methods=["DELETE"])
def owner_delete_category(category_id):
    """
    Delete category (Owner only)
    ---
    delete:
      summary: Delete category
      tags:
        - Owner Categories
      parameters:
        - name: category_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        204:
          description: Category deleted successfully
    """
    category_service.delete_category(category_id, g.household_id)
    return "", 204


# ================= EMPLOYEE – F202 (READ ONLY) =================

@employee_bp.route("", methods=["GET"])
@require_permission(function_code="F202", methods=["GET"])
def employee_list_categories():
    """
    List categories (Employee only – read only)
    ---
    get:
      summary: List categories (Employee)
      tags:
        - Employee Categories
      responses:
        200:
          description: List of categories
    """
    categories = category_service.list_categories(g.household_id)
    return jsonify(response_schema.dump(categories, many=True)), 200


@employee_bp.route("/<int:category_id>", methods=["GET"])
@require_permission(function_code="F202", methods=["GET"])
def employee_get_category(category_id):
    """
    Get category by id (Employee only – read only)
    ---
    get:
      summary: Get category detail (Employee)
      tags:
        - Employee Categories
      parameters:
        - name: category_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Category detail
        404:
          description: Category not found
    """
    category = category_service.get_category(category_id, g.household_id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    return jsonify(response_schema.dump(category)), 200