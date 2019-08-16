from django.shortcuts import render


def error_404_view(request, exception):
    """
    Page does not exist error
    """
    return render(request,'errors/404.html', context)

def error_500_view(request):
    """
    Server error 
    """
    return render(request,'errors/500.html', context)