# # Statistically typed
# # C, C++, Java
# # int a=10;
# # char c='a'

# # Dynamically typed ->
# # Literals
# import math
# a = 10  # int
# print(a)
# a = 'x'  # char
# print(a)
# a = "abc"  # string
# print(a)
# a = True  # boolean
# print(a)
# # immutable - we cant change the value once it is assign

# # concatenation
# print("abc"+" " + "efg")
# x = "abc"
# print(x)
# x = "abc" + "fdg"
# print(x)

# # k= input("Give a number ")
# # print(k)
# # print(int(k) + 10)

# # Type conversions
# print(int("123"))
# print(str(123) + "abc")
# i = 10
# print(i > 10)

# # Operands
# print(1+2)
# print(1*2)
# print(10/3)  # decimal
# print(10//3)  # round near the next digit
# print(10 % 3)  # reminder
# print(10**2)  # power

# print(math.floor(3.14))
# print(math.ceil(3.14))
# print(math.sqrt(100))
# print(math.pow(2, 100))

# # give 2 inputs
# # x= input("1st number")
# # y= input("2nd number")
# # print(int(x)+int(y))
# # print(int(x)-int(y))
# # print(int(x)*int(y))

# # print(int(input("first number: "))+ int(input("second number:")))

# a = 10
# print(a > 10)
# print(a >= 10)
# print(a < 10)
# print(a == 10)
# print(a != 10)

# a, b = 10, 20
# print(a < b)

# # conditional statements
# if a >= 10:
#     print(a)
# elif a >= 20:
#     print(a)
# else:
#     print(b)

# # lists -> arrays -> dynamic arrays
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arr)
# arr.append(10)
# print(arr)
# arr.pop()
# print(arr)
# arr.reverse()
# print(arr)
# arr.remove(1)
# print(arr)
# arr1 = [10, 20, 30, 40, 50, 60, 7]
# print(arr+arr1)

# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(tuple)
# tuple1 = (20, 19)
# tuple += tuple1
# print(tuple)

# # itself will increase the value
# for x in tuple:
#     print(x)

# for i in range(10, 2):
#     print(i)

# # k=1
# # while k<11:
# #     print(k)
# #     k+=1

# #
# #
# # arr1=[10,20,30,40,50,60,7]
# # arr2=[100,90,80,70,60,50,40]
# # for x,y in  enumerate(arr1):
# #     print(x,y)

# print(math.fabs(-200))
# print(math.log(100))
# print(math.log10(1000))


# x = 10
# y = 10
# z = 10
# print(id(x))
# print(id(y))
# print(id(z))


# print(ord('%'))

# print(len("abcdefgh"))  # 8
# print(len([1, 2, 3, 4, 5]))  # 5
# print(len((1, 2, 3, 4, 5)))  # 6
# print(type(([1, 2, 3, 4, 5])))  # list
# arr = [1, 2, 3, 4, 5]
# print(arr[0])

# string = "hello world"
# print(string[0:5])  # hello
# print(string[6:11])  # world
# print(string[2])  # d

# list = [(1, 2), (2, 3)]
# print(list)

# str = ["Hello", "world", "is", "great"]
# str = "hello world"
# str_new = "-".join(str)
# print(str_new)
# print(str)


# Falsy values
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))

# Truthy values
# print(bool(1))
# print(bool("abc"))
# print(bool([1, 2, 3]))
# print(bool((1, 2)))
# print(bool({1: 'a'}))

# a = ""
# list = []

# if list:
#     print("Hello")
# else:
#     print("World")

# n = 10
# arr = [1] * n
# print(arr)  # [1,1,1,1,1,1,1,1,1,1]


# a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)


# nums = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(nums)):
#     print(nums[i])

# for n in nums:
#     print(n)

# for i, k in enumerate(nums):
#     print(i, k)


# Multiple arrays
from typing import List
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, 2, 3, 4, 5, 6, 3]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)

# nums2.sort()
# print(nums2)
# nums2.count(3)
# print(nums2.count(3))

# if 10 in nums2:
#     print("Found")
# else:
#     print("Not Found")

# str = " Hello world "
# print(str.strip())

# arr = ["bob", "alice", "jane", "doe"]
# arr.sort()
# print(arr)

# arr.sort(key=lambda x: len(x))
# print(arr)

# i =0
# arr = ["a" for i in range(5)]
# print(arr)

dict_example = {}
dict_example['alice'] = 10
dict_example['bob'] = 20
print(dict_example)  # {'alice': 10, 'bob': 20}

nums = [1, 2, 3, 4, 5, 6]
squared = map(lambda x: x**2, nums)
print(list(squared))  # [1, 4, 9, 16, 25, 36]
filtered = filter(lambda x: x % 2 == 0, nums)
print(list(filtered))  # [2, 4, 6]


def double(X):
    return X * 2


doubled = map(double, nums)
print(list(doubled))  # [2, 4, 6, 8, 10, 12]
filtered_even = filter(lambda x: x % 2 == 0, nums)
print(list(filtered_even))  # [2, 4, 6]
