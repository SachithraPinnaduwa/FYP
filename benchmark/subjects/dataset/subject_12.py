class EventEmitter:
    def __init__(self): self.events = {}
    def on(self, event, cb): self.events.setdefault(event, []).append(cb)
    def emit(self, event, *args):
        if event in self.events:
            for cb in self.events[event]: cb(*args)
            return True
        return False
