def past_orders(request):
    all_orders = []
    user = User.objects.get(username=request.user)
    try:
        orders = Order.objects.filter(user=user)
    except:
        orders = None
    if orders is not None:
        for order in orders:
            if order.is_complete == False:
                order_dictionary = {'id':order.id, 'rent':order.rent, 'car':order.car, 'days':order.days, 'car_dealer':order.car_dealer}
                all_orders.append(order_dictionary)
    return render(request, "past_orders.html", {'all_orders':all_orders})
