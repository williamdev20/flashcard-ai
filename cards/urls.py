from django.urls import path
from . import views

urlpatterns = [
    # Em breve: /users/{id}/
    path('users/<str:username>/', views.create_and_show_category, name="create_and_show_category"),
    # /category/<str:category_name>
    path('users/<str:username>/<slug:category_slug>/', views.create_subcategory_or_cards, name="create_subcategory_or_cards"),
    path('users/<str:username>/<slug:category_slug>/<slug:subcategory_slug>/', views.show_cards_and_decks, name="show_cards_and_decks"),
    path('users/<str:username>/<slug:category_slug>/<slug:subcategory_slug>/<slug:deck_slug>/create_cards/', views.create_card, name="create_card"),
    path('category/view_card/', views.view_card, name="view_card")
]
