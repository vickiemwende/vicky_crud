from django.shortcuts import render, redirect
from .models import Student


def displaydata(request):
    data = Student.objects.all()
    context = {"data": data}

    return render(request, "index.html", context)


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        query = Student(name=name, email=email, phone=phone)
        query.save()
        return redirect("/")
    return render(request, "index.html")


def insert(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')

        d = Student.objects.get(id=id)
        d.name = name
        d.email = email
        d.Phone = Phone
        d.save()
        return redirect("/")
    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
