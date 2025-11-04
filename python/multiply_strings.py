def multiplyStrings(a, b):
    if a == '0' or b == '0':
        return '0'

    negative = False

    if a[0] == '-':
        negative = not negative
        a = a[1:]

    if b[0] == '-':
        negative = not negative
        b = b[1:]

    product = [0 for _ in range(len(a) + len(b))]

    for i in range(len(b) - 1, -1, -1):
        digit1 = int(b[i])
        carry = 0

        for j in range(len(a) - 1, -1, -1):
            digit2 = int(a[j])
            product[i + j + 1] += digit1 * digit2 + carry
            carry = product[i + j + 1] // 10
            product[i + j + 1] = product[i + j + 1] % 10

        nextIndex = i
        while carry:
            product[nextIndex] += carry
            carry = product[nextIndex] // 10
            product[nextIndex] = product[nextIndex] % 10
            nextIndex -= 1

    res = ''.join(str(x) for x in product)

    zeroes = 0
    while zeroes < len(res) - 1 and res[zeroes] == '0':
        zeroes += 1
    res = res[zeroes:]

    if negative and res != "0":
        res = '-' + res

    return res

if __name__ == '__main__':
    s1 = "0033"
    s2 = "2"
    print(multiplyStrings(s1, s2))
