#Q1)Write a Python program using if-elif-else that takes a student's marks (out of 100) as input and prints their grade based on the following
marks=int(input("Enter your Marks:"))
if marks<0 or marks>100:
    print("Invalid Marks! Please Enter the Valid Marks!!!")
elif marks>=90 and marks<=100:
    print("Grade Acquried:- A")
    print("Outstanding Grade")
elif marks>=80 and marks<=89:
    print("Grade Acquried:- B")
    print("Excellent Grade")
elif marks>=70 and marks<=79:
    print("Grade Acquried:- C")
    print("Very Good Grade")
elif marks>=60 and marks<=69:
    print("Grade Acquried:- D")
    print("Good Results")
elif marks>=50 and marks<=59:
    print("Grade Acquried:- E")
    print("Needs improvement")
else:
    print("Grade Acquried:- F")
    print("Failed, Needs to Work Harder")

'''Q2)Write a Python program using if-elif-else that takes a number as input and classifies it as follows:
Negative Even Number or Negative Odd Number
Positive Even Number or Positive Odd Number'''

number=int(input("Enter the number"))
if number==0:
    print("Neither. 0 is not even or odd.")
if number<0 and number%2==0:
    print("The Number is Negative Even number")
elif number<0:
    print("The Number is Negative Odd Number")
elif number%2==0:
    print("The Number is Positive Even Number")
else:
    print("The Number is Positive Odd Number")

#Q3)Write a Python program using if-elif-else that takes a month number (1–12) as input and prints the season it belongs to. 

month=int(input("Enter the Month in number:"))
if month==12 or month==1 or month==2:
    print("The Season of Entered Month is Winter")
elif month>=3 and month<=5:
    print("The Season of Entered Month is Spring")
elif month>=6 and month<=8:
    print("The Season of Entered Month is Summer")
elif month>=9 and month<=11:
    print("The Season of Entered Month is Autumn")
else:
    print("Invalid month number! Please Enter the Valid Month number (1-12)")