# how to write recursive function
# factorial

def factorial(n):
    # The constraint - step 3
    assert n >= 0 and int(n) == n, "The number must be postive integer only"
    # identifying the base case - step 2
    if n in [0, 1]:
        return 1
    else:
        # identifying the recursive case - step 1
        return n * factorial(n - 1)


print(factorial(3.1))