print("----------------------------------")
print("----------------------------------")
print("----------------------------------")
print("--------1 will bring MTN----------")
print("------2 will bring Vodafone-------")
print("------------0 to exit-------------")
print("----------------------------------")
print("----------------------------------")
print("----------------------------------")
Option = int(input("choose a bank"))
if (Option == 1):
    print("MTN is the beast")
elif(Option == 2):
    print("Vodafone: I hope you have tissues")
elif(Option == 0):
    print("Thank You! Catch you later")
    exit()
else:
    print("Invalid response, try again")
