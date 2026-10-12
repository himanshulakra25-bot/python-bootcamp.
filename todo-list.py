
tasks = []

while True:
    print("\n----- TODO APP -----")
    print("1. Add an item")
    print("2. Delete an item at index")
    print("3. Remove the last item")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            task = input("Enter a task (-1 to go back): ")

            if task == "-1":
                break

            tasks.append(task)
            print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("List is empty!")
        else:
            print("Current list:", tasks)
            index = int(input("Enter index to delete: "))

            if 0 <= index < len(tasks):
                del tasks[index]
                print("Updated list:", tasks)
            else:
                print("Invalid index!")

    elif choice == "3":
        if len(tasks) > 0:
            tasks.pop()
            print("Updated list:", tasks)
        else:
            print("List is empty!")

    elif choice == "4":
        tasks.sort()
        print("Sorted list:", tasks)

    elif choice == "5":
        print("Your To-Do List:", tasks)

    elif choice == "6":
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
