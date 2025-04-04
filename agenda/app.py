phonebook = {} # clave=name, value=number
msg_no_contact = '\nThe contact does not exist in the Phonebook!\n'
def show_contacts():
    if not phonebook:
        print('\nThe Phonebook is empty\n')
    else:
        print('\nName'.ljust(20) + 'Number')
        print('-' * 35)
        for name, number in phonebook.items():
            print(f'{name.ljust(20)}{number}')
        print('\n')

def add_contact():
    print('\n*** Add new contact ***')
    name = input('Contact name: ').upper()
    number = input('Contact Number: ')

    phonebook[name] = number
    print('\nThe contact was successfully added\n')

def del_contact():
    print('\n*** Delete contact ***')
    name = input('Enter the contact to delete: ').upper()
    if name in phonebook:
        phonebook.pop(name)
        print('\nThe contact was successfully deleted !\n')
    else:
        print(msg_no_contact)

def search_contact():
    name = input('Enter the contact name: ').upper()
    if name in phonebook:
        print(f'\nName: {name}, Number: {phonebook[name]}\n')
        return name
    else:
        print(msg_no_contact)
        return False

def edit_contact():
    print('\n*** Edit contact ***')

    name = search_contact()
    if name:
        print('\nLeave blank the value you do not want to change')
        new_name = input('Enter the new contact name: ').upper()
        new_number = input('Enter the new contact number: ')

        if not new_name and not new_number:
            print('Nothing to modify')
            return None
        elif new_name and new_number:
            phonebook[new_name] = new_number
            phonebook.pop(name)

        elif new_name:
            phonebook[new_name] = phonebook[name]
            phonebook.pop(name)
            
        elif new_number:
            phonebook[name] = new_number
            
        print('\nThe contact was successfully edited !\n')


def main_menu(name):
    print(f"{name.upper()}'s Phonebook.")
    print('*' * 35)
    print("""
          1- Search Contact.
          2- Add Contact.
          3- Show Contacts.
          4- Edit Contact.
          5- Delete Contact.
          6- Exit
    """)
    option = int(input('Choose an option 1-5: '))
    return option

def options(option):
    if option == 1:
        print('\n*** Search contact ***')
        search_contact()
    elif option == 2:
        add_contact()
    elif option == 3:
        show_contacts()
    elif option == 4:
        edit_contact()
    elif option == 5:
        del_contact()
    elif option == 6:
        print('Thanks see you soon')
        return 0
    else:
        print('Invalid Option!')
    return 1

if __name__ == '__main__':
    name = input('Enter your name please: ').upper()
    carryon = True
    while carryon:
        option = main_menu(name)
        carryon = options(option)