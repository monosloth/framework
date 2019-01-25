from app.singleton import MetaSingleton


class EventManager(metaclass=MetaSingleton):

    def set_listeners(self, listeners):
        self.listeners = listeners

    def attach_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def detach_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def work(self):
        for event in pygame.event.get():
            for listener in self.listeners:
                listener.invoke(event)

                if listener.stop_event_propagation(event):
                    return
                elif listener.stop_propagation(event):
                    break
