class TariffCalculator:
    def __init__(self, base_rate: float, peak_multiplier: float):
        self.base_rate = base_rate
        self.peak_multiplier = peak_multiplier
        self.peak_hours = range(17, 21)  # 5 PM to 8 PM

    def calculate_cost(self, consume_kwh: float, hour_of_day: int, is_weekend: bool) -> float:
        if consume_kwh <= 0:
            return 0.0
            
        rate = self.base_rate
        
        # Weekends have a 10% discount on base
        if is_weekend:
            rate *= 0.9
            
        # Peak hours override weekend discount with multiplier
        if hour_of_day in self.peak_hours:
            rate = self.base_rate * self.peak_multiplier
            
        total = consume_kwh * rate
        # Add 5% tax
        return total * 1.05