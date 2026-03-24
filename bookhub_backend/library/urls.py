from django.urls import path
from . import views

urlpatterns = [
    # Main Pages
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delivery/', views.delivery_dashboard, name='delivery_dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('categories/', views.categories_view, name='categories'),

    # --- DELIVERY PORTAL AJAX ACTION ---
    # This line is critical for the "Accept" and "Delivered" buttons to work on the map page
    path('update-order-status/', views.update_order_status, name='update_order_status'),

    # --- ADMIN DASHBOARD ACTIONS ---
    
    # Action to add a book
    path('admin-dashboard/add-book/', views.add_book, name='add_book'),
    
    # Action to delete a book (takes the book's ID)
    path('admin-dashboard/delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    
    # Action to edit a book (takes the book's ID)
    path('admin-dashboard/edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    
    # Action to add a rider
    path('admin-dashboard/add-rider/', views.add_rider, name='add_rider'),
    
    # Action to assign an order to a rider
    path('admin-dashboard/assign-order/', views.assign_order, name='assign_order'),
]