import re
def func_to_be_decorated():
    print("Inside - To be decorated")


def func_decorator(func):
    def inner():
        print("Inside Decorator")
        func()
    return(inner)


func = func_decorator(func_to_be_decorated)
func()

def func_decorator_with_args(func):
    def inner(*args, **kwargs):
        print("Deco with args")
        if args[0] < 0:
            print("Enter positive numbers")
            return 0
        else:
            #As function returns the value we used return statement
            return(func(*args, **kwargs))
            # If function does not return any value - simply call it
            # func(*args, **kwargs)
        # func(*args, **kwargs)
    return(inner)


@func_decorator_with_args
def func_to_be_decorated_with_args(a, b):
    if b > a:
        return b
        # print(b)
    else:
        return a
        # print(a)

func_with_args_test = func_decorator_with_args(func_to_be_decorated_with_args)
ret = func_with_args_test(-25, 35)
print(ret)

ret1 = func_to_be_decorated_with_args(20, 12)
print(ret1)


ptn = re.compile(r'((25[0-5]|24[0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|24[0-9]|[01]?[0-9][0-9]?)')
x = ptn.search("IP address 10.20.40.30 abc 11.22.33.44")
print(x.group())
