def sum_distance(from_value, to_value):
    # Проверяем, если первое число больше второго, меняем их местами
    if from_value > to_value:
        from_value, to_value = to_value, from_value

    # Используем встроенную функцию sum для суммирования чисел в диапазоне
    result = sum(range(from_value, to_value + 1))
    return result


# Ввод чисел с клавиатуры
from_value = int(input("Введите первое число: "))
to_value = int(input("Введите второе число: "))

result_sum = sum_distance(from_value, to_value)

print(f"Сумма чисел от {from_value} до {to_value} равна: {result_sum}")
