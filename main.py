contacts = {}
valid_command = ['show all', 'add',  'search', 'delete', 'exit']

def main(): 
    while True:
        #Ask the user what they want to do?
        user_func = input('What do you want to do? (show all, add, search, delete, exit): ')
        if user_func not in valid_command:
            print('Invalid command')
            pass
        else:
            #if the user said show all 
            if user_func == 'show all':
                if not contacts:
                    print('No contacts saved.')
                else:
                    output_list = []
                    for name, pn in contacts.items():
                        contacts_str = f"{name}: {pn}"
                        output_list.append(contacts_str)
                    
                    output = ", ".join(output_list)
                    print(output)
            
            #if the user said add
            elif user_func == 'add':
                #Handle name
                name = input('Name: ')
                if name in contacts:
                    print ('Name already used')
                    continue
                if name == '':
                    print ('Please type in a name')
                    continue
                #Handle phone number
                pn = input('Phone Number: ')
                if pn == '':
                    print('Please type in phone number')
                    continue
                if not pn.isdigit():
                    print('Invalid phone number')
                    continue
                if pn in contacts.values():
                    print('Phone Number already used')
                    continue
                #Update contacts
                contacts.update({name: pn})
            
            #if the user said search
            elif user_func == 'search':
                user_search = input('Name: ')
                if user_search in contacts:
                    pn = contacts[user_search]
                    print(f"{user_search}'s phone number is {pn}")
                else:
                    print("Contact not found")
            
            #if the user said delete 
            elif user_func == 'delete':
                user_delete = input('Name: ')
                if user_delete in contacts:
                    del contacts[user_delete]
                    print(f"{user_delete} is deleted")
                else:
                    print("Contact not found")
            elif user_func == 'exit':
                print('Goodbye!')
                break

main()