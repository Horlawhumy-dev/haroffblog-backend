from django.urls import path
from .views import MessageView

urlpatterns = [
    path('/message', MessageView.as_view())
]