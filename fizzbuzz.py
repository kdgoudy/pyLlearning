#Creating FizzBuzz game. 
#If number / 3 = "Fizz"
#If number / 5 = "Buzz"
#If number / 3 and / 5 = "FizzBuzz"


for number in range(0, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
