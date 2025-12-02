import random
print("Welcome to the random number generator!")
while True:
 print("Select a number(number cannot be smaller than 1, there are no limits on maximum lenth).")
 try:
  a=int(input())
 except ValueError:
  print("That is not a number, please enter a valid and real number that is larger than 0.9")
  continue
 b=random.randint(1, a)
 print("Your random number is")
 print(b)