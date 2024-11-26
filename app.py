import time

user_prompt="Enter a todo"
# todos=[]

#way1
#from functions import get_todos,write_todos
#way2
from modules import functions

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)

while True:
    user_action=input("Type add, show, edit, complete or exit:=")
    user_action=user_action.strip() ##remove spaces

    if user_action.startswith("add"):
    #if 'add' in user_action:

        todo=user_action.replace("add","").strip(" ")
        #todo = input(user_prompt) + "\n"

        # file=open('file/todo.txt', 'r')
        # todos=file.readlines()
        # file.close()

        todos = functions.get_todos()

        todos.append(todo)

        # file=open('file/todo.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos_arg=todos)
        """with open('file/todo.txt', 'w') as file:
            file.writelines(todos)"""

    elif user_action.startswith("show"):
    #elif 'show' in user_action:

        todos = functions.get_todos("todo.txt")

        # file=open('file/todo.txt', 'r')
        # todos=file.readlines()
        # file.close()

        # new_todo=[]
        #
        # for item in todos:
        #     new_item=item.strip("\n")
        #     new_todo.append(new_item)

        # new_todo=[item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith("edit"):
    #elif 'edit' in user_action:
        #number = int(input("Number of the todo to edit:= "))
        try:
            number=int(user_action.replace("edit","").strip(" "))
            number = number - 1

            todos = functions.get_todos("todo.txt")

            new_todo = input("Enter new todo:= ")
            todos[number] = new_todo + '\n'

            functions.write_todos(filepath="todos.txt", todos_arg=todos)
            """with open('file/todo.txt', 'w') as file:
                file.writelines(todos)"""

            # print('Here is todos existing',todos)

            # print("Here is how it is will be",todos)
        except ValueError:
            print("Your command is not valid.")
            continue
            #user_action = input("Type add, show, edit, complete or exit:=")
            #user_action = user_action.strip()

    elif user_action.startswith("complete"):
    #elif 'complete' in user_action:
        try:
            #number = int(input("Number of the todo to complete:= "))
            number = int(user_action.replace("add", "").strip(" "))

            todos = functions.get_todos("todo.txt")
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(filepath="todos.txt", todos_arg=todos)
            """with open('file/todo.txt', 'w') as file:
                file.writelines(todos)"""

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
    #elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye!!!")


