import sys
from collections import defaultdict

def maxSubArraySum(a):
    size = len(a)
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            # print(max_so_far)

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

print(maxSubArraySum([-11, -2, -14, -5, -3, -8, -5]))


def get_max_multiply(arr):
    size = len(arr)
    minMul = arr[0]
    maxMul = arr[0]
    maxVal = arr[0]

    for i in range(1, size):
        if arr[i] < 0:
            tmp = minMul
            maxMul = minMul
            minMul = tmp

        minMul = min(arr[i], minMul * arr[i])
        maxMul = max(arr[i], maxMul * arr[i])
        # Get Max product
        maxVal = max(maxMul, maxVal)
        # Get minium multiply
        # maxVal = min(minMul, maxVal)

    return(maxVal)

arr_mul = [-18, 0, -4, 0]
res = get_max_multiply(arr_mul)
print(res)


# Number of subarrays having sum less than K
def sum_less_k(arr, k):
    res = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum < k:
                res += 1
            else:
                break

    return res


array = [1, 11, 2, 3, 15 ]
k = 10
res = sum_less_k(array, 10)
print("RES: {}".format(res))


def product_less_k(arr, k):
    res = 0

    for i in range(0, len(arr)):
        pdt = 1
        for j in range(i, len(arr)):
            pdt *= arr[j]
            if pdt <= k:
                res += 1
            else:
                break
    return res

array = [1, 11, 2, 3, 15 ]
k = 35
res = product_less_k(array, k)
print("RES: {}".format(res))


def get_max_non_substring(str):
    start = 0
    max_len = 0
    seen = {}

    for end in range(0, len(str)):
        # If we have seen the number, move the start pointer to position after the last occurrence
        if str[end] in seen:
            start = max(start, seen[str[end]] + 1)
            print(start)
        seen[str[end]] = end
        if end - start + 1 > max_len:
            start_final = start
            end_final = end
        max_len = max(max_len, end-start + 1)
    return(str[start_final:end_final+1])

# print("Max Len ", max_len)
# print("Start, End ", start_final, end_final)
# print(str[start_final:end_final+1])
str = "greeksforgreeks"
res = get_max_non_substring(str)
print(res)

def findSubString(str):

    num_distict = len(set(str))
    counter = defaultdict(lambda: 0)
    dist_count = 0
    start = 0
    min_len = len(str)

    for end in range(len(str)):
        counter[str[end]] += 1
        if counter[str[end]] == 1:
            dist_count += 1

        if(dist_count == num_distict):
            while(counter[str[start]] > 1):
                counter[str[start]] -= 1
                start += 1

            len_window = end - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start

    return str[start_index: start_index + min_len]



res = findSubString("AABBCDAA")
print(res)
