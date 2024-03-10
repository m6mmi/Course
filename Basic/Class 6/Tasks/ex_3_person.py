class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}."

class Student(Person):
    def __init__(self, name, age, id="N/A"):
        super().__init__(name, age)
        self.id = id

    def greet(self):
        return (f"Hello {self.name}\n"
                f"ID: {self.id}")


person1 = Person("Juku", 99)
student1 = Student("Janek", 38)
student2 = Student("Peeter", 5, 2345256677)


print()
print(f"{student1.greet()}\n\n"
      f"{person1.greet()}\n\n"
      f"{student2.greet()}")


