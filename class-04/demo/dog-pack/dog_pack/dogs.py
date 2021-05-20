class Dog:
    def __init__(self, name="unknown"):
        self.name = name

    def sleep(self):
        return "zzz"


class Boxer(Dog):
    def greet(self):
        return f"The name's {self.name}. Pleasure."


class Puggle(Dog):
    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"
