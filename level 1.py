
n = input("Enter the input: ")

# Question: 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# for i in range(2000,3200):
#     if i%7 == 0 and i%5 != 0:
#         print(i,end=",")



# Question: 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# def fact(x):
#     if x == 0:
#         return 1
#     f = 1
#     for i in range(1,x+1):
#         f = 0
#     return f
#
# x=int(input("enter the number: "))
# print (fact(x))


# Question 3
# Level 1
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# n = int(input("Enter the number: "))
# dict = {}
# for i in range(1,n+1):
#     dict.update({i:i**2})
# print(dict)


# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# n = input("Enter the number: ")
# n = n.split(",")
# n_list = list(n)
# print(n_list)
# n_tuple = tuple(n_list)
# print(n_tuple)


# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class Problem:
#     def __int__(self):
#         self.string = ""
#
#     def get_string(self):
#         self.string = input("Enter the string: ")
#
#     def print_string(self):
#         print(self.string.upper())
#
# test = Problem()
# test.get_string()
# test.print_string()


# Question 6
# Level 2
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# C = 50
# H = 30
# D = input("Enter the values: ")
# D_list = D.split(",")
#
# for i in range(0,len(D_list)):
#     Q = (2 * C * int(D_list[i])/H)**0.5
#     D_list[i] = round(Q)
# print(D_list)

# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# n = input("Enter two numbers: ")
# n = n.split(",")
#
# I = int(n[0])
# J = int(n[1])
# column = [[0 for i in range(0,J)] for i in range(0,I)]
#
# for i in range(0,I):
#     for j in range(0,J):
#         column[i][j] = i*j
#
# print(column)


# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


# n = input("Enter the words: ")
# n = n.split(',')
# n.sort()
# print(n)

# Question 9
# Level 2
#
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# n = input("Enter the words: ")
# print(n.upper())

# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# n = n.split(" ")
#
# for i in range(0,len(n)-1):
#     try:
#         temp = n[i]
#         n.remove(n[i])
#
#         if temp in n:
#             pass
#         else:
#             n.append(temp)
#     except:
#         break
# print(sorted(n))

# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# n = n.split(",")
# result = []
# for i in range(0,len(n)):
#     n[i] = int(n[i],2)
#
#     if n[i]%5 == 0:
#
#         result.append(bin(n[i])[2:])
#
# print(result)