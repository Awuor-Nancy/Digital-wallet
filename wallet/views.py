from django.shortcuts import render
from .forms import UserRegistrationForm, WalletRegistrationForm,CardRegistrationForm,AccountRegistrationForm,CurrencyRegistrationForm,TransactionRegistrationForm,LoanRegistrationForm,ReceiptRegistrationForm,NotificationsRegistrationForm,ThirdpartyRegistrationForm


# Create your views here.
def registerUser(request):
    form = UserRegistrationForm()
    return render(request, "wallet/register_customer.html", {'form': form})

def registerWallet(request):
    form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html", {'form': form})

def registerCard(request):
    form = CardRegistrationForm()
    return render(request, "wallet/register_card.html", {'form': form})

def registerAccount(request):
    form = AccountRegistrationForm()
    return render(request, "wallet/register_account.html", {'form': form})

def registerCurrency(request):
    form = CurrencyRegistrationForm()
    return render(request, "wallet/register_currency.html", {'form': form})

def registerTransaction(request):
    form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html", {'form': form})

def registerLoan(request):
    form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html", {'form': form})

def registerThirdparty(request):
    form = ThirdpartyRegistrationForm()
    return render(request, "wallet/register_thirdparty.html", {'form': form})

def registerReceipt(request):
    form = ReceiptRegistrationForm()
    return render(request, "wallet/register_receipt.html", {'form': form})

def registerNotification(request):
    form = NotificationsRegistrationForm()
    return render(request, "wallet/register_notification.html", {'form': form})

     

