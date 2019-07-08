from django.shortcuts import render


def payments(request):

    return render(request, 'payments/payments_list.html')
