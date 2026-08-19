'''
Functions-->Variable length arguments(*args)
         -->Keywords variable length arguments(**kwargs)

Variable length arguments -->The number of poisitional arguments are not limit
we can pass any number of arguments ,but we need to use the * representation, data is dtored in tuple..
'''
'''
def sample(*args):
    """simple demo for *args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,5,6)#any number
sample('codegnan','saketh',23)
details=[24,45,35,65]
sample(details)#passing a collection
sample(*details)#upacking values from collection
'''
'''
a,b,c=13,4,'da'
print(a,b,c)
#a,*b,c='python','codegnan',23,45,9.7,'data'
#a,b,*c='python','codegnan',23,45,9.7,'data'
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)
'''
'''
#Task --> We wanted to calculate the sum of given objects using Function
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        #if type(i)==int or type(i)== float or type(i) == complex:
        if type(i) in (int,float,complex):
            result=result+i
        elif type(i)==str:
            result=result
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(20,24,25))
#print(add(3,4,5,'poll','dear',4.5))
#print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("Enter the values:").split(',')))
print(add(*b))
print(*b)
for i in b:
    print(i,end=' ')#same as here
'''
'''
def details(**kwargs):
    """Usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #returns empty dictionary
#details(2,3,4,6) #raises TypeError
details(name="codegnan",place="hyd",batch="da")
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''
#now let us include both of them into a function
def sample(*a,**b):
    """Usage of both Variable length and keyword variable length argument"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23")
#sample(name="codegnan",23,ids=23445)#postional args follows keysword args

