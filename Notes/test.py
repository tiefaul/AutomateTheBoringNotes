# Testing page
print("List things you have to do today, leave blank to close out:")

list = {}

def toDo_list():
    while True:
        add_list = input()
        if add_list.isalpha():
            list[add_list] = " "
        elif add_list == "":
            break
toDo_list()
print(list)
#complete_list()
