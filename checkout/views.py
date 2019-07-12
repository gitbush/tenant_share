from django.shortcuts import render, get_object_or_404
from payments.models import Payment
from .forms import MakePaymentForm

def checkout(request, payment_id):
    """
    Handle each users payment of maintenance request
    """
    payment_to_pay = get_object_or_404(Payment, id=payment_id)
    payment_form = MakePaymentForm()

    context = {
        'payment_to_pay': payment_to_pay,
        'payment_form': payment_form
    }
    return render(request, 'checkout/checkout.html', context)
