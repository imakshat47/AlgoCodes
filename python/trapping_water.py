def maxWater(arr):
    st = []
    res = 0

    for i in range(len(arr)):
        while st and arr[st[-1]] < arr[i]:
            pop_height = arr[st.pop()]

            if not st:
                break

            distance = i - st[-1] - 1
            water = min(arr[st[-1]], arr[i])
            water -= pop_height
            res += distance * water
        st.append(i)

    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))
