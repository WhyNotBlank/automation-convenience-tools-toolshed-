print("Welcome to the weapon calculator!")
print("Enter your weapon`s speed(in seconds) and damage stats to get a strength value.")
print("If a weapon`s strength value is higher than another weapon`s strength value it means that")
print("that weapon is better.")

print("=" * 50)
print("IMPORTANT, make sure you multiply weapon speed by 100.")
print("Exampe; weapon speed = 1.5 seconds, what you put in: 150.")

while True:

    print("=" * 50)   
    damage = input("Enter weapon damage: ")
    speed = input("Enter weapon speed: ")
    print("=" * 50)

    try:

        damage = int(damage)
        speed = int(speed)

    except ValueError:

        print("=" * 50)  
        print("ValueError! Try again, please input correct values!")
        continue

    #Formula is damage divided by speed(which is first multiplied by 100).

    result = damage / speed

    print(f"Your weapon`s strength is {result}.")      