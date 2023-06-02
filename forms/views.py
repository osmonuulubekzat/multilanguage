from django.contrib import messages
from django.shortcuts import render
from .forms import *


# Create your views here.
def Index(request):
    if request.method == "POST":
        forms = Forms(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'data is successfully recorded')
    return render(request, "index.html")


def Display(request):
    data = Bloggers.objects.all()
    context = {"context": data}
    return render(request, "display.html", context)
