from rest_framework import serializers

from maintenance.models import MaintRequest

class MaintenanceRequestSerializer(serializers.ModelSerializer):
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