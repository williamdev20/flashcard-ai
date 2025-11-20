from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Category


@login_required(login_url="/login/")
def create_card(request):
    return render(request, "cards/create_card.html")


@login_required(login_url="/login/")
def create_and_show_category(request, username):
    error = ""

    if not User.objects.filter(username=username).exists():
        raise Http404()

    if request.method == "POST":
        category_name = request.POST.get('category_name')

        try:
            Category.objects.create(
                name=category_name
            )
        except IntegrityError as e:
            error = "Já existe uma categoria com esse nome!"
            print(f"ERROR: Erro ao tentar criar uma categoria: {e}")

    categories = Category.objects.all()

    return render(request, "cards/show_category.html", {
        "error": error,
        "categories": categories
    })


@login_required(login_url="/login/")
def create_subcategory_or_cards(request):
    return render(request, "cards/create_subcategory_or_cards.html")


@login_required(login_url="/login/")
def view_card(request):
    return render(request, "cards/view_card.html")