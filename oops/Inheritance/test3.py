 # Import a class from same module
from test2 import person2
# print(employee2)
obj4 = person2()
print(obj4.yob)
obj4.hello()

# import a class from different package
from utils.util1 import person3
obj5 = person3("sneha","priya",1997)
print(obj5.yob1)
