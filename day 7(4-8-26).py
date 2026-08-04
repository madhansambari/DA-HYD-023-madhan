'''
l=[1,0,1,1,1,0,1]
streak=0
highest_streak=0
for i in l:
    if i==1:
        streak+=1
        if streak>highest_streak:
            highest_streak= streak
    else:
        streak=0
else:
    print(highest_streak)
 
'''
'''
#for-else with notifications scenario

notifications =[0,0,0,0]
for i in notifitions:
    if i==1:
        print("unread notifitions")
        break
else:
    print("all catch up")
'''
'''
notifition=list(map(int,input("enter value").split(",")))
for i in notifition:
    if i==1:
        print("unread notifition")
        break
else:
    print("all catch up")
'''

#while  --> it relies on condition, it will be completely executed untilthe conditon is satisified....


'''
syntax while:

while<condition>:
    statement(s).....
    .....
    ........
'''
'''
while True:
    print("yes")
'''
'''
i=0
while i<=10:
    print(i)
    i=i+1
   '''
'''
i=0
while i>=9:
    print(10-i)
    i=i+1
   '''
pin = "2612"
max_attempts=3
current_attempt=0
while current_attempt<=max_attempts:
    entered_pin=input("enter the atm pin:")
    if entered_pin == pin:
        print("login successful")
        break
    else:
        print("Entered PIN is worng.. try again carefully")
        current_attempt +=1
else:
    print("Account locked,try after 24hours...")
    
