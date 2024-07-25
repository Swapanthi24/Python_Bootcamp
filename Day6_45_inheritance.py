#inheritance
#write a code to write single, multiple, multilevel
class Animal:
    def Speak():#method1
        return "Animal is speaking"
#single
class Dog(Animal):
    def Bark():#method2
        return "Bow..."

#multi level    
class Puppy(Dog):
    def puppy_speak():
        return "hi im pup"

obj1=Animal
obj2=Dog
obj3=Puppy
print(obj2.Speak())
print(obj2.Bark())
print(obj3.puppy_speak())


#multiple
class Father():
    def father_speak():
        return "father class"
class Mother():
    def mother_speak():
        return "mother class"
class Kid(Mother,Father):
    def kid_speak():
        return "i have both props"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())
