from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from main.views.ajax_view import AjaxView
from main.views.application_view import ApplicationView
from main.views.client_view import ClientView, edit_client
from main.views.vendors_view import VendorView, edit_vendor

application_view = ApplicationView.as_view()
vendor_view = VendorView.as_view()
client_view = ClientView.as_view()
ajax_view = AjaxView.as_view()

urlpatterns = [
    path('vendor/edit/<int:vendor_id>', edit_vendor, name='edit_vendor'),
    path('client/edit/<int:client_id>', edit_client, name='edit_client'),
    url(r'^vendor($|/)', vendor_view),
    url(r'^client($|/)', client_view),
    url(r'^ajax($|/)', csrf_exempt(ajax_view)),
    url(r'^', application_view)
]
