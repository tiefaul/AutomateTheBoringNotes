#! Python3
# First self project

def toDo():
    toDo_list = {}
    while True:
        list = input("List something you need to do and press 'Enter'. To exit type 'exit': ")

        if list.lower() == 'exit':
            break
        
        toDo_list[list] = " "

    print(toDo_list)
    print("Check off things you have completed: ")

