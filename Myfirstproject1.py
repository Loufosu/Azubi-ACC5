
from pickle import PicklingError


def my_function(fname):
    print(fname + " Amoah")


my_function("Ajara")
my_function("Joseph")
my_function("Anita")

x = 5
y = 2.5
print(type(x))
print(type(y))

a = 56
print(float(a))

b = 56.0
print(int(b))

c = 56.8
print(int(c))

colour = ["red", "blue", "green"]
print(colour)
colour[0] = "pink"
colour[-2] = "white"

print(colour)

tuple = (1, 2, 3,)
print(tuple)
print(tuple[0])

x = "Python is"
y = "awesome"
z = x + " " + y
print(z)

a = 'Hello, '
b = 'How are you?'
c = a + b
print(c)

# Variables
x = 5
x = "Dog"
print(x)

b = "John"
print(type(b))

ecobank = {
    "firstName": "Akwasi",
    "lastName": "Dankwa",
    "accType": "Savings",
    "accNumber": 1456567,
    "accBalance": 15000

}
# print(ecobank.items())
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
if fname == ecobank["firstName"]:
    print(lname)
accNumber = input("Enter your account number: ")
if accNumber == ecobank["accNumber"]:
    print("This is a Savings account and your account balance is " +
          ecobank["accBalance"])
