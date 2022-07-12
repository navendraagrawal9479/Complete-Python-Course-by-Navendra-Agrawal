# bmi = weight/(height*height)
# bmi<=18.5 - underweight
# 18.5<bmi<=25.9 - normal
# 25.9<bmi<=29.9 - overweight
# bmi>29.9 - obese

weight = float(input("What is your weight in Kgs- "))
height = float(input("what is your height in m- "))

bmi = round(weight/(height**2),3)
print(f"Your BMI is {bmi}")

if bmi<=18.5:
    print("You are underweight.")
elif bmi>18.5 and bmi<=25.9:
    print("You are normal.")
elif bmi>25.9 and bmi<=29.9:
    print("You are overweight.")
else:
    print("You are obese.")
