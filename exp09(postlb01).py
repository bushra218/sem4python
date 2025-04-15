#Aim:Write a Python Program to Reverse a Stack using Recursion.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03

def reverse_stack(stack):
    if stack:
        # Pop the top element
        element = stack.pop()
        # Recursively reverse the rest of the stack
        reverse_stack(stack)
        # Push the popped element to the bottom
        insert_at_bottom(stack, element)

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
    else:
        # Pop and recursively insert
        top = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(top)

# Driver code
stack = list(map(int, input("Enter elements of the stack separated by space: ").split()))

print("Original Stack:", stack)
reverse_stack(stack)
print("Reversed Stack:", stack)

print("Exiting program...\nThankYou \nAnsari Bushra \n03 \n231P046")
