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
#    if (c==4):
#       print("Break te loop when c is 4",)
#       break
    print("c value is:",c)
else:
    print("the loop has ended and c is", c)
