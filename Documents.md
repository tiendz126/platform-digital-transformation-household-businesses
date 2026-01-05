# Platform to Support Digital Transformation for Household Businesses

**Vietnamese:** Nền tảng hỗ trợ chuyển đổi số cho hộ kinh doanh.  
**Abbreviation:** BizFlow

## a. Context

*   **Economic Role:** In Vietnam, household businesses play a critical role in the local economy, especially in traditional sectors such as building materials, construction supplies, and hardware retail. The majority of these fall under Group 1 or Group 2 classifications as defined by the Ministry of Finance's Decision 3389/QĐ-BTC (2025).
*   **Current State:** Consequently, most of these businesses still operate using fully manual workflows. Daily tasks such as recording sales, managing inventory, tracking customer debts, and processing phone/Zalo orders are typically performed with handwritten notebooks or simple Excel files. Moreover, household businesses often lack the budget to hire accountants.
*   **Gap in Market:** Despite the rapidly growing demand for digital transformation across industries, existing commercial POS or business management solutions are often designed for restaurants, retail fashion, or large enterprises. These systems fail to meet the unique operational characteristics of household businesses, which include:
    *   Multi-channel orders (at-counter sales and phone/Zalo orders).
    *   Customer debt management with long-term transaction history.
    *   Low digital literacy among store owners.
*   **Hardware Limitations:** Most household businesses also lack the essential hardware required to adopt existing digital solutions. Many operate with only a single smartphone, without computers, barcode scanners, receipt printers, POS terminals, or cash drawers. This limitation makes POS systems impractical, as such solutions typically require multiple devices and a stable hardware setup. The high upfront cost of purchasing these devices further prevents household businesses from transitioning to digital workflows, forcing them to continue relying on fully manual processes.
*   **Challenges:** Due to the lack of a specialized platform, household businesses face several challenges: frequent errors in manual calculations, slow order processing, difficulty tracking inventory, inconsistent debt records, and no access to real-time business insights. The result is reduced operational efficiency, financial risks, and an inability to scale or modernize business operations.
*   **Proposed Solution:** To address this gap, we propose developing a **Platform to support digital transformation for household businesses**, a comprehensive system designed specifically for traditional stores. The platform integrates an interface with an AI-powered assistant capable of understanding natural language requests (via text or voice) to automatically create draft orders and auto fill data into templates. This combination supports automation, reduces human errors, and provides business owners with real-time visibility into their operations.

## b. Proposed Solutions

Build an application (mobile and/or web) that supports the following core functionalities:

### Roles & Responsibilities

#### Employee
*   Login to the system.
*   Create at-counter orders quickly (search products, add quantity, add customers details).
*   Print sales orders.
*   Record debt for registered customers.
*   Receive real-time notifications for new orders.
*   View and confirm "Draft Orders" created by the AI.

#### Owner
*   *Includes all Employee permissions.*
*   Manage product catalog (name, price, multiple units of measure).
*   Manage inventory (new stock, view stock levels).
*   Manage customers (info, purchase history, debt).
*   View reports and analytics (daily/monthly revenue, best-sellers, outstanding debt).
*   Manage employee accounts.

#### Administrator
*   Manage owner accounts.
*   View reports, analytics and feedback.
*   Manage Subscription Pricing.
*   Update system config and templates for financial reports.

#### System
*   Convert natural language into draft order.
*   Automatically does the bookkeeping.

---

### Functional Requirements

#### Employee
*   **Login:** Employees can log in using an account.
*   **Create At-Counter Orders:** Employees can quickly create orders for walk-in customers. They can search products, select quantity, assign customers (optional), and add items to the cart. The interface must support fast operations through keyboard shortcuts and instant product filtering.
*   **Record debt for registered customers:** If the customer chooses to buy on credit, the Employee can record the debt directly during order creation. The system automatically updates the customer’s outstanding balance.
*   **Print Sales Orders:** After creating an order, the employee can generate and print orders using pre-designed bill templates. The system stores each order in the database for future retrieval.
*   **Receive Real-Time Notifications for AI/Chatbot Orders:** When the AI assistant receives a message (text or voice) and generates a draft order, the interface will immediately display a real-time notification.
*   **View and confirm "Draft Orders" created by the AI:** The draft order will be sent to the employee for checking and confirmation.

#### Owner
*(Owner includes all Employee functions, plus the following additional capabilities)*
*   **Manage Product Catalog:** The owner can create, update, or disable products. They can define product attributes such as name, images, price, category, and multiple units of measure. Pricing rules can also be configured.
*   **Manage Inventory:** The owner can record stock imports, track stock levels in real time, and view inventory history. The system automatically deducts stock upon order confirmation.
*   **Manage Customers:** The owner can add and update customer information, view their purchase history, track outstanding debts, and review payment logs.
*   **View Reports & Analytics:** Provides interactive dashboards that show daily/weekly/monthly revenue, top-selling products, low-stock alerts, and total outstanding debts. Data visualization supports charts and summary widgets.
*   **Manage Employee Accounts:** The owner can create new employee accounts, reset passwords and deactivate accounts. Audit logs track who made each change for accountability.

#### System
*   **Convert natural language into draft order:** It "listens" (or reads) what the user says (e.g., "get 5 cement bags for Mr. Ba, put it on his tab") and automatically creates a draft order from that command.
*   **Automatically does the bookkeeping:** The system automatically performs bookkeeping for every sale, stock import, and customer debt transaction. Based on this recorded data, it automatically calculates, summarizes, and populates the official accounting books and financial reports required by **Circular 88/2021/TT-BTC** (Vietnam's official accounting standard for household businesses). This feature eliminates all manual calculation and data entry in Excel, ensuring that reports (e.g., Detailed Revenue Ledger, Outstanding Debt Report, Business Operations Report) are accurate and legally compliant for tax purposes. The platform guarantees that these report templates will be continuously updated to align with the latest government regulations as they are issued, ensuring long-term compliance for the business owner.

#### Administrator
*   **Owner Account Management:** Admins can view, search, filter, and manage all registered "Owner" (business household) accounts. This includes activating or deactivating accounts, and viewing detailed profiles.
*   **Manage Subscription Pricing:** Admins can define and update the pricing for the various subscription plans offered on the platform (e.g., set the monthly/annual cost for the Basic, Pro plans).
*   **Platform Analytics & Reporting:** Admins can access a global dashboard to monitor the health, growth, and revenue of the entire platform. This includes viewing total active users, new subscriptions.
*   **System & AI Configuration:** Admins can manage global system settings. Updating the master templates for financial reports (Circular 88/2021/TT-BTC), and broadcasting system-wide announcements.

### Non-functional Requirements

1.  **Security & Privacy**
    *   Protect the sales information of household businesses.
    *   Strict role-based access control for Employee, Owner, and Admin roles.
2.  **Performance & Scalability**
    *   Application responds quickly (< 2000 ms for core actions).
    *   Supports large product catalogs and multiple concurrent users.
3.  **Reliability & AI Accuracy**
    *   Employees or owners can review, edit, or reject AI-generated draft orders.
    *   Fall back to manual operation if AI is unavailable.
4.  **Usability & Accessibility**
    *   Simple, responsive web/mobile UI suitable for low digital literacy.
    *   Vietnamese interface; Unicode preserved.
    *   Real-time notifications.
5.  **Compliance & Reporting**
    *   Automatically generates accounting reports following Circular 88/2021/TT-BTC.
    *   Owners can review, edit, or reject AI-generated reports.
    *   The platform guarantees that all accounting report templates will be continuously updated to align with any future changes in the official declaration forms issued by the tax authorities.

---

## 3.2. Main Proposal Content (including result and product)

### a. Theory and Practice (Document)
*   Students should apply the software development process and UML 2.0 to model the system.
*   **The documentation includes:**
    *   User Requirement
    *   Software Requirement Specification
    *   Architecture Design
    *   Detailed Design
    *   System Implementation
    *   Testing Document
    *   Installation Guide
    *   Source code and deployable software packages
*   **Server-side technologies:**
    *   Clean architecture implemented in Python (BE)
    *   Data storage with SQL Server and PostgreSQL
    *   Caching: Redis
*   **AI:** Python
    *   RAG: ChromaDB, text-embedding-3-small
    *   LLM: OpenAI/Gemini
    *   Speech-to-Text: Google Speech-to-Text/Whisper
*   **Client-side technologies:**
    *   Mobile application: Flutter, Notification.
    *   Web Client: NextJS, Tanstack Query, Shadcn UI, TailwindCSS

### b. Products
*   Mobile application
*   Web application

### c. Proposed Tasks
*   **Task Package 1:** Deploy databases (MySQL and PostgreSQL)
*   **Task Package 2:** Set up clean architecture with Python
*   **Task Package 3:** Develop and deploy the mobile application using Flutter
*   **Task Package 4:** Develop and deploy the web application

## Appendix: Function Permissions

### 1. Admin (F0xx)
| Code | Name | Methods |
| :--- | :--- | :--- |
| F001 | manage_households | C,R,U,D |
| F002 | manage_subscription_plans | C,R,U,D |
| F003 | manage_subscriptions | C,R,U,D |
| F004 | view_platform_analytics | R |
| F005 | manage_admin_users | C,R,U,D |
| F006 | manage_system_config | R,U |
| F007 | view_all_accounting_ledgers | R |

### 2. Owner (F1xx)
| Code | Name | Methods |
| :--- | :--- | :--- |
| F101 | manage_employees | C,R,U,D |
| F102 | view_own_household | R,U |
| F103 | manage_categories | C,R,U,D |
| F104 | manage_products | C,R,U,D |
| F105 | manage_units | C,R,U,D |
| F106 | manage_inventory | C,R,U,D |
| F107 | manage_warehouses | C,R,U,D |
| F108 | manage_import_receipts | C,R,U,D |
| F109 | manage_customers | C,R,U,D |
| F110 | manage_sellers | C,R,U,D |
| F111 | manage_all_invoices | C,R,U,D |
| F112 | manage_payments | C,R,U,D |
| F113 | manage_payment_methods | C,R,U,D |
| F114 | manage_debt_records | C,R,U,D |
| F115 | view_household_reports | R |
| F116 | view_accounting_ledgers | R |
| F117 | export_reports | R |
| F118 | manage_export_receipts | C,R,U,D |

### 3. Employee (F2xx)
| Code | Name | Methods |
| :--- | :--- | :--- |
| F201 | view_products | R |
| F202 | view_categories | R |
| F203 | view_inventory | R |
| F204 | view_units | R |
| F205 | view_customers | R |
| F206 | view_customer_debt | R |
| F207 | create_sales_invoice | C,R |
| F208 | view_own_invoices | R |
| F209 | update_draft_invoice | U |
| F210 | confirm_invoice | U |
| F211 | record_payment | C,R |
| F212 | record_debt | C,R |
| F213 | view_draft_orders | R |
| F214 | confirm_draft_order | U |
| F215 | receive_notifications | R |
