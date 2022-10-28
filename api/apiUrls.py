from django.urls import URLPattern, path, include
from rest_framework import routers
from wallet.models import Account
from .views import AccountBuyAirtimeView, AccountDepositView, AccountRepayLoanView, AccountRequestLoanView, AccountTransferView, AccountViewSet, AccountWithdrawView, CardViewSet, LoanViewSet, NotificationsViewSet, ReceiptViewSet, RewardViewSet, ThirdPartyViewSet, TransactionsViewSet, UserViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"wallet", WalletViewSet)
router.register(r"account", AccountViewSet)
router.register(r"transaction", TransactionsViewSet)
router.register(r"notification", NotificationsViewSet)
router.register(r"receipt", ReceiptViewSet)
router.register(r"loan", LoanViewSet)
router.register(r"reward", RewardViewSet)
router.register(r"card", CardViewSet)
router.register(r"thirdparty", ThirdPartyViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("transfer/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("transfer/", AccountRequestLoanView.as_view(), name="requestloan-view"),
    path("transfer/", AccountRepayLoanView.as_view(), name="repayloan-view"),
    path("transfer/", AccountBuyAirtimeView.as_view(), name="buyairtime-view"),
    
] 