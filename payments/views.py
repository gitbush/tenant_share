from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import PaymentForm
from .models import Payment


def payments_list(request):
    """
    List all payment history of the current user.
    Add new payment to list
    """
    payment_list = Payment.objects.filter(user=request.user).order_by('-payment_date')
    paginator = Paginator(payment_list, 2)
    page = request.GET.get('page')
    payments = paginator.get_page(page)

    if request.method == 'POST':
        payment_form = PaymentForm(request.user.profile.rental, request.POST, request.user)
        if payment_form.is_valid():
            new_payment = payment_form.save(commit=False)
            new_payment.user = request.user
            new_payment.save()
            messages.add_message(request, messages.INFO, f'New pending payment added')
            return redirect('payments-list')
    else:
        payment_form = PaymentForm(request.user.profile.rental, initial = {'maint_request': 'Please select'})

    context = {
        'payment_form': payment_form,
        'payments': payments
    }
    return render(request, 'payments/payments_list.html', context)
