def final_jellybeans(n, m, updates):
    diff = [0] * (n + 1)

    for a, b, v in updates:
        start = a - 1
        diff[start] += v
        if b < n:
            diff[b] -= v

    res = []
    current = 0
    for i in range(n):
        current += diff[i]
        res.append(m + current)

    return res


# Example
if __name__ == "__main__":
    n = 5
    m = 10
    updates = [(1, 2, 5), (2, 4, 2), (5, 5, 10)]
    print(final_jellybeans(n, m, updates))
  
