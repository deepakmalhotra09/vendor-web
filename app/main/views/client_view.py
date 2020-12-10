from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.backend.factory import Factory
from main.constants import countries
from main.views.base_view import BaseView


class ClientView(LoginRequiredMixin, BaseView):
    def index(self, request: HttpRequest):
        factory = Factory()
        client_service = factory.get_service('client')
        clients = client_service.get_clients()
        return TemplateResponse(request, 'templates/client/client.html',
                                {'client_list': clients})

    def add(self, request: HttpRequest):
        return TemplateResponse(request, 'templates/client/add_client.html',
                                {'country_list': countries, 'update_client': False})


@login_required()
def edit_client(request: HttpRequest, client_id: int):
    factory = Factory()
    client_service = factory.get_service('client')
    client = client_service.get_client(client_id)
    return TemplateResponse(request, 'templates/client/add_client.html',
                            {'client': client, 'country_list': countries, 'update_client': True})
