# Math C(n,k) = n!/k!(n-k)!
def combinations(n,k):
    combs = []
    helper(1, combs, [], n, k)
    return combs


def helper(i, combs, curComb, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    # same subset 2 choices code can also be used here instead of the below optimized version
    curComb.append(i)
    helper(i+1, combs,curComb, n, k)
    curComb.pop()

    helper(i+1, combs, curComb, n, k)

    # [OPTIMIZED VERSION] derived from the math formula
    for j in range(i, n+1):
        curComb.append(j)
        helper(j+1, combs, curComb, n, k)
        curComb.pop()

def main():
    combs = combinations(5, 2)
    print("Combination for range 1 to 5 of size k = 2")
    print(combs)

if __name__ =="__main__":
    main()