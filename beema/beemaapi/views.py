from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CustomerSerializer, PolicySerializer
from .models import Customer, Policy


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all().order_by('first_name')
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    filter_fields = ['dob', 'first_name', 'last_name']


class QuoteViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    @action(detail=True, url_path='accept', methods=['put'])
    def accept(self, request, pk=None, *args, **kwargs):
        quote = self.get_object()
        quote.state='quoted'
        quote.save()
        return Response({'quote_id': pk, 'state': 'accepted'})

    @action(detail=True, url_path='pay', methods=['put'])
    def pay(self, request, pk=None, *args, **kwargs):
        quote = self.get_object()
        quote.state = 'bound'
        quote.save()
        return Response({'quote_id': pk, 'state': 'paid'})


class PolicyViewSet(QuoteViewSet):
    queryset = Policy.objects.filter(state='bound')

    filter_fields = ['customer_id']













