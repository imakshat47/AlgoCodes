def findMaxAvgSubarray(arr, n, k):
    if n < k:
        return 0

    res_index = 0
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum
            res_index = i - k + 1

    print("Subarray between [", res_index, ",", (res_index + k - 1), "] has maximum average")

arr = [3, 7, 90, 20, 10, 50, 40]
k = 3
n = len(arr)
findMaxAvgSubarray(arr, n, k)
