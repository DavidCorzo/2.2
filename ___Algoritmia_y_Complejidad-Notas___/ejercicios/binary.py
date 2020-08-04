from math import floor

def print_binary(n: int):
    stack = list()
    while (n != 0):
        r = n % 2
        n = floor(n / 2)
        stack.append(r)

    while (len(stack) != 0):
        print(stack.pop(),end="")

def print_binary_rec(n: int):
    if (n >= 2):
        print_binary_rec(int(n/2))
        print(n%2,end="")
    else: 
        print(n,end="")

print_binary_rec(67)
