def edit_car(request, myid):
    car = Car.objects.filter(id=myid)[0]
    if request.method == "POST":
        car_name = request.POST['car_name']
        city = request.POST['city']
        capacity = request.POST['capacity']
        rent = request.POST['rent']
 
        car.name = car_name
        car.city = city
        car.capacity = capacity
        car.rent = rent
        car.save()
 
        try:
            image = request.FILES['image']
            car.image = image
            car.save()
        except:
            pass
        alert = True
        return render(request, "edit_car.html", {'alert':alert})
    return render(request, "edit_car.html", {'car':car})
