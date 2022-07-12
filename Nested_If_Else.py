# age >=18 - ticket price = Rs.30
# age<18 - ticket price = Rs.20

# height = int(input("What is your height in cm? "))
# if height>=130:
#     print("You can ride.")
#     age = int(input("What is your age? "))
#     if age<18:
#         print("Your ticket costs Rs.20.")
#     else:
#         print("Your ticket costs Rs.30.")
# else:
#     print("You have to grow taller.")

# age >=18 - ticket price = Rs.30
# 12<age<18 - ticket price = Rs.20
# age<=12 -  ticket price = Rs.10

height = int(input("What is your height in cm? "))
if height>=130:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age<=12:
        print("Your ticket costs Rs.10.")
    elif age<=18:
        print("Your ticket costs Rs.20.")
    else:
        print("Your ticket costs Rs.30.")
else:
    print("You have to grow taller.")