from django.conf import settings
from rest_framework import serializers

from .models import Customer, Policy


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    dob = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    policies = serializers.CharField(source='policy', read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob', 'email', 'gender', 'policies')


class PolicySerializer(serializers.HyperlinkedModelSerializer):

    customer_id = serializers.CharField(source='customer.pk', read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Policy
        fields = ('id', 'type', 'premium', 'cover', 'customer_id', 'customer', 'state')
