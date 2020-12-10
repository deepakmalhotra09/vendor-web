from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.template.response import TemplateResponse

from main.backend.factory import Factory
from main.constants import countries
from main.views.base_view import BaseView


class VendorsView(LoginRequiredMixin, BaseView):
    def index(self, request: HttpRequest):
        factory = Factory()
        vendor_service = factory.get_service('vendor')
        vendors = vendor_service.get_vendors()
        # return render(request, 'templates/vendor/vendor.html', {'vendors_list': vendor})
        return TemplateResponse(request, 'templates/vendor/vendor.html',
                                {'vendors_list': vendors})

    def add(self, request: HttpRequest):
        return TemplateResponse(request, 'templates/vendor/add_vendor.html',
                                {'country_list': countries, 'update_vendor': False})


@login_required()
def edit_vendor(request: HttpRequest, vendor_id: int):
    factory = Factory()
    vendor_service = factory.get_service('vendor')
    vendor = vendor_service.get_vendor(vendor_id)
    return TemplateResponse(request, 'templates/vendor/add_vendor.html',
                            {'vendor': vendor, 'country_list': countries, 'update_vendor': True})
