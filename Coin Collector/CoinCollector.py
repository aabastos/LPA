coins = []
flag_coins = []

def withdraw(money):
    if money == 0:
        return
    else:
        flag = False
        aux = len(coins)
        for i in reversed(coins):
            aux = aux - 1
            if flag == True:
                break
            if int(i) <= money:
                flag_coins[aux] = True
                flag = True
                withdraw(money - int(i))

numTests = int(input())

for i in range(0, numTests):
    numCoins = int(input())
    money = 0
    flag_coins.clear()

    coins = input().split(" ")
    for j in range(0, numCoins):
        money = money + int(coins[j])
        flag_coins.append(False)

    withdraw(money)

    cont = 0
    for j in flag_coins:
        if j == True:
            cont = cont + 1

    print(cont)
