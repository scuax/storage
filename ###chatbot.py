###chatbot
name=input("hello, what's your name?\n")
print("Nice to meet you,",name)
hobbies=input("What are your hobbies? ")
day=input("Please enter your birth day (DD): ")
#check if the input is a number
if type(int(day))!=int:
    print("The day must be a number.")
else:
    month=input("Please enter your birth month (MM): ")
    if type(int(month))!=int:
        print("The month must be a number.")
    else:
        year=input("Please enter your birth year (YYYY): ")
        if type(int(year))!=int:
            print("The year must be a number.")
        else:
            print("Thanks for providing your date of birth: ",day,"/",month,"/",year)
#print the outputs
print("here's what I've learned about you,",name,":")
print("your date of Birth is",day,"/",month,"/",year,"and your hobbies are",hobbies)
print("thanks for chatting with me")