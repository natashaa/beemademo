from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .serializers import CustomerSerializer, PolicySerializer
from .models import Customer, Policy


class CustomerCreate(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)


# class QuoteCreate(generics.CreateAPIView):
#     queryset = Policy.objects.all()
#     serializer_class = PolicySerializer
#     permission_classes = (AllowAny,)


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

    def create(self, request, *args, **kwargs):
        if 'customer_id' in request.data:
            request.data['state'] = 'quoted'
        return super(QuoteViewSet, self).create(request, *args, **kwargs)


class PolicyViewSet(QuoteViewSet):
    queryset = Policy.objects.filter(state='bound')

    filter_fields = ['customer_id']













