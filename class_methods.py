# Document at least 3 use cases of class

# Document at least 3 use cases of instance methods


class Parent:

    salary = 0

    def __init__(self, name, company_name):
        self.name = name
        self.company_name = company_name

    def display(self):
        return f'User: {self.name} \n Company: {self.company_name} \n {self.salary}'

    @classmethod
    def set_salary(cls):
        cls.salary = 1000

    @classmethod
    def raise_salary(cls, new_salary):
        cls.salary = new_salary

    @classmethod
    def class_constructor(cls, values):
        """Takes string with delimiter * Eg: 'James*Company'"""
        name, company_name = values.split('*')
        return cls(name, company_name)


obj = Parent.class_constructor('James*Adobe')
obj2 = Parent.class_constructor('John*Cluster.com')
obj.set_salary()
print(obj.display())
obj2.raise_salary(3000)
print(obj2.display())
print(obj.display())
