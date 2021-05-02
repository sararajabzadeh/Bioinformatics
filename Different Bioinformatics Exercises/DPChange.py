import math
def DPChange(money , coins):
    MinNumCoins = [0]
    for i in range(1,money+1):
        MinNumCoins += [math.inf]
        for j in range(len(coins)):
            if i>=coins[j]:
                if MinNumCoins[i-coins[j]] +1<MinNumCoins[i]:
                    MinNumCoins[i] = MinNumCoins[i-coins[j]] +1
    return MinNumCoins[money]

money  = int(input())
coins = list(map(int , input().split()))
print(DPChange(money , coins))