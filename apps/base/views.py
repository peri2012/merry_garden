from django.shortcuts import render

from apps.base.models import ToBook

# Create your views here.

def index(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        to_book = ToBook.objects.create(fullname=fullname, phone=phone, date=date, adults_quantity=adults_quantity, childs_quantity=childs_quantity)
    return render(request, 'index.html', locals())