# 1. Apply set union
A = { 55, 6, 8, 9, 11}
B = {44, 55, 89,54}
print('Set union : ' ,A|B )
print('Set union : ' ,A.union(B) )

# 2. Which data type not allow duplicate item. Ans is set
# example is :
s = {55, 6, 8, 9, 11,44, 55, 89,54}
print('set is : ', s)


# 3. Dictionary print keys.
mydict = {
    'Django': 16,
    'Project': 8,
    'Students': 20
}
keys = mydict.keys()
print("Dictionary print keys : ",keys)


# 4. Create a function & call the function.

def fristfunction( ):
    print("MD.Abdullah al shaharir")

fristfunction()

def info(name, address):
    print('My Name is :', name, ', My Address is :',address)

print(info('Abdullah Al Shahriar','Jhenaidah , Khulna'))

#5. Create Class & Object.

class cars_info:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def BrandFunction(self):
        print("My Car's Brand Name is : " ,self.brand)


    def ModelFunction(self):
        print("My Car's Model Name is : " ,self.model)


    def PriceFunction(self):
        print("My Car's Price is : " ,self.price)
car = cars_info('BMW','X1 Sports ', '$39,100')


car.BrandFunction()
car.ModelFunction()
car.PriceFunction()


# 6. Give an example of Inheritance.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname)
        print(self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("Abdullah", "Shahriar")
x.printname()


class Fperson:
    car = "BMW"
    taka = "100K"
    home = "kcp"
    house = "big"


class Sperson(Fperson):
    tree = "mango"
    wecam = "cannon"
    baiek = "Yamaha"


class Tperson(Sperson):
    phone = "samsung"
    face = "beautiful"
    camera = "soney"


class Fperson(Tperson):
    job = " "
    selali = ""


r = Fperson()
print(r.car)
print(r.taka)
print(r.home)
print(r.tree)
print(r.wecam)
print(r.baiek)
print(r.phone)
print(r.face)
print(r.camera)
print(r.house)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("RaseL", "Abdullah")
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("RaseL", "Abdullah", "2024")
print(x.graduationyear)
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("RaseL", "Abdullah", "2024")
x.welcome()
x.printname()
