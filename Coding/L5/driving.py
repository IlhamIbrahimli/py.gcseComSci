age = int(input("Enter Age:"))
car = input("Do you have a car?(y/n):")
license = input("Do you have a car?(y/n):")

if age >=17 and car=="Y" and license=="Y":
    print("You are good to hit the road!")
elif car=="N":
    print("You are going to need a car!")
elif license == "N":
    print("You better take that test!")
else:
    print("You are gonna have to wait a couple of years!")
