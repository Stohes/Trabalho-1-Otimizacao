import textwrap
# import sys
# num = str(sys.argv[1])
# num2 = str(sys.argv[2])


num = "105"
num2 = "6175"


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
    carry = False
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) + int(num2[i]) > 9:
            newNum = str(int(num[i]) + int(num2[i]))[1] + newNum
            carry = True
        else:
            if carry:
                newNum = str(int(num[i]) + int(num2[i]) + 1) + newNum
                carry = False
            else:
                newNum = str(int(num[i]) + int(num2[i])) + newNum
    return newNum


print(add(num, num2))
