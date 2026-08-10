'''
string -->CaseConversions, Searching & Finding, String testing methods, Replace, Space removal
'''

#Searching ,Finding,Replacing,Joining....

a="Codegnan"
print(len(a))
print(min(a))
print(max(a))

'''
b=a.index('g') #it returns the index position
print(b)
c=a.index('n')#it returns only the first occurance
print(c)
d=a.index('n',6) #it returns the next occurence
print(d)
#e=a.index('n',8)#value error
#print(e)
#f=a.index('t') #value error
#print(f)
'''
'''
#rindex() -->returns last occurence
b=a.rindex('g')
print(b)
c=a.rindex('n')#here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it returns ValueError
#print(d)
'''
'''
#count() -->returns the number of items object is repeating
print('Codegnan'.count('n'))
print('Code'.count('w'))#it returns 0 as we dont 'W' in 'code'
print('Cakshjasaksajs'.count('a'))
'''

'''
#find() --> first occurence but it avoid error returns  -1 if substring is not found
print('Codegnan'.find('r'))
print('Codegnan'.find('n'))

'''
'''
a="DataAnalysis"
print(len(a))
for i in a:
   # print(i)
    print(a.count(i),a.index(i))
'''

'''  
#Replaceing,Splitting,joining

#Strings are Immutable
a='Codegnan'
#a[4]='s'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('asdfghjkl#qwertyuiop#zxcvbnm#'.replace('#',' '))
print(a.replace('x','saketh'))

'''
'''
a='code saketh python'
b=a.split() # by default if we have space it splits(returns list)
print(b)
print(len(b))
c='code,saketh,python'
d=c.split()
print(d)
e=c.split(',')
print(e)
'''
'''
#join()
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))
'''

'''
#sting testing methods(boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....

a='Codegnan123'
print(a.isalnum())#returns True for alphanumberic strings else False
b='Codegnan'
print(b.isalnum())
print(a.isalpha())#returns True only for alphabets
print(a.isdigit())#returns true only for digit string
print('9182181508'.isdigit())
print('2345'.isnumeric()) #this has upper edge(numbers,fractions,romans)
#startswith() -->how to starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
print('codegnan'.endswith('an'))
'''
'''
print('codegnan'.islower())#returns True for all lowercase
print('COdegnan'.isupper())#returns True for all uppercase
print('Codegnan python'.istitle())
'''

'''
#Space removal-->strip()(removes leading and trailing spaces)

a=' codegnan '
print(a.strip())
b=input("Enter the string:").strip().lower()
print(b)
'''
#zfill() -->filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),ljust(),rjust()-->Alignment of strings(check lenth and then modify the width accordingly)
print('hai'.center(6))
print('hai'.center(7,'#'))
print('hai'.ljust(7,'#'))
print('hai'.rjust(7,'#'))
