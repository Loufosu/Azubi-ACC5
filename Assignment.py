# Build a robot that asks for a bank customer's first name, last name & account number. The robot now has to provide the customer's account type (whether Savings(S) or Current(C)) and their account balance.
# Logic 1. Ask for User's first name 2. Ask for User's last name 3. Ask for User's account number
# Accept account number of 7 digits
# Savings acc should start with 14 & current acc should start with 20
# Define dictionaries for each acc

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
accNumber = input("Enter your account number: ")
ecobank[fname + lname] = accNumber

print(ecobank)
