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
