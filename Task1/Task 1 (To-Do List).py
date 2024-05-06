class ToDoList:
def __init__(self):
self.tasks = []

def add_task(self, task):
self.tasks.append(task)
print("Task added successfully!")

def remove_task(self, task_index):
if 0 <= task_index < len(self.tasks):
del self.tasks[task_index]
print("Task removed successfully!")
else:
print("Invalid task index.")

def display_tasks(self):
if self.tasks:
print("Your To-Do List:")
for index, task in enumerate(self.tasks, start=1):
print(f"{index}. {task}")
else:
print("Your To-Do List is empty.")

def main():
todo_list = ToDoList()

while True:
print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task")
print("3. Display tasks")
print("4. Quit")

choice = input("Enter your choice: ")

if choice == '1':
task = input("Enter the task: ")
todo_list.add_task(task)
elif choice == '2':
task_index = int(input("Enter the task index to remove: ")) - 1
todo_list.remove_task(task_index)
elif choice == '3':
todo_list.display_tasks()
elif choice == '4':
print("Goodbye!")
break
else:
print("Invalid choice. Please try again.")

if __name__ == "__main__":
main()