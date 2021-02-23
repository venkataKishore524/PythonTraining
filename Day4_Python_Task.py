#Task 1 - Write an iterator yourself
class IterTest:
    print(' Write an iterator yourself')
    def __init__(self):
        self.inp=[]
    def Itr(self,InputString):
        print(InputString)
        self.inp= InputString
        it=iter(self.inp)
        try:
            for x in range(len(InputString)):
                print(next(it))
                next(it)
        except StopIteration:
            pass
        finally:
            print("Iteration is done \n")
o1 = IterTest()
o1.Itr("Hello")


#2
import csv
print('create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.')
with open('express.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open('express.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Kishore",524])
with open('express.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Task 4 Recursive
import os
print('Recursive')
for dirpath, dirs, files in os.walk("."):
	print(dirpath)


# Task 5 - use standard lib sys to list all the command line args given to your program
import sys
print('use standard lib sys to list all the command line args given to your program')
print(f"Aruguments is : {sys.argv}")


# Task 6 - Rewrite the guessing game program to throw a custom error when the user is out of tries.
import random
print('Rewrite the guessing game program to throw a custom error when the user is out of tries.')
guess=random.randint(1,15)
num=int(input("Enter the number "))
count=1
while guess!=num :
    try:
        if(count==3):
            raise Exception
        if(num<guess):
            print("Your Guess value is lower than the real value")
            num=int(input("Enter the number : "))
            count=count+1
        else:
            print("Your Guess value is higher than the real value")
            num=int(input("Enter the number : "))
            count=count+1
    except Exception:
        print(f"You Lost it \n\n")
        break
if(guess==num):
    print(f"You Won it\n\n")


#7 accept input from a user and handle type, value errors
import math
print('Accept input from a user and handle type, value errors')
num=int(input("Enter the number : "))
try:
    res=math.sqrt(num)
    print(res)
except ValueError:
    print("The value should be greater than 0")   # if num = -1


# Type Error
import math
num=input("Enter the number : ")
try:
    res=math.sqrt(num)
    print(res)   
except TypeError:
    print("The type of num should be an integer ")    #if num='a'


 #Task 8 - demonstrate key and index errors in an example
print('Demonstrate key and index errors in an example')
details={"Kishore":1,"Nellutla":2,"Venkata":3}
try:
    print(details["Kishore"])
    print(details["Nellutla"])
except KeyError:
    print("Enter the correct key :")

#indexError
array=[100,122,123]
try:
    print(array[1])
    print(array[5])
except IndexError:
    print("Index out of bound Exception ")