import math
x =input("write your first number here: " )
y = input("write your second number here or leave it blank for some match functions: " )
z = input("what do you want to do? +, -, *, /, power, factorial, abs for absolute, OR for bitwise OR, AND for bitwise AND, XOR for bitwise XOR: ")

if z == "+" :
    print("the result is: " + str(int(x) + int(y)) )
elif z == "-" :
    print("the result is: " + str(int(x) - int(y)) )
elif z == "*" :
    print("the result is: " + str(int(x) * int(y)) )
elif z == "/" :
    print("the result is: " + str(int(x) / int(y)) )
elif z == "power" :
    print("the result is: " + str(int(x) ** int(y)) )
elif z == "factorial" :
    print("the result is: " + str(math.factorial(int(x))))
elif z == "abs" :
    print("the result is: " + str(abs(int(x))))
elif z == "OR" :
    print("the result is: " + str(int(x) | int(y)))
elif z == "AND" :
    print("the result is: " + str(int(x) & int(y)))
elif z == "XOR" :
    print("the result is: " + str(int(x) ^ int(y)))
