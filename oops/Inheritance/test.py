# Public, private and protected variable. In python it's just a notation.
# This concept exists inside python but ot doesn't exist


class person1:
    def __init__(self, name, surname, yob):
        self._name1 = name # protected variable
        self.__surname1 = surname # private variable
        self.yob1 = yob # public variable
madhu = person1("Madhu", "Priya", 1994)
print(madhu._name1)
#print(madhu.__surname1)--> it gives error
print(madhu._person1__surname1) # we can access the private varianle using _classname
