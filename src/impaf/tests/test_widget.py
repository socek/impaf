from mock import MagicMock
from pytest import fixture

from ..widget import Widget


class TestWidget(object):

    @fixture
    def mrequest(self):
        return MagicMock()

    @fixture
    def widget(self):
        return Widget()

    def test_feed_request(self, widget, mrequest):
        widget.feed_request(mrequest)

        assert widget.context == {
            'request': mrequest,
            'self': widget,
        }
