height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height * height)
print(round(bmi))

if bmi < 18:
  print("You are underweight")
elif bmi > 18 and bmi < 25:
  print("You have normal weight")
elif bmi > 26 and bmi < 30:
  print("You are slightly overweight")
elif bmi > 30 and bmi < 35:
  print("You are obese")
else:
  print("You are clinically obese")
