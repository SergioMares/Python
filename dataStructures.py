################################################3
#Tuples. Almost the same as a list, but immutable. As tuples are immutable, the append method won't work
#index method will bring you back the first time that an element appears in the tuple. Also works with lists
tuple.index(1234)

#count method count how many times a value is in the tuple. This also works with lists
tuple.count('asdf')

#####################################
#Sets: Disordered collections of unique elements, used to make tests of permanency and delete duplicate elements
#as sets are unorderer, they have no index. The elements in a set are auto 'ordered'.
mySet = set() #making an empty set
mySet = {1,2,3,4,5,5,6,7,8,9,0} #The duplicated 5 will be deleted
mySet.add("wakala") #add a new element.
'wakala' in mySet #if wakala is in mySet, returns true. in also works with lists
