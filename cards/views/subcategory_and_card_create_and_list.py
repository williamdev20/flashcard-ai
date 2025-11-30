from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from cards.models import Category, Subcategory, Deck


@login_required(login_url="/login/")
def subcategory_and_card_create_and_list(request, username: str, category_slug: str):
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