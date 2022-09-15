# encapsulation:- not allowing the user to change the value of variable dirctly or at run time is called as encapsulation. so we make  the vsrisble as private variable.
#  example:- capsules.
# encapsulating the value of variable so that user can't modify it.
#  diff. b/w abstraction and encapsulation?
#  abstaction means hiding the data behind sth i.e class in this case but encapsulation means modification of data using class method.
#  abstraction is about access of data but encapsulation is about modificaton of data

class KLH:
    def __init__(self):
        self.students1 = "python"

    def students(self):
        print(self.students1)

k = KLH()
k.students()
k.students1 = "data science" # trying to override the value of a variable in run time
k.students()


class KLH1:
    def __init__(self):
        self.__students1 = "python"

    def students(self):
        print(self.__students1)
    #
    # def student_change(self):
    #     self.__students1 = "data analytics"


    def student_change(self, new_value):  # setter function
        self.__students1 = new_value

k1 = KLH1()
k1.students()
k1.__students1  = "data science" # in case of private variable we can't update the value of a variable with the help of object but we can do it using class method.
k1.students()
k1.student_change("madhu") # changing tha value of private variable using class method is called encapsulation.
k1.students()

