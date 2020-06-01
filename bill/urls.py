from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',views.BillDetail.as_view()),
    url(r'^create/$',views.BillCreate.as_view()),
    url(r'ordercreate/$',views.OrderCreate.as_view()),
]

format_suffix_patterns = format_suffix_patterns(urlpatterns)
