def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        change_input = input(f"Do you want to change phone for {name}? y/n: ")
        if change_input == 'y':
            return change_contact(args, contacts)
        else:
            return "Contact not updated."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        add_input = input("Contact not exist. Do you want to add this contact? y/n: ")
        if add_input == 'y':
            return add_contact(args, contacts)
        else:
            return "New contact not added."
        
def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not exist."

def show_all(contacts):
    all_contacts = ''
    for name, phone in contacts.items():
        all_contacts += f'{name}: {phone}\n'

    if all_contacts != '':
        return all_contacts
    else: 
        return "Contact list is empty."

def show_help():
    help_info = '''
        hello - just text greetings
        add - add [name] [phone]: adding new contact with phone
        change - change [name] [phone]: change existing contact phone
        phone - phone [name]: show phone of contact
        all - show all contacts with phones
        close - close the program
        exit - close the program
        help - show all existing commands
    '''
    return help_info

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Print 'help' for list of existing commands")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == 'change':
                print(change_contact(args, contacts))
            elif command == 'phone':
                print(show_phone(args, contacts))
            elif command == 'all':
                print(show_all(contacts))
            elif command == 'help':
                print(show_help())
            else:
                print("Invalid command.")
        except:
            print("Invalid command.")

if __name__ == "__main__":
    main()