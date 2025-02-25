import json
class ToDoList:
    def __init__(self, dosya_adi = "taskler.json"):
        self.running = True
        self.dosya_adi = dosya_adi
        self.tasks = []
        self.dosyayi_oku()
        
    def dosyayi_yaz(self):
        with open(self.dosya_adi, "w") as dosya:
            json.dump(self.tasks, dosya, indent=4)
            
    def dosyayi_oku(self):
        try:
            with open(self.dosya_adi, "r") as dosya:
                self.tasks = json.load(dosya)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
        
    def menu(self):
        while self.running:
            print("Please select what you want to do:\n1: Adding task\n2: Removing task\n3: Task completed\n4: Listing task\nQ: Exit")
           
            
            selection = input("Your selection is: ").strip().upper()
            if selection == "Q":
                print("Exit is in progress..")
                self.running = False
            elif selection == "1":
                self.addTask()
            elif selection == "2":
                self.removeTask()
            elif selection == "3":
                self.completeTask()
            elif selection == "4":
                self.listingTask()
            else:
                print("invalid selection, pleaase try again!")
    
        
    def addTask(self):
        task_name = input("Task which you want to add: ").strip()
        if task_name:
            new_id = 1 if not self.tasks else self.tasks[-1]["id"] + 1
            self.tasks.append({"id" : new_id, "task": task_name, "completed": False})
            self.dosyayi_yaz()
            print(f"task added: {task_name}")
            
    def removeTask(self):
        self.listingTask()
        task_id = input("Id which you want to remove: ").strip()
        if task_id.isdigit():
            task_id = int(task_id)
            self.tasks = [task for task in self.tasks if task["id"] != task_id]
            self.dosyayi_yaz()
            print(f"Task {task_id} removed")
            
    def completeTask(self):
        self.listingTask()
        task_id = input("Task id you want to mark as comleted: ").strip()
        if task_id.isdigit():
            task_id = int(task_id)
            for task in self.tasks:
                if task["id"] == task_id:
                    task["completed"] = True
                    self.dosyayi_yaz()
                    print(f"Task {task_id} mark as completed. ")
                    return
            print("Task not found!")
        else:
            print("Please enter a valid id!")
            
    def listingTask(self):
        if not self.tasks:
            print("No tasks available")
            return
            
        self.tasks = sorted(self.tasks, key=lambda x: x["id"])
        print("\nList of tasks:")
        for task in self.tasks:
            durum = "+" if task["completed"] else "x"
            print(f"{task['id']}: {task['task']} [{durum}]")
        
        
            
if __name__ == "__main__":
    toDo = ToDoList()
    toDo.menu()
    
                   
            
            
         
        