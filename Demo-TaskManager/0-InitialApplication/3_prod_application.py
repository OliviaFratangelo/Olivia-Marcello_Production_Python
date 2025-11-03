"""
Generates a todo list application that allows users to add tasks,
view tasks, mark tasks as done, and exit the application.
"""
def to_do(listo: list = None) -> None:
    """
    Generates a todo list application that allows users to add tasks,
    view tasks, mark tasks as done, and exit the application.
    Args:
        listo (list, optional): _description_. Defaults to None.
    """
    if listo is None:
        listo = []
    while True:
        x: str = input("Enter your choice")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("="*50)
        if x == '1':
            tsk: str = input("Enter task: ")
            listo.append(tsk)
            print("-"*50)
        elif x == '2':
            print("Tasks:")
            for i, t in enumerate(listo):
                print(f"{i+1}. {t}")
            print("-"*50)
        elif x == '3':
            usr_input: str = input("Enter task number to mark as done: ")
            if 0 <=  int(usr_input) - 1 < len(listo): 
                listo.pop(int(usr_input) - 1)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif x == '4':
            print("Exiting.")
            print("-"*50)
            break
        else:
            print("Invalid choice.")
            print("-"*50)

output = to_do()

print(output)