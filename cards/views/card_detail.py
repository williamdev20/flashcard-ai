from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from cards.models import Category, Subcategory, Deck



@login_required(login_url="/login/")
def card_detail(request):
    return render(request, "cards/view_card.html")