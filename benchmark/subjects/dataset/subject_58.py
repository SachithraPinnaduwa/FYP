from collections import deque

class InventoryManager:
    def __init__(self):
        self.stock = {}
        self.transactions = []

    def add_stock(self, item_id: str, quantity: int, cost_per_unit: float):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if item_id not in self.stock:
            self.stock[item_id] = deque()
            
        # FIFO approach: append to right
        self.stock[item_id].append({"qty": quantity, "cost": cost_per_unit})

    def sell_stock(self, item_id: str, quantity: int) -> float:
        if item_id not in self.stock or not self.stock[item_id]:
            raise ValueError("Item not found or out of stock")
            
        total_cost = 0.0
        remaining_to_sell = quantity
        
        while remaining_to_sell > 0 and self.stock[item_id]:
            batch = self.stock[item_id][0]
            if batch["qty"] <= remaining_to_sell:
                total_cost += batch["qty"] * batch["cost"]
                remaining_to_sell -= batch["qty"]
                self.stock[item_id].popleft()
            else:
                total_cost += remaining_to_sell * batch["cost"]
                batch["qty"] -= remaining_to_sell
                remaining_to_sell = 0
                
        if remaining_to_sell > 0:
            raise ValueError("Not enough stock to fulfill order")
            
        self.transactions.append({"item": item_id, "sold": quantity, "cogs": total_cost})
        return total_cost