def earnings(request):
    username = request.user
    user = User.objects.get(username=username)
    car_dealer = CarDealer.objects.get(car_dealer=user)
    orders = Order.objects.filter(car_dealer=car_dealer)
    all_orders = []
    for order in orders:
        all_orders.append(order)
    return render(request, "earnings.html", {'amount':car_dealer.earnings, 'all_orders':all_orders})
