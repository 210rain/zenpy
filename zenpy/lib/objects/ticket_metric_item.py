from zenpy.lib.objects.base_object import BaseObject


class TicketMetricItem(BaseObject):
    def __init__(self, api=None, **kwargs):
        self.api = api
        self.calendar = None
        self.business = None

        for key, value in kwargs.iteritems():
            setattr(self, key, value)