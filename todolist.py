Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> todo_list=[]
>>> # Main program loop
... while True:
...     print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
...     choice = input("Enter your choice: ")
... 
...     if choice == "1":
...         todo_list.append(input("Enter a task: "))
...     elif choice == "2":
...         if not todo_list:
...             print("Your to-do list is empty.")
...         else:
...             print("Your to-do list:")
...             for index, task in enumerate(todo_list, start=1):
...                 print(f"{index}. {task}")
...     elif choice == "3":
...         if not todo_list:
...             print("Nothing to remove. Your to-do list is empty.")
...         else:
...             view_tasks = "\n".join([f"{index}. {task}" for index, task in enumerate(todo_list, start=1)])
...             print(f"Tasks:\n{view_tasks}")
...             del todo_list[int(input("Enter the number of the task to remove: ")) - 1]
...             print("Task removed successfully!")
...     elif choice == "4":
...         print("Exiting program.")
...         break
...     else:
...         print("Invalid choice. Please try again.")
... 
...         

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 1
Enter a task: eat

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: play
Invalid choice. Please try again.

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 1
Enter a task: play

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 1
Enter a task: cook

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: clean
Invalid choice. Please try again.

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
