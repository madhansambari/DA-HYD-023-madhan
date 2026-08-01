#explation of yestad class
'''
# Take input from the user
marks = int(input("Enter your marks: "))

# Validate the marks
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

'''

'''
marks = int(input("enter the marks(1-1000):"))
if marks > 0 and marks <=100:
    if marks >= 90:
        print("grade A")
    if marks >=80 and marks <=89:
        print("grade B")
    if marks >=70 and marks <=79:
        print("grade C")
    if marks >=60 and marks <= 69:
        print("grade d")
    if marks < 60:
        print("fail")

else:
    print("enter ony +ve numbers ")
'''

'''
#intro to elif in condutional statements

if <condution >
   satement.....

elif <con1>
     satement....
elif <con2>
    staement....
else<final con>
    statement.....

'''
'''
age = int (input("enter the age :"))
if age>=18 and age <=100:
    print('------- user has vote eligibility -----')
    print('------- access granted------')
elif age<18 and  age>0:
    print('------- user still need to grt vote eligibility -----')
    print('------- user need to wait for more years------')
else:
    print('------ only +ve valuesand less than 100 -------')

'''
'''
#output formatting -->old style formatting (using commas)
# %usage (%f,%d),.format() usage, fstring notation

a,b=7,9
print(a)
print(b)
print(a,b)
name =  "madhan";batch = "DA"
print(name,batch)
print(name,batch,sep=',')
print(name,batch,sep='----------->')

print(name, batch,sep='\t')
print(a,b,end='')
print("HYD")

'''

name='codegnan'; age=7;batch='DA-023';place='HYD'
'''
print(batch, 'is in',name)
print(name,'is in',place,'age is', age,'years')

salary = 24253.256
print("his salary is %d"%(salary))
print("his salary is %f"%(salary))
print("his salary is %.1f"%(salary))
'''

print("{} is in {}".format(name,place))

#fstring usage(more recommended)
print(f'{name} is in {place}')
print (f'{"madhan"} is in {name}')
