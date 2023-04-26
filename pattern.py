for i in range(1,5):
    for j in range(1, i+1):
         print(i,end = "")
    print()

for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(1,5):
    for j in range(1,6-i):
        print(i, end = "")
    print()

# to get lower triangule
for i in range(1,7):
    for j in range(1,7):
        if(i == 6 or j == 1 or i == j):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()









