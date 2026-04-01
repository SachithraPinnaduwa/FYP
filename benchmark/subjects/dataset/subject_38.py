class WeightedRoundRobin:
    def __init__(self, servers: dict):
        self.servers = [{"name": k, "weight": v, "current_weight": 0} for k, v in servers.items()]
        
    def get_next(self) -> str:
        if not self.servers:
            return None
            
        total_weight = sum(s["weight"] for s in self.servers)
        best = None
        
        for s in self.servers:
            s["current_weight"] += s["weight"]
            if best is None or s["current_weight"] > best["current_weight"]:
                best = s
                
        if best:
            best["current_weight"] -= total_weight
            return best["name"]
        return None