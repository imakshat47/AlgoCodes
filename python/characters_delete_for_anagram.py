def remAnagram(s1, s2):
    cnt = [0] * 26

    for ch in s1:
        cnt[ord(ch) - ord('a')] += 1

    for ch in s2:
        cnt[ord(ch) - ord('a')] -= 1

    ans = sum(abs(x) for x in cnt)
        
    return ans

if __name__ == "__main__":
    str1 = "bcadeh"
    str2 = "hea"
    print(remAnagram(str1, str2))
