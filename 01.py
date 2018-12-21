class test():
    age = 18
    name = "damin"

    def student(self):
        self.age = 20
        self.name = "sunlimin"

# 此时，test为类的实例
print(test.name)
print(test.age)
print(id(test.age))
print(id(test.name))

print("*" * 20)

# t 代表test的一类中一个具体的对象  即对象的实例~~~
t =  test()

print(t.name)
print(t.age)
print(id(t.age))
print(id(t.name))
