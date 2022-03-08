name = input("Enter your name: ")
age = input("Enter your age: ")
try:
    if int(age) >= 18:
        print("Hello " + name +
              " you are eligible to continue the application for the job ")
    else:
        print("you are young and cannot apply for this job")
except:
    print("Sorry, try again")

countries = ["Ghana", "Kenya", "Rwanda", "Ukraine", "Russia", "India", "Niger"]
for item in countries:
    print(countries[1])
counter = 0
# while counter <=5:
#     print("Welcome to Jumanji")
counter += 1

print(2*3+3**2)
msg = "The answer is:"
**msg2 = msg + "AWS"**
print(msg2)
