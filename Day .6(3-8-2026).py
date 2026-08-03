'''
control statements --> control of flow execution of the program
                   --> conditional statement --> if, elif, else.....
                   --> Rwpetition statement(Loops)--> for,while,(fro with else)(while with else)
                   --> Jumping Statements -->break,continue,pass
'''

#Loops --> Loops are helpful for repetition (Automative tasks)
#for keyword will be helpful to iterate over a sequence / range 
#syntax for(for keyword):

'''
for <temp_var> in range/sequence:
    statement(s)..........
    ..............

'''

'''
#range function(start,stop,step)
#by default range picks 0 as start value
for i in range (10):
    print(i)
#In above case we got 10 iterations
   '''
'''
for i in range(1,10):
    #if i > 5:
     #   print(f' value of i is -->{i}')
    if i >5 and i%2 == 0:
        print(f' value of i is -->{i}')
        
'''
'''
for i in range(1,10,-1):
    print(i)
    print("Done")


    '''
'''
#print -10 to -1


for i in range(-10,0):
    print(i)
  '''
'''
#[] --> we generally Lists
names = ['madhan','mani','akash']
print(len(names))
for i in names:
    #print(names)
    #print(f'studrnt name is {names}')
    if names =="sairam":
        print(f"studrnt name is {names}")
'''
'''
# calculate the sum of first 10 numbers
#first understand your input  --> range(11) -->10 numbers
#second we need to map the logic
result=0
for i in range(11):

    result = result +i
    
    print(f' now the result is {result}')
    print(f'sum of 10 numbers is {result}')
'''
'''
result=0
for i in range(21):
    if i%2==0:
        result = result +i
    print(result)
    '''

work_log=[0,1,1,1,0,1,0]
longest_streak=0
current_streak=0
for day in work_log:
    if day==1:
        current_streak= current_streak+1
        if longest_streak > longest_streak:
              longest_streak = current_steak
print(longest_streak)

                
