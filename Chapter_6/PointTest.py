from Shape import Point

a = Point(2, 3)
b = Point(3, 4)

print(a + b)

a += b 
print(a)

print(a - b - b)

a -= b
print(a)

print(a * 3)

a *= 2
print(a)

print(a / 2)
# a /= b
# print(a/b)

print(b // 2)
