import datetime

from django.db.models import Q

import django_filters.rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CustomerSerializer, PolicySerializer
from .models import Customer, Policy


class CustomerFilter(filters.FilterSet):

    full_name = filters.CharFilter(method='search_by_full_name')

    def search_by_full_name(self, qs, name, value):
        for term in value.split():
            qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
        return qs

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'full_name', 'dob']


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all().order_by('first_name')
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)
    filterset_class = CustomerFilter


class QuoteViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    @action(detail=True, url_path='accept', methods=['put'])
    def accept(self, request, pk=None, *args, **kwargs):
        """ PUT method to pay for the quote, updates state to quoted and accepted_at timestamp """
        quote = self.get_object()
        quote.state='quoted'
        quote.accepted_at = datetime.datetime.now()
        quote.save()
        return Response({'quote_id': pk, 'state': 'accepted'})

    @action(detail=True, url_path='pay', methods=['put'])
    def pay(self, request, pk=None, *args, **kwargs):
        """ PUT method to pay for the quote, updates state to bound and paid_at timestamp """
        quote = self.get_object()
        quote.state = 'bound'
        quote.paid_at = datetime.datetime.now()
        quote.save()
        return Response({'quote_id': pk, 'state': 'paid'})


class PolicyViewSet(QuoteViewSet):
    queryset = Policy.objects.filter(state='bound')

    filter_fields = ['customer_id']

    @action(detail=True, url_path='history', methods=['get'])
    def history(self, request, pk=None, *args, **kwargs):
        """ Displays history of policy object based on created, accepted and paid on dates """
        quote = self.get_object()
        serializer = self.get_serializer(quote)
        history_dict = {'history': {'created_on': quote.created_at,
                                    'accepted_on': quote.accepted_at,
                                    'paid_on': quote.paid_at
                        }}
        response_dict = {**serializer.data, **history_dict}
        return Response(response_dict)













