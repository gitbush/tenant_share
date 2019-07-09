from django.shortcuts import render
from .forms import PaymentForm


def payments_list(request):

    payment_form = PaymentForm()

    context = {
        'payment_form': payment_form
    }
    return render(request, 'payments/payments_list.html', context)
