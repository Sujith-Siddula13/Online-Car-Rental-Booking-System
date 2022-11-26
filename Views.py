def index(request):
    cars = Car.objects.all()
    return render(request, "index.html", {'cars':cars})
