from main.backend.vendor import VendorService


class Factory():
    def __init__(self):
        self.service_list = {
            'vendor': VendorService
        }

    def get_service(self, service_name: str):
        return self.service_list.get(service_name, '')
