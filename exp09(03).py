# A python program to create a linked list and perform operation on list.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03
# create empty linked list
l1=[]

# add some string type to l1
l1.append ("Hindustan");
l1.append ("Bharat");
l1.append ("India");

# display the list
print (" Existing list : ", l1)

# display menu
choice=0;
while (choice<5):
    print (" Linked list Opeartions ")
    print (" 1. Add Element ")
    print (" 2. Remove Element ")
    print (" 3. Replace Element ")
    print (" 4. Search Element ")
    print (" 5. Exit ")
    choice=int(input(" Enter Your choice :"))

    # perform task depending on users choice
    if choice==1:
        element=(input("Enter Element : "))
        pos=int(input("Enter Position : "))
        l1.insert(pos, element)

    elif choice==2:
        try:
            element=(input("Enter Element : "))
            l1.remove(element)
        except valueError:
            print("element not found")

    elif choice==3:
        element=(input("Enter new Element : "))
        pos=int(input("Enter Position : "))
        l1.pop(pos)
        l1.insert(pos, element)

    elif choice==4:
        element=(input("Enter new Element : "))
        try:
            pos=l1.index(element)
            print("element found at position: ",pos)
        except valueError:
            print("element not found")
    else:
        print("Exiting program...\nThankYou \nAnsari Bushra \n03 \n231P046")
        break

    # display element list
    print (" List: ",l1)
