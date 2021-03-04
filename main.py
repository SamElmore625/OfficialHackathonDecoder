# This is a sample Python script.

code = input("Please Input Code Here:\n")
print ("Confirmed code:", code)

code = code.replace("123562547", " ")
#replaces the seperator with a space

code = code.split(" ")
#splits each 3 digit code into its own element in a list. Splits into new element every time there's a space

str_length = len(code)
# determines number of characters in string

digitsList = [0] * str_length
#determines how long the list should be based on length of sentence entered.
# Fills in all spots with 0's as placeholder

x = 0
while x < str_length:
    newCharacter = code[x]
    digitsList[x] = int(newCharacter)
    #assigns space (known as x) in list to newly converted character
    x = x + 1

a = 0
while a < len(code):
    digitsList[a] = (digitsList[a] - 34) / 3
    #Takes code and subtracts 34, then divides by three (Opposite of what we did to encode)
    a = a + 1

b = 0
while b < len(code):
    digitsList[b] = chr(int(digitsList[b]))
    #Converts ascii numbers back into actual characters
    b = b + 1

print(digitsList)
#Prints list with each individual character
print(*digitsList, sep='')
#Prints list as a string without any seperators