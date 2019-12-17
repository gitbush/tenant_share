from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .models import *
from .forms import *
from.filters import MaintListFilter
from chat.models import ChatMessage
from chat.forms import MessageForm

@login_required
def Home(request):
    """
    If user has a rental assigned, show rental details and tenants. 
    Else show only user profile details
    """
    currentUser = request.user
    if currentUser.profile.rental: 
        userRental = currentUser.profile.rental
        userLandlord = userRental.landlord
        userTenants = userRental.profile_set.filter(register_as='Tenant').all()

        context = {
            'userProfile': currentUser.profile,
            'userRental': userRental, 
            'userLandlord': userLandlord,
            'userTenants': userTenants
        }
    else:
        context = {
            'userProfile': currentUser.profile,
        }
            
    return render(request, 'maintenance/home.html', context)

@login_required
def MaintRequestList(request):
    """
    Displays any/all maintenance requests associated with the current user rental.
    If no rental attached to user then show jumbotron with next steps text.
    """

    if request.user.profile.rental:
        user_rental = request.user.profile.rental
        maintenance_requests = user_rental.maintrequest_set.all()
        total = maintenance_requests.count()
        maint_filter = MaintListFilter(request.GET, queryset=maintenance_requests.order_by('-date_raised'))
        paginator = Paginator(maint_filter.qs, 5)
        page = request.GET.get('page')
        requests = paginator.get_page(page)

        context = {
            'maint_filter': maint_filter,
            'requests': requests,
            'total': total,
        }
        return render(request, 'maintenance/maint_requests.html', context)
    else:
        return render(request, 'maintenance/maint_requests.html')

@login_required
def MaintRequestCreate(request):
    """
    Create maintenance issue relevant to user and user rental
    """
    request_create_form = MaintenanceCreationForm()

    if request.method == 'POST':
        request_create_form = MaintenanceCreationForm(request.POST, request.FILES)
        if request_create_form.is_valid():
            new_request = request_create_form.save(commit=False)
            request_rental = request.user.profile.rental
            new_request.property_ref = request_rental
            new_request.author = request.user
            new_request.save()
            messages.success(request, 'New maintenance request created')
            return redirect('maint-detail', id=new_request.id)

    context = {
        'request_create_form': request_create_form,
    }
    return render(request, 'maintenance/maint_create.html', context )

@login_required
def MaintRequestDetail(request, id):
    """
    If user has current rental assigned to their profile.
    Display detail view of particular maintenance request.
    Allow for landlord to assign cost to tenant/landlord
    """
    maint_request = get_object_or_404(MaintRequest, id=id) 
    chat_messages = ChatMessage.objects.filter(maint_request=maint_request) # get chat messages

    if request.user.profile.rental == maint_request.property_ref:
        message_form = MessageForm()
        if request.method == 'POST':
            if 'cost' in request.POST:
                assign_cost_form = MaintenanceQuoteForm(request.POST, request.FILES, instance=maint_request)
                if assign_cost_form.is_valid():
                    assign_cost_form.save()
                    messages.success(request, 'Cost of work updated')
                    return redirect('maint-detail', id=id)
            
            elif 'status' in request.POST:
                status_form = StatusUpdateForm(request.POST, instance=maint_request)
                if status_form.is_valid():
                    status_form.save()
                    messages.success(request, 'Status of request updated')
                    return redirect('maint-detail', id=id)
                    
        assign_cost_form = MaintenanceQuoteForm(instance=maint_request)
        status_form = StatusUpdateForm(instance=maint_request)

        context = {
            'maint_request': maint_request,
            'chat_messages': chat_messages,
            'message_form': message_form,
            'assign_cost_form': assign_cost_form,
            'status_form': status_form,
        }

        return render(request, 'maintenance/maint_detail.html', context)
    else:
        raise PermissionDenied()

@login_required
def MaintRequestDelete(request, id):
    """
    Delete relevant maintenance request
    """

    current_request = get_object_or_404(MaintRequest, id=id)
    current_request.delete()
    messages.success(request, 'Maintenance request has been deleted')
    return redirect('maint-list')