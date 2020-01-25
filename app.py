# luckyNum = [4, 5, 6, 16]
# friends = ["Jon", "Lee", "Mike"]
# convert_friends = [i.lower() for i in friends]
# print(convert_friends.index("mike"))

# coordinates = [(4, 5, 6, 7), (8,7)]
# print(coordinates[1])

# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age))
# say_hi("Mike", "35")
# say_hi("Lee", 33)


#
# def cube(num):
#     return num * num * num
#
# result = cube(4)
# print(result)

# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are neither tall nor a male")

#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(3, 4, 5))

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions.get("Mic", "Not a valid key"))
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with loop")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, YOU LOSE!")
# else:
#     print("You win!")

# friends = ["Jim", "Karen", "Kevin", "me"]
# # len(friends)
# for i in range(5):
#     if i == 0:
#         print("first iteration")
#     else:
#         print("Not first")

# ###################  # DICTIONARIES, EXPONENTS,**********
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)

# Giraffe Language
# vowels -> g
# -----------
#
# dog -> dgg
#
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#
#         else:
#             translation += letter
#     return translation
#
# print(translate((input("enter a phrase: "))))

# Invalid input except and try *************
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by Error:")
# except ValueError:
#     print("Invalid input")

# employee_file = open("employees.txt", "a")
# employee_file.write("Hello")
# employee_file = open("index.html", "w")
# employee_file.write("<p>Hello</p>")
#
# # print(employee_file.readlines())
# employee_file.close()

# o = open("usefultools.py", "w")
# o = open("usefultools.py", "a")
# o.write('import random')
# o.write('\n\nfeet_in_mile = 5200')
# o.write('\nmeters_in_kilometer = 1000')
# o.write('\nbeatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]')
# o.write('\n\ndef get_ext(filename):\n   return filename[filename index(" ") + 1:]\n\ndef roll_dice(num):\n  return random.randint(1, num)')

import usefultools
print(usefultools.roll_dice(10))

