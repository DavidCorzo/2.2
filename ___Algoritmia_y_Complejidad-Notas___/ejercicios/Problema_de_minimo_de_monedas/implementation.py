V = int(input("Enter the value for V:"))

denominations = [1,5,10,25,50]
coins_needed = {1:0,5:0,10:0,25:0,50:0}

i = len(denominations) - 1

while (0 <= i):
    while (V >= denominations[i]):
        V = V - denominations[i]
        coins_needed[denominations[i]] += 1
    i = i - 1

for k,v in coins_needed.items():
    if (v != 0): 
        print(f"{v} coins of denomination {k}")


