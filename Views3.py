def add_car(request):
    if request.method == "POST":
        car_name = request.POST['car_name']
        city = request.POST['city']
        image = request.FILES['image']
        capacity = request.POST['capacity']
        rent = request.POST['rent']
        car_dealer = CarDealer.objects.get(car_dealer=request.user)
        try:
            location = Location.objects.get(city=city)
        except:
            location = None
        if location is not None:
            car = Car(name=car_name, car_dealer=car_dealer, location=location, capacity=capacity, image=image, rent=rent)
        else:
            location = Location(city=city)
            car = Car(name=car_name, car_dealer=car_dealer, location=location, capacity=capacity, image=image, rent=rent)
        car.save()
        alert = True
        return render(request, "add_car.html", {'alert':alert})
    return render(request, "add_car.html")
