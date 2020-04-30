from django import template

register = template.Library()


@register.filter(name='get_key')
def get_key(data, key) -> str:
    if data:
        load_json = eval(data)
        return load_json[key]
    return ''
