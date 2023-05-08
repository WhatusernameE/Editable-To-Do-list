# Build a program that lets you create a to do list. It should let you add and remove items from the list
#

todo = []

user = input("What chores do you need to do?")

if user:
    todo.append(user)
    print(todo)
    complete = input("Did you complete a chore?")

    if complete == "yes":

        chore = input("Which chore?")
        if chore == "Sweeping":
            todo = ["Dishes, Vacuuming"]
            print(todo)
        elif chore == "Dishes":
            todo = ["Sweeping", "Vacuuming"]
            print(todo)
        elif chore == "Vacuuming":
            todo = ["Sweeping", "Dishes"]
            print(todo)
        else:
            print("Stupid")
            quit()
