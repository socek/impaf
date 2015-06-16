from mock import MagicMock
from pytest import fixture

from ..helper import Helper


class TestHelper(object):

    @fixture
    def mrequest(self):
        return MagicMock()

    @fixture
    def helper(self):
        return Helper()

    def test_feed_request(self, helper, mrequest):
        helper.feed_request(mrequest)

        assert helper.context == {
            'request': mrequest,
            'self': helper,
        }
