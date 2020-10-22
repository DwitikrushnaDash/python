from itertools import permutations as pm
# Subarray with given sum
arr = [10, 2, 5, 20, 13, 34]
total = 50


def get_subarray_with_given_sum(arr, total):
    start = 0
    cur_sum = 0
    size = len(arr)

    print(total)
    for i in range(size):
        cur_sum += arr[i]

        while(cur_sum > total):
            cur_sum -= arr[start]
            start += 1

        if(cur_sum == total):
            return (start, i)


(start, end) = get_subarray_with_given_sum(arr, total)
print(start, end)

def get_subarry_with_sum_havine_neg(arr, total):

    map = {}
    cur_sum = 0
    size = len(arr)
    for i in range(size):
        cur_sum += arr[i]
        if cur_sum == total:
            print(0, i)
        if cur_sum - total in map:
            print(map[cur_sum - total] + 1, i)
        map[cur_sum] = i

arr_neg = [7, 5, 2, -2, 4]
total = 9

get_subarry_with_sum_havine_neg(arr_neg, total)


def get_triplet_with_sum(arr, total):
    sorted(arr)
    for i in range(len(arr) -1, 0, -1):
        j = 0
        k = i -1
        while(j < k):
            if(arr[j] + arr[k] == arr[i]):
                print(arr[j], arr[k], arr[i])
            elif(arr[j] + arr[k] > arr[i]):
                k -= 1
            else:
                j += 1


def merge_two_sorted_array(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)

    i = j = 0
    tmp = []

    while(i < size1 and j < size2):
        if arr1[i] < arr2[j]:
            tmp.append(arr1[i])
            i += 1
        else:
            tmp.append(arr2[j])
            j += 1

    while(i < size1):
        tmp.append(arr1[i])
        i += 1

    while(j < size2):
        tmp.append(arr2[j])
        j += 1

    print("Merged list: ", tmp)


arr1 = [2, 5, 8, 9, 10]
arr2 = [1, 3, 4]
merge_two_sorted_array(arr1, arr2)


def arrange_max_min_alternate(arr):
    start = 0
    end = len(arr) - 1
    flag = True
    tmp = []
    for i in range(len(arr)):
        if flag:
            tmp.append(arr[end])
            end -= 1
        else:
            tmp.append(arr[start])
            start += 1
        flag = bool(1 - flag)

    for i in range(len(tmp)):
        arr[i] = tmp[i]

    print("Alternate Max- Min: ", arr)


arr = [1, 7, 9, 12, 13]
arrange_max_min_alternate(arr)


def reverse_arr_in_group(arr, k):
    for i in range(0, len(arr), k):
        start = i
        end = i + k - 1
        while(start < end and end < len(arr)):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    print("Reverse in group: ", arr)


arr = [1,2,3,4,5,6,7,8,9,10]
k = 1
reverse_arr_in_group(arr, k)


def zig_zag_arrange(arr):
    # If a[i] < a[i+1]  ===> check for <
    flag = True
    for i in range(len(arr) - 1):
        # Check for arr[i] < arr[i+1]
        if flag:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # Check for arr[i] > arr[i+1]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1 - flag)

    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zig_zag_arrange(arr)


arr = [54, 546, 548, 80]
tmp = []
for i in pm(arr):
    print(i)
    tmp.append("".join(map(str, i)))
print(max(tmp))