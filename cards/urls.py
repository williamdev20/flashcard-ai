from django.urls import path
from . import views

urlpatterns = [
    # Em breve: /users/{id}/
    path('create_cards/', views.create_card, name="create_card"),
    path('users/<str:username>/category/', views.create_and_show_category, name="create_and_show_category"),
    # /category/<str:category_name>
    path('category/create_subcategory_or_cards/', views.create_subcategory_or_cards, name="create_subcategory_or_cards"),
    path('categort/view_card/', views.view_card, name="view_card")
]
