print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisors(num):
    div_list = []
    for i in range(1, num+1):
        if num % i == 0:
            div_list.append(i)
    return div_list
    
print(divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(num1, num2):
    if num1 in divisors(num2) or num2 in divisors(num1):
        return True
    else:
        return False

print(factor(5, 10))
print(factor(5, 11))



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


# A2a:

def alphabet_index(char):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    index = alphabet.index(char.lower()) + 1
    return index

# def alphabet_index(char):
#     for i, letter in enumerate(alphabet):
#         if letter == char:
#             index = i + 1
#     return index
    

print(alphabet_index('e'))
        

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def name_ID(name):
    indexes_list = []
    for char_n in name:
        indexes_list.append(str(alphabet_index(char_n)))
    return ''.join(indexes_list)

print(name_ID("Michail"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def name_pass(name):
    sum = 0
    for i in name_ID(name):
        sum += int(i)
    return int(name_ID(name)) - sum

        
print(name_pass("michail"))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime():
    number = int(input("Please enter a number: "))
    if len(divisors(number)) > 2:
        return False
    return True


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def is_prime_nr():
    try:
        number = int(input("Enter a number: "))
        if len(divisors(number)) > 2:
            return False
        return True
    
    except Exception:
        print("Invalid input. Please enter a valid integer.")
        
    

print(is_prime_nr())

# -------------------------------------------------------------------------------------- #






