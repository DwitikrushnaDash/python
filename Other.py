# import copy
# import re
# x = [1, 2, 3, 5]
# y = copy.deepcopy(x)
# y[0] = 5
# print(x)
#
#
# # def find_ternary(num):  #2
# #     qua = num / 3
# #     rmd = num % 3
# #     if qua == 0:
# #         return ""
# #     return(find_ternary(int(qua)) + str(int(rmd)))
# #
# #
# # number = int(input("Enter a number : ")) #1
# # print(find_ternary(number))
# #
dict_first = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
dict_second = {'One':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10}

dict_first.update(dict_second)
for key, val in dict_first.items():
    print(key, val)

# # #==================================================
# # for tmp in reversed(x):
# #     print(tmp)
# #
# # #=================================================
#
# names = ['Bob Samson', 'Bob Cristo', 'Michel Simons', 'John Smith']
# for tmp in sorted(names, key=lambda name: name.split()[-1].lower()):
#     print(tmp)
# #================================================
#
# '''
#     (lambda x, y, z: x + y + z)(1, 2, 3)
#     6
#     >>> (lambda x, y, z=3: x + y + z)(1, 2)
#     6
#     >>> (lambda x, y, z=3: x + y + z)(1, y=2)
#     6
#     >>> (lambda *args: sum(args))(1,2,3)
#     6
#     >>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
#     6
#     >>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
# '''
# ############ Decorator without args ###############################
#
#
# def func_to_be_decorated():
#     print("Inside - To be decorated")
#
#
# def func_decorator(func):
#     def inner():
#         print("Inside Decorator")
#         func()
#     return(inner)
#
#
# func = func_decorator(func_to_be_decorated)
# func()
# import sys
# # sys.exit()
# ptn = re.compile(r'(?:25[0-5])|24[0-9]|[01]?[0-9][0-9]?\.){3}(?:25[0-5]|24[0-9]|[01]?[0-9][0-9]?)')
# # ptn = re.compile(r'(?:25[0-5]|24[0-9]|[01]?[0-9][0-9]?\.){3}(?:25[0-5]|24[0-9]|[01]?[0-9][0-9]?)')
# # y = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', "IP address 10.20.40.30 abc 11.22.33.44")
# x = ptn.findall("IP address 10.20.40.30 abc 11.22.33.44")
# print("IP adress")
# print(x)

def func_decorator_with_args(func):
    def inner(*args, **kwargs):
        print("Deco with args")
        ret = func(*args, **kwargs)
        return(ret)
    return(inner)

@func_decorator_with_args
def func_to_be_decorated_with_args(a, b):
    if b > a:
        return b
    else:
        return a

# func_with_args_test = func_decorator_with_args(func_to_be_decorated_with_args)
# ret = func_with_args_test(25, 35)
ret = func_to_be_decorated_with_args(25, 35)
print(ret)

ret1 = func_to_be_decorated_with_args(20, 12)
print(ret1)
import sys
sys.exit()

'''
    ^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.↵
    (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.↵
    (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.↵
    (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
'''