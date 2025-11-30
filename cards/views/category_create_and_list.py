from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from cards.models import Category


@login_required(login_url="/login/")
def category_create_and_list(request, username):
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