from django.urls import path
from . import views
# from .views import listAccount, listCard, listCurrency, listLoan, listNotification, listReceipt, listReward, listThirdparty, listTransaction, listWallet, register_User, registerAccount, registerCard, registerCurrency, registerLoan, registerNotification, registerReceipt, registerReward, registerThirdparty, registerTransaction, registerWallet,listUser


urlpatterns = [
    path("",views.register_User, name = "register"),
     path("wallet/",views.registerWallet, name = "wallet"),
      path("card/",views.registerCard, name = "card"),
       path("account/",views.registerAccount, name = "account"),
        path("currency/",views.registerCurrency, name = "currency"),
         path("transaction/",views.registerTransaction, name = "transaction"),
          path("thirdparty/",views.registerThirdparty, name = "thirdparty"),
           path("receipt/",views.registerReceipt, name = "receipt"),
            path("notification/",views.registerNotification, name = "notification"),
             path("loan/",views.registerLoan, name = "loan"),
               path("reward/",views.registerReward, name = "rewards"),

             path("user/",views.listUser, name = "user_list"),

              path("loans/",views.listLoan, name = "loan_list"),
               path("accounts/",views.listAccount, name = "account_list"),
                path("rewards/",views.listReward, name = "reward_list"),
                 path("receipts/",views.listReceipt, name = "receipt_list"),
                  path("cards/",views.listCard, name = "card_list"),
                   path("transactions/",views.listTransaction, name = "transaction_list"),
                    path("wallets/",views.listWallet, name = "wallet_list"),
                     path("thirdpartys/",views.listThirdparty, name = "thirdParty_list"),
                       path("currencys/",views.listCurrency, name = "currency_list"),
                         path("notifications/",views.listNotification, name = "notification_list"),
                        
                     
]