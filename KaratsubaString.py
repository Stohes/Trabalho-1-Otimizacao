num = "633333"
num2 = "24"


while (len(num) % 3) != 0:
    num = "0" + num

while (len(num2) % 3) != 0:
    num2 = "0" + num2

while len(num) != len(num2):
    if len(num) > len(num2):
        num2 = "0" + num2
    else:
        num = "0" + num


def karatsuba(a, b):
    if len(str(a)) == 1:
        return int(a) * int(b)

    third = len(str(a)) // 3

    a1 = a[0:third]
    a2 = a[third:third*2]
    a3 = a[third*2:]
    b1 = b[0:third]
    b2 = b[third:third*2]
    b3 = b[third*2:]

    a1b1 = karatsuba(a1, b1)
    a1b2 = karatsuba(a1, b2)
    a1b3 = karatsuba(a1, b3)
    a2b1 = karatsuba(a2, b1)
    a2b2 = karatsuba(a2, b2)
    a2b3 = karatsuba(a2, b3)
    a3b1 = karatsuba(a3, b1)
    a3b2 = karatsuba(a3, b2)
    a3b3 = karatsuba(a3, b3)

    return a1b1 + a1b2 + a1b3 + a2b1 + a2b2 + a2b3 + a3b1 + a3b2 + a3b3


print(num)
print(num2)
print(karatsuba(int(num), int(num2)))
