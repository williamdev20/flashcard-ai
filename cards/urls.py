from django.urls import path
from cards.views.category_create_and_list import category_create_and_list
from cards.views.card_create import card_create
from cards.views.subcategory_and_card_create_and_list import subcategory_and_card_create_and_list
from cards.views.deck_create_and_list import deck_create_and_list
from cards.views.card_detail import card_detail

urlpatterns = [
    path('users/<str:username>/', category_create_and_list, name="create_and_show_category"),

    path('users/<str:username>/<slug:category_slug>/create_cards/', card_create, name="create_card_without_subs_and_decks"),

    path('users/<str:username>/<slug:category_slug>/<slug:subcategory_slug>/<slug:deck_slug>/create_cards/', card_create, name="create_card"),

    path('users/<str:username>/<slug:category_slug>/', subcategory_and_card_create_and_list, name="create_subcategory_or_cards"),

    path('users/<str:username>/<slug:category_slug>/<slug:subcategory_slug>/', deck_create_and_list, name="show_cards_and_decks"),
    
    path('category/view_card/', card_detail, name="view_card")
]
