class Person :
    # constructor:- pass information to class. default method or function
    def __init__(self, name, surname, emailId, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailId = emailId
        self.year_of_birth = year_of_birth


anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994) # class variable is called object
madhu = Person("Madhu", "Priya", "madhu.priya@klh.edu.in", 2344) # real entity
sudh = Person("sudhanshu", "Kumar", "sudhanshu@gmail.com",7687)

print(anuj_var.name1)
print(anuj_var.surname)
print(anuj_var.emailId)
print(anuj_var.year_of_birth)
print(sudh.name1)
print(type(sudh))


# itis similar to a variable we have created as a int, string, list, tuple etc. and all these are object
