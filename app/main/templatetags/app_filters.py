from django import template

from main.backend.factory import Factory

register = template.Library()


@register.filter(name='get_key')
def get_key(data, key) -> str:
    if data:
        load_json = eval(data)
        return load_json[key]
    return ''


@register.filter(name='get_client_name')
def get_client_name(client_id: int) -> str:
    factory = Factory()
    client_service = factory.get_service('client')
    client = client_service.get_client(client_id)
    return client.name
