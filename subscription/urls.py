from django.urls import path
from .views import SubscriptionView

urlpatterns = [
    path('/mail', SubscriptionView.as_view())
]