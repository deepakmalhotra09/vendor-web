from django.http import Http404
from django.utils.encoding import escape_uri_path
from django.views import View

from main.constants import views_list


class BaseView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        uri = escape_uri_path(request.path)
        segments = uri.lstrip('/').rstrip('/').split('/')
        segment_count = len(segments)
        if segments[segment_count-1] == '' or segments[segment_count-1] in views_list:
            handler = getattr(self, 'index', None)
        else:
            method_name = segments[segment_count - 1].lower()
            print(method_name)
            # method_name = re.sub('[^a-z0-9]', '', method_name)
            handler = getattr(self, method_name, None)
        print(handler)
        if handler is not None:
            return handler(request)
        else:
            raise Http404()
