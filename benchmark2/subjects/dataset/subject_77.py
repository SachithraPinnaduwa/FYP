import math

def mine_gold(goldMines, centralHub):
    # sort the gold mines based on their proximity to the central hub
    goldMines = dict(sorted(goldMines.items(), key=lambda x: math.sqrt((centralHub[0]-x[1][0])**2 + (centralHub[1]-x[1][1])**2)))

    # extract the maximum amount of gold while maintaining a minimum distance of 20 units between the central hub and any gold mine
    totalGold = 0
    distanceTraveled = 0
    for mine in goldMines:
        if math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2) >= 20:
            totalGold += 10
            distanceTraveled += math.sqrt((centralHub[0]-goldMines[mine][0])**2 + (centralHub[1]-goldMines[mine][1])**2)

    return totalGold, distanceTraveled