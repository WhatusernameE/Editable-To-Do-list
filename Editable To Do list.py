# Build a program that lets you create a to do list. It should let you add and remove items from the list


def remove():

    todo.remove(user)


def extend():

    todo.append(userThree)
    
    
todo = ['Sweeping', 'Dishes', 'Vacuuming', 'Kitchen Table']
print(todo)

while True:
    user = input("What chore do you want to do?")
    print('Your chore is: ', user)

    userTwo = input("\nWould you like to add another chore?")
    if userTwo == 'yes':
        
        userThree = input("\nAdd your chore: ")
        print('\nYour extra chore is: ', userThree)
        extend()
        print(todo)

    complete = input("\nDid you complete original chore? ")
    
    if complete == "yes":
    
        if user == "Sweeping":
            remove()
            print(todo)
            
        elif user == "Dishes":
            remove()
            print(todo)
            
        elif user == "Vacuuming":
            remove()
            print(todo)
            
        elif user == "Kitchen Table":
            remove()
            print(todo)
            
        elif user == userThree:
            remove()
            print(todo)
            
        else:
            print("Stupid")
            quit()
    else:
        print("You cant spell: Yes")

    if todo == []:
        print('You completed your chores!')
        print("Congrats!")
        quit()
