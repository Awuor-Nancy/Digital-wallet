from django.urls import path
from .views import registerAccount, registerCard, registerCurrency, registerLoan, registerNotification, registerReceipt, registerThirdparty, registerTransaction, registerUser, registerWallet


urlpatterns = [
    path("", registerUser, name = "register"),
     path("wallet/", registerWallet, name = "wallet"),
      path("card/", registerCard, name = "card"),
       path("account/", registerAccount, name = "account"),
        path("currency/", registerCurrency, name = "currency"),
         path("transaction/", registerTransaction, name = "transaction"),
          path("thirdparty/", registerThirdparty, name = "thirdparty"),
           path("receipt/", registerReceipt, name = "receipt"),
            path("notification/", registerNotification, name = "notification"),
             path("loan/", registerLoan, name = "loan"),

]