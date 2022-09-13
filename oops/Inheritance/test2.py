class person2:
    # these are global variable
    _name = "madhu"
    __surname = "priya"
    yob = 1994

    def hello(self):
        print("Hello")

    def _age(self, current_year): # protected function
        return current_year-self.yob

    def __age1(self, current_year): # private function
        return current_year - self.yob

obj = person2()
print(obj._age(2022))
print(obj._person2__age1(2022))
# Hence the way we treat our variable exact similar way we treat out functions

class employee2:
    _name = "Sarita"
    __surname = "Kumari"
    yob = 1993

obj1 = employee2()
print(obj1)
print(obj1.yob)
print(obj1._name)
