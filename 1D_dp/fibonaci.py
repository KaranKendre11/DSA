# fibonacci using dynamic programming

# Using memorization (debateable as not a dp way of solving things) [TOP DOWN APPROACH], space complexity: O(n)
def fibo(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = fibo(n-1, cache) + fibo(n-2, cache)
    return cache[n]

# [BOTTOM UP APPROACH] space complexity: O(1)
def fibov2(n):
    if n <= 1:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]


def main():
    n = int(input("Enter range of fibonacci?"))
    print("[TOP DOWN APPROACH]")
    for i in range(n):
        print(fibo(i,{}), end=", ")
    print("\n[BOTTOM UP APPROACH]")
    for i in range(n):
        print(fibov2(i,), end=", ")

if __name__ == "__main__":
    main()