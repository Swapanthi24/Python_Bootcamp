#polymorphism: it only possible in python by overloading and overridding
#method overridding -------run time polymorphism
class Animal:
    def Speak():
        return "speak...."
class Dog(Animal):
    def Speak():
        return "dog is speaking"
class puppy(Dog):
    def  Speak():
        return "puppy is speaking"
obj3=puppy
print(obj3.Speak())

#method overloading(increasing the capacity)--------complie time
class cal:
    def add(self,*args):
        return sum(args)
#takes input
obj1=cal()#for static no need of (), but for dynamic we need ()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))