#tuple
tu=(10,25,89,90,40,30)
print('Tuple value is :',tu)
print('Type is :',type(tu))

#tuple can't be extended, updated, inserted, appended

 #concatenation
t1=tu+(15,60,75)
print('After concatenation',t1)

#repeatation
print((20,10,45)*4)

print(tu)
print(len(tu))
print(tu.count(10))

print('Sum of tuple elements:',sum(tu))
print('Max of tuble:',max(tu))
print('Minimum of tuple:',min(tu))
l=[22,44,66,88,99,11,22]
print(l[2])
print(l.index(66))

print(tu[1])
print(tu.index(90))

#accessing
print(tu[-1])
print(tu[:4])
print(tu[1:4])
print(tu[1:])

print(tu[:-1])
print(tu)
print(tu[::-1]) #reversing

#Assignment 1)Unpacking a list

a,b,*c,d,e=['a','b','Ashok','John','Puvan','Suresh',1,2]
print(a)
print(c)
print(e)

#Unpacking a tuple
a,b,*c,d,e=('a','b','Ashok','John','Puvan','Suresh',1,2)
print(b)
print(c)
print(d)

#converting a single tuple element to string
tu=(1,'a','Suresh')
print(tu)
print(type(tu))
str(tu)
z=str(tu)
print(z)
print(type(z))
