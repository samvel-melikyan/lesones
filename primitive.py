import math

print(0xb64)
print(hex(0xb64))
print(0xb64 == 2916)
print(hex(0xb64) == 2916)
print(type(hex(0xb64)))
print(0xb64 + 0o77)
print(bin(0xb64))
print(oct(256))
print(oct(99))
# print(-30 ** 99999)
print(3 ** 99.345)
print("=====================")
from decimal import Decimal
# special mathematics module to use float numbers correctly
print(Decimal("2.44") * Decimal("3.122"))

print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))   # dont forget the quotes!

print("=====================")

a = 64
b = float(a)
print(b)
print(type(b))

# a = 64.0
b = int(b)
print(b)
print(type(b))

a = Decimal("4.8")
b = float(a)
print(b)
print(type(b))
print("=====================")

a = round(12.5)
print(a)
print(type(a))
a = round(12.6)
print(a)
print(type(a))
print("=====================")

print(math.floor(50.99), " : floor - always down")
print(math.ceil(50.00001), " : ceil - always down")

print(abs(88))
print(abs(-88), "was minus")