import sys
'''

O(n^2) time and O(1) space algorithm ( without any workarounds and hanky-panky stuff! )

Rotate by +90:

    Transpose
    Reverse each row

Rotate by -90:

Method 1 :

    Transpose
    Reverse each column

Method 2 :

    Reverse each row
    Transpose

Rotate by +180:

Method 1: Rotate by +90 twice

Method 2: Reverse each row and then reverse each column (Transpose)

Rotate by -180:

Method 1: Rotate by -90 twice

Method 2: Reverse each column and then reverse each row

Method 3: Rotate by +180 as they are same
share improve this answer follow
edited Dec 22 '16 at 10:14
community wiki


'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# matrix = [[col for col in range(5)] for row in range(2)]
matrix1 = [[0] * 3 for i in range(5)]
print(matrix1)

trnsp = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]
print(trnsp)

for row in range(len(trnsp)):
    trnsp[row].reverse()

for row in trnsp:
    print(row)

col_cnt = len(matrix[0])
print("col_cnt:{}".format(col_cnt))

for col in range(col_cnt):
    start = 0
    end = len(matrix) - 1
    while end > start:
        matrix[start][col], matrix[end][col] = matrix[end][col], matrix[start][col]
        start += 1
        end -= 1

print(matrix)
#Transpose
# res = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         res[j][i] = matrix[i][j]
#
# print(res)

# for r in matrix:
#     print(r)
# print("=======================================")
# result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#
# for r in result:
#     print(r)


search = [[10, 20, 30],
          [15, 21, 31],
          [17, 23, 43]]

val = 21
row = 0
col = len(search[0]) - 1
while row < len(search) and col >= 0:
    if search[row][col] == val:
        print("Exists")
    if search[row][col] > val:
        col -= 1
    else:
        row += 1

arr = [1, 5, 4, 8, 9, 6, 7, 2, -7, 13]

def small_2_small(arr):
    if len(arr) < 2:
        print("Less than 2 elements")
        return
    first = second = sys.maxsize
    for i in range(0, len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        if arr[i] < second and arr[i] != first:
            second = arr[i]
    print("(Smallest:{}, Second_Smallest:{})".format(first, second))

small_2_small(arr)


def get_pair_with_sum(arr, sum):
    if len(arr) <= 1:
        return False
    total = {}
    for i in range(0, len(arr)):
        if (sum - arr[i]) in total:
            print("({},{})".format(arr[i], sum - arr[i]))
        else:
            total[arr[i]] = 1

get_pair_with_sum(arr, 6)


def find3Numbers(arr, sum):
    if len(arr) < 3:
        return
    size = len(arr)
    for i in range(0, size -2):
        for j in range(i+1, size - 1):
            for k in range(j+1, size):
                if(arr[i] + arr[j] + arr[k] == sum):
                    print("({}, {}, {})".format(arr[i], arr[j], arr[k]))

find3Numbers(arr, 20)

def get_triplet(arr, sum):
    arr.sort()

    for i in range(0, len(arr) - 2):
        first = i+1
        last = len(arr) - 1
        while(first < last):
            if(arr[i] + arr[first] + arr[last] == sum):
                print("({}, {}, {})".format(arr[i], arr[first], arr[last]))
            if arr[i] + arr[first] + arr[last] < sum:
                first += 1
            else:
                last -= 1
arr1 = [1, 4, 45, 6, 10, 8]
sum = 22
get_triplet(arr1, sum)


def get_triplet_hash(arr, sum):
    for i in range(0, len(arr) -1):
        cur_sum = sum - arr[i]
        total = {}
        for j in range(i+1, len(arr)):
            if (cur_sum - arr[j]) in total:
                print("({}, {}, {})".format(arr[i], arr[j], cur_sum - arr[j]))
            else:
                total[arr[j]] = 1

print("================================")


def remove_duplicate(arr):
    arr.sort()
    print(arr)
    j = 0
    tmp = []
    # 1 1 2 2 3 5
    for i in range(0, len(arr) - 1):
        print(i)
        if arr[i] != arr[i+1]:
            tmp[j] = arr[i]
            j += 1

    tmp[j] = arr[len(arr) - 1]

    print(tmp)


def binary_search(arr, val):
    # arr.sort()

    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        print(mid)
        if val == arr[mid]:
            return True
        if val > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False

arr = [1, 3, 5, 7, 14, 15, 47, 75]
if binary_search(arr, 5):
    print("Data exists")
else:
    print("Data does not exist")

# remove_duplicate(arr2)

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tmp = mat
print("================================")
# trans = []
# for row in range(0, len(mat)):
#     for col in range(0, len(mat[0])):
#         tmp = mat[row][col]
#         mat[row][col] = mat[col][row]
#         trans[col][row] = tmp
#         # mat[col][row], mat[row][col] = mat[row][col], mat[col][row]

mat = [[mat[col][row] for col in range(0, len(mat))] for row in range(0, len(mat[0]))]
print("=============Transpose==================")
for i in range(0, len(mat)):
    print(mat[i])
print("========================================")
for row in range(len(mat)):
    start = 0
    last = len(mat) - 1
    while(start <= last):
        mat[row][start], mat[row][last] = mat[row][last], mat[row][start]
        start += 1
        last -= 1

for i in range(0, len(mat)):
    print(mat[i])
print("================================")


# -90
#Reverse each row then transpose
for row in range(0, len(tmp)):
    start = 0
    last = len(mat[0]) - 1
    while(start <= last):
        tmp[row][start], tmp[row][last] = tmp[row][last], tmp[row][start]
        start += 1
        last -= 1
tmp = [[tmp[col][row] for col in range(0, len(tmp))] for row in range(0, len(tmp[0]))]

for row in range(0, len(tmp)):
    print(tmp[row])

# mat = [
#     [1, 2]
# ]
# tmp = [[3, 5, 6],
#        [4, 7, 9]]
res = [[0] * len(tmp[0]) for row in range(0, len(tmp))]


print("============== Multiply =====================")
for i in range(0, len(mat)):
    for j in range(0, len(tmp[0])):
        res[i][j] = 0
        for k in range(0, len(tmp)):
            res[i][j] += mat[i][k] * tmp[k][j]
for row in res:
    print(row)

print("============= Diagonal ===================")
for row in range(0, len(mat)):
    for col in range(0, len(mat[0])):
        if row == col:
            print(mat[row][col])

print("============= Lower Diagonal ===================")
for row in range(0, len(mat)):
    for col in range(0, len(mat[0])):
        if col <= row:
            print(mat[row][col])

print("====================== Count Neg Numbers ===========")
mat = [
      [-3, -2, -1,  1],
      [-2,  2,  3,  4],
      [4,   5,  7,  8]
    ]
start = 0
last = len(mat) - 1
count = 0
while(start < len(mat) and last >=0):
    if mat[start][last] < 0:
        count += (last + 1)
        start += 1
    else:
        last -= 1
print(count)

print("============== Count Zero ===============")
mat = [[0, 0, 0, 0, 1],
       [0, 0, 0, 1, 1],
       [0, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]]
start = 0
last = len(mat) - 1
count = 0
while start < len(mat) and last >=0:
    if mat[start][last] == 0:
        count += (last + 1)
        start += 1
    else:
        last -= 1
print(count)

print("======================= Search =======================")
mat = [
      [-3, -2, -1,  1],
      [-2,  2,  3,  4],
      [4,   5,  7,  8]
    ]

def search(mat):
    data = 7
    row = 0
    col = len(mat) - 1
    while row < len(mat) and col >= 0:
        if mat[row][col] == data:
            print("Exists")
            return True
        if mat[row][col] < data:
            row += 1
        else:
            col -= 1
    return False

if search(mat):
    print("Data Exists")
else:
    print("Data does not Exists")

print("============== Mat Multiply ===============")
row = [[0] * len(tmp[0]) for i in range(0, len(mat))]
# res = [[0] * len(tmp[0]) for row in range(0, len(tmp))]
for i in range(0, len(mat)):
    for j in range(0, len(tmp[0])):
        row[i][j] = 0
        for k in range(0, len(tmp)):
            row[i][j] += mat[i][k] * tmp[k][j]

for row_data in row:
    print(row_data)