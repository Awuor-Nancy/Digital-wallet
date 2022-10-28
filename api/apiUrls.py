from django.urls import URLPattern, path, include
from rest_framework import routers
from .views import AccountViewSet, CardViewSet, LoanViewSet, NotificationsViewSet, ReceiptViewSet, RewardViewSet, ThirdPartyViewSet, TransactionsViewSet, UserViewSet, WalletViewSet

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
    path("", include(router.urls))
] 