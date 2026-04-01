class DIContainer:
    def __init__(self):
        self._services = {}
        self._instances = {}

    def register(self, name: str, factory, singleton: bool = True):
        self._services[name] = {"factory": factory, "singleton": singleton}

    def resolve(self, name: str):
        if name not in self._services:
            raise ValueError(f"Service {name} not found")
            
        service_info = self._services[name]
        
        if service_info["singleton"]:
            if name not in self._instances:
                self._instances[name] = service_info["factory"](self)
            return self._instances[name]
            
        return service_info["factory"](self)