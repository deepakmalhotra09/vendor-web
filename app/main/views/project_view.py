from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.backend.factory import Factory
from main.views.base_view import BaseView


class ProjectView(BaseView):
    def index(self, request: HttpRequest):
        factory = Factory()
        project_service = factory.get_service('project')
        projects = project_service.get_projects()
        return TemplateResponse(request, 'templates/project/project.html',
                                {'projects': projects})

    def add(self, request: HttpRequest):
        factory = Factory()
        client_service = factory.get_service('client')
        clients = client_service.get_clients()
        return TemplateResponse(request, 'templates/project/add_project.html',
                                {'update_project': False, 'clients': clients})


def edit_project(request: HttpRequest, project_id: int):
    factory = Factory()
    project_service = factory.get_service('project')
    project = project_service.get_project(project_id)

    client_service = factory.get_service('client')
    clients = client_service.get_clients()

    return TemplateResponse(request, 'templates/project/add_project.html',
                            {'project': project, 'clients': clients, 'update_project': True})
