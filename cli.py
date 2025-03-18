import functions
import time

now = time.strftime("%d %b %Y, %H:%M:%S")
while True:
    user_action = input('Enter add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}.{item}')
        print(f'there are {len(todos)} items in the todo')
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input(f'Enter a new ToDo for {number+1}: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
            print(f"Last edited: {now}")
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            print(f'{todo_to_remove} is completed')
            todos.pop(index)

            functions.write_todos(todos)
        except IndexError:
            print("Number is out of range")
            continue

    else:
        print('Unknown command, please try again!')

