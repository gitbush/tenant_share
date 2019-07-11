from django.shortcuts import render, get_object_or_404
from payments.models import Payment

def checkout(request, payment_id):
    """
    Handle each users payment of maintenance request
    """
    payment = get_object_or_404(Payment, id=payment_id)

    context = {
        'payment': payment
    }
    return render(request, 'checkout/checkout.html', context)
