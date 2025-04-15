# using Stack class of stack.py program
from stack import Stack

#create empty  stack object
s=Stack()

# display menu
choice=0
while choice<5:
    print("STACK OPERATIONS")
    print("1. Push Element")
    print("2. Pop Element")
    print("3. Peep Element")
    print("4. Search an Element")
    print("5. Exit")
    choice=int(input("Enter Your Choice"))

    # perform task on users choice
    if choice==1:
        element=int(input("Enter Element :"))
        s.push(element)
    elif choice==2:
        element=s.pop()
        if element==-1:
            print("Stack is empty")
        else:
            print("Popped Element :",element)
    elif choice==3:
        element=s.peep()
        print("Top most element :",element)

    elif choice==4:
        element=int(input("Enter Element :"))
        pos=s.search(element)
        if pos==-1:
            print("Stack is empty")
        elif pos==-2:
            print("Elemnt not found in the stack")
        else:
            print("Element found at position:",pos)
    else:
        print("Program is exiting...\nThankYou \nAnsari Bushra \n03 \n231P046")
        break
    # display the content of stack object
    print("Stack=",s.display())
