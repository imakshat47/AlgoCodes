def computeLPSArray(string, M, lps):
    length = 0
    i = 1
    lps[0] = 0
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def isRepeat(string):
    n = len(string)
    lps = [0] * n
    computeLPSArray(string, n, lps)
    length = lps[n - 1]
    if length > 0 and n % (n - length) == 0:
        return True
    else:
        return False

txt = ["ABCABC", "ABABAB", "ABCDABCD", "GEEKSFORGEEKS", "GEEKGEEK", "AAAACAAAAC", "ABCDABC"]
for t in txt:
    print(isRepeat(t))
