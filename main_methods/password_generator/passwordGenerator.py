import sys, os
sys.path.append(os.getcwd())
from json_classes.settings.jsonSettings_abstract import JsonSettings

import random


class Password_Generator(JsonSettings):
    # Constructor
    def __init__(self):
        super().__init__()
        # 使用者名稱、備份密碼 元素
        self.__account = self.jsonController.jsonReader(self.ACCOUNT_PATH)
        self.__userName = ""
        self.__passwords_backup = self.jsonController.jsonReader(self.PASSWORDS_BACKUP_PATH)
        self.__passwords_backup_elements = []
        # 密碼
        self.__password_lst = []
        self.__password = ""
        # 密碼長度
        self.__password_length = 0
        # 長度至少為 14 個字元
        self.__password_length_limit = 14
        # 英文大寫字元 (A 到 Z)：65 ~ 90
        self.__upper_alphabets_length = 5
        self.__upper_alphabets = []
        # 英文小寫字元 (a 到 z)：97 ~ 122
        self.__lower_alphabets_length = 5
        self.__lower_alphabets = []
        # 10 進位數字 (0 到 9)：48 ~ 57
        self.__numbers_length = 4
        self.__numbers = []
        # 非英文字母字元 (例如: !、$、#、%)：32 ~ 126 ，不包含 48 ~ 57 、 65 ~ 90 、 97 ~ 122
        self.__symbols_elements = [chr(i) for i in range(32, 126+1) if not 48 <= i <= 57 and not 65 <= i <= 90 and not 97 <= i <= 122]
        self.__symbols_length = 0
        self.__symbols = []
    
    # Getter, Setter
    @property
    def userName(self) -> str:
        return self.__userName
    def __setUserName(self) -> None:
        self.__userName = self.__account["account"]["user"]
    # 備份密碼元素
    @property
    def passwordsBackupElements(self) -> list:
        return self.__passwords_backup_elements
    def __setPasswordsBackupElements(self) -> None:
        for i in range(self.__passwords_backup["length"]):
            password = self.__passwords_backup["account_passwords"][i]["password"]
            self.__passwords_backup_elements.append(password)

    # 英文大寫字元 (A 到 Z)：65 ~ 90
    @property
    def upperAlphabets(self) -> list:
        return self.__upper_alphabets
    def __setUpperAlphabets(self) -> None:
        self.__generator(self.__upper_alphabets_length, self.__upper_alphabets, 65, 90)
    # 英文小寫字元 (a 到 z)：97 ~ 122
    @property
    def lowerAlphabets(self) -> list:
        return self.__lower_alphabets
    def __setLowerAlphabets(self) -> None:
        self.__generator(self.__lower_alphabets_length, self.__lower_alphabets, 97, 122)
    # 10 進位數字 (0 到 9)：48 ~ 57
    @property
    def numbers(self) -> list:
        return self.__numbers
    def __setNumbers(self) -> None:
        self.__generator(self.__numbers_length, self.__numbers, 48, 57)
    # 非英文字母字元 (例如: !、$、#、%)：32 ~ 126 ，不包含 48 ~ 57 、 65 ~ 90 、 97 ~ 122
    @property
    def symbolsLength(self) -> int:
        return self.__symbols_length
    def __setSymbolsLength(self) -> None:
        self.__symbols_length = self.__password_length - self.__password_length_limit
    @property
    def symbols(self) -> list:
        return self.__symbols
    def __setSymbols(self) -> None:
        while True:
            for _ in range(self.symbolsLength):
                self.__symbols.append(random.choice(self.__symbols_elements))
            # 確認一字元不能重複出現三次
            if self.__check_characters_not_triplicate(self.__symbols):
                break
            self.__symbols.clear()

    # 密碼
    @property
    def passwordList(self) -> list:
        return self.__password_lst
    def __setPasswordList(self) -> None:
        self.__password_lst = self.lowerAlphabets + self.upperAlphabets + self.numbers + self.symbols
    @property
    def password(self) -> str:
        return self.__password
    @password.setter
    def password(self, password_length: int) -> None:
        # 密碼長度
        self.passwordLength = password_length
        # 非英文字母字元長度
        self.__setSymbolsLength()

        # 使用者名稱、備份密碼 元素
        self.__setUserName()
        self.__setPasswordsBackupElements()
        while True:
            # 密碼不為空字串
            # 密碼中，不可包含帳號相關字眼
            # 確認密碼不存在於備份密碼中
            if self.password != "" and self.__check_passwordSubstrings_not_in_UserName() and self.__check_password_not_in_passwords_backup_elements():
                break
            # 英文大寫字元 (A 到 Z)、英文小寫字元 (a 到 z)、10 進位數字 (0 到 9)、非英文字母字元 (例如: !、$、#、%)
            self.__setUpperAlphabets()
            self.__setLowerAlphabets()
            self.__setNumbers()
            self.__setSymbols()

            self.__setPasswordList()
            self.__password = ''.join(self.passwordList)

    @property
    def passwordLength(self) -> int:
        return self.__password_length
    @passwordLength.setter
    def passwordLength(self, password_length: int) -> None:
        self.__password_length = self.__password_length_limit if password_length < self.__password_length_limit else password_length
    

    # Others
    # 密碼中，不可包含帳號相關字眼
    def __check_passwordSubstrings_not_in_UserName(self) -> bool:
        for i in range(self.passwordLength):
            passwordSubstring = self.password[i:i+3]
            if passwordSubstring in self.userName:
                return False
        return True
    def __check_password_not_in_passwords_backup_elements(self) -> bool:
        return self.password not in self.passwordsBackupElements
    # 確認一字元不能重複出現三次
    def __check_characters_not_triplicate(self, lst: list) -> bool:
        for s in set(lst):
            if lst.count(s) > 2:
                return False
        return True
    # 英文大寫字元 (A 到 Z)、英文小寫字元 (a 到 z)、10 進位數字 (0 到 9) 生成器
    def __generator(self, length: int, lst: list, rangeFirst: int, rangeLast: int) -> list:
        while True:
            for _ in range(length):
                lst.append(chr(random.randint(rangeFirst, rangeLast)))
            # 確認一字元不能重複出現三次
            if self.__check_characters_not_triplicate(lst):
                break
            lst.clear()


def main():
    generator = Password_Generator()
    generator.password = 14
    password = generator.password
    print(password)


if __name__ == "__main__":
    main()