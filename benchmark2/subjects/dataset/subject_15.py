import hmac
import hashlib
import base64
import json
import time

class SimpleJWT:
    def __init__(self, secret: str):
        self.secret = secret.encode()

    def _b64(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip("=")

    def sign(self, payload: dict, exp_in_seconds: int = 3600) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        payload["exp"] = int(time.time()) + exp_in_seconds
        
        h_b64 = self._b64(json.dumps(header).encode())
        p_b64 = self._b64(json.dumps(payload).encode())
        
        msg = f"{h_b64}.{p_b64}".encode()
        sig = hmac.new(self.secret, msg, hashlib.sha256).digest()
        
        return f"{h_b64}.{p_b64}.{self._b64(sig)}"

    def verify(self, token: str) -> dict:
        parts = token.split(".")
        if len(parts) != 3: return None
        
        msg = f"{parts[0]}.{parts[1]}".encode()
        expected_sig = self._b64(hmac.new(self.secret, msg, hashlib.sha256).digest())
        
        if not hmac.compare_digest(parts[2], expected_sig):
            return None
            
        payload = json.loads(base64.urlsafe_b64decode(parts[1] + "==").decode())
        if payload.get("exp", 0) < time.time():
            return None
            
        return payload