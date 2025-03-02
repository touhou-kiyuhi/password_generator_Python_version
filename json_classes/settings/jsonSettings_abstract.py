import sys, os
sys.path.append(os.getcwd())
from json_classes.controller.jsonController_abstract import JsonController


class JsonSettings:
    def __init__(self):
        # Json Path
        self.ACCOUNT_PATH = "json_data/account.json"
        self.PASSWORDS_BACKUP_PATH = "json_data/passwords_backup.json"
        # Json Controller
        self.jsonController = JsonController()