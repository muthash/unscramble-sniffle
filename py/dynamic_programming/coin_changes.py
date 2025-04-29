"""
Given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Solution:
  - https://www.youtube.com/watch?v=DJ4a7cmjZY0
"""

def change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


def main():
    coins = [1, 2, 5]
    amount = 5
    print("The number of combinations: {}".format(change(coins, amount)))

    coins = [2]
    amount = 3
    print("The number of combinations: {}".format(change(coins, amount)))


if __name__ == '__main__':
    main()
