user_age = int(input("Hello would you like to buy a ticket? Please tell us your age!!"))
print(user_age)
#IF 5 or under FREE
if user_age <5 :
    print("You are under the age of 5 so your ticket is free")
#if 5 - 17 10$
elif user_age >=5 and user_age <=17:
    print("Your ticket will cost 10$")
#18 - 60
elif user_age >=18 and user_age <60:
    print("Your ticket will cost 20$")
#60
elif user_age >=60:
    print("ticket 15$!")
else:
    print("Your age is not suitable")



time = int(input("What time is it? "))
if 500 <= time <= 1100:
    print("It's breakfast you could have eggs, toast, or cereal.")
elif 1200 <= time <= 1600:
    print("It's lunch  you could have a sandwich, salad, or pasta.")
elif 1700 <= time <= 2100:
    print("It's dinner You could have steak, rice, or vegetables.")
elif 2200 <= time or time < 400:
    print("It's late-night want a snack  You could have chips, cookies, or fruit.")
else:
    print("Are you dumb!")


