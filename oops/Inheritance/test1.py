import test       # Trying to import the module
print(test)

# can we make object of person1 which is there in test module
obj3 = test.person1("Sneha", "Kumari", 1998)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)

# in other oops progrmming language like java, scala you can't access protected or private variable across the modules
# That's y public, private, protected concept is little bit different from other language

class person:
    # these are global variable
    _name = "madhu"
    __surname = "priya"
    yob = 1994

    def _age(self, current_year): # protected function
        return current_year-self.yob

    def __age1(self, current_year): # private function
        return current_year - self.yob

obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))
# Hence the way we treat our variable exact similar way we treat out functions

class employee(person):
    _name = "Sarita"
    __surname = "Kumari"
    yob = 1993

obj1 = employee()
print(obj1._age(2022)) # this works perfectly
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)
#print(obj1._employee__surname) this will give error bcz we have to give the classname of the variable