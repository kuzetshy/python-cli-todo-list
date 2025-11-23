def show_tasks(task_list):
    print("--- Your tasks: ---")
    if not task_list:
        print("No tasks yet.")
    else:
       
        for i, task in enumerate(task_list, start=1):
            
         
            if task['completed']:
                status = "[x]"
            else:
                status = "[ ]"
            
            
            print(f"{i}. {status} {task['text']}")
            
    print("---------------------")

def add_task(task_list):
    task_text = input("enter task: ")
    new_task = {'text': task_text, 'completed': False}
    task_list.append(new_task)
    print(f"Task '{task_text}' added.")


def complete_task(task_list):
    show_tasks(task_list)
    task_number_str = input("Enter number of the task to complete: ")

    try:
        i = int(task_number_str) - 1
    except ValueError:
        print("Error: Enter only numbers!")
        return
    

    if i >= 0 and i < len(task_list):
        task_list[i]['completed'] = True
        print("Task completed!")
    else:
        print("Error: Invalid task number.")



def delete_task(task_list):
    show_tasks(task_list)
    task_number = input("Choose a task to delete:")

    try:
        i = int(task_number) - 1
    except ValueError:
        print("Error: Enter only numbers!")
        return

    if i >= 0 and i < len(task_list):
        removing = task_list.pop(i)
        print(f"Task '{removing['text']}' deleted!")
    else:
        print("Error: invalid task number.")




tasks = []
while True:
    print("1. Show all tasks.")
    print("2. Add task.")
    print("3. Note as completed.")
    print("4. Delete task.")
    print("5. Exit.")
    
    

    try:
        choice = int(input("Choose operation: "))
    except ValueError:
        print("Enter only numbers!")
        continue


    if choice == 1:
        show_tasks(tasks)
    elif choice == 2:
        add_task(tasks)
    elif choice == 3:
        complete_task(tasks)
    elif choice == 4:
        delete_task(tasks)
    elif choice == 5:
        break
