def rebalance(krypfolio, prices, alloc, investment):
    """
    Rebalance the investment portfolio according to the specified allocation strategy.

    Args:
    krypfolio (dict): Current state of the investment portfolio.
    prices (dict): Dictionary of cryptocurrency prices.
    alloc (dict): Dictionary of allocation percentages.
    investment (float): Total investment amount.

    Returns:
    dict: Updated state of the investment portfolio after rebalancing.
    """
    target_alloc = {crypto: investment * percentage / 100 for crypto, percentage in alloc.items()}
    
    for crypto, target_amount in target_alloc.items():
        current_amount = krypfolio.get(crypto, 0)
        target_diff = target_amount - current_amount * prices[crypto]
        if target_diff > 0:  # Buy more of the cryptocurrency
            buy_amount = min(target_diff, investment)
            if buy_amount > 0:
                krypfolio[crypto] = current_amount + buy_amount / prices[crypto]
                investment -= buy_amount
        elif target_diff < 0:  # Sell some of the cryptocurrency
            sell_amount = min(-target_diff, current_amount * prices[crypto])
            if sell_amount > 0:
                krypfolio[crypto] = current_amount - sell_amount / prices[crypto]
                investment += sell_amount
        
    return krypfolio