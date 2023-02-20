import time

wavelength = int(input("What is the wavelength?")) 
space = " "
digit = "0"

def repeat_function():
  list_string = []
  for i in list(range(wavelength)):
    list_string.append(space)
    print(list_string)
    time.sleep(0.03)
  for i in list(range(wavelength)):
    list_string[i] = digit
    print(list_string)
    time.sleep(0.03)
  for i in list(range(wavelength)):
    list_string[i] = space
    print(list_string)
    time.sleep(0.03)

the_input = input("How many time to repeat?")
count = 0
while count <= the_input:
  repeat_function()
  count += 1