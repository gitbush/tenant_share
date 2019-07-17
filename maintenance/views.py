from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *
from.filters import MaintListFilter
from chat.models import Thread, ChatMessage
from chat.forms import MessageForm


def Home(request):
    currentUser = request.user
    try: 
        userRental = currentUser.profile.rental
        userLandlord = userRental.landlord
        userTenants = userRental.profile_set.filter(register_as='Tenant').all()
        # print(userRental.profile_set.filter(register_as='Tenant').all())
        # print(currentRental.profile_set.filter(register_as='Tenant').all())

        context = {
            'userProfile': currentUser.profile,
            'userRental': userRental, 
            'userLandlord': userLandlord,
            'userTenants': userTenants
        }
    except:
        context = {
            'userProfile': currentUser.profile,
        }
            
    return render(request, 'maintenance/home.html', context)

def MaintRequestList(request):
    """
    Displays any/all maintenance requests associated with the current user rental.
    If no rental attached to user then show jumbotron with next steps text.
    """

    if request.user.profile.rental:
        user_rental = request.user.profile.rental
        maintenance_requests = user_rental.maintrequest_set.all()
        total = maintenance_requests.count()
        maint_filter = MaintListFilter(request.GET, queryset=maintenance_requests)
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
            Thread.objects.create(rental=request_rental, maint_request=new_request) # create a message thread on maint request create
            return redirect('maint-detail', id=new_request.id)

    context = {
        'request_create_form': request_create_form,
    }
    return render(request, 'maintenance/maint_create.html', context )

def MaintRequestDetail(request, id):
    """
    Display detail view of particular maintenance request.
    Allow for landlord to assign cost to tenant/landlord
    """
    maint_request = get_object_or_404(MaintRequest, id=id)
    # message_thread = get_object_or_404(Thread, maint_request=maint_request)

    message_form = MessageForm()
    if request.method == 'POST':
        if 'cost' in request.POST:
            assign_cost_form = MaintenanceQuoteForm(request.POST, request.FILES, instance=maint_request)
            if assign_cost_form.is_valid():
                assign_cost_form.save()
                return redirect('maint-detail', id=id)
            else:
                print(assign_cost_form.errors)
        
        elif 'status' in request.POST:
            status_form = StatusUpdateForm(request.POST, instance=maint_request)
            if status_form.is_valid():
                status_form.save()
                return redirect('maint-detail', id=id)
                
    assign_cost_form = MaintenanceQuoteForm(instance=maint_request)
    status_form = StatusUpdateForm(instance=maint_request)

    context = {
        'maint_request': maint_request,
        # 'message_thread': message_thread,
        'message_form': message_form,
        'assign_cost_form': assign_cost_form,
        'status_form': status_form,
    }

    return render(request, 'maintenance/maint_detail.html', context)