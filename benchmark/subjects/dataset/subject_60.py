from datetime import datetime, timedelta

class SubscriptionManager:
    def __init__(self, monthly_rate: float):
        self.monthly_rate = monthly_rate
        self.users = {}

    def subscribe(self, user_id: str, trial_days: int = 14):
        self.users[user_id] = {
            "status": "TRIAL",
            "expires_at": datetime.now() + timedelta(days=trial_days),
            "balance": 0.0
        }

    def charge_user(self, user_id: str) -> bool:
        if user_id not in self.users:
            return False
            
        user = self.users[user_id]
        if user["status"] == "CANCELLED":
            return False
            
        if datetime.now() > user["expires_at"]:
            user["status"] = "ACTIVE"
            user["expires_at"] = datetime.now() + timedelta(days=30)
            user["balance"] += self.monthly_rate
            return True
            
        return False

    def cancel(self, user_id: str):
        if user_id in self.users:
            self.users[user_id]["status"] = "CANCELLED"