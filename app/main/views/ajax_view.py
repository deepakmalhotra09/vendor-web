import json

from django.http import JsonResponse, HttpRequest

from app.models import Vendor, Client, Project, ProjectVendorAssign
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
            'company_name': data.get('client_c_n', ''),
            'company_website': data.get('client_c_w', ''),
        }
        client_service.add_update_client(client)
        return JsonResponse(data, safe=False)

    def delete_client(self, request: HttpRequest) -> json:
        client_id = get_request_param('id', request)
        factory_class = Factory()
        client_service = factory_class.get_service('client')
        client_service.delete_client(client_id)
        return JsonResponse(client_id, safe=False)

    def add_project(self, request: HttpRequest):
        data = get_request_param_json('data', request)
        project_id = int(data.get('id', ''))
        factory_class = Factory()
        project_service = factory_class.get_service('project')
        project = Project()
        if project_id:
            project = project_service.get_project(project_id)
        project.name = data.get('project_name', '')
        project.project_id = data.get('project_id', '')
        project.client_id = data.get('project_client_id', '')
        project.link = data.get('project_link', '')
        project.target = data.get('project_target', '')
        project.cost = data.get('project_cost', '')
        project.start_date = data.get('project_start_date', '')
        project.end_date = data.get('project_end_date', '')
        project_service.add_update_project(project)
        return JsonResponse(data, safe=False)

    def delete_project(self, request: HttpRequest) -> json:
        project_id = get_request_param('id', request)
        factory_class = Factory()
        project_service = factory_class.get_service('project')
        project_service.delete_project(project_id)
        return JsonResponse(project_id, safe=False)

    def add_assignee(self, request: HttpRequest):
        data = get_request_param_json('data', request)
        project_vendor_assignee_id = int(data.get('id', ''))
        factory_class = Factory()
        project_vendor_assignee_service = factory_class.get_service('project-assignee')
        project_service = factory_class.get_service('project')
        project_vendor_assignee = ProjectVendorAssign()
        if project_vendor_assignee_id:
            project_vendor_assignee = project_vendor_assignee_service.get_project_vendor_assignee(
                project_vendor_assignee_id)
        project_id = data.get('project_id', '')
        project = project_service.get_project(project_id)
        client_project_id = project.project_id
        links = {
            'completed': data.get('project_completed_link', ''),
            'quota_full': data.get('project_quota_full_link', ''),
            'terminated': data.get('project_terminated_link', '')
        }
        project_vendor_assignee.project_id = project_id
        project_vendor_assignee.client_project_id = client_project_id
        project_vendor_assignee.vendor_id = data.get('vendor_id', '')
        project_vendor_assignee.cost = data.get('cost', '')
        project_vendor_assignee.links = links
        project_vendor_assignee_service.add_update_project_vendor_assignee(project_vendor_assignee)
        return JsonResponse(data, safe=False)
