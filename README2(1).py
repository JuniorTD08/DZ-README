def analys_vowels():

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    text_1 = input("Введите текст: ")

    vowels_list =[char for char in user_text if char in vowels]

print("Список глассных букв", analys_vowels)
print("Длина списка", len(vowels_list))