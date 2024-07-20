from math import sqrt
from heapq import heappush, heappop

def printTransactions(money, k, d, name, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        # Calculate the price change rate from the second last to the last day
        return (price[-1] - price[-2]) / price[-2]

    # Collect stock information based on the price trend
    res = []
    drop = []

    for i in range(k):
        cur_info = info(prices[i])
        if cur_info > 0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heappush(drop, (cur_info, i, name[i]))

    # Buy stocks from the drop heap until we run out of money
    while money > 0.0 and drop:
        rate, idx, n = heappop(drop)
        amount = int(money // prices[idx][-1])
        if amount > 0:
            res.append((n, 'BUY', str(amount)))
            money -= amount * prices[idx][-1]

    # Print the number of transactions
    print(len(res))
    # Print each transaction
    for r in res:
        print(' '.join(r))

# Example usage with sample input
if __name__ == '__main__':
    # Use raw_input for Python 2.x or input for Python 3.x
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    m, k, d = float(data[0]), int(data[1]), int(data[2])
    index = 3
    names = []
    owned = []
    prices = []

    for i in range(k):
        names.append(data[index])
        owned.append(int(data[index + 1]))
        prices.append(list(map(float, data[index + 2:index + 7])))
        index += 7

    printTransactions(m, k, d, names, owned, prices)
