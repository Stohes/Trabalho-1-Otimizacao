import textwrap
# import sys
# num = str(sys.argv[1])
# num2 = str(sys.argv[2])


num = "12345"
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

# print(textwrap.wrap(num, int(len(num) / 3)))
# print(textwrap.wrap(num2, int(len(num2) / 3)))


def add(num, num2):
    newNum = ""
    carry = 0
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
    return newNum


def divide(num):
    if (len(num[0]) == 1) and (isinstance(num, list)):
        return num

    if (isinstance(num, list)) and (len(num[0]) > 2):
        for i in range(len(num)):
            num[i] = textwrap.wrap(num, int(len(num) / 3))
            return num[i]
    else:
        for i in num:
            return list(i)

    num = textwrap.wrap(num, int(len(num) / 3))

    return divide(num)


print(add(num, num2))
print(divide(num))


# for i in range(0, len(num), 2):
#     return int(num[i]) * int(num[i + 1])
