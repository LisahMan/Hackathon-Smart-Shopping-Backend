from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<bar_id>[0-9]+)/$',views.ProductDetail.as_view()),
    url(r'^order/(?P<rf_id>[0-9]+)/$',views.OrderProduct.as_view()),
    url(r'^search/$',views.SearchProduct.as_view()),
]

format_suffix_patterns = format_suffix_patterns(urlpatterns)
