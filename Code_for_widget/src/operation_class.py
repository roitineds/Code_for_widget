from _datetime import datetime


class Operation:
    def __init__(self, operation):
        """Принятие словаря с данными"""
        self.operation = operation

    def __repr__(self):
        """Возвращение информации об экземпляре"""
        return f"Class Operation({self.operation})"

    def date(self):
        """Вывод даты операции"""
        operation_date_str = self.operation["date"]
        operation_date = datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date.strftime("%d.%m.%Y")

    def description(self):
        """Вывод описания операции"""
        return self.operation["description"]

    def account_from(self):
        """Вывод данных счёта и карты отправления, если они есть"""
        if "from" in self.operation.keys():
            return self.operation["from"]
        else:
            return ""

    def account_to(self):
        """Ввывод данных счёта и карты назначения"""
        return self.operation["to"]

    def hide_number(self, account):
        if account == "":
            return "Внесение средств"
        else:
            account = account.split(" ")
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = " ".join(account)
            if "Счёт" in account:
                return f"{account_name} **{account_number[16:20]}"
            else:
                return f"{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}"

    def amount(self):
        """Вывод суммы и валюты операции"""
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'
