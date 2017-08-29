# -*- coding: utf-8 -*-
"""
Created on Fri May 05 10:22:14 2017

@author: WHuang07
"""
# class and object
import os
os.chdir('C:\Dentsu\Code 1 Infinity\Infinity Reboot\codes')
class PlaywithName():
    def createName(self, name): #self refers to the object, which we dont know the name
        self.name = name
        self.pool = 3 # assign the attribute value to object
    def displayName(self):
        print('My name is %s' %self.name)
        
print PlaywithName
firstperson = PlaywithName()
firstperson.createName('Wilson') # the line must be there to create the attribute name for self
firstperson.displayName()
firstperson.name
firstperson.pool

# Another Example
class Student():
    def __init__(self, name, age):
        self.attend = 0
        self.grades = []
        print ("Hello My Name is %s" %name)
        
    def attendDay(self):
        self.attend +=1
    def addGrade(self, grade):
        self.grades.append(grade)
    def getAverage(self):
        return sum(self.grades)/len(self.grades)

import random
wilson = Student('Wilson', 'fets') # class only take in functions in the module in the first line of class definition, which you want to use that in your customized class, but not take in any variable, because the variable will go to __init__ function. which here the second variable value must be provided, 'fets' otherwise will got errors, as see below. 
try:
    tomy =Student('Tomy')
except Exception as e:
    print('Error genenrated')   
    print e
print wilson.attend
for _ in range(10):
    wilson.attendDay()
print wilson.attend
for i in range(10):
    wilson.addGrade(random.randrange(60, 101))
print wilson.grades
print wilson.getAverage()

#http://stackoverflow.com/questions/9663562/what-is-difference-between-init-and-call-in-python
#So, the __init__ method is used when the class is called to initialize the instance, while the __call__ method is called when the instance is called 
class foo:
    def __call__(self, a, b, c):
        return a+b+c
test = foo()
print test(1,2,3)

class foo2:
    def __init__(self, a, b, c):
        print a+b+c
foo2(1,2,3)

#=========================================================================================
#Multi-threading
import threading
class adsDownloader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print self
adsDownloader().start() # to start a new thread for new job

#========================================================================================
#subclass and superclass 
class ParrentClass:
    var1 = 'i am var1'
    var2 = 'i am var2'
    def __init__(self):
        self.public = 1
        

class ParrentClass2:
    var3 = 'i am var3'

# inherit from multiple superclasses  
class ChildClass(ParrentClass, ParrentClass2):
    pass
# modify the variable in superclass
class ChildClass2(ParrentClass):
    var1 = 'i am modified var1'

parentObject = ParrentClass()
print parentObject.var1 # 'i am var1'
print parentObject.public # 1
childObject = ChildClass()
print childObject.var1 # 'i am var1'
try: 
    print childObject.public 
except Exception as e:
    print e
    
print childObject.var3 # 'i am var3'
childObject2 = ChildClass2()
print childObject2.var1 # 'i am modified var1'

#constructor
class NewPrintConstructor():
    def __init__(self, pool):
        print "test the constructor"
        self.pool = pool         
        
NewPrintConstructor(3)
#test the constructor
#<__main__.NewPrintConstructor instance at 0x000000000B013748>
NewPrintConstructor(5).pool # 5 

#Make function reusable as module (will save all the functions and variables, and can import it anytimes)
#remember the module can only been imported one time, which means the changes on the module wont reflected, unless the session been restarted, in spyder case, need to close the spyder application!!!! or you can use the reload function 

#need to put py file under C:\Users\WHUANG07\AppData\Local\Continuum\Anaconda2\Lib\site-packages
import testModule
testModule.testMod()
testFun = testModule.testMod # assign a variable to the function in the module
testFun()
reload(testModule)
testFun = testModule.testMod # one relaod, need assign the function to variable
testFun() 

while True:
    try:
        number = int(input('what is your favourite number?\n'))
        print(18/number)
        break
    except NameError:
        print("Make sure you enter the number")
    except ZeroDivisionError:
        print("Dont pick zero")
    except:
        break #but will hide the expection
    finally:
        print("loop complete") #no matter what, finally will be executed 
#=================================================================================================================
class YourClass:
    public = 1100
    __thing = 1
    _parameter =100
    print __thing
    print _parameter
    print public
        
class MyClass(YourClass):
    pass
#    def __init__(self):
##        print self.__thing
##        print self._YourClass__thing
##        print self._parameter
#        self.__thing = "My thing" 
#        print self.__thing

testyourclass = YourClass()
testyourclass._YourClass__thing

testClass = MyClass()
testClass.public
testClass._parameter
testClass._YourClass__thing
#testClass.public
#=================================================================================================================

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    def __Name(self):
        return self.firstname + ' ' + self.lastname

class testPerson:
    def __init__(first, last):
        return first + ' ' + last
# must have self as first variable, otherwise use staticmethod or classmethod. 
#https://stackoverflow.com/questions/14327794/can-python-have-class-or-instance-methods-that-do-not-have-self-as-the-first-a
try:
    x_test = testPerson("Marge", "Simpson")
except Exception as e:
    print e
    
#https://www.codecademy.com/en/forum_questions/53edd6977c82ca555200102f
class testPerson2:
    def __init__(ttest, first, last):
        print first + ' ' + last
        # cannot use return, as contructor can only return none, so need to use print
x_test2 = testPerson2("Marge", "Simpson")

x = Person("Marge", "Simpson")
print x
x.Name()

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum
#    if dont define the below function, it will inherited from superclass
    def __str__(self):
        return Person.__str__(self) + ", "+ self.staffnumber
#        now self.Name() is referring to the function in the subclass itself, so need to change Name to __Name(), but since you change it, it becomes private method, which should not be overwritten
    def __Name(self):
#        return self.Name()+ ", "+ self.staffnumber
#        maximum recursion depth exceeded
        return Person._Person__Name(self)+ ", "+ self.staffnumber
    def GetEmployee(self):
#        return self.first #fails the test
        return self._Person__Name() + ", "+self.staffnumber
#        try to understand the difference between self and super()
    def currentName(self):
        return self.__Name()

#so conclusion, unless call the superclass same function name within the function (use super or superclass name), the rest use self.{function_name}, but take care of the case, some variables or functions might refined in the current class 
       
y = Employee("Homer", "Simpson", "1007")
print y
print y.GetEmployee()
print y._Employee__Name()
print y.currentName()
print y._Person__Name()


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    def _Name(self):
        return self.firstname + ' ' + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum
#    if dont define the below function, it will inherited from superclass
    def __str__(self):
        return self._Name() + ", "+ self.staffnumber

y = Employee("Homer", "Simpson", "1007")
print y

# overloading in python
def f(n):
     return n + 42
 
def f(n,m):
    return n + m + 42
f(3,4)
try:
    f(3)
except Exception as e:
    print e
    
def f(n, m=None):
    if m:
        return n + m +42
    else:
        return n + 42
f(3,4) #49
f(3) #45

def g(*x):
    if len(x) == 1:
        return x[0] + 42
    else: 
        return x[0] + x[1] + 42

print g(3,4) #49
print g(3) #45

#https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')

#You should use **kwargs if you want to handle named arguments in a function
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

greet_me(name="yasoob") 
greet_me(age=10)            

#Now lets talk about how you can use *args and **kwargs to call a function with a list or dictionary of arguments.

def test_args_kwargs(*argv):
    for arg in argv:
        print "variable passed in is %s" %arg
        
args = ("two", 3, 5, 10) #type is tuple
#cannot use test_args_kwargs(args)
test_args_kwargs(*args)

def test_args_kwargs2(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args2 = ("two", 3, 5)   
test_args_kwargs2(*args2)
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs2(**kwargs)

def test(fargs,*args,**kwargs):
    print "first normal arg:", fargs
    for arg in args:
        print "non_keyworded variable passed in is %s" %arg
    for key, value in kwargs.iteritems():
        print "The Key %s with the value of %s" %(key,value)
test("first variable")
test("first variable", "2nd_var", 100, 123)
test("first variable", "2nd_var", 100, 123, x=100)
test("first variable", x=100)

 
def zero():
    print "You typed zero.\n"
 
def sqr():
    print "n is a perfect square\n"
 
def even():
    print "n is an even number\n"
 
def prime():
    print "n is a prime number\n"
    
options = {0 : zero,
                1 : sqr,
                4 : sqr,
                9 : sqr,
                2 : even,
                3 : prime,
                5 : prime,
                7 : prime,
}
    
options[1]()

#https://www.youtube.com/watch?v=VBokjWj_cEA
cities = ['shanghai', 'shenzhen', 'fuzhou']
for index, city in enumerate(cities):
    print '%s : %s'%(index, city)

#walk through multiple list at the same time
x_list = [1, 2, 3]
y_list = [4, 5, 6]
z_list = [7, 8, 9]
for x, y, z in zip(x_list, y_list, z_list):
    print (x, y, z)
    
# swap variable
x = 10
y = 20
x,y,z = 1,3,4
print 'before x = %d and y = %d' %(x,y)
x,y = y,x
print 'after x = %d and y = %d' %(x,y)

#handle dict
ages = {
    'Mary': 18,
    'Terry': 12,
    'Dave': 29,
    'Kate': 'whatever'    
}
#set the default value in case key is not in the dictionary
age = ages.get('Dave', 'not in the dict')
print "Dave has an age of %s"%age

needle = 'd'
haystack = ['a', 'b', 'c']
for letter in haystack:
    if needle == letter:
        print('found')
        break
else: #if no break occurred
    print('not found!')

#f = open('some.txt')
#for line in f:
#    print line
#f.close()

#with open('some.txt') as f:
#    for line in f:
#        print line
#with is used to create context, no need to worry about the cleaning off, like close
#use with statement to work with text file

print 'Converting'
try:
    print(int('1'))
except:
    print('Conversion Failed!')
else: # if no-except
    print('Conversion Succeed!')
finally: # always happen, which is used to clean up, e.g. close the file
    print('Done!')

#https://www.youtube.com/watch?v=cKlnR-CB3tk
#understand lambda, map, filter, reduce functions
mx = lambda x, y: x if x>y else y
#mx is the function defined by lambda
print(mx(8,5))

#map can apply same function to each element of sequence or list
n = [4,3,2,1]
print list(map(lambda x: x**2, n)) # map the first variable is the function, second is the list
n_squared = map(lambda x: x**2, n)
type(n_squared) #still list
#list comprehension
print [x**2 for x in n]

#filter function
print list(filter(lambda x: x>2, n)) # map the first variable is the condition, second is
#list comprehension
print [x for x in n if x>2]

#reduce function
#use result of operation as first param of next operation
#return an item, not a list
print reduce(lambda x,y: x*y, n) #give the result of 24

#Python Tutorial: Generators 
#https://www.youtube.com/watch?v=bD05uGo_sVI


import pandas as pd
x = pd.DataFrame({0: [1,2,3], 1: [4,5,6], 2: [7,8,9], 3:[10,11,12]})
x = x.apply(lambda x: x*2)

#dropout implementation for deep learning
import numpy as np
p = 0.5
#x.shape give the tuple as result
U1=(np.random.rand(*x.shape)<p)/p
x*=U1

X = x - np.mean(x, axis = 0) # 0 for vertical and 1 for horizontal
cov = np.dot(X.T, X) / X.shape[0] 

# local variable vs global variable
# https://www.youtube.com/watch?v=r9LtArXOYjk








