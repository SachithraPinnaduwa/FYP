class PubSubBus:
    def __init__(self):
        self.topics = {}
        self.wildcards = {}

    def subscribe(self, topic: str, handler):
        if "*" in topic:
            if topic not in self.wildcards:
                self.wildcards[topic] = []
            self.wildcards[topic].append(handler)
        else:
            if topic not in self.topics:
                self.topics[topic] = []
            self.topics[topic].append(handler)

    def publish(self, topic: str, payload: dict):
        if topic in self.topics:
            for handler in self.topics[topic]:
                handler(payload)
                
        for w_topic, handlers in self.wildcards.items():
            if self._matches(w_topic, topic):
                for handler in handlers:
                    handler(payload)

    def _matches(self, wildcard: str, actual: str) -> bool:
        w_parts = wildcard.split('.')
        a_parts = actual.split('.')
        
        if len(w_parts) != len(a_parts):
            return False
            
        for w, a in zip(w_parts, a_parts):
            if w != "*" and w != a:
                return False
        return True