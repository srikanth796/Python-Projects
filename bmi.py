weight = int(input("what is your weight?\n"))
height = int(input("what is your height(cm)?\n"))
BMI = round(weight/height**2,2)
if BMI <= 18.5:
    print("underweight")
elif BMI >= 18.5 & BMI <= 25:
    print("normal weight")
elif BMI >= 30 & BMI <= 35:
    print("obese")
else:
    print("critically obese") 