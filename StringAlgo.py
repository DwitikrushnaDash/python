import itertools
from collections import Counter
from collections import OrderedDict
import sys
# form itertools import permutations
arr = [x for x in range(10)]
print(list(filter(lambda x: x % 2 == 0, arr)))



s = 'badcfeg'
''.join([s[x:x+2][::-1] for x in range(0, len(s), 2)])
# #'abcdef'
print(s)


arr = []
for i in range(0, len(s), 2):
    arr.append(s[i:i+2][::-1])
print(''.join(arr))


str = "India is great"
str_rev = str[::-1]
print(str_rev)

str = "India is great"
arr = str.split(" ")
str_word_rev = ' '.join(reversed(arr))
print(str_word_rev)

print("=========================== Non Consecutive Duplicate =====================")
str = "AAAAABBBCCDD"
tmp = ""
for i in range(0, len(str) - 1):
    if str[i] != str[i + 1]:
        tmp += str[i]

tmp += str[len(str) - 1]
print(tmp)

print()


def maxRepeating(str):
    count = 0
    cur_count = 1

    # Traverse string except
    # last character
    for i in range(len(str)):

        # If current character
        # matches with next
        if (i < len(str) - 1 and str[i] == str[i + 1]):
        # if (str[i] == str[i + 1]):
            cur_count += 1

        # If doesn't match, update result
        # (if required) and reset count
        else:
            if cur_count > count:
                count = cur_count
                res = str[i]
            cur_count = 1
    return res
print("Max repeating char")
print(maxRepeating("AAAAAAAAABBBCCCCCC"))


def get_dup_char(str):
    char_dict = Counter(str)
    for key, val in char_dict.items():
        if val > 1:
            print(key)


def delete_dup_char(str):
    seen = []
    for ch in str:
        if ch not in seen:
            seen.append(ch)
    strtmp = ''.join(seen)

    return strtmp


def check_analgram(str1, str2):
    if len(str1) != len(str2):
        return False
    return (sorted(str1) == sorted(str2))


def permute(str, start, end):

    if start == end:
        print(str)
        return
    strng = list(str)
    for i in range(start, end+1):
        #Swap first character by rest
        strng[start], strng[i] = strng[i], strng[start]
        # recursion for rest of the string
        permute(''.join(strng), start+1, end)
        #Back track --> restore string to original
        strng[start], strng[i] = strng[i], strng[start]


print("================== Permute ==========================")
permute("ABC", 0, 2)


def reverse_rec(str):
    if len(str) == 1:
        return str
    return(reverse_rec(str[1:]) + str[0])


def get_first_non_repeat_char(str):
    word_cnt = OrderedDict()
    for ch in str:
        if ch in word_cnt:
            word_cnt[ch] += 1
        else:
            word_cnt[ch] = 1
    for key, val in word_cnt.items():
        if val == 1:
            return key


def check_string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    tmp = str1 + str1
    if str2 in tmp:
        return True
    else:
        return False
''''
    How do you find the length of the longest substring without repeating characters? (solution)
    Given string str, How do you find the longest palindromic substring in str? (solution)
'''


def max_non_repeating(str):
    # seen = {}
    # maximum_length = 0
    #
    # # starting the inital point of window to index 0
    # start = 0
    #
    # for end in range(len(str)):

    #     # Checking if we have already seen the element or not
    #     if string[end] in seen:
    #         # If we have seen the number, move the start pointer
    #         # to position after the last occurrence
    #         start = max(start, seen[string[end]] + 1)
    #
    #         # Updating the last seen value of the character
    #     seen[string[end]] = end
    #     if maximum_length < end -start + 1:
    #         start_final = start
    #         end_final = end
    #     maximum_length = max(maximum_length, end - start + 1)
    # print(maximum_length)
    # print(string[start_final: end_final+1])
    # return maximum_length
    #
    seen = {}
    start = 0
    max_len = 0

    for end in range(len(str)):
        if str[end] in seen:
            start = max(start, seen[str[end]] + 1)

        seen[str[end]] = end

        if max_len < end - start +1:
            start_final = start
            end_final = end
        max_len = max(max_len, end-start+1)

    res = str[start_final: end_final + 1]
    print(res)
    print(max_len)

print("Max non repeat")
print(max_non_repeating("AABBcdeffGG"))

sys.exit(0)
#=======================================================================================================
get_dup_char("India is great")
str = delete_dup_char("AABCDEFCCDDRTGQ")
print("Delete dup chars: {}".format(str))
print("Check Analgram: str1: {} - str2:{} => status:{}".format("India", "dianI",
                                                               check_analgram('Welcome', 'comeWel')))
# permute("ABC", 0, len("ABC") - 1)

print(reverse_rec("India"))
print("First not repeating char: {}".format(get_first_non_repeat_char("AABBBCDDDCEFG")))