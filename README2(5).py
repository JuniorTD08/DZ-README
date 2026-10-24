s = input("Введите строку: ")

first_h = s.find("h")
last_h = s.rfind("h")

reversed_part = s[first_h + 1 : last_h][::-1]

print(f"Развёрнутая последовательность между первым и последним h: {reversed_part}")
