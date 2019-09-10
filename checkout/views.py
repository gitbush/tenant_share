from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from payments.models import Payment
from .forms import MakePaymentForm
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request, payment_id):
    """
    Handle each users payment of maintenance request
    """
    payment_to_pay = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            # stripe processing
            try:
                customer = stripe.Charge.create(
                    amount = int(payment_to_pay.amount * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    payment_to_pay.is_paid = True
                    payment_to_pay.payment_token = payment_form.cleaned_data['stripe_id']
                    payment_to_pay.save()
                    messages.success(request,  'Payment made successfully ')
                    return redirect(reverse('payments-list'))
                else:
                    messages.error(request, 'Unable to take payment')
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined!')
        else:
            print(payment_form.errors)
            messages.error(request, 'Card details are incorrect')

    else:
        payment_form = MakePaymentForm()

    context = {
        'payment_to_pay': payment_to_pay,
        'payment_form': payment_form,
        'publishable' : settings.STRIPE_PUBLISHABLE,
    }
    return render(request, 'checkout/checkout.html', context)
