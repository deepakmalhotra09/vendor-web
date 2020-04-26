import json

from django.http import JsonResponse, HttpRequest

from app.models import Vendor
from main.backend.factory import Factory
from main.constants import countries
from main.core import get_request_param_json, get_request_param
from main.views.base_view import BaseView


class AjaxView(BaseView):
    def __init__(self):
        super(AjaxView, self).__init__()

    def index(self, request: HttpRequest):
        pass

    @staticmethod
    def get_countries(self) -> json:
        return JsonResponse(countries, safe=False)

    def add_vendor(self, request: HttpRequest) -> json:
        data = get_request_param_json('data', request)
        vendor = Vendor()
        vendor.name = data.get('vendor_name', '')
        vendor.mobile_no = data.get('vendor_mobile', '')
        vendor.email = data.get('vendor_email', '')
        vendor.property = {
            'address': data.get('vendor_address', ''),
            'country': data.get('vendor_country', ''),
            'country_code': data.get('vendor_country_code', ''),
            'zip_code': data.get('vendor_zip_code', ''),
            'company_email': data.get('vendor_c_email', ''),
            'company_website': data.get('vendor_c_w', '')
        }
        factory_class = Factory()
        vendor_service = factory_class.get_service('vendor')
        vendor_service.add_vendor(vendor)
        return JsonResponse(data, safe=False)

    def delete_vendor(self, request: HttpRequest) -> json:
        vendor_id = get_request_param('id', request)
        factory_class = Factory()
        vendor_service = factory_class.get_service('vendor')
        vendor_service.delete_vendor(vendor_id)
        return JsonResponse(vendor_id, safe=False)
