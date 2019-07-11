from django.shortcuts import render, get_object_or_404
from payments.models import Payment

def checkout(request, payment_id):
    """
    Handle each users payment of maintenance request
    """
    payment_to_pay = get_object_or_404(Payment, id=payment_id)

    context = {
        'payment_to_pay': payment_to_pay
    }
    return render(request, 'checkout/checkout.html', context)
