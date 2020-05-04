from django.shortcuts import render
from django.utils.encoding import escape_uri_path
from django.views import View

from main.backend.factory import Factory
from main.constants import views_list


class BaseView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.factory = Factory()

    def dispatch(self, request, *args, **kwargs):
        uri = escape_uri_path(request.path)
        segments = uri.lstrip('/').rstrip('/').split('/')
        segment_count = len(segments)
        if segments[segment_count-1] == '' or segments[segment_count-1] in views_list:
            handler = getattr(self, 'index', None)
        else:
            method_name = segments[segment_count - 1].lower()
            handler = getattr(self, method_name, None)
        if handler is not None:
            return handler(request)
        else:
            return render(request, 'templates/404.html')
