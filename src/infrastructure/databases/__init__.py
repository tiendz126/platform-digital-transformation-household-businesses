from infrastructure.databases.mssql import init_mssql
from infrastructure.models import (
    AccountingLedger,
    Category,
    Customer,
    DebtRecord,
    ExportDetail,
    ExportReceipt,
    Household,
    ImportDetail,
    ImportReceipt,
    Inventory,
    InvoiceDetail,
    Invoice,
    Payment,
    PaymentMethod,
    Product,
    Seller,
    Subscription,
    SubscriptionPlan,
    TodoModel,
    Unit,
    User,
    Warehouse
)

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base