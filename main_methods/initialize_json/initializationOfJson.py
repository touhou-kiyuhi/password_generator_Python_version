import sys, os
sys.path.append(os.getcwd())
from json_classes.settings.jsonSettings_abstract import JsonSettings


class Initialization_Of_Json(JsonSettings):
    def __init__(self):
        super().__init__()

    def setupAccountJson(self, user, password):
        data = {
            "account": {
                "user": user, 
                "password": password
            },
            "domain_name": {
                "at": "@",
                "email": "example.com"
            }
        }
        # json writer
        self.jsonController.jsonWriter(self.ACCOUNT_PATH, data)
        # json viewer
        data = self.jsonController.jsonReader(self.ACCOUNT_PATH)
        self.jsonController.jsonViewer(data)

    def backupPasswordsJson(self, password):
        data = {
            "length": 1, 
            "account_passwords": [
                {
                    "number": 0, 
                    "password": password
                }
            ]
        }
        # json writer
        self.jsonController.jsonWriter(self.PASSWORDS_BACKUP_PATH, data)
        # json viewer
        data = self.jsonController.jsonReader(self.PASSWORDS_BACKUP_PATH)
        self.jsonController.jsonViewer(data)


def main():
    init = Initialization_Of_Json()
    user = "Test_TT.User"
    password = "abcdeABCDE1234"
    init.setupAccountJson(user, password)
    init.backupPasswordsJson(password)


if __name__ == "__main__":
    main()