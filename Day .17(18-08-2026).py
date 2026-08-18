'''
Tokens,Datatypes -->Control Folw Statements --->if,elif,elde,for,while,break continue........

procedure,Oriented programming

Functions-->A Function is a block of code which preforms a specific task
Its a reuseable group of statements where we define using
def Keyword

Advantages -->Code reuseablity,code maintainablity,ease of debugging,avoiding code duplication....


def fname(parameters):       function defn
    """Doc String"""   Description
    statement(s).....
    ................     Function body
    retuen value(s)...
fname(args)   function call


len('codegnan')
len(['poll',23])

'''

# To Perfrom sum of given objects
#a='code'
#b='gnan'
#print(a+b)
'''
def add(a,b):
    """sum of objects"""
    c=a+b
    return c
print(add(12,2)) #Addition
print(add('code','gnan')) #Concatenation
print(add([12,5],[12,34])) #Merging
c,d=map(int,input("Enter the values:").split())
print(c,d)
print(add(c,d))
'''
'''
def add (a,b)
    """Sum of object without return"""
    print(a+b)
add('code','gnana')
print(add(12,-34)) #it returns result along with None
'''
'''
name,age,salary="saketh",32,500000
#usage of return

def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+34+45
print(details())
'''
'''
There are 5 types of arguments:
---:> positional Arguments
---:>Default Arguments
---:>Keyword Arguments
---:>Varible length Arguments(*args)
---:>Keyword varable length arguments(**kwargs)
'''
'''
#Postitonal Arguments --> Number of Arguments in function definition should match with function call (order has to be maintained)
#print(len(123,234)) this is as per bulit-in len(obj) will accept  one argument

def details(name,place):
    """To store the details"""
    #name="codegnan"
    #name="hyderabad"
    #return name,place
    print(f'Name is {name}')
    print(f'palce is {place}')
print(details("saketh","codegnan"))
print(details("sai","vizag"))
#print(details("vizag","shyam",34))#raises TypeError as only 2 arguments
c,d=map(str,input("Enter the value").split(','))
details(c,d)
'''
'''
#Default arguments --> We can make arguments as default but not first argument as default
#def grocery(item="cheese",price=100):
#def grocery(item="Burger",price):
    """usage of default argument"""
    print(f'The Item is {item} and price is {price}')
grocery("milk",32)
#grocery(32,"milk")
grocery("Bread")#by default we have given price as 35
grocery("Bread",45)#as both item and price as default arguments
'''
#Keyword arguments ---> Whenevefr we wanr=t to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """keyword arguements usage"""
    print(f'Employee name is {name},role is {role} and {salary} works in {place}')
employee("sai",20000,"Admin")
employee(salary=25000,role="Frontdesk",name="Asha")

#♥☺☻♦••◘○☺
