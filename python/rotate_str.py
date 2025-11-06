def isRotated(str1, str2):
    n = len(str1)
    clockwise, anticlockwise = True, True

    for i in range(n):
        if str1[i] != str2[(i + 2) % n]:
            clockwise = False
            break

    for i in range(n):
        if str1[(i + 2) % n] != str2[i]:
            anticlockwise = False
            break

    return clockwise or anticlockwise


if __name__ == "__main__":
    str1 = "amazon"
    str2 = "azonam"
    print(isRotated(str1, str2))

    str1 = "amazon"
    str2 = "onamaz"
    print(isRotated(str1, str2))
