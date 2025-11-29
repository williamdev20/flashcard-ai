from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Category, Subcategory, Deck


@login_required(login_url="/login/")
def create_and_show_category(request, username):
    error = ""

    procfile_user = User.objects.filter(username=username).first()
    if procfile_user is None:
        raise Http404()

    if request.method == "POST":
        category_name = request.POST.get('category_name')

        try:
            Category.objects.create(
                user=request.user,
                name=category_name
            )
        except IntegrityError as e:
            error = "Já existe uma categoria com esse nome!"
            print(f"ERROR: Erro ao tentar criar uma categoria: {e}")

    categories = Category.objects.filter(user=procfile_user)

    if request.headers.get("HX-Request"): # Requisão do HTMX
        html = render_to_string(
                "cards/partials/category_list.html",
                {"categories": categories},
                request=request
        )
        return HttpResponse(html)


    return render(request, "cards/show_category.html", {
        "error": error,
        "categories": categories
    })


@login_required(login_url="/login/")
def create_subcategory_or_cards(request, username: str, category_slug: str):
    error = ""

    user = User.objects.filter(username=username).first()
    if user is None:
        raise Http404()

    if request.user.username != username:
        raise PermissionDenied # Status 403 - Logado, mas sem permissão para acessar tal

    category = get_object_or_404(Category, user=request.user, slug=category_slug)
    

    if request.method == "POST":
        subcategory_name = request.POST.get("create_subcategory")

        try:
            Subcategory.objects.create(
                category=category,
                name=subcategory_name
            )
        except IntegrityError as e:
            error = "Já existe uma subcategoria com esse nome!"
            print(f"ERROR: Erro ao criar nova subcategoria: {e}")
            
    subcategories = Subcategory.objects.filter(category=category)

    if request.headers.get("HX-Request"):
        html = render_to_string(
            "cards/partials/subcategories_list.html",
            {"subcategories": subcategories},
            request=request
        )
        return HttpResponse(html)

    return render(request, "cards/create_subcategory_or_cards.html", {
        "category": category,
        "error": error,
        "subcategories": subcategories,
    })


@login_required(login_url="/login/")
def show_cards_and_decks(request, username, category_slug, subcategory_slug):

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


@login_required(login_url="/login/")
def create_card(request, username, category_slug, subcategory_slug, deck_slug):

    user = User.objects.filter(username=username).first()
    if user is None:
        raise Http404()
    
    if request.user.username != username:
        raise PermissionDenied

    category = get_object_or_404(Category, user=request.user, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, category=category, slug=subcategory_slug)
    deck = get_object_or_404(Deck, subcategory=subcategory, slug=deck_slug)

    return render(request, "cards/create_card.html", {
        "category_slug": category.slug,
        "subcategory_slug": subcategory.slug,
        "deck_slug": deck.slug
    })


@login_required(login_url="/login/")
def view_card(request):
    return render(request, "cards/view_card.html")