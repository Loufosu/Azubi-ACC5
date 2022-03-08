ecobank = {
    "firstname": "Pauline",
    "lastname": "Junior",
    "accType": "Current",
    "accNumber": "891011",
    "accBalance": "usd 45000"

}

firstname = input("Enter first name: ")
if firstname == ecobank["firstname"]:
    print("Your first name has been successfully verified")
else:
    print("Your first name cannot be verified, please try again")
lastname = input("Enter last name: ")
if lastname == ecobank["lastname"]:
    print("Your last name has been successfully verified")
else:
    print("Your last name cannot be verified, please try again")
accNumber = input("Enter account number: ")
if accNumber == ecobank["accNumber"]:
    print("This is a registered Current account with an account balance of " +
          ecobank["accBalance"])
else:
    print("Your account number is not in our database")
