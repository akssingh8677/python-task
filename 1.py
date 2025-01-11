# Simple To-Do List Application

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1] = new_task
            print(f'Task {task_number} updated to "{new_task}".')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print("Invalid task number.")

def main():
    todo = Todo()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo.add_task(task)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo.update_task(task_number, new_task)
        
        elif choice == '4':
            todo.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
