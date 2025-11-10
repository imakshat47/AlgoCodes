MAX_CHAR = 26

def longestUniqueSubstr(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)

    res = 0
    vis = [False] * 26
    left = 0
    right = 0

    while right < len(s):
        while vis[ord(s[right]) - ord('a')]:
            vis[ord(s[left]) - ord('a')] = False
            left += 1

        vis[ord(s[right]) - ord('a')] = True
        res = max(res, right - left + 1)
        right += 1

    return res

if __name__ == "__main__":
    s = "geeksforgeeks"
    print(longestUniqueSubstr(s))
