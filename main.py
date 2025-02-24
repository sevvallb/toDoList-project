import json
class ToDoList:
    def __init__(self, dosya_adi = "taskler.json"):
        self.running = True
        self.dosya_adi = dosya_adi
        self.tasks = []
        
    def dosyayi_yaz(self):
        with open(self.dosya_adi, "w") as dosya:
            json.dump(self.tasks, dosya, indent=4)
        
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
        
    def addTask(self):
        task_adi = input("Task which you want to add: ").strip()
        if task_adi:
            yeni_id = 1 if not self.tasks else self.tasks[-1]["id"] + 1
            self.tasks.append({"id" : yeni_id, "task": task_adi, "added": False})
            self.dosyayi_yaz()
            print("task added: {task_adi}")
            
    def removeTask(self):
        self.listingTask()
        task_id = input("Id which you want to remove: ").strip()
        if task_id.isdigit():
            task_id = int(task_id)
            new_tasks = []           #silmek istenmeyenler için
            for task in self.tasks:
                if task["id"] != task_id:
                    new_tasks.append(task)
            self.tasks = new_tasks
            self.dosyayi_yaz()
            print("Task {task_id} removed")
            
        
        
if __name__ == "__main__":
    toDo = ToDoList()
    toDo.menu()
    
                   
            
            
         
        