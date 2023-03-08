"""An example basis hint on nested classes, this example is from Alison"""
class Employee:
    company= "learn"
    def __init__(self,name, age , salary, gender,designation,department,responsibility,cpu, gpu, ram):
        self.names= name
        self.age= age
        self.salary= salary
        self.gender= gender
        self.email= self.generateEmail(Employee)#Employee is in bracket because we shall use its class variable cls
        self.job= self.Job(designation, department,responsibility)
        self.computer= self.Computer(cpu,gpu,ram)
    def generateEmail(self, cls):#lets create a function that creates emails, accepts the object refernceself  by default and class variable represented by cls.
        return f"{self.names}@{cls.company}.com"
    def Showinfo(self):
        print(self.names, self.age,self.salary, self.gender,self.email) 
    @classmethod
    def Letschangeconame(cls, newname):
          cls.company= newname
    @staticmethod
    def info():
        print("This all program can be regarded as one for creating Employee Objects and then it requires name, age , salary, gender as parameters ")
    class Job:#This is a nested class
         def __init__(self,designation, department, responsibilty):
           self.designation= designation
           self.department= department
           self.responsibility= responsibilty
         def showinfo(self):#Will not clash with the same method name  in the earlier class since they are from different classes
               print(self.designation, self.department, self.responsibility)
    class Computer:
         def __init__(self,cpu, gpu, ram):
            self.cpu= cpu
            self.gpu= gpu
            self.ram= ram
         def showinfo(self):
              print(self.cpu,self.gpu,self.ram)

obj= Employee("John",10, 100000, "Male", "Manager", "IT", "Servers" , "i7" , "gtx", "32GB")
obj.info()
obj.Showinfo()
obj.job.showinfo()
obj.Computer.showinfo()

# print(obj.generateEmail(Employee))
"""Example 2"""
class OuterClass:
    def __init__(self):
        self.inner_obj = OuterClass.InnerClass()

    class InnerClass:
        def __init__(self):
            self.inner_var = "inner_var"
outer_obj = OuterClass()
inner_obj = outer_obj.inner_obj
print(inner_obj.inner_var)  # output: "inner_var"
inner_obj1 = OuterClass.InnerClass()
inner_obj2 = OuterClass.InnerClass()
"""EXAMPLE 2"""
"""NESTED CLASSES """
class OuterClass:
    def __init__(self):
        self.inner_obj = OuterClass.InnerClass()
        self.another_inner_obj = OuterClass.AnotherInnerClass()

    class InnerClass:
        def __init__(self):
            self.inner_var = "inner_var"

    class AnotherInnerClass:
        def __init__(self):
            self.another_inner_var = "another_inner_var"
outer_obj = OuterClass()
print(outer_obj.another_inner_obj.another_inner_var)  # output: "another_inner_var"
inner_obj1 = OuterClass.InnerClass()
inner_obj2 = OuterClass.InnerClass()
another_inner_obj1 = OuterClass.AnotherInnerClass()
another_inner_obj2 = OuterClass.AnotherInnerClass()