# Time complexity : O(n^2 * n!) , number of permutations is equal to its len(nums) factorial = n!
# [Iterative code for permutations]
def permutations(nums):
    perms = [[]]

    for n in nums:
        nextPerm = []

        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerm.append(pCopy)
        perms = nextPerm

    return perms

def main():
    print("Permutations of [1,2,3,4] expected 24 permutations")
    perms = permutations([1,2,3,4])
    print(perms)
    print("\nSize: ",len(perms))

if __name__ == "__main__":
    main()