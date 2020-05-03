from main.backend.client import ClientService
from main.backend.project import ProjectService
from main.backend.project_assignee import ProjectAssigneeService
from main.backend.vendor import VendorService


class Factory():
    def __init__(self):
        self.service_list = {
            'vendor': VendorService,
            'client': ClientService,
            'project': ProjectService,
            'project-assignee': ProjectAssigneeService
        }

    def get_service(self, service_name: str):
        return self.service_list.get(service_name, '')
