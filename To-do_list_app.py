tasks_list=[]
while True:
    print(f"-"*50)
    print(f"-:Welcome to the to-do list program:-\n\tPlease select one of the options:")
    print("1.Add Task\n2.View Tasks\n3.Mark Task as done\n4.Delete task\n5.Exit")
    
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input! Please enter a number!")
        continue
        
    # Add a task
    if choice == 1:
        print(f"-"*50)
        task_name=input("Enter the task name:").strip()
        
        if task_name == "":
            print("Task cannot be empty!")
        else: 
            tasks_list.append({"Task":task_name,"Done":False})
            print("Task Added Successfully!")
    
    # View tasks
    elif choice == 2:
        print(f"-"*50)
        
        if not tasks_list:
            print("No tasks available!")
        else:
            for i,value in enumerate(tasks_list,start=1):
                if value["Done"]:
                    status="✅"
                else:
                    status="❌"
                    
                print(f"{i}.{value['Task']} [{status}]")
        
    # Mark task done
    elif choice == 3:
        print(f"-"*50)
        
        if not tasks_list:
            print("No tasks available!")
            continue
        
        try:
            user_input=int(input("Enter the task number:"))
            index=user_input - 1

            if index < 0 or index >= len(tasks_list):
                print("Invalid Index!")
            else:
                tasks_list[index]["Done"]=True
                print("Task mark done successfully!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Delete a task
    elif choice == 4:
        print(f"-"*50)
        if not tasks_list:
            print("No tasks available!")
            continue
        
        try:
            user_input=int(input("Enter the task number:"))
            index=user_input - 1

            if index < 0 or index >= len(tasks_list):
                print("Invalid Index!")
            else:
                tasks_list.pop(index)
                print("Task deleted successfully!")
        except ValueError:
            print("Please enter a valid number!")

    
    # Exit
    elif choice == 5:
        print(f"-"*50)
        print("Thank you for using the program!")
        print(f"-"*50)
        break
    
    else:
        print("Invalid choice!")
