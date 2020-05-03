from main.backend.client import ClientService
from main.backend.project import ProjectService
from main.backend.project_assignee import ProjectAssigneeService
from main.backend.project_vendor_user_assignee import ProjectVendorUserAssigneeService
from main.backend.vendor import VendorService


class Factory():
    def __init__(self):
        self.service_list = {
            'vendor': VendorService,
            'client': ClientService,
            'project': ProjectService,
            'project-assignee': ProjectAssigneeService,
            'project-vendor-user-assignee': ProjectVendorUserAssigneeService
        }

    def get_service(self, service_name: str):
        service = self.service_list.get(service_name, '')
        return service
