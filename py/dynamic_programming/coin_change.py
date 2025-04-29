"""
Given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Solution:
  - https://www.youtube.com/watch?v=jgiZlGzXMBw
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for amnt in range(coin, amount+1):
            dp[amnt] = min(dp[amnt], dp[amnt-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def main():
    coins = [1, 2, 5]
    amount = 11
    print("The fewest number of coins: {}".format(coin_change(coins, amount)))

    coins = [2]
    amount = 3
    print("The fewest number of coins: {}".format(coin_change(coins, amount)))


if __name__ == '__main__':
    main()