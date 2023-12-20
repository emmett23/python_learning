#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
# def main():
#     print("I am the function")


# main()

# print(main())
# print(main)
# TODO: function that takes arguments
# def func2(arg1, arg2):
#     print(arg1, " ", arg2)


# print(func2("3", "34"))
# TODO: function that returns a value


# def cube(x):
#     return x * x * x


# print(cube(3))
# TODO: function with default value for an argument


# def defaultFunc(num, x=1):
#     result = 1
#     for i in range(x):
#         result = result * num
#     return result


# print(defaultFunc(2, 3))
# print(defaultFunc(3))
# TODO: function with variable number of arguments


def add_to_do(*args):
    result = 1
    for x in args:
        result = result + x
    return result


print(add_to_do(1, 2, 4, 5))
