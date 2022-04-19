# Given an integer n, use the greedy algorithm to find the change for n cents using quarters,
# dimes, nickels, and pennies.

def findChange(n):
    coins = [25, 10, 5, 1] # quarters, dimes, nickels, and pennies.
    coinsLength = len(coins)
    
    ans = []

    for i in range(0, coinsLength):
        while (n >= coins[i]):
            n -= coins[i]
            ans.append(coins[i])
    for i in range(len(ans)):
        print(ans[i], end = " ")

n = 56
print(f"The change for {n} cents: ", end = "")
findChange(n)