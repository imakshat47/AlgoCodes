def spirallyTraverse(mat):
    m, n = len(mat), len(mat[0])

    res = []

    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(top,i)
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            print(i,right)
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(bottom,i)
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(i,left)
                res.append(mat[i][left])
            left += 1
    return res


if __name__ == "__main__":
    mat = [[13, 28, 32, 49], 
           [59, 64, 89, 81], 
           [94, 10, 11, 12], 
           [13, 14, 15, 16]]

    res = spirallyTraverse(mat)
    print(" ".join(map(str, res)))
