import sys
strng = "AADOBECODEBANC"
substrng = "ABC"


def min_substring_containing_all_chars(strng, substrng):
    count = len(set(substrng))
    min_len = len(strng)
    found = False
    seen = {}
    for i in substrng:
        seen[i] = seen.get(i, 0) + 1

    start, end = 0, 0
    while end < len(strng):
        if strng[end] in seen:
            seen[strng[end]] -= 1
            if seen[strng[end]] == 0:
                count -= 1

        while count == 0:
            if strng[start] in seen:
                seen[strng[start]] += 1
                if seen[strng[start]] > 0:
                    count += 1
            if min_len > end - start + 1:
                min_len = end - start + 1
                final_start = start
                final_end = end
                found = True

            start += 1

        end += 1
    if found:
        print(strng[final_start:final_end + 1])


# minimum_sum_subarray_of_size(arr, win_size)


# Longest substring with all distinct characters using a sliding window
def longest_substr_with_all_distinct_chars(strng):
    start, end = 0, 0
    seen = {}
    max_len = -1

    while end < len(strng):
        if strng[end] in seen:
            if max_len < end-start+1:
                max_len = end-start+1
                final_start = start
                final_end = end
                # print(final_start, final_end)
            start = max(start, seen[strng[end]]+1)
        seen[strng[end]] = end
        end += 1
    print(strng[final_start:final_end])


strng = "findlongestsubstring"
longest_substr_with_all_distinct_chars(strng)
strng = "longestsubstr"
longest_substr_with_all_distinct_chars(strng)


# Find all substrings of a string that are a permutation of another string
def find_substring_perm_of_target(strng, target):
    if len(target) > len(strng):
        print("NULL - Not available")
    start, end = 0, 0
    len_target = len(target)
    seen = {}
    for ch in target:
        seen[ch] = seen.get(ch, 0) + 1
    # counter = len_target
    tmp = {}
    while end < len(strng):
        tmp[strng[end]] = tmp.get(strng[end], 0) + 1
        if end-start+1 == len_target:
            if tmp == seen:
                print(strng[start:end+1])
            tmp[strng[start]] = tmp[strng[start]] - 1
            if tmp[strng[start]] == 0:
                del(tmp[strng[start]])
            start += 1
        end += 1


strng = "XYXZXZYZXXYZ"
target = "XYZ"
find_substring_perm_of_target(strng, target)


def count_distinct_chars_in_substr_of_size_target(strng, target):
    start, end = 0, 0
    count = 0
    seen = {}

    while end < len(strng):
        if strng[end] not in seen:
            count += 1
        seen[strng[end]] = seen.get(strng[end], 0) + 1

        if end-start+1 == target:
            print(strng[start:end+1], "Unique chars: ", count)
            seen[strng[start]] = seen[strng[start]] - 1
            if seen[strng[start]] == 0:
                count -= 1
                del(seen[strng[start]])
            start += 1
        end += 1


strng = "ABCACXYBC"
target = 3
# count_distinct_chars_in_substr_of_size_target(strng, target)


def longest_substr_of_continuos_zero_and_ones(arr):
    end = 0
    tmp = 0
    seen = {}
    max_len = 0

    # Convert all zero's to -1
    while end < len(arr):
        if arr[end] == 0:
            tmp += -1
        else:
            tmp += 1

        if tmp in seen:
            if max_len < end-seen[tmp]:
                max_len = end-seen[tmp]
                final_start = seen[tmp] + 1
                final_end = end

        seen[tmp] = end
        end += 1

    print(arr[final_start:final_end+1])


arr = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
longest_substr_of_continuos_zero_and_ones(arr)


# min_substring_containing_all_chars(strng, substrng)


def min_subarray_sum_target(arr, target):
    temp_sum = 0
    start, end = 0, 0
    min_len = len(arr)
    boolExist = False

    while end < len(arr):
        temp_sum += arr[end]
        # end += 1
        while temp_sum > target:
            temp_sum -= arr[start]
            start += 1
        if temp_sum == target:
            boolExist = True
            if min_len > end-start+1:
                final_start = start
                final_end = end
                min_len = end-start+1
        end += 1
    if boolExist:
        print(arr[final_start:final_end+1])
    else:
        print("Sub array does not exist")


arr = [5, 4, -1, 1, 1, -1, 4]
target = 3
min_subarray_sum_target(arr, target)


arr = [10, 4, 2, 5, 6, 3, 8, 1]
win_size = 3


def minimum_sum_subarray_of_size(arr, win_size):
    min_sum = sys.maxsize
    start, end = 0, 0
    temp_sum = 0
    while end < len(arr):
        temp_sum += arr[end]
        if end-start+1 == win_size:
            if min_sum > temp_sum:
                final_start = start
                final_end = end
                min_sum = temp_sum
                print(final_start, final_end, min_sum)
            temp_sum -= arr[start]
            start += 1
        end += 1
    print(arr[final_start:final_end+1], min_sum)


def find_smallest_subarr_sum_gt_num(arr, target):
    start, end = 0, 0
    tmp = 0
    min_len = len(arr)
    boolExist = False

    while end < len(arr):
        tmp += arr[end]
        while tmp > target:
            if min_len > end-start+1:
                boolExist = True
                final_start = start
                final_end = end
            tmp -= arr[start]
            start += 1
        end += 1

    if boolExist:
        print(arr[final_start:final_end+1])
    else:
        print("Subarr not exists")


arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 21
# find_smallest_subarr_sum_gt_num(arr, target)

