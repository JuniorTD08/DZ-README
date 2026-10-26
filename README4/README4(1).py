class Person:

    __count = 0

    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name:str):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            exit("Имя должно состоять только из букв!")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age:int):
        if (isinstance(age, int) and  age < 100 and age > 0):
            self._age = age
        else:
            exit("Возраст должен быть целым числом в диапазоне от 0 до 100!")

Vlad = Person("Vlad", 27)
Irina = Person("Irina", 19)

print(f"Имя: {Vlad.get_name()}, Возраст: {Vlad.get_age()}")
print(f"Имя: {Irina.get_name()}, Возраст: {Irina.get_age()}")