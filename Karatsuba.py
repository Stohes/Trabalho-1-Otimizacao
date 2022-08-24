num = "6"
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


def karatsuba(num, num2):
    if num < 10 or num2 < 10:
        return num * num2

    n = len(num)
    half = n // 2
    a = num // (10 ** (half))
    b = num % (10 ** (half))
    c = num2 // (10 ** (half))
    d = num2 % (10 ** (half))

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    adPlusBc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (adPlusBc * (10 ** half)) + bd


print(num)
print(num2)
print(karatsuba(int(num), int(num2)))
