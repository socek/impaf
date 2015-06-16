from .requestable import Requestable


class Helper(Requestable):

    def feed_request(self, request):
        super().feed_request(request)
        self._create_context()

    def _create_context(self):
        self.context = {
            'request': self.request,
            'self': self,
        }
