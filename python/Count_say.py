def nextTerm(prev):
    curr = ""
    count = 1
    
    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            curr += str(count) + prev[i - 1]
            count = 1
    
    curr += str(count) + prev[-1]
    
    return curr

def countAndSay(n):
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    
    return nextTerm(prev)

if __name__ == "__main__":
    n = 5
    print(countAndSay(n))
