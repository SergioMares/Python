#I used jupiter notebook to test all the lines bellow

#You don't need to use a ';' at the end of every sentence
#Also You don't need to put a variable type in python, it does automatically. like...
numberOne = 1
numberTwo = 1.123465789
#Exponentiation ... 3^2
3 ** 2

#strings
string = 'helloWorld'
stringWithTab = "here's a \t tab";
stringWithLineBreak = "here's a \n line break"
print(string, stringWithTab, stringWithLineBreak)

#Use 'r' to avoid special characters
print(r"C:\nombre\directorio") #in this case \n 

# use """ to write multiple lines
print("""A line
another line
also another line
I think this automatically makes a line break""")

#python also can multiply strings
ten_spaces = " " * 10
print("count ten spaces" + ten_spaces + "here ends the 10 spaces")

#index
str1 = "Python"
str1[0]

#Python also counts the negative numbers in the strings. you can already use strings as a array of characters. 
str1 = "Python"
print(str1[-1], 
str1[-2],
str1[-3],
str1[-4],
str1[-5],
str1[-6],
str1[0],
str1[1], 
str1[2],
str1[3],
str1[4],
str1[5]) 

#slicing -> select a range in the string to return string[x:y] where 'x' is from and 'y' is to. x the beginning and y the end of the range
str1[0:2]
print(str1[-6:6] +"\n"+
str1[0:6] +"\n"+
str1[-6:3]+str1[4])
str1[-5:] # if you do not put a number in the second... argument? it assumes that is til' the end
str1[:-4] # on the other hand, if you do not put a number in the first... place? it will start at the very beggining to the 'y'
str1[:] #I dare you to wonder what would happen ;)
# Python is very gross, but even python has to have a structure and some convention. If you put a index out of range, it wont work
#with slicing, you can take a index out of place and it will still work :) 

#you can't change a simple char in a string, like the comment bellow
#str1[0] = "N"
#but you can do it with slicing and concatenating
str1 = 'Python'
str1 = "N" + str1[3:] 
str1

#length. You already know what this funtion do
len(str1)




