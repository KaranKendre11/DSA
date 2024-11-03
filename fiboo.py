def rec_fib(n):
    if n <= 1:
        return n
    return rec_fib(n-1) + rec_fib(n-2)

def run_feb(n):
    print("Running recursively")
    for i in range(0,n):
        print(rec_fib(i))

def itr_feb(n):
    print("Running iteratively")
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(0,n-2):
        c = a + b
        a = b
        b = c
        print(c)  
