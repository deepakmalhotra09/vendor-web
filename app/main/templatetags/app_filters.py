from django import template

from app import settings
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


@register.filter(name='get_vendor_name')
def get_vendor_name(vendor_id: int) -> str:
    factory = Factory()
    client_service = factory.get_service('vendor')
    vendor = client_service.get_vendor(vendor_id)
    return vendor.name


@register.filter(name='generate_vendor_link')
def generate_vendor_link(vendor_id: int, client_project_id: int) -> str:
    return '{0}{1}?pid={2}_{3}&uid=<uid>'.format(settings.SITE_URL, settings.VENDOR_API_SLUG, vendor_id, client_project_id)

