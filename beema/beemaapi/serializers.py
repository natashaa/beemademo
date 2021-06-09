from django.conf import settings
from rest_framework import serializers

from .models import Customer, Policy


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    dob = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    policies = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob', 'email', 'gender', 'policies')


class PolicySerializer(serializers.HyperlinkedModelSerializer):

    customer_id = serializers.PrimaryKeyRelatedField(source='customer', queryset=Customer.objects.all())
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Policy
        fields = ('id', 'name', 'type', 'premium', 'cover', 'customer_id', 'customer', 'state', 'created_at',
                  'accepted_at', 'paid_at')
