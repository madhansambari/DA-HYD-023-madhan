'''
Sequences -->Strings,Lists,Tuples,Sets
Mapping --> Dictionary
'''
'''
#Lists ---> Collection of heterogenous elements(items)
#List --->Indexed,Ordered,Mutable,Heterogenous,We use [] to store the data

marks=[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#Operations : Indexing,slicing,striding,Membership,Merging,Repetition
'''
'''
#Nested Lists --> A list inside another list

names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)

print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type( names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:])

#get the output as cdga
print(names[0][::2])
names[0]=names[0][::-1]
print(names)
'''
'''
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing ,slicing --> Mutable
names[2]='python'
print(names)
#By indexing if we change the elements,length of coolection will remain same
names[4]=['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4][0][4:])


names[2:4]='Abhiram','Sai','Saketh','Sairam'
print(names)
#In Slicing whatever elements u pass as per the logic length keeps on increasing
#o/p as follows:
#['Codegnan', 25, 'Abhiram', 'python', 'Saketh', 'java', 'DA23', 34]


names[3:6:2]=['python','java']
print(names)
'''
#create a nested list with strings, lists and work on Indexing , slicing, striding
#added advantageif u could add string funcations also to it
#Lists Functions -->append(), insert(),extend(),pop(),remove(),clear()

names=['codegnan','saketh']
#append() -->inserts single element to the eng of the list
names.append('data')
print(names)
#names.append('analysis','agents') #TypeError
names.append(['analysis','agents'])
print(names)
#append() will always increment the length of list by 1
print(names[3])
print(names[3].append('chatgpt'))#it returns None as append is applicable on list not print
print(names)

#extend() --> inserts multiple elements to the end of list


'''
names.extend('analysis')
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) TypeError
#print(names)
'''

'''
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4], ['a','b'])#syntax Error
#print(names)
names.insert(-1,'AAA')
print(names)

'''

#pop(),remove(),clear()
#pop() by default last,else given index

print(names.pop())
print(names)
names.pop(2)
print(names)

#remove() --> we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
#names.remove (14) #it raises value error
del names[1:3]
print(names)
names.clear()
print(names)


#data=['codegnan','saketh'.'python','java']  #i/p
#o/p should be as follows
'''
0:codegnan
1:saketh
2:python
3:java
'''
