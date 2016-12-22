# from django.shortcuts import render, HttpResponse
# from cart.items import Items
# import json
#
#
# def add_item(request):
#     if request.method == 'POST':
#         item_id = request.POST.get('item_id', '')
#         item = Items(request)
#         alert = item.add_item(request, item_id)
#         return HttpResponse(json.dumps({'alert': alert}), content_type="application/json")
#
#
# def cart(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'cart.html', context)
