print("1.")
num_1 = 10
num_2 = 2
print(f"\tnum_1: {num_1}, num_2: {num_1}")

print("2.")
A = [
    num_1+num_2, num_1-num_2, num_1*num_2, num_1/num_2
]
print("\tVector resultado = " + str(A))

print("3.")
print(f"\tSuma de num_1({num_1}) & num_2({num_2}): {A[0]}")
print(f"\tResta de num_1({num_1}) & num_2({num_2}): {A[1]}")
print(f"\tMultiplicación de num_1({num_1}) & num_2({num_2}): {A[2]}")
print(f"\tDivisión de num_1({num_1}) & num_2({num_2}): {A[3]}")

print("4.")
A = [
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
]
print("[")
for i in A:
    for ii in i: 
        print("\t"+str(ii)+" ",end="")
    print("")
print("]")

print("5.")
cur = 0
for i in A:
    i[cur] += 2
    cur += 1
print("[")
for i in A:
    print("\t"+str(i))
print("]")
