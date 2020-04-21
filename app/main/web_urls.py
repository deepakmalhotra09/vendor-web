
from django.conf.urls import url

from main.views.application_view import ApplicationView
from main.views.vendors_view import VendorsView

application_view = ApplicationView.as_view()
vendors_view = VendorsView.as_view()

urlpatterns = [
    url(r'^vendors($|/)', vendors_view),
    url(r'^', application_view)
]