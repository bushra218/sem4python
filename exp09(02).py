"""Aim:WAP to perform following operation on queue
(i) Add
(ii) Delete
(iii) Search
(iv) Exit"""
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03
class Queue:
    def __init__(self):
        self.queue = []

    
    def add(self, element):
        self.queue.append(element)
        print(f"Element {element} added to the queue.")

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot delete.")
            return None
        return self.queue.pop(0)

    
    def search(self, element):
        if element in self.queue:
            return self.queue.index(element)  
        return -1  

    
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print(f"Current queue: {self.queue}")



def menu():
    q = Queue()
    
    while True:
        print("\nQUEUE OPERATIONS")
        print("1. Add Element")
        print("2. Delete Element")
        print("3. Search Element")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            element = input("Enter element to add: ")
            q.add(element)
        elif choice == 2:
            deleted_element = q.delete()
            if deleted_element is not None:
                print(f"Deleted element: {deleted_element}")
        elif choice == 3:
            element = input("Enter element to search: ")
            position = q.search(element)
            if position == -1:
                print(f"Element {element} not found in the queue.")
            else:
                print(f"Element {element} found at position {position} in the queue.")
        elif choice == 4:
            print("Exiting program...\nThankYou \nAnsari Bushra \n03 \n231P046")
            break
        else:
            print("Invalid choice! Please enter a valid option between 1 and 4.")
        
        q.display()


menu()
