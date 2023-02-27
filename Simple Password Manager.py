import base64

def add_password(service, username, password):
    # Encrypt the password / Password Encode Byte
    encoded_password = base64.b64encode(password.encode())
    
    # Store the encrypted password in a file with the service name and username as the filename
    #nama file, write
    with open(f"{service}_{username}.txt", 'w') as f:
        f.write(encoded_password.decode())

def retrieve_password(service, username):
    # Read the encrypted password from the file with the service name and username as the filename
    # Decrypt the password / Password Decode Byte
    try :
        with open(f"{service}_{username}.txt", 'r') as f :
            encrypted_password = f.read()
        password = base64.b64decode(encrypted_password.encode())
        return password.decode()
    except FileNotFoundError :
        return 'password not found'
        
def main():
    while True:
        # Prompt the user to choose an action (add a password, retrieve a password, or exit the program)
        choice = input("Enter your choice: ")
        if choice == '1':
            # Add a password
            service = input("Enter Name Of Service : ")
            username = input("Enter Username : ")
            password = input("Enter Password : ")
            add_password(service,username,password)
            print("Password Added")
        elif choice == '2':
            # Retrieve a password
            service = input("Enter Name Of Service : ")
            username = input("Enter Username : ")
            password = retrieve_password(service,username)
            print(password)
        elif choice == '3':
            # Exit the program
            print("See You Later")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()