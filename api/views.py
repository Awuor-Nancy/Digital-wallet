
# Create your views here.
from rest_framework import viewsets
from wallet.models import User
from .serializers import UserSerializer

class CustomerViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
