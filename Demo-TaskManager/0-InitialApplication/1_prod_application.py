def todo_list(listo: list = None) -> None:

    if listo is None:
        listo = []
    
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("="*50)
        x: str = input("Enter your choice: ")
        if x == '1':
            tsk = input("Enter task: ")
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

todo_list()
# this is a test lol
lizzo = 'flautist'
nicki_minaj = 'rapper'
benson_boone = 'backflipper'
azelia_banks = 'canceled'

artists_list = [lizzo, nicki_minaj, benson_boone, azelia_banks]
print(artists_list)

# test two
new_list = [1,2,3]

t = 'Taylor Swift'

def artist(arg1: str) -> None:
    print(f'And the Grammy goes to... {arg1}!')

s = artist(t)
print(s)



