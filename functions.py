FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Return the data read of opened file"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the Data in textfile"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)