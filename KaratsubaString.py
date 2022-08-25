import sys
num = str(sys.argv[1])
num2 = str(sys.argv[2])


while (len(num) % 243) != 0:
    num = "0" + num

while (len(num2) % 243) != 0:
    num2 = "0" + num2

while len(num) != len(num2):
    if len(num) > len(num2):
        num2 = "0" + num2
    else:
        num = "0" + num


def add(num, num2):
    newNum = ""
    carry = 0
    num = str(num)
    num2 = str(num2)

    while len(num) != len(num2):
        if len(num) > len(num2):
            num2 = "0" + num2
        else:
            num = "0" + num

    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) + int(num2[i]) + carry > 9:
            if carry == 1:
                newNum = str(int(num[i]) + int(num2[i]) + 1)[1] + newNum
            else:
                newNum = str(int(num[i]) + int(num2[i]))[1] + newNum
            carry = 1
        else:
            if carry == 1:
                newNum = str(int(num[i]) + int(num2[i]) + 1) + newNum
                carry = 0
            else:
                newNum = str(int(num[i]) + int(num2[i])) + newNum
    if carry:
        return "1" + newNum
    return newNum


def karatsuba(a, b):
    if len(str(a)) == 1:
        return str(int(a) * int(b))

    third = len(str(a)) // 3
        
    a1 = a[0:third]
    a2 = a[third:third*2]
    a3 = a[third*2:]
    b1 = b[0:third]
    b2 = b[third:third*2]
    b3 = b[third*2:]

    a1b1 = karatsuba(a1, b1) + (len(a) - len(a1) + len(b) - len(b1)) * "0"
    a1b2 = karatsuba(a1, b2) + (len(a) - len(a1) + len(b) - len(b1) - len(b2)) * "0"
    a1b3 = karatsuba(a1, b3) + (len(a) - len(a1)) * "0"
    a2b1 = karatsuba(a2, b1) + (len(a) - len(a1) - len(a2) + len(b) - len(b1)) * "0"
    a2b2 = karatsuba(a2, b2) + (len(a) - len(a1) - len(a2) + len(b) - len(b1) - len(b2)) * "0"
    a2b3 = karatsuba(a2, b3) + (len(a) - len(a1) - len(a2)) * "0"
    a3b1 = karatsuba(a3, b1) + (len(b) - len(b1)) * "0"
    a3b2 = karatsuba(a3, b2) + (len(b) - len(b1) - len(b2)) * "0"
    a3b3 = karatsuba(a3, b3)

    return add(a1b1, add(a1b2, add(a1b3, add(a2b1, add(a2b2, add(a2b3, add(a3b1, add(a3b2, a3b3))))))))


print(karatsuba(num, num2).lstrip("0"))

