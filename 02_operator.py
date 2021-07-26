

a = 10
b = 3

# Arithmatic operators plus minus division multiplication
print("The value of 3+4 is = ", a+b)
print("The value of 3-4 is = ", a-b)
print("The value of 3*4 is = ", a*b)
print("The value of 3/4 is = ", a/b)
print(type(a/b))

# Assignment operators = ,+= ,-+    *=, /= can also be aplied
c = 54  # c will contain 54 value
c += 2  # 56
c = c + 3  # 59
print(c)


# comparison operator  returns boolean value true or false  > < => =< == !=
b = (4 > 7)
d = (4 > 2)
print(b, d)  # false

print(b != 5)


# logical operators
bool1 = True
bool2 = False
print(bool1 and bool2)  # return true if both are true
print(bool1 or bool2)  # return true if one is true
print(not bool1)  # return true if false or false if true
