#! Python3
# First self project

def toDo():
    toDo_list = {}
    while True:
        list = input("List something you need to do and press 'Enter'. To exit type 'exit': ")

        if list.lower()  == 'exit':
            break
        
        toDo_list[list] = " "

    for task in toDo_list.keys():
        print(f"{task}:")
        

    while True:
        completed = input("Type things you have completed to add an 'X' next to it: ")

        if completed in toDo_list:
            toDo_list[completed] = 'X'

        elif completed.lower() == 'exit':
            break
        
        elif completed not in toDo_list:
            print("This is not in your list.")
        
        
    for task, status in toDo_list.items():
        print(f"{task} : {status}")

toDo()