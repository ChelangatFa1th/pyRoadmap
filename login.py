#Simply tells the user to create an account
print("Create an Account")
#prompts tha user to enter the credentials
#Password and username
username = input("Enter your username: ")
password = int(input("Enter your password: "))
#Display to the user that the account was created successfully
print("Account created successfully!" )
#Displays to the user to login to the account
print("Login")
#prompts the user to enter the credentials again
username2 = input("Enter your username: ")
password2 = int(input("Enter your password"))
#if statements checks whether the credentials are correct or not
#if the credentials are correct a login success message is displayed
#if not correct an error message is displayed
if (username == username2 and password == password2):
    print("Logged in successfully")
else:
    print("Incorrect credentials! Try Again ")  
#thanks the user for login
print("Thank you for logging in")