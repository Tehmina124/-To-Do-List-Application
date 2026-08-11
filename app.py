# ============================================
# Project Name : To-Do List Application
# Language     : Python
# Project      : Project 1 (DecodeLabs)
# Author       : Tehmina Anwar
# ============================================

tasks = []

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Count Tasks")
    print("6. Search Task")
    print("7. Mark Task as Completed")
    print("8. View Completed Tasks")
    print("9. Clear All Tasks")
    print("10. View Pending Tasks")
    print("11. Sort Tasks by Priority")
    print("12. Show Statistics")
    print("13. Mark Task as Pending")
    print("14. Exit")
    choice = input("Enter your choice (1-14): ")

    # ==========================
    # Add Task
    # ==========================
    if choice == "1":

        task = input("Enter your task: ").strip()

        if task == "":
            print("❌ Task cannot be empty!")

        else:

            priority = input("Enter Priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter Due Date (DD-MM-YYYY): ")

            tasks.append({
                "task": task,
                "priority": priority,
                "due_date": due_date,
                "status": "Pending"
            })

            print("✅ Task Added Successfully!")

    # ==========================
    # View Tasks
    # ==========================
    elif choice == "2":

        if len(tasks) == 0:
            print("❌ No tasks found.")

        else:

            print("\n========== YOUR TASKS ==========")

            for index, task in enumerate(tasks, start=1):

                print(f"""
Task {index}
Task     : {task['task']}
Priority : {task['priority']}
Due Date : {task['due_date']}
Status   : {task['status']}
""")

    # ==========================
    # Update Task
    # ==========================
    elif choice == "3":

        if len(tasks) == 0:
            print("❌ No tasks available.")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']}")

            try:

                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    new_task = input("Enter new task: ").strip()
                    new_priority = input("Enter New Priority (High/Medium/Low): ").capitalize()
                    new_due_date = input("Enter New Due Date (DD-MM-YYYY): ")

                    tasks[number-1]["task"] = new_task
                    tasks[number-1]["priority"] = new_priority
                    tasks[number-1]["due_date"] = new_due_date

                    print("✅ Task Updated Successfully!")

                else:
                    print("❌ Invalid Task Number!")

            except ValueError:
                print("❌ Please enter a valid number.")

    # ==========================
    # Delete Task
    # ==========================
    elif choice == "4":

        if len(tasks) == 0:
            print("❌ No tasks available.")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']}")

            try:

                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    deleted = tasks.pop(number-1)

                    print(f"✅ '{deleted['task']}' deleted successfully!")

                else:
                    print("❌ Invalid Task Number!")

            except ValueError:
                print("❌ Please enter a valid number.")

    # ==========================
    # Count Tasks
    # ==========================
    elif choice == "5":

        print(f"\n📋 Total Tasks: {len(tasks)}")

    # ==========================
    # Search Task
    # ==========================
    elif choice == "6":

        if len(tasks) == 0:

            print("❌ No tasks available.")

        else:

            keyword = input("Enter task to search: ").lower()

            found = False

            for index, task in enumerate(tasks, start=1):

                if keyword in task["task"].lower():

                    print(f"""
Task {index}
Task     : {task['task']}
Priority : {task['priority']}
Due Date : {task['due_date']}
Status   : {task['status']}
""")

                    found = True

            if not found:
                print("❌ Task not found.")

    # ==========================
    # Mark Completed
    # ==========================
    elif choice == "7":

        if len(tasks) == 0:

            print("❌ No tasks available.")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']} ({task['status']})")

            try:

                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    tasks[number-1]["status"] = "Completed"

                    print("✅ Task marked as Completed!")

                else:

                    print("❌ Invalid Task Number!")

            except ValueError:

                print("❌ Please enter a valid number.")

    # ==========================
    # View Completed Tasks
    # ==========================
    elif choice == "8":

        found = False

        for index, task in enumerate(tasks, start=1):

            if task["status"] == "Completed":

                print(f"""
Task {index}
Task     : {task['task']}
Priority : {task['priority']}
Due Date : {task['due_date']}
Status   : {task['status']}
""")

                found = True

        if not found:
            print("❌ No completed tasks.")

    # ==========================
    # Clear All Tasks
    # ==========================
    elif choice == "9":

        if len(tasks) == 0:

            print("❌ No tasks available.")

        else:

            confirm = input("Are you sure? (yes/no): ").lower()

            if confirm == "yes":

                tasks.clear()

                print("✅ All tasks deleted successfully!")

            else:

                print("Operation Cancelled.")

    # ==========================
    # View Pending Tasks
    # ==========================
    elif choice == "10":

        found = False

        for index, task in enumerate(tasks, start=1):

            if task["status"] == "Pending":

                print(f"""
Task {index}
Task     : {task['task']}
Priority : {task['priority']}
Due Date : {task['due_date']}
Status   : {task['status']}
""")

                found = True
        if not found:
            print("🎉 No pending tasks.")

    # ==========================
    # Sort Tasks by Priority
    # ==========================
    elif choice == "11":

        if len(tasks) == 0:
            print("❌ No tasks available.")

        else:

            priority_order = {"High": 1, "Medium": 2, "Low": 3}

            tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))

            print("✅ Tasks sorted by priority.")

    # ==========================
    # Show Statistics
    # ==========================
    elif choice == "12":

        total = len(tasks)
        completed = 0
        pending = 0

        for task in tasks:

            if task["status"] == "Completed":
                completed += 1
            else:
                pending += 1

        print("\n========== TASK STATISTICS ==========")
        print(f"Total Tasks      : {total}")
        print(f"Completed Tasks  : {completed}")
        print(f"Pending Tasks    : {pending}")
       # ==========================
    # Mark Task as Pending
    # ==========================
    elif choice == "13":

        if len(tasks) == 0:

            print("❌ No tasks available.")

        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']} ({task['status']})")

            try:

                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):

                    tasks[number-1]["status"] = "Pending"

                    print("✅ Task marked as Pending!")

                else:
                    print("❌ Invalid Task Number!")

            except ValueError:
                print("❌ Please enter a valid number.")

    # ==========================
    # Exit
    # ==========================
    elif choice == "14":

        print("\n👋 Thank You! Have a Nice Day.")
        break

    else:
        print("❌ Invalid Choice! Please select between 1 and 14.")
