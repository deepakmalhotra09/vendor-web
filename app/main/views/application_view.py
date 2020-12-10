from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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


def forgot_password(request: HttpRequest):
    wrong_username = False
    if request.POST:
        user = None
        username = request.POST['username']
        if username:
            try:
                user = User.objects.get(username=username)
            except Exception:
                wrong_username = True
            if user is not None:
                if user.is_active:
                    return render(request, 'templates/reset-password.html',
                                  {'username': username})
            else:
                wrong_username = True
    return render(request, 'templates/forgot-password.html',
                  {'wrong_username': wrong_username})


def reset_password(request: HttpRequest):
    pass_len_short = False
    if request.POST:
        password = request.POST['password']
        conf_pass = request.POST['conf_password']
        username = request.POST['username']
        if username and password == conf_pass and password.__len__() >= 6:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/login')
        else:
            pass_len_short = True
    return render(request, 'templates/reset-password.html',
                  {'pass_len_short': pass_len_short})


@login_required(login_url='/login')
def change_password(request: HttpRequest):
    success = False
    error = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        new_password = request.POST['new_password']
        if new_password.__len__() < 6:
            error = True
        user = authenticate(username=username, password=password)
        if user is not None and not error:
            if user.is_authenticated:
                user.set_password(new_password)
                user.save()
                login(request, user)
                success = True
            else:
                error = True
        else:
            error = True
    return render(request, 'templates/change-password.html',
                  {'success': success, 'error': error})


def page_not_found(request: HttpRequest):
    return render(request, 'templates/404.html')