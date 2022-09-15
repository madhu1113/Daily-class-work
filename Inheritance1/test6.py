# polymorphism:- one object but multiple behaviour.  different forms of a particular instances in different- different situations.
#  example:- same person act as brother, son, husband, father, collegue, friend of someone in differet differet circumstances. in hindi bahurupiya

# def test(a,b):
#     return a+b
#
# print(test(3,5)) # perform addition operation
# print((test("madhu"," priya"))) # concatenation operation

class KLH:
    def students(self):
        print("print the KLH students detail")

class HONS():
    def students(self):
        print("print the Hßons students detail")

def KLH_external(a): # as we can say that this single function is able to both the object of different class simultaneously. It's behaviour is changing w.r.t input we are passing.
    a.students()  # this function behaves like common interface or bridge or connection n/w all the classes e.g - daughter connecting me to my parents

k = KLH()
h = HONS()
KLH_external(k)
KLH_external(h)

# Task:-
# for all the concepts we have discussed in class point by point write atleast 10 ec=xample
# you have to make sure that you use KLH_students, number_of_courses, blog, internship, jobs, placed as a reference example.
