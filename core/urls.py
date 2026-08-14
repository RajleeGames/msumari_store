from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),

    path('pos/', views.pos, name='pos'),
    path('pos/checkout/', views.pos_checkout, name='pos_checkout'),

    path('products/', views.products, name='products'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/toggle/', views.product_toggle, name='product_toggle'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('units/<int:pk>/update/', views.unit_update, name='unit_update'),
    path('units/<int:pk>/delete/', views.unit_delete, name='unit_delete'),

    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    path('stock/', views.stock, name='stock'),
    path('stock/opening/', views.opening_stock, name='opening_stock'),
    path('stock/opening/<int:pk>/delete/', views.opening_batch_delete, name='opening_batch_delete'),
    path('stock/adjust/', views.stock_adjust, name='stock_adjust'),

    path('purchases/', views.purchases, name='purchases'),
    path('purchases/add/', views.purchase_create, name='purchase_create'),
    path('purchases/<int:pk>/edit/', views.purchase_edit, name='purchase_edit'),
    path('purchases/<int:pk>/delete/', views.purchase_delete, name='purchase_delete'),

    path('sales/', views.sales, name='sales'),
    path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sales/<int:pk>/void/', views.sale_void, name='sale_void'),

    path('debts/', views.debts, name='debts'),
    path('debts/customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('debts/customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('debts/customers/<int:pk>/toggle/', views.customer_toggle, name='customer_toggle'),
    path('debts/customers/<int:pk>/payments/add/', views.customer_payment_create, name='customer_payment_create'),
    path('debts/payments/<int:pk>/void/', views.customer_payment_void, name='customer_payment_void'),


    path('end-day/', views.end_day, name='end_day'),
    path('end-day/<int:pk>/amend/', views.cash_closing_amend, name='cash_closing_amend'),

    path('stocktakes/', views.stocktakes, name='stocktakes'),
    path('stocktakes/<int:pk>/', views.stocktake_detail, name='stocktake_detail'),

    path('data-tools/', views.data_tools, name='data_tools'),
    path('data-tools/export/<str:kind>/', views.export_csv, name='export_csv'),
    path('data-tools/export-all/', views.export_all_zip, name='export_all_zip'),
    path('data-tools/backup/', views.backup_download, name='backup_download'),

    path('expenses/', views.expenses, name='expenses'),
    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),

    path('reports/', views.reports, name='reports'),

    path('users/', views.users, name='users'),
    path('users/add/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/toggle/', views.user_toggle, name='user_toggle'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    path('settings/', views.settings_view, name='settings'),


    # ============================================================
# QZ TRAY
# ============================================================

path(
    'qz/cert/',
    views.qz_certificate,
    name='qz_certificate'
),

path(
    'qz/sign/',
    views.qz_sign,
    name='qz_sign'
),
]
