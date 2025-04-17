import sys

#Create contact dictonary
contacts = {}
#Lists of valid command
valid_command = ['-add', '-delete', '-search', '-showall']


#main function
def main():
    while True:
        #Check if the user have put in command or not 
        if len(sys.argv) == 1:
            print('Command-line not found.')

        #If user put in invalid command
        elif len(sys.argv) == 2 or len(sys.argv) == 3:
            if sys.argv[1] not in valid_command:
                print ('Invalid command-line')
            #When the command [2] is valid
            else:
                if len(sys.argv) == 2: 
                    #If the user ask for show all
                    if sys.argv[1] == '-showall':
                            print (contacts)
                    #If the user ask for add
                    elif sys.argv[1] == "-add": 
                        user_input_name = input('Name: ')
                        try:
                            user_input_pn = int(input('Phone Number: '))
                        except ValueError:
                            print ('Please enter a valid phone number')
                        #Add the informations into the dictonary
                        contact = {user_input_name: user_input_pn}
                        contacts.update(contact)
            
            #If the user ask for add, search, and delete
                elif len(sys.argv) == 3:
                    #If the user ask for search
                    if sys.argv[1] == '-search': 
                        if sys.argv[2] in contacts:
                            for contact in contacts:
                                print(contact)
                        elif sys.argv[2] == '':
                            print('Please put the name of the contact you want to search.')
                    
                    #If the user ask for delete
                    elif sys.argv[1] == '-delete':
                        if sys.argv[2] in contacts:
                            for contact in contacts:
                                contacts.update('')
                        elif sys.argv[2] == '':
                            print('Please put the name of the contact you want to delete.')
                    else:
                        print("Invalid usage")
                    

main()
