class person:
    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self,email_id):
        print("take the mail id from person and print it ", email_id)

    def ask_name(self):
        name = input("Tell me your name")
        return name

    def ask_dob(self):
        dob = input("Tell me your date of birth")
        return dob

madhu = person()
sudh = person()
sant = person()
cheeku = person()
gargi = person()

sudh.email_id_input("sudhanshu@gmail.com")
print(sudh.ask_name())
print(sudh.ask_dob())
print(sudh.age(2022, 1994))
print(gargi.ask_dob())

# By doing this we are able to increase the scalability and reusability of code.
# It looks very streuctured
# advantage:- Robustness, structure, easy to find, easy to develop and easy to implement
# usability of code is the core concept of OOPS
# Task1 = In past whatever qs i have given wrt list, tuple, string, dictionary try to create a seperate class for each and everything
# and restructure your code for all the segment and submit
# I1: always use exception Handling
# I2: use logging

