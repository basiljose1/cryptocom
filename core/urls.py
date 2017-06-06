from django.conf.urls import url
from core.api.views import TokenView 

urlpatterns = [
    url(r'^api/token/$', TokenView.as_view(), name='get_token_status'),
    ]