from django.urls import path
from . import views

urlpatterns = [
    # Em breve: /users/{id}/
    path('', views.create_card, name="create_card"),
    path('category/', views.show_category, name="show_category"),
    # /category/<str:category_name>
    path('category/create_subcategory_or_cards/', views.create_subcategory_or_cards, name="create_subcategory_or_cards"),
]
