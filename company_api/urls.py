from django.conf.urls import url, include

from rest_framework import routers

from company_api import views

router = routers.DefaultRouter()
router.register(r'', views.CompanyView)

urlpatterns = [
    # '',
    # url(r'^$', views.index_view, name='index_view'),
    url(r'^', include(router.urls)),
]

