class person3:
    def __init__(self, name, surname, yob):
        self._name1 = name # protected variable
        self.__surname1 = surname # private variable
        self.yob1 = yob # public variable
madhu = person3("Madhu", "Priya", 1994)
print(madhu._name1)
print(madhu._person3__surname1)