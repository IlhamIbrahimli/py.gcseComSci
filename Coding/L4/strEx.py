
# Keep this here - you need it for exercises 1 and 2
message = "This is a message. It is a made up of many words."


# Write your solutions in the appropriate subroutines below
def ex1():
    
    print(message[5])
    print(message[1:9])
    print(len(message))
    print(message.title())

    
def ex2():
    
    print(len(message.split(" ")))


def ex3(pwd):
    
    if len(pwd) < 8 or len(pwd) > 14:
        print("Invalid")
    else:
        print("Valid")



def ex4(pwd):
    CharList = ["$","!","%","@","-"]
    TempCount = 0
    for i in CharList:
        if i in pwd:
            TempCount += 1

    if (len(pwd) < 8 or len(pwd) > 14) or TempCount < 2:
        print("Invalid")
    else:
        print("Valid")


def ex5(og_text):
    og_text = og_text.lower()
    og_text = og_text.replace("e","3")
    og_text = og_text.replace("1","!")
    og_text = og_text.replace("a","@")
    og_text = og_text.replace("i","1")
    og_text = og_text.replace("o","0")
    og_text = og_text.replace("s","5")
    print(og_text)


# Run your subroutines - comment out any that you don't want to run anymore!
#ex1()
#ex2()
#ex3(input("Enter pwd:"))
#ex4(input("Enter pwd:")) # you can change the argument to anything you like to test your solution
ex5("mystrongpassword") # you can change the argument to anything you like to test your solution
