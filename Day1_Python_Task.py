# Task 1 -- Print Unique Names
names = ["john", "jake", "jack", "george", "jenny", "jason"]
print('\n #Task 1 -- Print Unique Names')
for uniName in names:
    if "e" not in uniName and len(uniName) < 5:
        print('Unique Names are : ' +uniName)


#Task 2 -- Slicing
print('\n #Task 2 -- Slicing')
newString = 'python'
sliceString = newString[2:6]
print('Initial Slice is : ' +sliceString)
concatString ='c'
print('Concatinate String is : ' +concatString + sliceString[:6])


# Task 3 -- Print Dict Key and Values
import json
print('\n #Task 3 - Print Dict Key and Values ')
dictKV = {"name": "python", "ext": "py", "creator": "guido"}
for key, values in dictKV.items():
    print('Key is : ' +key + ' and Value is : ' +values)

# Task 4 -- FizzBuzz
print('\n #Task 4 - FizzBuzz')
for fizzbuzz in range(200):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

# Task 5 -- Guessing Game
print('\n # Task 5 - Guessing Game')
import random
hidden = random.randint(1, 20)
captureGuess = int(input("Please enter your guess: "))
if captureGuess == hidden:
    print("Success Hit !!! \n")
elif captureGuess < hidden:
    print("Your guess is too low \n")
else:
    print("Your guess is too high \n")