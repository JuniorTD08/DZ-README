alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

request = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = ""

for letter in request:
    if letter in alphabet:
        current = alphabet.index(letter)
        new_index = (current + shift) % 33
        encrypted_message = encrypted_message + alphabet[new_index]
    else:
        encrypted_message = encrypted_message + letter

print(encrypted_message)
