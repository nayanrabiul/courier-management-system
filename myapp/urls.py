from django.urls import path
from . import views

handler404 = views.handler404

urlpatterns = [
    path('sendmail/', views.sendmail, name="sendmail"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
    path('admin_user/', views.admin_user, name="admin_user"),
    path('officer/', views.officer, name="officer"),
    path('disp/', views.disp, name="disp"),
    path('cheakout/', views.cheakout, name="cheakout"),


    path('inventory/', views.inventory, name="inventory"),


    path('update_user/<str:pk>/', views.update_user, name="update_user"),
    path('delete_user/<str:pk>/', views.delete_user, name="delete_user"),

    path('view_product/<str:pk>/', views.view_product, name="view_product"),
    path('view_product', views.view_products, name="view_products"),
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('user_update_for_disp/<str:pk>/',
         views.user_update_for_disp, name="user_update_for_disp"),
    path('user_update_for_disp_return/<str:pk>/',
         views.user_update_for_disp_return, name="user_update_for_disp_return"),

    path('paid_for_user/<str:pk>/', views.paid_for_user, name="paid_for_user"),
    path('product_return/<str:pk>/', views.product_return, name="product_return"),

    path('branch_product/', views.branch_product, name="branch_product"),

    path('product_registration', views.product_registration,
         name='product_registration'),
    path('change_password', views.change_password, name='change_password'),


    path('', views.home, name="home")

]
