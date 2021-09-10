#import required libraries (For Regex and CSV functionalities)
import csv
import re

#password validation function
def validatePassword(password):
    while True:
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters!")
            exit()

        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it.")
            exit()

        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it.")
            exit()

        else:
            return True

#user registration function
def registerUser():
    #open csv file and write data into it
    with open("./data/userData.csv", mode="a", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        #get user email
        email = input("Please enter email?: ")

        #check empty input
        if not email:
            print("Email cannot be empty!")
            return registerUser()

        #get user password
        password = input("Please enter password?: ")

        #check empty input
        if not password:
            print("Password cannot be empty!")
            return registerUser()

        #call password validation function
        isValidPassword = validatePassword(password)

        #check validation function result
        if isValidPassword:
            #get user's confirmed password
            confirmedPassword = input("Please confirm password?: ")

            #check password similarity
            if password == confirmedPassword:
                #exception handler
                try:
                    #read csv file to check already registered users
                    with open("./data/userData.csv", mode="r",encoding="utf-8-sig") as file:
                        reader = csv.reader(file, delimiter=",")
                        for row in reader:
                            if row[0] == email:
                                print("User already exists!")
                                exit()
                        #newly users write into the csv file
                        writer.writerow([email,password])
                    #success message
                    print("\nUser registered successfully!")  

                except Exception as e:
                    print('Something went wrong in registration!',e)
            else:
                print("Password does not match. Please try again!")
                exit()
        else:
            return False

#user login function
def loginUser():
    #get user email
    email = input("Please enter email?: ")

    #check empty input
    if not email:
        print("Email cannot be empty!")
        return loginUser()
        
    #get user password
    password = input("Please enter password?: ")

    #check empty input
    if not password:
        print("Password cannot be empty!")
        return loginUser()
    #exception handler
    try:
        #read csv file to check registered users
        with open("./data/userData.csv", mode="r") as file:
            reader = csv.reader(file, delimiter=",")

            for row in reader:
                if row == [email, password]:
                    print("\nYou are logged In successfully!")
                    return True
            
        print("Invalid credentials. Please try again!")
        return False

    except Exception as e:
        print('Something went wrong in login!',e)

########### CALL MAIN FUNCTIONS ############

print("\n------- REGISTER ---------\n")

#call register function
registerUser()

print("\n------- LOGIN ---------\n")

#call login function
loginUser()