#Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
print('\n # Task 2 - Print Elements along with their Positions one per line')
arrayList=['a','b','c','d','e','f']
for key, value  in enumerate(arrayList):
    print(key, ":" ,value)

# Loop over a dict and print the value and key in the format value belongs to key.
print('\n # Task 3 - print the value and key in the format value belongs to key')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key, value in thisdict.items():
    print(value, 'for ', key)


print('\n # Task 4 - Demonstrate the else clause being invoked in a while loop. try the opposite as well.')
initial = 5
while initial > 0:
    initial = initial - 1
    if initial == 2:
        break
    print(initial)
else:
    print("Else Loop is not Executed \n")

print('\n # Task 4 - Demonstrate the else clause being invoked in a while loop. try the opposite as well. Try 2')
initial = 5
while initial < 2:
    initial = initial - 1
    if initial == 2:
        break
    print(initial)
else:
    print("Else Loop is Executed \n")

# Task 5 : 
print('\n # Task 5')
def multi(num1: int, num2: int) -> int:
    '''Taking two values as input and print them as '''
    multi = num1 * num2
    return multi
print(multi(1, 5))
print(multi(5, 10))
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
print(multi.__doc__)
print(multi(first, second), '\n')


# Task 6:
print('\n # Task 6')
def greetings_task(*arguments):  
    for task in arguments:  
        print (task) 
greetings_task("Hello", "Good Morning", "Greetings for the day") 

# Task 7:
print('\n # Task 7')
def kwargs(**kw):
    count=0
    for key, value in kw.items():
     print(value , ' -> ', key)
     print(" you passed ",count, "args ")
     count +=1
kwargs(Name="Kishore",Greeting="Hi!")

# Task 8:
def argtest(**args):
   print(len(args))
argtest(Name="Kishore",Greeting="Hi!")

#Task 11
print('# Task 11')
initial=0
while initial < 5:
    print(initial)
    initial+=1 
else:
  print("While test is done")
  
 #without else
initial=0
while initial < 5:
    print(initial)
    initial+=1 

 #task 12
print('# Task 12')
testNumberList = [1, 3, 3, 4, 5, 6]
newlist = [x**2 for x in testNumberList if (x%2)>0]
print(newlist)
 
#task 13
print('# Task 13')
lamb = lambda a,b : a /b
num=int(input("Enter a Number- "))
cnt=int(input("Enter a Count- "))
print(lamb(num,cnt))
