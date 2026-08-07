'''
runs=[4,6,1,0,2,4,0,6]
sum=0
boundarys=0
dot=0
for i in runs:
    
    if i==0:
        dot += i
        print('dot balls')
    elif i==4 or i==6:
        boundarys + i
        print('boundarys',boundarys)
    
        print('total scores')
        sum=i+1
        sum=runs
        
else:
    print('out')
    
    
'''

'''
scoure=[4,6,1,0,2,4,0,6]
boundarys=0
dot=0
total_scoure=0
for i in scoure:
    total_scoure+=i
    if i == 4 or i == 6:
        boundarys +=i
    elif i == 0:
        dot+=1
print(boundarys)
print(dot)
print(total_scoure)

'''
'''
pin='1310'
max_attempts=5
current_attempt=0
while current_attempt<=max_attempts:
    
    enter_pin=input("enter pin")
    if enter_pin==pin:
        print('correct')
        break
    else :
        print("lock")
        current_attempt+1
else:
    print("locked for 24 hrs")
    '''
pin='1310'
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    
    enter_pin=input("enter pin")
    if enter_pin==pin:
        print('correct')
        current_attempt=3
        break
    else :
        print("lock")
        current_attempt+1
else:
    print("locked for 24 hrs")

