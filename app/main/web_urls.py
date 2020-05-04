from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from main.views.ajax_view import AjaxView
from main.views.api_view import api_vendor_view, api_client_view
from main.views.application_view import ApplicationView, login_user, logout_user, forgot_password, reset_password, \
    change_password
from main.views.client_view import ClientView, edit_client
from main.views.project_view import ProjectView, edit_project
from main.views.vendors_view import VendorsView, edit_vendor

application_view = ApplicationView.as_view()
vendor_view = VendorsView.as_view()
client_view = ClientView.as_view()
project_view = ProjectView.as_view()
ajax_view = AjaxView.as_view()

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('reset-password', reset_password, name='reset-password'),
    path('change-password', change_password, name='change-password'),
    url(r'^api/vendor($|/)', api_vendor_view),
    url(r'^api/client($|/)', api_client_view),
    path('vendor/edit/<int:vendor_id>', edit_vendor, name='edit_vendor'),
    path('client/edit/<int:client_id>', edit_client, name='edit_client'),
    path('project/edit/<int:project_id>', edit_project, name='edit_project'),
    url(r'^vendor($|/)', vendor_view),
    url(r'^client($|/)', client_view),
    url(r'^project($|/)', project_view),
    url(r'^ajax($|/)', csrf_exempt(ajax_view)),
    url(r'^', application_view)
]

# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
handler404 = 'main.views.application_view.page_not_found'
# handler500 = 'my_app.views.server_error'

