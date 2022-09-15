class car :
    def __init__(self, body, engine,tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milege(self):
        print("milege of this car")

c = car("solid", "v6", "radial")
print(c)
#
class tata(car):
    pass

# t  = tata()
# print(t)
#
# # t = tata()  it will give error since car his having constructor
# # print(t)
#
t = tata("solid1", "v61", "radial1")
print(t)
print(t.milege())


