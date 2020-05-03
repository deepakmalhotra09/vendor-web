from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.backend.factory import Factory
from main.views.base_view import BaseView


class ProjectView(LoginRequiredMixin, BaseView):

    def index(self, request: HttpRequest):
        project_service = self.factory.get_service('project')
        projects = project_service.get_projects()
        return TemplateResponse(request, 'templates/project/project.html',
                                {'projects': projects})

    def add(self, request: HttpRequest):
        client_service = self.factory.get_service('client')
        clients = client_service.get_clients()
        return TemplateResponse(request, 'templates/project/add_project.html',
                                {'update_project': False, 'clients': clients})

    def assign(self, request: HttpRequest):
        vendor_service = self.factory.get_service('vendor')
        vendors = vendor_service.get_vendors()
        project_service = self.factory.get_service('project')
        projects = project_service.get_projects()
        return TemplateResponse(request, 'templates/project/assign_project.html',
                                {'projects': projects, 'vendors': vendors})

    def assignees(self, request: HttpRequest):
        project_service = self.factory.get_service('project-assignee')
        project_assignees = project_service.get_project_vendor_assignees()
        print(project_assignees)
        return TemplateResponse(request, 'templates/project/project_assignees.html',
                                {'project_assignees': project_assignees})


@login_required()
def edit_project(request: HttpRequest, project_id: int):
    factory = Factory()
    project_service = factory.get_service('project')
    project = project_service.get_project(project_id)

    client_service = factory.get_service('client')
    clients = client_service.get_clients()

    return TemplateResponse(request, 'templates/project/add_project.html',
                            {'project': project, 'clients': clients, 'update_project': True})

