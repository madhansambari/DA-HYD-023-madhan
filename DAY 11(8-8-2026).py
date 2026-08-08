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


'''
'''
pin = '2580'
max_attempts = 10
current_attempt = 0

while current_attempt < max_attempts:
    enter_pin = input("Enter password: ")

    if enter_pin == pin:
        print("Correct password")
        break

    current_attempt += 1
    print("Incorrect password.")
    print("Attempts remaining:", max_attempts - current_attempt)

else:
    print("Locked for 30 seconds")

   ''' 
'''

otp = '2580'
max_attempts = 7
current_attempt = 0

while current_attempt < max_attempts:
    enter_otp = input("Enter otp: ")

    if enter_otp == otp:
        print("Correct otp")
        break

    current_attempt += 1
    print("Incorrect otp.")
    print("Attempts remaining:", max_attempts - current_attempt)

else:
    print("Request for New OTP")


'''
''''
pin = '2580'
max_attempts = 10
current_attempt = 0

while current_attempt < max_attempts:
    enter_pin = input("Enter password: ")

    if enter_pin == pin:
        print("Correct password")
        break

    current_attempt += 1
    print("Incorrect password.")
    print("Attempts remaining:", max_attempts - current_attempt)

else:
    print("Locked for 30 seconds")
'''


'''
food = input("Show menu: ")
count = 0

while food != "Exit":
    count += 1
    food = input("Enter another item (Exit to stop): ")

print("Total no of items:", count)

'''

'''
# write a python pro palindrome 
text=input("Enter a string")
if text ==text[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


'''

score=20
limit=0
attempts=3
while limit < attempts:
    goal=int(input("enter:"))
    if goal == score  :
        print("you won")
        break
    else:
        attempts=attempts-limit
        print(f"you need to score more")
        limit += 1
else:
    print("you loss")
















