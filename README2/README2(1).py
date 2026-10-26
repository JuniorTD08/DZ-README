def analys_vowels():

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    text_1 = input("Введите текст: ")

    vowels_list =[char for char in text_1 if char in vowels]

    return vowels_list

print("Список гласных букв", analys_vowels())
print("Длина списка", len(analys_vowels()))
