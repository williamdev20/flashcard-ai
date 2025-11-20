from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError

def register(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            User.objects.create_user(
                username=username,
                password=password
            )

            return redirect("make_login")
        
        except IntegrityError as e:
            error = "Esta conta já existe!"
            print(f"Erro ao tentar cadastrar: {e}")

    return render(request, "register/register.html", {"error": error})
