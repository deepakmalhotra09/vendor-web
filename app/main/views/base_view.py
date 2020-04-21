import re

from django.http import Http404
from django.utils.encoding import escape_uri_path
from django.views import View


class BaseView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        uri = escape_uri_path(request.path)
        segments = uri.lstrip('/').rstrip('/').split('/')
        segment_count = len(segments)
        if segments[segment_count-1] == '':
            handler = getattr(self, 'index', None)
        else:
            method_name = segments[segment_count-1].lower()
            method_name = re.sub('[^a-z0-9]', '', method_name)
            handler = getattr(self, method_name, None)

        if handler is not None:
            return handler(request)
        else:
            raise Http404()
