from rest_framework import serializers
from maintenance.models import MaintRequest

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for maintenance request model for api
    """
    class Meta:
        model = MaintRequest
        fields = ('id', 
                  'property_ref', 
                  'author', 
                  'title', 
                  'details', 
                  'priority', 
                  'status',
                  'date_raised',
                  'cost',
                  'paid_by',
                  'invoice_pdf')