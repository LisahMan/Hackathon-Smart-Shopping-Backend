from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^create/',views.UserCreate.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.UserDelete.as_view()),
    url(r'login/',views.CheckUserDetail.as_view()),
]

format_suffix_patterns = format_suffix_patterns(urlpatterns)
