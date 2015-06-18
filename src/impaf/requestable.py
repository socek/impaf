from pyramid.request import Request


class Requestable(object):

    def feed_request(self, request):
        self._convert_request(request)
        self._unpack_request(self.request)

    def _convert_request(self, request):
        self.request = ImpafRequest(request)

    def _unpack_request(self, request):
        self.registry = request.registry
        self.POST = request.POST
        self.GET = request.GET
        self.matchdict = request.matchdict
        self.route_path = request.route_path
        self.settings = self.registry['settings']
        self.paths = self.registry['paths']


class ImpafRequest(Request):

    def __init__(self, request):
        self.__dict__ = request.__dict__

    @property
    def settings(self):
        return self.registry['settings']

    @property
    def paths(self):
        return self.registry['paths']
