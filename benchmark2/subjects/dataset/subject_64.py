import base64

class BasicAuthHeaderHelper:
    def __init__(self, default_realm: str = "SecureArea"):
        self.default_realm = default_realm

    def create_header(self, username: str, password: str) -> str:
        credentials = f"{username}:{password}"
        encoded = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        return f"Basic {encoded}"

    def decode_header(self, header: str) -> dict:
        if not header or not header.startswith("Basic "):
            return None
            
        encoded = header[6:]
        try:
            decoded = base64.b64decode(encoded).decode("utf-8")
            if ":" not in decoded:
                return None
            u, p = decoded.split(":", 1)
            return {"username": u, "password": p}
        except Exception:
            return None