#This is example for why we use self in parameter at function
#self parameter in method or function be like "this" keyword in java


class name:
    b=5
    def __init__(self):
        print("This is constructor Example in python")

    def add(self, a):
        a=self.b+20
        print(a)


ram=name()
ram.add(1)
