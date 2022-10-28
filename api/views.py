
# Create your views here.
from api.serializer import AccountSerializer, CardSerializer, CurrencySerializer, LoanSerializer, NotificationsSerializer, ReceiptSerializer, RewardSerializer, ThirdPartySerializer, TransactionSerializer, UserSerializer, WalletSerializer
from rest_framework import viewsets
from wallet.models import User


class UserViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WalletViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = WalletSerializer

class CardViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = CardSerializer

class AccountViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

class CurrencyViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrencySerializer

class TransactionsViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = TransactionSerializer

class RewardViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = RewardSerializer

class NotificationsViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = NotificationsSerializer

class LoanViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = LoanSerializer

class ThirdPartyViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = ThirdPartySerializer

class ReceiptViewSet(viewsets.modelViewSet):
    queryset = User.objects.all()
    serializer_class = ReceiptSerializer