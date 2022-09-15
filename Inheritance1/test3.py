# Method overriding:- when parent and child class has method with same name. Here we are trying to override a method which we have inherited from parent class.
# example- Sati Pratha, drawback of parents
class KLH:
    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list of all the achievers ")

    def Placed(self):
        print("print everyone who got placed")

class KLH_vision(KLH):

    def student(self):
        print("These are the filtered student list")

kv = KLH_vision()
kv.student()

