def mult(n,m):
    if (m <= 0):
        return 0
    return n + mult(n,m-1)

print(mult(3,4))
