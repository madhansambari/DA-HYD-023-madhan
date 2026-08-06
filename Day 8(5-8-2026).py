'''
Tokens --> keywords, Identifiers,Literals,Operators,punctuators,Variables
Operators -->Numeric data (int,float,complex) ,bool
Control Flow --> if,elif,else,for,while
Secquences--> string,lists,sets,tuples,mapping/(dict)
'''
#strings-->Group of characterss, we use single or double or triple quotes
#for representation of strings.....
#strings are Immutable,ordered,indexd collection
#space is also a character

'''
name='code gnan'
names='codegnan'
print(name)
print(names)
print(type(name))
print(len(name))#len -->reurns the number of items in container
print(len(names))

#index() --> fetch the object (position) starts at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(names[5])

#print(name[25])#IndexError --> as its out of range
# Negative Indexing --> -1 to len(obj)
print(name[-1])#it returns last character
print(names[-3])
#print(names([-33])
'''

'''
#slicing --> we can access group of characters(objects)
#We use [start:end]#start default -->0, start is included, end is excluded

name='codegnan'
print(name[:])#returns entire string 
print(name[:4])#starts at 0th index before 4th index
print(name[0:])#returns entire string 
print(name[1:5])#returns from given index to end index
#print(name[-4:-1])
print(name[1:3:7])

'''
'''
name='python'
print(name[3:7])
print(name[7:3]) #returns empty as strings are immutable
#slicing is applicable from lower index to higher index
print(name[:45]) #returns till end of the string
print(name[45:])
'''

'''
name='python'
print(name[-1:-5])
print(name[-5:-1])
print(name[4:])
print(name[4:6])
print(name[-2:])

'''
'''
name='python'
print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve & -ve,-ve & +ve,-ve all possibilities
'''

'''
#striding -->[start:end:step]

course='DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1])#returns all chararters
print(course[::2])#includes start to end skipping1 character

print(course[::4])

print(course[1:6:3]) #[1:6]-->ataAn-->[1::]
print(course[2:12:3])

'''

'''
#task:Workoutwit all possibilities of slicing and striding on a example

name='codegnan'
#name[3]='w'#strings are immutable

# operations on strings -->Indexing,concatenation, Repetiton
print(name*3)
print('*'*25)


#concatenation --> combining strings


data = 'saketh'+'python'+'database'
print(data)
print('123'*4)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')

'''
'''
for i in 'codegnan':
    print(i,end=' ')

'''

'''
name="datacodegnan"
#built-in functions -->len(),min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name))

'''
'''
#Methods on Strings --> Case-Conversions, Finding/ searching...
name='Codegnan data'
#case-conversions -->upper(),lower(),title(),capitalize()
a= name.upper()
print(a)
b=name.lower()
print(b)
#Capitalize() -->converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title()#converts evert work first letter to uppercase
print(d)

'''
#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#USE LOOP AND STRINGS TO RETURN A-Z

for i in range(A , Z):
print(i)












