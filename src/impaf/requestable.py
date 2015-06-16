class Requestable(object):

    def feed_request(self, request):
        self.request = request
        self.registry = request.registry
        self.POST = request.POST
        self.GET = request.GET
        self.matchdict = request.matchdict
        self.settings = self.registry['settings']
        self.paths = self.registry['paths']
        self.route_path = request.route_path
