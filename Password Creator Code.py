import random
import time

master_list = []
repeat_value = True

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
caps_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

while repeat_value == True:
  unique_pass = ""
  website_name = input("Which website would you like to create a password for?")
  pass_length = int(input("How long do you want your password to be?"))
  pass_list = list(range(pass_length))
  for i in pass_list:
    list_pick = random.choice([alphabet, caps_alphabet, numbers, special_characters])
    character_pick = random.choice(list_pick)
    unique_pass = unique_pass + str(character_pick)
  master_list.append([website_name, unique_pass])
  time.sleep(0.5)
  repeat_answer = input("Would you like to make another password?")
  if repeat_answer == "yes":
    repeat_value = True
  else:
    repeat_value = False
   
print("Here are your available passwords: ")
print(str(master_list))
    