import json
import os


# Определение пути к файлу данных в переменную
path_to_data = os.path.abspath("../data/")
path_to_operations = os.path.join(path_to_data, "operations.json")


# Создание функции
def load_operations():
    """Загрузка данных из файла и формирование списка всех операций"""
    with open(path_to_operations, "r", encoding='utf8') as file:
        operations_list = json.load(file)

        return operations_list


def get_last_five_operations(operations_list):
    """Составление отсортированного по дате списка из пяти последних выполненныхопераций"""
    operations_list_clean = [opr for opr in operations_list if opr != {} and opr["state"] == "EXECUTED"]
    operations_list_clean.sort(key=lambda dictionary: dictionary["date"], reverse=True)
    last_five_operations = operations_list_clean[0:5]

    return last_five_operations
