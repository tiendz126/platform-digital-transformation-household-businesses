from flask import Blueprint, request, g
from services.product_service import ProductService
from infrastructure.repositories.product_repository import ProductRepository
from api.schemas.product import (
    ProductRequestSchema,
    ProductUpdateSchema,
    ProductResponseSchema
)
from api.responses import success_response, error_response, not_found_response
from api.decorators.auth_decorators import require_permission

# ================= BLUEPRINT =================

owner_bp = Blueprint(
    "owner_products",
    __name__,
    url_prefix="/api/owner/products"
)

employee_bp = Blueprint(
    "employee_products",
    __name__,
    url_prefix="/api/employee/products"
)

product_service = ProductService(ProductRepository())

request_schema = ProductRequestSchema()
update_schema = ProductUpdateSchema()
response_schema = ProductResponseSchema()

# ================= OWNER – F104 =================

@owner_bp.route("", methods=["GET"])
@require_permission(function_code="F104", methods=["GET"])
def owner_list_products():
    """
    Get list of products (Owner only)
    ---
    get:
      summary: List products
      tags:
        - Owner Products
      responses:
        200:
          description: List of products
    """
    products = product_service.list_products(g.household_id)
    return success_response(response_schema.dump(products, many=True))


@owner_bp.route("", methods=["POST"])
@require_permission(function_code="F104", methods=["POST"])
def owner_create_product():
    """
    Create product (Owner only)
    ---
    post:
      summary: Create new product
      tags:
        - Owner Products
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProductRequest'
      responses:
        201:
          description: Product created successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return error_response(errors, 422)

    product = product_service.create_product(
        household_id=g.household_id,
        category_id=data["category_id"],
        name=data["name"],
        image_url=data.get("image_url"),
        description=data.get("description"),
        status=data.get("status")
    )
    return success_response(
        response_schema.dump(product),
        "Product created successfully"
    )


@owner_bp.route("/<int:product_id>", methods=["GET"])
@require_permission(function_code="F104", methods=["GET"])
def owner_get_product(product_id):
    """
    Get product by id (Owner only)
    ---
    get:
      summary: Get product detail
      tags:
        - Owner Products
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Product detail
        404:
          description: Product not found
    """
    product = product_service.get_product(product_id, g.household_id)
    if not product:
        return not_found_response("Product not found")

    return success_response(response_schema.dump(product))


@owner_bp.route("/<int:product_id>", methods=["PUT"])
@require_permission(function_code="F104", methods=["PUT"])
def owner_update_product(product_id):
    """
    Update product (Owner only)
    ---
    put:
      summary: Update product
      tags:
        - Owner Products
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProductUpdate'
      responses:
        200:
          description: Product updated successfully
        422:
          description: Validation error
    """
    data = request.get_json()
    errors = update_schema.validate(data)
    if errors:
        return error_response(errors, 422)

    product = product_service.update_product(
        product_id=product_id,
        household_id=g.household_id,
        category_id=data.get("category_id"),
        name=data.get("name"),
        image_url=data.get("image_url"),
        description=data.get("description"),
        status=data.get("status")
    )
    return success_response(
        response_schema.dump(product),
        "Product updated successfully"
    )


@owner_bp.route("/<int:product_id>", methods=["DELETE"])
@require_permission(function_code="F104", methods=["DELETE"])
def owner_delete_product(product_id):
    """
    Delete product (Owner only)
    ---
    delete:
      summary: Delete product
      tags:
        - Owner Products
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        204:
          description: Product deleted successfully
    """
    product_service.delete_product(product_id, g.household_id)
    return success_response(None, "Product deleted successfully")


# ================= EMPLOYEE – F201 (READ ONLY) =================

@employee_bp.route("", methods=["GET"])
@require_permission(function_code="F201", methods=["GET"])
def employee_list_products():
    """
    List products (Employee only – read only)
    ---
    get:
      summary: List products (Employee)
      tags:
        - Employee Products
      responses:
        200:
          description: List of products
    """
    products = product_service.list_products(g.household_id)
    return success_response(response_schema.dump(products, many=True))


@employee_bp.route("/<int:product_id>", methods=["GET"])
@require_permission(function_code="F201", methods=["GET"])
def employee_get_product(product_id):
    """
    Get product by id (Employee only – read only)
    ---
    get:
      summary: Get product detail (Employee)
      tags:
        - Employee Products
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Product detail
        404:
          description: Product not found
    """
    product = product_service.get_product(product_id, g.household_id)
    if not product:
        return not_found_response("Product not found")

    return success_response(response_schema.dump(product))
