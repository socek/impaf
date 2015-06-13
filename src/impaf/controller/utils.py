from pyramid.httpexceptions import HTTPFound

from .exceptions import QuitController


class ControllerUtils(object):

    def redirect(self, to, quit=False, **kwargs):
        url = self.request.route_url(to, **kwargs)
        self.response = HTTPFound(location=url)
        if quit:
            raise QuitController(self.response)

    def add_helper(self, name, cls, *args, **kwargs):
        self.context[name] = cls(self.request, *args, **kwargs)
