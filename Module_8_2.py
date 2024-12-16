def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            if isinstance(item, (int, float)):
                result += item
            else:
                raise TypeError
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1
    return result, incorrect_data
def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError("Некорректный тип данных")
        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None
print(f'Result 1: {calculate_average("1, 2, 3")}')
print(f'Result 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Result 3: {calculate_average(567)}')
print(f'Result 4: {calculate_average([42, 15, 36, 13])}')
