from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Magazine, Purchase


# Create your views here.
@login_required(login_url='/login/')
def all_magazines(request):
    magazines = Magazine.objects.all()
    purchases = Purchase.objects.all()
    args = {"magazines": magazines, "purchases": purchases}
    return render(request, "magazines/magazines.html", args)
