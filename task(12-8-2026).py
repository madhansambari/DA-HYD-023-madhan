# TASK --> Data = ['codegnan','saketh','python','java'] -- Input
# Output should be as follows
'''
    0 : codegnan
    1 : saketh
    2 : python
    3 : java
'''


data = ['codegnan','saketh','python','java']
int = 0
for i in data:
    print(f"{int} : {i}")
    int += 1



for obj in data:
    print(data.index(obj),':',obj)


for obj in range(len(data)):
    print(obj,':',data[obj])
