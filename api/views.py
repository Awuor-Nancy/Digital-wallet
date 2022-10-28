
# Create your views here.
from api.serializer import AccountSerializer, CardSerializer, CurrencySerializer, LoanSerializer, NotificationsSerializer, ReceiptSerializer, RewardSerializer, ThirdPartySerializer, TransactionSerializer, UserSerializer, WalletSerializer
from rest_framework import viewsets, views
from wallet.models import Account, User
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


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



class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)


class AccountWithdrawView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)


class AccountTransferView(views.APIView):
   """
   This class allows transfer of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)


class AccountRequestLoanView(views.APIView):
   """
   This class allows Loan requests to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)


class AccountRepayLoanView(views.APIView):
   """
   This class allows loan repayment to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)


class AccountBuyAirtimeView(views.APIView):
   """
   This class allows airtime purchase an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)