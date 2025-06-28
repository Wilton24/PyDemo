# numberInputted = input("Input a number: ")

# if int(numberInputted) <= 10:
#     print('The number you inputted is SMOL')
# elif int(numberInputted) > 10 and int(numberInputted) <= 50:
#     print("your number is MID")
# else:
#     print("Your number is as big as yo Mama!")


# temperature = input("Input a temperature: ")
# message = "Temperature is too hight" if int(
#     temperature) > 99 else "Temperature is normal"

# print(message)


# for c in range(3):
#     print(c)


# target = 420

# for c in range(1, 500):
#     print(c)
#     if c == target:
#         print("Happy Weed day")
#         break


password = ""

while password != "pass123":
    password = input('Input password: ')
    if password == "pass123":
        break
    print("Wrong password")


print('Logged in!')
