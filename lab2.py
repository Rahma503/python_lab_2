# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
# # Expected Output: 15

# op = input("please enter operation add sub div multi : ").lower()
# n1=int(input("plesae enter num 1 : "))
# n2=int(input("plesae enter num 2 : "))
# match op:
#     case "add" :
#         print("summtion is ",n1+n2)
#     case "sub" :
#         print("subtraction is  ",n1-n2)
#     case "multi" :
#         print("multiplication is ",n1*n2)
#     case "div" :
#         if n2==0:
#             print("error can't devide on 0")
#         else :

#             print("division is ",n1/n2)
#     case _:
#         print("invalid input ")

# ================================================================================


# Question 2 :
# Write a program to filter out even numbers from a list and 
# count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9], Count = 5

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = [num for  num in range(len(numbers)) if num % 2 != 0]  
# count = len(res)

# print(f"{res = }  {count = }")


# ================================================================================
#   Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# Expected Output: "Valid Password"
# password = input("Enter password : ")

# if len(password) >= 8:
#     flag1=False
#     flag2=False
#     for char in password:
#         if char.isupper():
#             flag1=True
        
#         if char.isdigit():
#             flag2=True
#     if flag1 and flag2 :
#         print("Valid password")
#     else:
#         print("inValid password")

# else :
#     print("inValid password")

# ======================================================

# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# dic4= dic1 | dic2 | dic3
# print(f"{dic4 = }")


# =====================================================
# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu

# name = input("enter string : ")

# l = list(name)

# longest =current= l[0] 
# for i in range(1,len(l)):
#     if l[i] >=l[i-1]:
#         current+=l[i]
#     else:
#         if len(current) > len(longest):
#             longest=current
#         current=l[i]

# print(f"{longest = }")

# ===========================================
import re 
email = input("Enter email: ")

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
        
        print("Valid email")
else:
        print("inValid email")

