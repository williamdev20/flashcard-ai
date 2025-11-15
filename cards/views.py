from django.shortcuts import render

def create_card(request):
    return render(request, "cards/create_card.html")


def show_category(request):
    return render(request, "cards/show_category.html")
