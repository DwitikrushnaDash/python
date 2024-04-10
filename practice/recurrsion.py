def if_sorted(arr, indx=0):
    if indx == len(arr) -1:
        return True
    return arr[indx] <= arr[indx+1] and if_sorted(arr, indx+1)


arr_test = [1,5, 5, 9]
ret = if_sorted(arr_test, 0)
print(ret)


def if_present(arr, target, indx):
    if indx == len(arr):
        return False
    return arr[indx] == target or if_present(arr, target, indx+1)


arr_test = [1,22,100,5,34,79,100,45,76]
ret = if_present(arr_test, 76, 0)
print(ret)


#Get index where element is present
def get_pos(arr, target, indx):
    if indx == len(arr):
        return -1
    if arr[indx] == target:
        return indx
    return(get_pos(arr, target, indx+1))


ret = get_pos(arr_test, 12, 0)
print(ret)


# Find all pos of an element
def find_all(arr, target, res=[], indx=0):
    if indx == len(arr):
        return res
    if arr[indx] == target:
        res.append(indx)
    return(find_all(arr, target, res, indx+1))


ret = find_all(arr_test, 100)
print(ret)


def find_all_2(arr,target, indx=0):
    res = []
    if indx == len(arr):
        return res
    if arr[indx] == target:
        res.append(indx)
    tmp_arr = find_all_2(arr, target, indx+1)
    tmp_arr.extend(res)
    return tmp_arr


ret = find_all_2(arr_test, 100)
print(ret)

arr_test1 = [2, 4, 7, 5, 9]


# def get_subset(arr, target, indx=0):
#     res = []
#     if indx == len(arr):
#         return res
#     if target == 0:
#         return res
#
#     if target >= arr[indx]:
#         tmp_arr = get_subset(arr, target-arr[indx], indx+1)
#         tmp_arr.extend(res)
#         tmp_arr.pop()
#     tmp_arr = get_subset(arr, target, indx+1)
#     tmp_arr.extend(res)
#     return tmp_arr


# ret = get_subset(arr_test1, 7)
# print(ret)

