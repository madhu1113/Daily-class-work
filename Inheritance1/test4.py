# abstraction(Data Hiding):- if we are not giving direct access of data to user i.e called abstraction.
#  example:- writing abstract in research paper
class KLH:
    __students = "python"

    def hiding(self):
        print( KLH.__students)

k = KLH()
k.hiding()
# k.__students   --> we are hiding __students variable behind class. This concept is called data abstraction.
# print(k._KLH__students)

# list()