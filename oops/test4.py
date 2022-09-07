class Person:
    # constructor:- pass information to class. default method or function
    def __init__(madhu, name, surname, emailId, year_of_birth):
        madhu.name1 = name
        madhu.surname = surname
        madhu.emailId = emailId
        madhu.year_of_birth = year_of_birth

        # Create one more init
        # so we can see that it is overriding the first one. So if you are passing multiple constructor it will always take the latest one

    def __init__(madhu, name, surname):
        madhu.name1 = name
        madhu.surname = surname



anuj_var = Person("anuj", "bhandari")  # class variable is called object
madhu = Person("Madhu", "Priya")  # real entity
sudh = Person("sudhanshu", " Kumar")

print(anuj_var.name1)
print(anuj_var.surname)
print(sudh.name1)
print(type(sudh))

# itis similar to a variable we have created as a int, string, list, tuple etc. and all these are object
# do the concatenation of name and surname
print(sudh.name1 + sudh.surname)
# it is similar to string concatenation
a = "Madhu"
b = " Priya"
print(a + b)

# find the age of madhu
# example of same thing
s = "madhu"
print(s.upper())
