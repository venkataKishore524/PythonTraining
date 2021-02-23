# Task 1 : Make a generator to perform the same functionality of the iterator
import sys
print('\n Make a generator to perform the same functionality of the iterator')
def generator_test(value):
    for x in value:
        yield(x*2)
resultValue= generator_test([10,20,30,40,50])
try:
    for x in resultValue:
        print(x)
        #print(next(resultValue))
except StopIteration:
    sys.exit()


# Task 2 - Try overwriting some default dunder methods and manipulate their default behavior
class defDunder:
    print('\n Try overwriting some default dunder methods and manipulate their default behavior')
    def __init__(self, myName, myQuestion):
        self.name = myName
        self.question = myQuestion
    def __str__(self):
        return "Hello {}, {} \n".format(self.name, self.question)
checkDD = defDunder('Kishore','Thanks for the DefDunder')
print(checkDD) 

#Task 3 - Write a decorator that times a function call using timeit start a timer before func call end the timer after func call print the time diff
from functools import wraps
import time
print('Write a decorator that times a function call using timeit start a timer before func call end the timer after func call print the time diff')
def dec_timeit(func):
    @wraps(func)
    def timeitwrapper(*args, **kwargs):
        starttime = time.perf_counter()
        print(f"Start time {starttime}")
        func(*args, **kwargs)
        endtime = time.perf_counter()
        print(f"end time {endtime}")
        print(f"time spent is {endtime-starttime}")
    return timeitwrapper
@dec_timeit
def Hello():
    print('Hello')
@dec_timeit
def Hello1(name,question):
    print(f"Hello {name} , {question}")
Hello()
Hello1("Kishore","Thanks for TimeIT !!")