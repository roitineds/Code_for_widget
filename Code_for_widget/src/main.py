from src.utils import load_operations, get_last_five_operations
from src.operation_class import Operation

# Загрузка списка операций
operations_list = load_operations()

# Создание списка из пяти последних выполненных операций
last_five_operations = get_last_five_operations(operations_list)

# Перебирание списка, вывод данных
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.date()} {operation.description()}
{operation.hide_number(operation.account_from())} -> {operation.hide_number(operation.account_to())}
{operation.amount()}""")
