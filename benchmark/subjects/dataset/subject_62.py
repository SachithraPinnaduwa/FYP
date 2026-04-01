import hashlib

class FeatureToggle:
    def __init__(self):
        self.features = {}

    def register_feature(self, name: str, rollout_percentage: float):
        if not 0.0 <= rollout_percentage <= 100.0:
            raise ValueError("Rollout must be between 0 and 100")
        self.features[name] = rollout_percentage

    def is_enabled(self, feature_name: str, user_id: str) -> bool:
        if feature_name not in self.features:
            return False
            
        percentage = self.features[feature_name]
        if percentage == 0.0:
            return False
        if percentage == 100.0:
            return True
            
        # Hash user_id + feature to get deterministic 0-100 bucketing
        hash_val = int(hashlib.md5(f"{feature_name}_{user_id}".encode()).hexdigest(), 16)
        bucket = hash_val % 10000 / 100.0  # 0.00 to 99.99
        
        return bucket < percentage