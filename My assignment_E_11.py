coins = [1, 5, 5, 8]
targets = [15, 11, 5, 14]

def can_i_pay(coins, target):
    for i in range(len(coins)):
        for j in range(i + 1, len(coins)):
            for k in range(j + 1, len(coins)):
                if coins[i] + coins[j] + coins[k] == target:
                    return [coins[i], coins[j], coins[k]]
    return "not possible"

for target in targets:
    print(f"Target: {target}, Result: {can_i_pay(coins,target)}")


