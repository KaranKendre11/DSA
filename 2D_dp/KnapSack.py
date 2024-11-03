def knapSackDp(profit, weight, capacity):
    N, M = len(profit), capacity
    # making a N X M + 1 matrix with 0 in all values
    dp = [[0] * (M + 1) for _ in range(N)]

    # prepping the matrix
    for currentCapacity in range(M + 1):
        if currentCapacity - weight[0] >= 0:
            dp[0][currentCapacity] = profit[0]

    # computation
    for i in range(1, N):
        for j in range(1, M + 1):
            skip = dp[i-1][j]
            include = 0
            if j - weight[i] >= 0:
                include = profit[i] + dp[i-1][j - weight[i]] # dp[i-1][j - weight[i]] gives us the element which is max and fills the capacity
            dp[i][j] = max(skip, include) # max profit when you skip profit or when you add profit
    return dp[N - 1][M]

profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8

print(knapSackDp(profit, weight, capacity))
