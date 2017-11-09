class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_old(self):
        if self.age > 50:
            return True
        else:
            return False
    def get_nice_name(self):
        nice_name = ">>>{}<<<".format(self.name)
        print(nice_name)
        return nice_name
