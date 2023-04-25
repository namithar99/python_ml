a = int(input("enter the coeffeicient of x^2:"))
b = int(input("enter the coeffeicient of x^1:"))
c = int(input("enter the coefficient of x^0:"))
k = (b**2)-(4*a*c)
d = k**0.5
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print("The first roots is ", x1)
print("And second root is ",x2)