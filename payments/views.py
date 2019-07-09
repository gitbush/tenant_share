from django.shortcuts import render, redirect, reverse
from .forms import PaymentForm
from .models import Payment


def payments_list(request):
    """
    List all payment history of the current user.
    Add new payment to list
    """
    payment_list = Payment.objects.filter(user=request.user).order_by('-payment_date')
    
    if request.method == 'POST':
        payment_form = PaymentForm(request.user.profile.rental, request.POST, request.user)
        if payment_form.is_valid():
            new_payment = payment_form.save(commit=False)
            new_payment.user = request.user
            new_payment.save()
            return redirect('payments-list')
    else:
        payment_form = PaymentForm(request.user.profile.rental)

    context = {
        'payment_form': payment_form,
        'payment_list': payment_list
    }
    return render(request, 'payments/payments_list.html', context)
