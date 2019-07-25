from django.shortcuts import render, get_object_or_404
from .models import ChatMessage
from maintenance.models import MaintRequest, Rental
    
def GetMessages(request, id):

    """
    Get all messages related to current maintenance request.
    """
    maint_request = get_object_or_404(MaintRequest, id=id)
    messages = ChatMessage.objects.filter(maint_request=maint_request)

    context = {
        'messages': messages,
    }

    return render(request, 'maintenance/request_messages.html', context)

