from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from cards.models import Category, Subcategory, Deck


@login_required(login_url="/login/")
def deck_create_and_list(request, username, category_slug, subcategory_slug):

    user = User.objects.filter(username=username).first()
    if user is None:
        raise Http404()
    
    if request.user.username != username:
        raise PermissionDenied
    
    category = get_object_or_404(Category, user=request.user, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, category=category, slug=subcategory_slug)

    return render(request, "cards/show_cards_and_decks.html", {
        "category_slug": category.slug,
        "subcategory_slug": subcategory.slug
    })