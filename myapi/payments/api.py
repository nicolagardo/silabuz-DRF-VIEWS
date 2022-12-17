from rest_framework import viewsets, permissions
from rest_framework import mixins  
from .models import Payments
from .serializers import PaymentSerializer

class PaymentSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset= Payments.objects.get_queryset().order_by('id')
    serializer_class= PaymentSerializer
    pagination_class= 0
    filter_backends= 0
    permission_classes= [permissions.AllowAny]

    ser_fields = ['user_id', 'date_payment', 'service']
    throttle_classes = 0