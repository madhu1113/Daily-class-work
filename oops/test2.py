class Person :
    # constructor:- pass information to class. default method or function
    def __init__(madhu, name, surname, emailId,year_of_birth ):
        madhu.name1 = name
        madhu.surname = surname
        madhu.emailId = emailId
        madhu.year_of_birth = year_of_birth

    def age(madhu, current_year):
        return current_year - madhu.year_of_birth


anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994) # class variable is called object
madhu = Person("Madhu", "Priya", "madhu.priya@klh.edu.in", 2344) # real entity
sudh = Person("sudhanshu", " Kumar", "sudhanshu@gmail.com",7687)


print(anuj_var.name1)
print(anuj_var.surname)
print(anuj_var.emailId)
print(anuj_var.year_of_birth)
print(sudh.name1)
print(type(sudh))


# itis similar to a variable we have created as a int, string, list, tuple etc. and all these are object
# do the concatenation of name and surname
print(sudh.name1+ sudh.surname)
# it is similar to string concatenation
a = "Madhu"
b = " Priya"
print(a+b)

# find the age of madhu
print(madhu.age(2022))
# example of same thing
s = "madhu"
print(s.upper())


# passing different no. of arguments
madhu = Person("Madhu", "Priya", "madhu.priya@klh.edu.in") # since we have defined 4 data but providing only 3 so it will give error
