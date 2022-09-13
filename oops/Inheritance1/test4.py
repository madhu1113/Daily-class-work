# abstraction(Data Hiding):- if we are not giving direct access of data to user i.e called abstraction.
class KLH:
    __students = "python"

    def students(self):
        print("print the calss of students", KLH.__students)

k = KLH()
k.students()
# k.__students   --> we are hiding __students variable behind class. This concept is called data abstraction.
print(k._KLH__students)

