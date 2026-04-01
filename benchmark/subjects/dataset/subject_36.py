class IPv4Network:
    def __init__(self, cidr: str):
        self.ip_str, self.prefix = cidr.split('/')
        self.prefix = int(self.prefix)
        self.ip_int = self._ip_to_int(self.ip_str)
        self.mask = (0xFFFFFFFF >> (32 - self.prefix)) << (32 - self.prefix)
        self.network = self.ip_int & self.mask
        self.broadcast = self.network | (~self.mask & 0xFFFFFFFF)

    def _ip_to_int(self, ip: str) -> int:
        parts = list(map(int, ip.split('.')))
        return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

    def _int_to_ip(self, num: int) -> str:
        return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

    def contains(self, ip: str) -> bool:
        return (self._ip_to_int(ip) & self.mask) == self.network

    def get_network_address(self) -> str:
        return self._int_to_ip(self.network)

    def get_broadcast_address(self) -> str:
        return self._int_to_ip(self.broadcast)