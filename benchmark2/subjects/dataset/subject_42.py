def calculate_fuel_cost(litres, price_per_litre):
    # Calculate the discount based on the number of litres
    discount_per_litre = int(min(litres, 10) / 2) * 0.05
    
    # Ensure the discount does not exceed the maximum allowed
    discount_per_litre = min(discount_per_litre, 0.25)
    
    # Calculate the final price per litre after discount
    final_price_per_litre = price_per_litre - discount_per_litre
    
    # Calculate the total cost
    total_cost = final_price_per_litre * litres
    
    # Return the total cost rounded to 2 decimal places
    return round(total_cost, 2)