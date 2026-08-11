'''
a=input("enter the sentence")
print(a.lower())
print(a.upper())
print(a.title())
print(a.capitalize())
print(a.swapcase())
'''
'''
a= input("Enter the Sentence")
methods=["upper", "lower"," title","capitalize"," swapcase"," casefold", "isupper","islower", "istitle"]
for a in methods:
    if a=="upper":
        print("upper",methods)

'''
'''
elif a.lower():
        print(a)
    elif a.title():
        print(a)
'''
'''
sentence = input("Enter the Sentence: ")

methods = ["upper", "lower", "title", "capitalize", "swapcase", "casefold", "isupper", "islower", "istitle"]

for method in methods:
    if method == "upper":
        print("upper:", sentence.upper())

    elif method == "lower":
        print("lower:", sentence.lower())

    elif method == "title":
        print("title:", sentence.title())
    elif method == "capitalize":
        print("capitalize:", sentence.capitalize())
    elif method == "swapcase":
        print("swapcase:", sentence.swapcase())
    elif method == "casefold":
        print("casefold:", sentence.casefold())
    #elif method == "isupper":
        #print(issupper
else:
    print("hgch")
'''

'''
name=input("enter user name")

methods=[ "isalnum", "isalpha","isidentifier", "isascii"]

while True:
    
    if name == "isalnum":
        value=input("enter a string:")
        print("isalnum",value.isalnum())
        
    elif name == "isalpha":
        value=input("enter a string:")
        print("isalpha",name.isalpha())
        
    elif name == "isidentifier":
        value=input("enter a string:")
        print("isidentifier",name.isidentifier())
        
        
    elif name == "isascii":
        value = input("Enter a string: ")
        print("isascii",name.isascii())
        
    else:
        print("Invalid method")

        name = input("\nEnter method name or 'quit': ")

print("Program ended")
'''

name = input("Enter username: ")

while True:

    if name == "quit":
        break

    print("isalnum:", name.isalnum())

    if name[0].isalpha():
        print("First character is a letter")
    else:
        print("First character is not a letter")

    print("isidentifier:", name.isidentifier())

    print("isascii:", name.isascii())

    name = input("\nEnter username or 'quit': ")

print("Program ended")



    


