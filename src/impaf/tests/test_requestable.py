from mock import MagicMock
from pytest import fixture

from ..requestable import Requestable


class TestRequestable(object):

    @fixture
    def model(self):
        return Requestable()

    @fixture
    def mrequest(self):
        return MagicMock()

    def test_feed_request(self, model, mrequest):
        model.feed_request(mrequest)

        assert model.request == mrequest
