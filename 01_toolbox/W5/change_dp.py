# Uses python3
import sys

def get_change(m):
    """The minimum number of coins with denominations 1, 3, 4 that changes money
    """
    coins_arr = [1, 3, 4]
    money_dict = {}
    money_dict[0] = 0

    for money in range(1, m + 1):
        #print(money_dict)
        money_dict[money] = m + 1
        for coin in coins_arr:
            if coin <= money:
                numCoins= money_dict[money - coin] + 1
                if numCoins < money_dict[money]:
                    money_dict[money] = numCoins          

    return money_dict[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
