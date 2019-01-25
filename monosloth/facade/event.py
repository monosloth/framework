from . import AbstractFacade
from monosloth.singleton import Dispatcher


class EventFacade(AbstractFacade):

    def __init__(self):
        super().__init__('event')

    def invoke(self, event, payload=[]):
        """Dispatch the given event.

        :param event: The event to dispatch.
        :param: payload: The event data to process.

        :return: The result of the event.

        """
        return Dispatcher().dispatch(event, payload)
