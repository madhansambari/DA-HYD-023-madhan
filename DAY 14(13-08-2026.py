'''
Lists,Tuples...
'''
'''
#List -->Mutable,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()

details=['codegnan',7,2018,'hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python'))#valueError

print(details.count(21))
print(details.count('python'))#it returns 0 as we dont have it
'''
'''
#copy() -->shallow copy of the given collection

data=['codegnan','saketh','python','java']
     
new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic AI'
print(new)
print(data)

data.append('saketh')
print(data)
print(new)
'''
'''
data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='Agents' #whenever we make changes in nested list original will also be effected
print(new)
print(data)


new[1]='python'
print(new)
print(data)
'''

'''
marks=[14,24,-45,27,35,'sad']
print(marks)
#print(marks.sort())#returns none
#print(marks)#returns in ascending order
#marks.sort(reverse=True)#returns in descending order...
#print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
'''
'''
#type(),len(),max(),min(),print()

print(sorted('codegnan')) #returns List in ascending order
#print(sorted(['code','23',34,45])) #raises error
'''
'''
#tuples --> tuples are Indexed,ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer() for tuple notation

a=()
print(type(a))
print(len(a))
dimensions=1.5,2.5
print(dimensions)
print(type(dimensions))
'''
'''
#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition
courses=('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))
print(courses[-1][2])
print(courses[2][-1])
print(courses[3][-2:])
print(courses[4][-1])
#courses[2]=23 tuples are Immutable
courses[-1].append('codegnan')#We can make any modifications inside list
print(courses)  

#create a Nested tuple as above and work on slicing ,striding and list function
print('PFS' in courses)#Membership
d=courses*2 #repetiton
print(d)
e= courses+(2,3,4,5) #merging
print(e)
'''
'''
#Tuples Immutable -->count(),index()
courses=('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses.index('AgenticAI')) #return first occurance
print(courses.count('Agents'))

#print(courses.sort()) #Attribute Error --->sort() is in lists not a tuple

print(sorted(courses[-1])) #as we have mixed type

#TypeCasting
d=tuple(sorted((23,12,3,4,5)))
print(d)
#accept group of integers space separated
a,b=map(int,input("Enter the value").split())
print(a,b)

a=tuple(map(int,input("Enter the value").split()))
print(a)'''

print('9+4')
#eval() funcation can take any kind of input
print(eval('9+4'))

a=eval(input("Enter a list")) #in this case u can exactly enter data as list
print(a)
print(type(a))


#Task:Take a user input as string, do this in two ways....
'''
1)give the count of ench repeating character
test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]
'''
