from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from main.views.ajax_view import AjaxView
from main.views.application_view import ApplicationView
from main.views.vendors_view import VendorView

application_view = ApplicationView.as_view()
vendor_view = VendorView.as_view()
ajax_view = AjaxView.as_view()

urlpatterns = [
    url(r'^vendor($|/)', vendor_view),
    url(r'^ajax($|/)', csrf_exempt(ajax_view)),
    url(r'^', application_view)
]
