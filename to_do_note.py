import json
from time import sleep

JSON_FILE_NAME = "ToDoList.json" # JSON FILE NAME

# DEALING WITH JSON FILE
def deal_with_json_file(operation):
    if operation == "SHOW":
        with open(JSON_FILE_NAME,"r") as json_file:
            file_data = json.load(json_file)
            json_file.close()
            return file_data
    elif operation == "UPDATE":
        json_file = open(JSON_FILE_NAME,"r")
        file_data = json.load(json_file)
        json_file = open(JSON_FILE_NAME,"w")
        return file_data,json_file

# USER INTERFACE FUNCTION
def userInterface(): # Return Int Value - Range(0-5)
    print("="*44)
    print("-"*12,f" ## TO-DO-LIST ## ","-"*12)
    print("="*44)
    while True:
        print(f"\t~ Select Options Number ~")
        print("\t","-"*23)
        print("[1] Show\t [2] Add\t [3] Check")
        print("[4] Delete One\t [5] Delete All")
        print("[0] Exit\n")
        user_input = input("~: ")
        if user_input in ["0","1","2","3","4","5"]:
            return int(user_input)
        else:
            print(f"[!] WRONG CHOIS\n")
            sleep(1)

# SHOW TO-DO LIST
def list_todo_items(todo):
    for i in range(0,len(todo)):
        id = todo[i].get('id')
        title = todo[i].get('title')
        discription = todo[i].get('discription')
        todo_case = todo[i].get('case')
        if todo_case:
            checked = "#"
        else:
            checked = " "
        show = f"({id}) {title} [{checked}]\n{discription}\n"
        print(show)

# ADD NEW TO-DO Item || CHECK TO-DO AS DONE
def update_todo_item(todo=0,json_file=0,operation=0):
    if operation == 'ADD':
        for i in range(0,len(todo)):
            id = int(todo[i].get('id'))+1

        while True:
            title = input("TO-DO Title: ")
            if len(title) == 0:
                print("[!] TO-DO Title is required")
            else:
                break
        discription = input("TO-DO Discription: ")
        try:
            new_todo = {"id": id, "title": title, "discription": discription, "case": False}
            todo.append(new_todo)
            json.dump(todo,json_file)
        except:
            id = 1
            new_todo = {"id": id, "title": title, "discription": discription, "case": False}
            todo.append(new_todo)
            json.dump(todo,json_file) 
        json_file.close()
        final_value = '-'*12
        final_value += ' The TO-DO Created '
        final_value += '-'*12
        final_value += f"\nTO-DO ID: {id}\n"
        final_value += f"TO-DO Title: {title}\n"
        final_value += f"TO-DO Discription: {discription}\n"
        final_value += '-'*43
        return final_value
    elif operation == 'CHECK':
        while True:
            user_input = input("What is The TO-DO ID: ")
            if len(user_input) != 0:
                break
        msg = f"[!] No TO-DO ID With {user_input} ID" # USER INPUT NOT EXIST MESSAGE
        for i in range(0,len(todo)):
            if int(todo[i].get('id')) == int(user_input):
                # START UPDATE THE TO-DO CHECK CASE
                todo,json_file = deal_with_json_file(operation='UPDATE')
                id = todo[i].get('id')
                print(id)
                title = todo[i].get('title')
                discription = todo[i].get('discription')
                todo[i].update({"id": id, "title": title, "discription": discription, "case": True})
                json.dump(todo,json_file)
                json_file.close()
                msg = f"TO-DO {user_input} CHECKED" # CHECK OPERATION DONE MESSAGE
                break
        return msg
        
# DELETE ONE TO-DO OR ALL TO-DO LIST
def delete_todo(todo=0,operation=0):
    if operation == 'ONE':
        user_input = input("What is The TO-DO ID: ")
        msg = f"[!] No TO-DO ID With {user_input} ID" # USER INPUT NOT EXIST MESSAGE
        for i in range(0,len(todo)):
            if int(todo[i].get('id')) == int(user_input):
                # START DELETE THE TO-DO
                todo,json_file = deal_with_json_file(operation='UPDATE')
                ask_user = input("Are You Sure About Delete This TO-DO [y/n]: ").upper()
                if ask_user == "Y":
                    del todo[i]
                    msg = f"TO-DO With ID {user_input} Deleted"
                    json.dump(todo,json_file)
                    json_file.close()
                    break
                else:
                    msg = f"TO-DO With ID {user_input} Do Not Deleted"
                break
        return msg

    elif operation == 'ALL':
        # START DELETE THE TO-DO
        todo,json_file = deal_with_json_file(operation='UPDATE')
        ask_user = input("Are You Sure About Delete ALL TO-DO List [y/n]: ").upper()
        if ask_user == "Y":
            count = 0
            for i in range(0,len(todo)):
                count += 1
                todo.pop()
            msg = f"TO-DO LIST Deleted With {count} Item"
            json.dump(todo,json_file)
            json_file.close()
        else:
            msg = "TO-DO LIST Do Not Deleted"
        
        return msg

# MAIN FUNCTION
def main():
    if __name__ == '__main__':
        while True:
            user_chois = userInterface()
            if user_chois == 0: # EXIT
                print("~ Exiting ~")
                exit()
            elif user_chois == 1: # SHOW
                todo_dict = deal_with_json_file(operation='SHOW')
                list_todo_items(todo_dict)
            elif user_chois == 2: # ADD
                todo_dict,json_file = deal_with_json_file(operation='UPDATE')
                show = update_todo_item(todo_dict,json_file,operation='ADD')
                print(show)
            elif user_chois == 3: # CHECK
                todo_dict = deal_with_json_file(operation='SHOW')
                show = update_todo_item(todo=todo_dict,operation='CHECK')
                print(show)
            elif user_chois == 4: # DELETE ONE
                todo_dict = deal_with_json_file(operation='SHOW')
                show = delete_todo(todo_dict,operation='ONE')
                print(show)
            elif user_chois == 5: # DELETE ALL
                show = delete_todo(operation='ALL')
                print(show)
            input('[PRESS ENTER TO CONTINUE]')

# Call Main Function
main()
