from django.http import HttpRequest
from django.shortcuts import render
from django.template.response import TemplateResponse

from main.views.base_view import BaseView


class ApplicationView(BaseView):
    def index(self, request: HttpRequest):
        return render(request, 'templates/index.html', {'': ''})
        # return TemplateResponse(request, 'main/templates/index.html')

    def vendor(self, request: HttpRequest, **kwargs):
        demo = {'name': 'deepak malhotra'}
        return TemplateResponse(request, 'templates/vendor.html', {
            'name': demo
        })
