#keyword, name of the class(first letter capital)
class Myclass:
    def add(a,b): #defining a method
        return a+b

#creating an object    
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.add(12,5))#passing diffrent parameters

#using many methods
class Myclass:
    def add(a,b): 
        return a+b
    def mul(a,b): 
        return a*b
    def sub(a,b): 
        return a-b
    def div(a,b): 
        return a/b
    def mod(a,b): 
        return a%b

obj1=Myclass
print(obj1.add(2,5))
print(obj1.sub(12,5))
print(obj1.mul(12,5))
print(obj1.div(12,5))
print(obj1.mod(12,5)) 


#garbage collector: removes the unused variables automatically
#variable: holds the value


#constructor
class Myclass:
    def _init_(self,a,b): 
        self.a=a
        self.b=b

#instance variable
class Myclass:
    cls_var="im class variable"  
    def add(a,b):
        ins_variable_add="im instanace var"
        return a+b

obj1=Myclass     
print(obj1.add(2,5))



