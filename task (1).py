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
