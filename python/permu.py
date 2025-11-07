def recurPermute(index, s, ans):
    if index == len(s):
        ans.append("".join(s))
        return
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recurPermute(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]

def findPermutation(s):
    ans = []
    recurPermute(0, list(s), ans)
    ans.sort()
    return ans

if __name__ == "__main__":
    s = "ABC"
    res = findPermutation(s)
    for x in res:
        print(x, end=" ")
