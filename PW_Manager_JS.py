import firebase_admin
import keyboard
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from icecream import ic
exit_option = False  

# set the credentials for the firebased SDK
cred = credentials.Certificate("securityTokenKey.json")
firebase_admin.initialize_app(cred)

# need to add some kind of authentication service at some point so you need to sign in to save passwords
# set the authentication for the firebase db
# email = input('Enter your email address: ')
# password = input('Enter your password: ')

# user = auth.create_user(email = email, password = password)
# print(f'User created sucsessfully! User ID: {user.uid} \n')

# create an instance of the firebase as a db variable
db=firestore.client()

# create a reference to a collection called passwords
password_ref = db.collection('Passwords')

# create a function to display all the password vault options
def display():
    print('\n')
    print('Welcome to your password vault.')
    print('Please select an option from below:')
    print('1: Add a password')
    print('2: Delete a password')
    print('3: Update an existing password')
    print('4: View all currently saved passwords') # will prompt if they want to see usernames & passwords or just Name of login
    print('5: Exit')
    selection = input('> ')
    if selection == '1':
        add_password()
    elif selection == '2':
        delete_password()
    elif selection == '3':
        update_password()
    elif selection == '4':
        view_passwords()
    elif selection == '5':
        global exit_option # shows that the vairable exit_option is a global variable outside of funciton scope
        exit_option = True
        
# a function to prompt users for input to store as documents in the password collection of the cloud database 
def add_password():
    name = input('Enter an Account Name: ').lower()
    user_name = input('Enter Username: ')
    password = input('Enter Password: ')
    password_ref.document(f'{name}').set({'Username':f'{user_name}', 'Password':f'{password}'})
    print("Password saved!" + '\n')
    
# a function to delete passwords, preferably it will list the name of all the available passwords in the vault for them to select one to delete.
# could even prompt if they want a list or if they want to type in the name themselves.
def delete_password():
    name_list_exit = input("Enter in password name[a] OR list all saved websites[b] (press 'e' to exit to display): ")
    if name_list_exit == 'a':
        password_name = input("Password Name: ").lower()
        doc_ref = db.collection('Passwords').document(f'{password_name}')
        doc = doc_ref.get()
        if doc.exists:
            final_check = input(f'Do you want to delete saved data for password named...{password_name}? [y][n]: ')
            if final_check == 'y':
                db.collection('Passwords').document(f'{password_name}').delete()
                print("Password deleted! + \n") 
            elif final_check == 'n':
                delete_password()
        else:
            print('No such document!')
            delete_password()    
    elif name_list_exit == 'b': # extra functionality
        docs = db.collection('Passwords').get()
        doc_name_list = []
        for doc in docs:
            doc_name_list.append(doc.id)
        for index in range(len(doc_name_list)):
            print(f'{index}: {doc_name_list[index]}')
        selection = int(input('Select the number for the password you would like to delete: '))
        password_name = doc_name_list[selection].lower()
        doc_ref = db.collection('Passwords').document(f'{password_name}')
        doc = doc_ref.get()
        if doc.exists:
            final_check = input(f'Do you want to delete saved data for password named...{password_name}? [y][n]: ')
            if final_check == 'y':
                db.collection('Passwords').document(f'{password_name}').delete()
                print("Password deleted! + \n")
            elif final_check == 'n':
                delete_password()
    elif name_list_exit == 'e':
        display()
    
def update_password():
    selection = input("Enter login name: ").lower()
    doc_ref = db.collection('Passwords').document(f'{selection}')
    doc = doc_ref.get()
    if doc.exists:
        user_name = input("Enter new Username: ")
        password = input("Enter new Password: ")
        db.collection('Passwords').document(f'{selection}').set({'Username':f'{user_name}', 'Password':f'{password}'})
        print("Username/Password updated successfully! + \n")
    else:
        print("No such login exists!")

# a function to display all of the passwords in the 'vault'
def view_passwords():
    docs = db.collection('Passwords').get()
    for doc in docs:
        print(f'{doc.id}: {doc.to_dict()}')
# add some functionality to loop through the key/value pair to print nicer
        
while exit_option == False:
    display()
    # if keyboard.is_pressed('esc'):
    #     display()

