def find_drag_race_winner(n, matches):
    # Dictionary to keep track of the winners and losers
    status = {}
    
    # Process each match result
    for match in matches:
        racer1, racer2 = match.split()
        
        # Initialize the status of racers if not already present
        if racer1 not in status:
            status[racer1] = True
        if racer2 not in status:
            status[racer2] = False
        
        # Update the status based on the match result
        if status[racer1]:
            status[racer2] = False
        else:
            status[racer1] = False
            status[racer2] = False
    
    # Find and return the winner
    for racer, is_winner in status.items():
        if is_winner:
            return racer

    # In case no winner is found (which shouldn't happen given the problem constraints)
    return None