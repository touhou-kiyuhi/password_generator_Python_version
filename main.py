from main_methods.initialize_json.initializationOfJson import Initialization_Of_Json
from main_methods.password_generator.passwordGenerator import Password_Generator
from main_methods.update_json.UpdateOfJson import Update_Of_Json


def initialization(user, password):
    init = Initialization_Of_Json()
    init.setupAccountJson(user, password)
    init.backupPasswordsJson(password)
    pass

def password_generator(passwordLength):
    generator = Password_Generator()
    generator.password = passwordLength
    password = generator.password
    print(password)

def update_json(new_password):
    update = Update_Of_Json()
    update.updateAccountJson(new_password)
    update.updateBackupJson(new_password)

def main():
    # Initialization
    user = "Test_TT.User"
    password = "abcdeABCDE1234"
    initialization(user, password)

    # Passwords Generator
    passwordLength = 20
    password_generator(passwordLength)

    # To update the .json of the account and passwords_backup because we save them in json file
    password = "edcbaEDCBA4321"
    update_json(password)


if __name__ == "__main__":
    main()