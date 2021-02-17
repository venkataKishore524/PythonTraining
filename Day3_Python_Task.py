#Task 1 - use dict comprehension to create a dict of squares 
print('\n # Task 1 - use dict comprehension to create a dict of squares ')
nums = [1, 2, 3]
dict_of_squares = {compre: compre * compre for compre in nums}
print(dict_of_squares)


# Task 2 - using list comprehension - try 1
print('\n # Task 2 - using list comprehension - try 1')
dict_of_squares1 = [compre*compre for compre in dict_of_squares]
print(dict_of_squares1)

# Task 2 - using list comprehension - try 2
print('\n # Task 2 - using list comprehension - try 2')
dict_of_squares1 = list(dict_of_squares.values())
print(dict_of_squares1)

# Task 3 - given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}
print('\n Set Comprehensive')
givenList = [1, 2, 5, 2, 3, 1, 4, 5]
squares_of_unique = {compre * compre for compre in set(givenList)}
print(squares_of_unique)


# Task 4 - list of tuples with current and min balances
print('\n # Task 4 - list of tuples with current and min balances')
print(' \n # a - dict of those with proper balances ')
list_of_tuple= [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
def ConvertToDict(lst):
    output = {}
    for lt in lst :
        tupleData = list(str(lt).replace("(", "").replace(")","").split(","))
        name = tupleData[0].replace("\'", "")
        salary = tupleData[1]
        if int(salary) >= 2000:
            output[name] = salary
    return output
         
print (ConvertToDict(list_of_tuple))

print('\n # b- set of all balances {2000, -52, 900}')
balance = set()
for index in list_of_tuple:
    balance.add(index[1])
print(balance)

print('\n # c- list of account holders ["Guido", "Raymond", "Jack", "Brandon"]')
accountHolder = list()
for index in list_of_tuple:
    accountHolder.append(index[0])
print(accountHolder)

print('\n  # d - Min Balance')
minBalance = {name : minBal-curBal for (name, curBal, minBal) in list_of_tuple if curBal < minBal}
print(minBalance)

print('\n  # e - List Balance')
listBalance = {name : curBal for (name, curBal, minBal) in list_of_tuple if curBal > 0}
print(listBalance)

print(#Write a Developer class that has a code function and a languages list.)
class Developer :

     def __init__(self, devlanguages):
         self.devlanguages= ["C","C++","Java","Php","Python"]
     def code(self,devlanguage): 
            if(devlanguage in list(map(lambda x: x.upper(), self.devlanguages ))): 
                  print(f"code in {devlanguage}")
            else:
                 print(f"You entered code {devlanguage} is not in the list")          

     def resume(self):
        print(self.devlanguages) 
        
inputlanguage = input("Please enter the coding language: ")
devlanguage = inputlanguage.upper()
s = Developer("")
s.code(devlanguage)

#task5
from math import factorial
class Factorial:
    def __init__(self):
        self.result = []
    def computeFactorial(self,numbers):
        for number in numbers:
            self.result.append(factorial(number))
        return self.result
newObject = Factorial()
print(newObject.computeFactorial([3,2]))
