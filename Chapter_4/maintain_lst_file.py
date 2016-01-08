import sys
import os
import collections

ADD = 0
DELETE = 1
SAVE = 2
QUIT = 3
CONTINUE = 4

TWO_ACTIONS = 0
ALL_ACTIONS = 1

NO_ITEM = 0

def main():
    lst_files = get_all_lst_files()
    input_file = get_string("\nChoose filename: ")
    filename = get_filename(input_file, lst_files)        
    items = show_items(filename, lst_files)
    while True:
        items = take_actions(filename, items)
        

class UnsupportedFileNameError(Exception): pass

def get_string(msg, minimum = 1, maximum = 50):
    filename = input(msg)
    if not minimum <= len(filename) <= maximum:
        raise UnsupportedFileNameError(
            "String is too short or too long")
    else:
        if filename.isdigit():
            return filename
    return filename

def get_all_lst_files():
    print("{0:-^30}".format("all lst files"))
    files = os.listdir(".")
    lst_files = list()
    count = 1
    for single_file in files:
        if single_file.endswith(".lst"):
            lst_files.append(single_file)
            print("{0}. {1}".format(count, single_file))
            count += 1
    return lst_files

def get_filename(name, lst_files):
    if name.isdigit():
        return lst_files[int(name) - 1]
    else:
        if name in lst_files:
            return name
        elif name:
            return name + '.lst'
        else:
            return None

def show_items(filename, lst_files):
    if filename is None or not filename in lst_files:
        print("\n{0:-^30}".format('no items are in the list'))
        return list()    
    lines = list()    
    for line in open(filename, encoding = "utf-8"):
        if line is not None:
            line = line.replace("\n", '')
            lines.append(line)
    if len(lines) == 0:
        print("no items in the list")
        return list()
    for i in range(len(lines)):
        print("{0}. {1}".format(i + 1,
                                lines[i]))
    print('')
    return lines

def take_actions(filename, items):
    if len(items) == NO_ITEM:
        action = get_action("[A]dd [Q]uit [a]: ", TWO_ACTIONS)
    else:
        action = get_action("[A]dd [D]elete [S]ave [Q]uit [a]: ", ALL_ACTIONS)

    if action == ADD:
        item = get_string("Add item: ")
        if item is not None:
           items.append(item)
    elif action == DELETE:
        item = get_string("Delete item: ")
        if item.isdigit() and 1 <= int(item) <= len(items):
            items.pop(int(item) - 1)
        else:
            items.remove(item)
    elif action == SAVE:
        user_input = input('Save unsaved changes(y/n)[y]: ')
        if user_input.lower() == 'y':
            fh = open(filename, mode = 'w', encoding = 'utf-8')
            for item in items:
                fh.write(item)
                fh.write('\n')
            fh.close()
        sys.exit()
    elif action == QUIT:
        sys.exit()
    else:
        pass
    for i in range(len(items)):
        print("{0}. {1}".format(i+1, items[i]))
    return items

def get_action(msg, actions_type):
    ERROR_MSG = "ERROR: invalid choice--enter one of {0}"
    action = input(msg).lower()
    if len(action) != 1:
        print("ERROR: wrong input, please enter again")
    if actions_type == TWO_ACTIONS:
        if not action in 'AaQq':
            action = err_action(ERROR_MSG.format("'AaQq'"))
    else:
        if not action in 'AaDdSsQq':
            action = err_action(ERROR_MSG.format("'AaDdSsQq'"))
    actions = dict(a = ADD, d = DELETE, s = SAVE, q = QUIT, c = CONTINUE)
    return actions[action]                    
                                
def err_action(msg):
    print(msg)
    action = input("Press Enter to continue...")
    if len(action) == 0:
        return 'c'
    else:
        return 'q'

main()
            
            


        
