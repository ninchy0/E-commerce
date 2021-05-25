from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from home.models import *
from .models import Cart, Contact
from home.views import BaseView
from django.contrib.auth.decorators import login_required

# --------------Cart-------------------
@login_required
def add_to_cart(request, slug):
    username = request.user.username
    price = Item.objects.get(slug=slug).price

    discounted_price = Item.objects.get(slug=slug).discounted_price

    if discounted_price > 0:
        original_price = discounted_price
    else:
        original_price = price

    if Cart.objects.filter(username=username, slug=slug, checkout=False).exists():
        quantity = Cart.objects.get(username=username, slug=slug, checkout=False).quantity
        quantity = quantity + 1
        total = original_price*quantity
        Cart.objects.filter(username=username, slug=slug, checkout=False).update(quantity=quantity, total=total)
        return redirect('cart:my_cart')
    else:
        quantity = 1

    total = original_price * quantity

    data = Cart.objects.create(
        username=username,
        items=Item.objects.filter(slug=slug)[0],
        slug=slug,
        quantity=quantity,
        total=total
    )
    data.save()
    return redirect('cart:my_cart')


class CartView(BaseView):
    def get(self, request):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username=username, checkout=False,)
        return render(request, 'cart.html', self.views)


def delete_cart(request, slug):
    username = request.user.username
    Cart.objects.filter(username=username, checkout=False, slug=slug).delete()
    return redirect('cart:my_cart')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        email = EmailMessage(
            f'Hello {name}\n{email}',
            f'subject:{subject}\n{message}',
            'from@example.com',
            ['to1@example.com'],
        )
        email.send()

    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')