class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        super().say_hello()
        print(f"My student ID is {self.student_id}.")
    
    def get_student_id(self):
        return self._student_id
    

p= Person("John", 25)
p.say_hello()

s = Student("Jane", 21, "1234")
s.say_hello()

print(p)
print(s)