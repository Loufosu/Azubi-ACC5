# msg = "Hello world"
# print(msg)

# name = input("Enter your first name here ")
# print("Hi " + name)

print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("----------1 will bring MTN----------")
print("--------2 will bing vodafone--------")
print("-------------0 to exit--------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
Option = int(input("choose a bank "))
if (Option == 1):
    print("MTN is the beast")
elif (Option == 2):
    print("Vodafone: I hope you have sorted yourselves out")
elif (Option == 0):
    print("Thank You! Catch you later")
    exit()
else:
    print("Invalid response, try again")
