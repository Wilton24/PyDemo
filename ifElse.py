# numberInputted = input("Input a number: ")

# if int(numberInputted) <= 10:
#     print('The number you inputted is SMOL')
# elif int(numberInputted) > 10 and int(numberInputted) <= 50:
#     print("your number is MID")
# else:
#     print("Your number is as big as yo Mama!")


temperature = input("Input a temperature: ")
message = "Temperature is too hight" if int(
    temperature) > 99 else "Temperature is normal"

print(message)
