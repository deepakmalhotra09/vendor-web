
from django.conf.urls import url

from main.views.application_view import ApplicationView

application_view = ApplicationView.as_view()

urlpatterns = [
    url(r'^', application_view)
]