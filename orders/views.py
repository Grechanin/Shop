from django.http import JsonResponse
from django.shortcuts import render
from .forms import CheckoutContactForm
from .models import *


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("product_qnt")
    nmb = int(nmb)
    is_delete = data.get("is_delete")
    print(is_delete)
    print(product_id)

    if is_delete == 'true':
        product = ProductInBasket.objects.get(product_id=product_id)
        print('HERE!!!!! %s' % product)
        product.is_active = False
        product.save(force_update=True)

    else:

        product_to_update, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={'nmb': nmb})
        if not created:
            product_to_update.nmb = nmb
            product_to_update.is_active = True
            product_to_update.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    total_product_qnt = products_in_basket.count()

    return_dict["total_product_qnt"] = total_product_qnt
    return_dict["products"] = list()

    for obj in products_in_basket:
        product_dict = dict()
        product_dict['id'] = obj.product.id
        product_dict['name'] = obj.product.name
        product_dict['price_pre_item'] = obj.price_pre_item
        product_dict['nmb'] = obj.nmb
        return_dict['products'].append(product_dict)
    # print(return_dict['products'])
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    # print(request.session.session_key)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('Form is valid!')
            data = request.POST
            name = data['client_name']
            phone = data['phone']
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name':name})
            order = Order.objects.create(user=user, name=name, phone=phone, status_id=1)
            for key, value in data.items():
                if key.startswith('product_nmb_in_basket_id_'):
                    product_in_basket_id = key.split('product_nmb_in_basket_id_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                                  price_pre_item=product_in_basket.price_pre_item, total_price=product_in_basket.total_price,
                                                  order=order)

        else:
            print("Form isn't valid!!!")
    return render(request, 'orders/checkout.html', locals())