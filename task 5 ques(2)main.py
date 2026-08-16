# Student Marks Manager - 1
'''
marks = []

for i in range(3):
    mark = int(input("Enter the mark:"))
    marks.append(mark)

print("Original marks:", marks)

marks.insert(0, 95)
marks.extend([70, 80])

if 70 in marks:
    marks.remove(70)

removed_mark = marks.pop()

print("Removed mark:", removed_mark)
print("Final marks:", marks)
print("Number of marks:", len(marks))
'''
#Q2
'''
# Number List Analyser - 2

numbers = [15, 25, 35, 15, 45, 15]

numbers.sort()
print("Ascending order:", numbers)

numbers.reverse()
print("Descending order:", numbers)

num = int(input("Enter the number:"))

if num in numbers:
    print("Number is available")
    print("Count:", numbers.count(num))
    print("Index:", numbers.index(num))
else:
    print("Number is not available")

print("Smallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total sum:", sum(numbers))
'''
#Q3
'''
# Even and Odd Number Separator - 3

numbers = [12, 17, 22, 27, 32, 37]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

print("First 2:", numbers[:2])
print("Last 1:", numbers[-1:])

backup = numbers.copy()

numbers.clear()

print("Original list:", numbers)
print("Backup list:", backup)
'''
#Q4
'''
# Unique Name Manager - 4

names = ["Ravi", "Sita", "Ravi", "Kiran", "Sita"]

names = set(names)

print("Unique names:", names)

names.add("Anu")
names.update(["Raj", "Pooja"])

if "Kiran" in names:
    names.remove("Kiran")

names.discard("Mohan")

print("Final unique names:")

for name in names:
    print(name)
'''
#Q5
'''
names=["chandu","Rahul","mani","jeev","Rahul"]
a=set(names)
print(a)
a.add("babbi")
a.update({'madhan','niharika'})
print("the names added:",a)
if "John" in a:
    print("name found!")
    a.remove("mani")
    print("after removing mani:",a)
a.discard('jeev')
print("after discarding jeev:",a)
print("Final unique names:")
for i in a:
    print(i)
'''
