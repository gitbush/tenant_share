from django.shortcuts import render, redirect, reverse
from .forms import PaymentForm


def payments_list(request):
    """
    List all payment history of the current user.
    Add new payment to list
    """
    
    if request.method == 'POST':
        payment_form = PaymentForm(request.user.profile.rental, request.POST, request.user)
        if payment_form.is_valid():
            new_payment = payment_form.save(commit=False)
            new_payment.user = request.user
            new_payment.is_paid = True
            new_payment.save()
            return redirect('payments-list')
    else:
        payment_form = PaymentForm(request.user.profile.rental)

    context = {
        'payment_form': payment_form
    }
    return render(request, 'payments/payments_list.html', context)
