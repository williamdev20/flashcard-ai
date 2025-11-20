from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def make_login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("create_and_show_category", username=username)
        else:
            error = "Username ou senha inválidos!"

    return render(request, "login/login.html", {"error": error})
