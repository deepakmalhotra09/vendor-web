from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.backend.factory import Factory
from main.views.base_view import BaseView


class VendorView(BaseView):
    def index(self, request: HttpRequest):
        factory = Factory()
        vendor_service = factory.get_service('vendor')
        vendors = vendor_service.get_vendors()
        return TemplateResponse(request, 'templates/vendors/vendor.html',
                                {'vendors_list': vendors})

    def add(self, request: HttpRequest):
        return TemplateResponse(request, 'templates/vendors/add_vendor.html')
