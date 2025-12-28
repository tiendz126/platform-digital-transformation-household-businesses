from infrastructure.databases.mssql import init_mssql
from infrastructure.models import (
    AccountingLedger,
    AppointmentModel,
    Category,
    ConsultantModel,
    CourseModel,
    CourseRegisterModel,
    Customer,
    DebtRecord,
    ExportDetail,
    ExportReceipt,
    FeedbackModel,
    Household,
    ImportDetail,
    ImportReceipt,
    Inventory,
    InvoiceDetail,
    Invoice,
    Payment,
    PaymentMethod,
    Product,
    ProgramModel,
    Seller,
    Subscription,
    SubscriptionPlan,
    SurveyModel,
    TodoModel,
    Unit,
    User,
    Warehouse
)

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base