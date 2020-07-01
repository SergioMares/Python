#all the logic operators in one line
(True and False) or  (not 0) != 1

#If, else and elif. Look that it has no parentesis, all is in the convention
#try changing the 'n' value to see all the diferent responses
n = 24
if n < 100:
    print("it's lower than 100")
    if n < 25:
        print("And it's lower than 25")
elif n > 100:
    print("it's greater than 100")
else:
    print("it's equal to 100")
    
#######################
#while loop. You can add an else at the very end to do something when the loop ends

c = 0
while c <= 5:
    c+=1
    if (c==4):
#       print("Break te loop when c is 4",)
#       break
        print("here comes the continue")
        continue
        print("this message will never out because of the continue")
    print("c value is:",c)
else:
    print("Se ha completado toda la iteración y c vale", c)
    
############################
#for loop. it´s a foreach loop or a auto-indexed loop. to change a value in a data structure, you've to access by the index. the for loop also works with strings
list = ["asf",'qwer',"zxcv"]
for string in list:
    print(string)

#you can get the index adding a parameter to the for loop 
numbers = [2, 234, 32, 423, 25, 566, 97, 812, 91, 310]
for index,number in enumerate(numbers):
    print("number:" ,number)#the value in the list
    print("index:",index)#pretty explains itself
numeros
    
#the range method will return a list of numbers. 
#range(x,y,z) where 'x' is the beggining (if you put nothing strats from 0) 'y' is the end and 'z' the steps (if nothing will be 1 by 1)    
for x in range(2, 30, 3):
  print(x)   
