def get_todos(filepath="todo.txt"):
    with open(f'file/{filepath}', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath,todos_arg):
    with open(f'file/{filepath}', 'w') as file:
        file.writelines(todos_arg)

def count(phrase):
    return phrase.count('.')