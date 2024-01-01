import time
import random
import os

# for i in range(10):
#     print("Hello World!")
#     time.sleep(0.5)
# print("Hiiii")    

# def hello(fname,lname,age):
#     print("Hello " + lname)
#     print("I am " + fname)
#     print('I am '+ str(age) + " years old")
      
# hello("Mikail","Bro",18)

# def multiply(num1,num2):
#     # result = num1*num2
#     # return result
#     return num1 * num2

# print(multiply(3,2))

# print(round(abs(float(input("Enter a whole positive number: ")))))


# name = "Haziq"  #global scope
# def display_name():
#     name = 'Mikail'    #local scope
#     print(name)

# print(name)
# display_name()



#                      #*args pack argument into tuple
# def add(*args):     # * is important,what after that doesnt matter
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6,7,8,9))


#          #**kwargs pack argument into dictionary
# def hello(**kwargs):
#     #print("Hello " + kwargs['fname'] + " " + kwargs['lname'])
#     print("Hello",end=' ')
#     for key,value in kwargs.items():
#         print(value,end=" ")

# hello( fname='Haziq' , mname="Abdul" , lname="Mikail" )



# STRING FORMAT

# animal = "cow"
# item = "moon"
# print('the {0} jump over the {1}'.format(animal,item))
# text = "the {} jump over the {}"
# print(text.format(animal,item))

# print("Hello, my name is {:<10} .nice to meet you".format('Mikail'))
# print("Hello, my name is {:>10} .nice to meet you".format('Mikail'))
# print("Hello, my name is {:^10} .nice to meet you".format('Mikail'))

# number = 10000
# print("The number is {:3f}".format(number)) # num after decimal
# print("The number is {:,}".format(number)) 
# print("The number is {:b}".format(number)) #binary
# print("The number is {:o}".format(number)) #octo
# print("The number is {:x}".format(number)) #hexadecimal
# print("The number is {:e}".format(number)) #scientific notation



#RANDOM NUMBER

# x = random.randint(1,6)
# y = random.random()

# mylist = ['rock','paper','scissor']
# z = random.choice(mylist)

# card = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
# random.shuffle(card)

# print(card)



#EXECTION HANDLING  event that interupt flow of program
# try :
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator   
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
# except ValueError as e:
#     print(e)
#     print('Enter only number please')
# except Exception as e:
#     print(e)
#     print('Something went wrong.Sorry')
# else:
#     print(result)
# finally:
#     print('Anything else?')



# METHOD CHAINING
# class Car:

#     def turn_on(self):
#         print("You start the engine")
#         return self

#     def drive(self):
#         print("You drive the car")
#         return self

#     def brake(self):
#         print("You step on the brake")
#         return self

#     def turn_off(self):
#         print("You turn off the engine")
#         return self

# car = Car()
# car.turn_on().drive()



#FILE DETECTION

path = "C:\\Users\\HP\\OneDrive\\Desktop"

if os.path.exists(path):
    print("that location exist")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("that location doesn't exist")













































































































