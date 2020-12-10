import json

from django.http import HttpRequest, JsonResponse


def get_request_param(key: str, request: HttpRequest):
    data = None
    try:
        data = request.POST.get(key, '')
    except KeyError:
        return
    finally:
        return data


def get_request_param_json(key: str, request: HttpRequest):
    data = None
    try:
        data = json.loads(request.POST.get(key, ''))
    except KeyError:
        return
    finally:
        return data


def json_response(status: bool, data: json) -> json:
    response = {
        'status': status,
        'data': JsonResponse(data, safe=False)
    }
    response_str = json.dumps(response)
    return json.loads(response_str)
