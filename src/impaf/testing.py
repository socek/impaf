from mock import MagicMock
from mock import patch

from pytest import fixture
from pytest import yield_fixture


class RequestFixture(object):

    @fixture
    def mrequest(self):
        return MagicMock()

    @fixture
    def registry(self):
        return {
            'settings': {},
            'paths': {},
        }

    @fixture
    def POST(self):
        return {}

    @fixture
    def GET(self):
        return {}

    @fixture
    def matchdict(self):
        return {}

    @fixture
    def mroute_path(self, mrequest):
        return mrequest.route_path

    @fixture
    def settings(self, registry):
        return registry['settings']

    @fixture
    def paths(self, registry):
        return registry['paths']


class ControllerFixture(RequestFixture):

    def _cls_controller(self):
        pass

    def _prepere_controller(self, cls, context):
        def set_request(self, request):
            self.request = request
        cls._convert_request = set_request
        cls.context = context

    @fixture
    def root_factory(self):
        return MagicMock()

    @fixture
    def controller(self, root_factory, mrequest, context):
        cls = self._cls_controller()
        self._prepere_controller(cls, context)
        return cls(root_factory, mrequest)

    @fixture
    def context(self):
        return {}

    @yield_fixture
    def mredirect(self, controller):
        patcher = patch.object(controller, 'redirect')
        with patcher as mock:
            yield mock

    @yield_fixture
    def madd_widget(self, controller):
        patcher = patch.object(controller, 'add_widget')
        with patcher as mock:
            yield mock
