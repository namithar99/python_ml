# x = input("enter a string:")
# n = x.swapcase()
# print(n)

k = ""
name = input("enter a string:")
for i in name:
    if i.islower():
        k+=i.upper()
    else:
        k+=i.lower()
print(k)

def swapi(x):
    k = ""
    for i in x:
        print(i)
        if i.islower():
            k+=i.upper()
        else:
            k+=i.lower()
    return k
name = input("enter a name")
n = swapi(name)
print(n)




