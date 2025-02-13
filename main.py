class ToDoList:
    def __init__(self):
        self.running = True
        
    def menu(self):
        while self.running:
            print("Please select what you want to do:\n1: Adding task\n2: Removing task\n3: Task completed\n4: Listing task\nQ: Exit")
           
            
            selection = input("Your selection is: ")
            if selection == "Q":
                print("Exit is in progress..")
                self.running = False
            elif selection == "1":
                self.addingTask()
            elif selection == "2":
                self.removingTask()
            elif selection == "3":
                self.taskCompleted()
            elif selection == "4":
                self.listingTask()
            else:
                print("invalid selection, pleaase try again!")
    
    def addingTask(self):
        print("Adding task selected.")
    def removingTask(self):
        print("Removing task selected.")
    def taskCompleted(self):
        print("Task completed selected.")
    def listingTask(self):
        print("Listing task selected.")
        
if __name__ == "__main__":
    toDo = ToDoList()
    toDo.menu()
    
                   
            
            
         
        