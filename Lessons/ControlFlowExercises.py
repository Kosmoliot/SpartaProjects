# print("\nQ1a\n")
# # Q1a: Print only the first 5 numbers in this list
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# # A1a:
# print(x[:5])

# print("\nQ1b\n")
# # Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# # A1b:
# for i in x:
#     if i % 2 == 0:
#         print(i)


# print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# # A1c:
# for i in x[0:5]:
#     if i % 2 == 0:
#         print(i)

# -------------------------------------------------------------------------------------- #

# print("\nQ2a\n")
# # Q2a: from the list of names, create another list that consists of only the first letters of each first name
# # e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# # A2a:
# name_init_list = []
# for name in names:
#     name_init_list.append(name[0])
# print(name_init_list)


# print("\nQ2b\n")
# # Q2b: from the list of names, create another list that consists of only the index of the space in the string
# # HINT: use your_string.index("substring")
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# # A2b:
# space_index_list = []
# for name in names:
#     space_index = name.index(' ')
#     space_index_list.append(space_index)
# print(space_index_list)



# print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
# name_init_list = []
# for name in names:
#     name_init = name.split(' ')
#     name_init_list.append(name_init[0][0] + ' ' + name_init[1][0])
# print(name_init_list)

# # -------------------------------------------------------------------------------------- #

# print("\nQ3a\n")
# # Q3a: Here is a list of lists, print only the lists which have no duplicates
# # Hint: This can be easily done by using sets as a set does not contain duplicates
# list_of_lists = [[1,5,7,3,44,4,1],
#                  ["A", "B", "C"],
#                  ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
#                  ["one", "Two", "Three", "Four"]]


# # A3a:
# for list in list_of_lists:
#     if len(list) == len(set(list)):
#         print(list)
            

# # -------------------------------------------------------------------------------------- #

# print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
# cycle = True

# while cycle:
#     user_input = input("Enter a number greater than 100: ")
#     if int(user_input) >= 100:
#         print(f"Number you have entered is: {user_input}")
#         cycle = False
#     else:
#         print("Incorrect input, please try again!")
        
        
        
# print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
# cycle = True

# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
            
    
# while cycle:
#     user_input = int(input("Enter a number greater than 100: "))
#     if user_input >= 100 and is_prime(user_input):
#         print(f"Number you have entered is: {user_input} and it's a Prime number")
#         cycle = False
        
#     elif user_input >= 100:
#         print(f"Number you have entered is: {user_input}")
#         cycle = False
        
#     else:
#         print("Incorrect input, please try again!")




