from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

from main.views.base_view import BaseView


class ApplicationView(LoginRequiredMixin, BaseView):
    def index(self, request: HttpRequest):
        project_service = self.factory.get_service('project')
        vendor_service = self.factory.get_service('vendor')
        client_service = self.factory.get_service('client')
        total_projects = project_service.get_total_project_count()
        total_vendors = vendor_service.get_total_vendor_count()
        total_clients = client_service.get_total_client_count()
        # return render(request, 'templates/index.html')
        return TemplateResponse(request, 'templates/index.html',
                      {'total_projects': total_projects, 'total_clients': total_clients,
                       'total_vendors': total_vendors})


def login_user(request: HttpRequest):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_authenticated:
                login(request, user)
                redirect_to = '/'
                if request.GET and request.GET['next']:
                    redirect_to = request.GET['next']
                return HttpResponseRedirect(redirect_to)
    return render(request, 'templates/login.html')


def logout_user(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect('/login')
