import json

from django.http import JsonResponse, HttpRequest

from app.models import Vendor, Client
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
        vendor_id = int(data.get('vendor_id', ''))
        factory_class = Factory()
        vendor_service = factory_class.get_service('vendor')
        vendor = Vendor()
        if vendor_id:
            vendor = vendor_service.get_vendor(vendor_id)
        vendor.name = data.get('vendor_name', '')
        vendor.mobile_no = data.get('vendor_mobile', '')
        vendor.email = data.get('vendor_email', '')
        vendor.property = {
            'address': data.get('vendor_address', ''),
            'country': data.get('vendor_country', ''),
            'country_code': data.get('vendor_country_code', ''),
            'zip_code': data.get('vendor_zip_code', ''),
            'company_email': data.get('vendor_c_email', ''),
            'company_website': data.get('vendor_c_w', ''),
            'company_name': data.get('vendor_c_n', ''),
        }
        vendor_service.add_update_vendor(vendor)
        return JsonResponse(data, safe=False)

    def delete_vendor(self, request: HttpRequest) -> json:
        vendor_id = get_request_param('id', request)
        factory_class = Factory()
        vendor_service = factory_class.get_service('vendor')
        vendor_service.delete_vendor(vendor_id)
        return JsonResponse(vendor_id, safe=False)

    def add_client(self, request: HttpRequest) -> json:
        data = get_request_param_json('data', request)
        client_id = int(data.get('client_id', ''))
        factory_class = Factory()
        client_service = factory_class.get_service('client')
        client = Client()
        if client_id:
            client = client_service.get_client(client_id)
        client.name = data.get('client_name', '')
        client.mobile_no = data.get('client_mobile', '')
        client.email = data.get('client_email', '')
        client.property = {
            'address': data.get('client_address', ''),
            'country': data.get('client_country', ''),
            'country_code': data.get('client_country_code', ''),
            'zip_code': data.get('client_zip_code', ''),
            'company_email': data.get('client_c_email', ''),
            'company_website': data.get('client_c_w', ''),
            'company_name': data.get('client_c_n', ''),
        }
        client_service.add_update_client(client)
        return JsonResponse(data, safe=False)

    def delete_client(self, request: HttpRequest) -> json:
        client_id = get_request_param('id', request)
        factory_class = Factory()
        client_service = factory_class.get_service('client')
        client_service.delete_client(client_id)
        return JsonResponse(client_id, safe=False)
