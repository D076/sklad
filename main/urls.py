from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('index/<int:id>', views.product_list, name='product_list'),
    # path('products/<int:id>/delete', views.product_delete, name='product_delete'),
    # path('products/<int:id>/edit', views.product_edit, name='product_edit'),
    # path('products/<int:id>', views.product_view, name='product_view'),
    # path('products/create', views.create_item, name='create_item'),
    # path('search/', views.search_list, name='search'),
    # path('login/', views.login_user, name='logs'),
    # path('logout/', views.logout_user, name='logout')
]
