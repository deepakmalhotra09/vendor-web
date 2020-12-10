from app.models import Client


class ClientService(object):
    def __init__(self):
        self.Client = Client

    @staticmethod
    def add_update_client(client: Client):
        client.save()

    @staticmethod
    def get_clients():
        client_obj = Client.objects.all()
        return client_obj

    @staticmethod
    def get_total_client_count():
        client_obj = Client.objects.all().count()
        return client_obj

    @staticmethod
    def delete_client(client_id: int) -> None:
        Client.objects.filter(id=client_id).delete()
        return None

    @staticmethod
    def get_client(id: int):
        client = Client.objects.get(id=id)
        if client:
            return client
        return Client()

    @staticmethod
    def get_client_by_name(client_name: str):
        client = Client.objects.get(name=client_name)
        if client:
            return client
        return Client()
