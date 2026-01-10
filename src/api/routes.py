from api.controllers.todo_controller import bp as todo_bp
from api.controllers.auth_controller import auth_bp
from api.controllers.user_controller import admin_bp as admin_users_bp, owner_bp as owner_employees_bp
from api.controllers.role_controller import bp as admin_roles_bp
from api.controllers.function_controller import bp as admin_functions_bp
from api.controllers.role_function_controller import bp as admin_role_functions_bp
from api.controllers.product_controller import owner_bp as owner_products_bp, employee_bp as employee_products_bp
from api.controllers.category_controller import owner_bp as owner_categories_bp, employee_bp as employee_categories_bp
from api.controllers.unit_controller import owner_bp as owner_units_bp, employee_bp as employee_units_bp
from api.controllers.warehouse_controller import owner_bp as owner_warehouses_bp, employee_bp as employee_warehouses_bp

def register_routes(app):
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_users_bp)
    app.register_blueprint(owner_employees_bp)
    app.register_blueprint(admin_roles_bp)
    app.register_blueprint(admin_functions_bp)
    app.register_blueprint(admin_role_functions_bp) 

    app.register_blueprint(owner_products_bp)
    app.register_blueprint(employee_products_bp)
    app.register_blueprint(owner_categories_bp)
    app.register_blueprint(employee_categories_bp)
    app.register_blueprint(owner_units_bp)
    app.register_blueprint(employee_units_bp)
    app.register_blueprint(owner_warehouses_bp)
    app.register_blueprint(employee_warehouses_bp)