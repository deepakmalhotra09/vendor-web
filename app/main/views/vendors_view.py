from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.views.base_view import BaseView


class VendorsView(BaseView):
    def index(self, request: HttpRequest):
        return TemplateResponse(request, 'templates/vendor.html')

    def add(self, request: HttpRequest):
        return TemplateResponse(request, 'templates/3.html')
