def generate_custom_list(length):
    result = []

    for i in range(1, length + 1):
        if i % 2 == 0:
            result.append(1)
        else:
            result.append(i % 5)

    return result


list_length = int(input("Введите длину списка: "))
print("Результат:", generate_custom_list(list_length))