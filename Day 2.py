'''
Tokens -->Variables

Variables --> Named memory location, its a placholed for data
#Rules are to be followed

#MultiAssignment of variables

name, age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place, sep=',')
print(name,age,place,sep='------>')
print(name,age,place,sep='  #')

#a,b = 2,4,5 #valueError as too many values to unpack
a,b = 2,4 

name ="codegnan"
a,b = 4,1.5
print(a,b)
a , b = b , a    #swapping

print(a,b,sep=',')

#a , b = b , c   #name error
#print(a,b)
#deleting the variables -->del

#del a
#print(a)

#punchuators --> [](lists),()(tuples),{}(Dist, sets)

name = "codegnan is inst" ;age = 7 ;course = 'Data analysis'
print(name,age,course, sep = '---_---')


#datatype
#  -->Numeric(int, float, complex), boolean , none
#  -->sequences -->Lists,tuples,sets, strings,
#  -->Frozensets, mapping(dict)


#Numeric type --> int,float,complex

#int  datatype --> quantity, age...
age = 7
print(age)
print(type(age))# type --> returns the datatype of a object

print(type(264))

#quantity = 03 #it is notr allowed
#print(quantity)
#float datatype --> temp, salary, price
price = 750.24;discount=2.5
print(price, discount)
print(type(price))


#complex --> combination of real and img
i2=4
data = 5+i2
print(data)

data = 5+2j
print(data)
print(type(data))

#Boolean -->true/False

valid = True
print(type(valid))

error = False
print(type(error))

#typecasting -->converting one type to anoter type
#python by default follows implicit type (we need not mention the datatype)

#we will go for explicit conversion

#Every built-in datatype is a built - in function
#int,float,complex,bool

#typecasting --> int--> float, complex,bool
age =35
print(type(age))
b= float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)


#float--> typecasting

age =35.5
print(type(age))
b= int(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)


e=int(float(bool(45)))
print(e)
f=bool(int(float(25)))
print(f)
'''
f=45+2.5+2+3j+False
print(f)
