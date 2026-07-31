## DAY 4 ##


'''
identity operators --> checks the identity of a object --> id()
'''
'''
a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(a==5)
'''
'''
a= [1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#As Wehave lists (mutable collection) both c and a lists will have different
#ods whereas values are same 
print(c is a) #output False
print(c == a) #output true
print (a is not c)

'''

'''
#***
#Bitwise operators

#--> we perfrom bitwise operations over operands
# & (and) , | (or), ^(XOR) shifting operators(<<,>>)
a=5
b=3

print(a)
print(b)
print(a & b)#both a and b to be converted binary and bitwise and is performed
print(a ^ b)#bitwise XOR
print(a | b)#bitwise OR
print(5 and 3)
print(5 or 3)
'''

'''
#leftshift operator <<,right shift operator>>
pasrint(5<1)
print(5<<1)
print(15<<2)

print(15>>2)
'''
#input formatting --> input(), int(input()),float(input())
#you know -->single input
#2 or 3 input --> map()
#group of integers --> list(map(int,input()),float(input().split(','))
'''
names = input("Enter the names:").split(',')
print(names)
name1,name2 = map(str,input("Enter the Friends Names:").split(','))
print(name1,name2)
'''
#token --> Numeric Datatypes --> operators -->Flow of the program
#Control Block statements
#Conditional Statements --> if, else,elif(rely on condition to be executed)
#Repetition statements(loops) -->for,while
#conditional satements -->if usage
'''
syntax :
    if<condition>:
        statement(s)....
        ......
'''
'''
age = int(input("Enter the age :"))
if age >=18:
    print('Your age is:',age)

'''
'''
age = int(input("Enter the age :"))
if age>=18 and age in [19,21,20]:
    print('your age is ',age)
print(age)    

# else keyword --> if-else

else:
    statement(s)....
    ....
    '''
#Vote Elibity ->To check his /her voter eligibility and give access....
age = int(input("enter the age"))
if age>=18:
    print("u have voter eligibility and age is ",age)
    print("access Granted")
else:
    age = 18-age
    print("u need to wait for more",age,"years")
