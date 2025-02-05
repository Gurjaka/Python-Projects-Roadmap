import random

set1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
set2 = "1234567890"
set3 = "!@#$%&*-=_+`"
charset = ""

while True:
    pass_str = input("Choose the password level, Low, Medium, or High : ")
    pass_str = pass_str.lower()
    match pass_str:
        case "low":
            charset = set1
        case "medium":
            charset = set1 + set2
        case "high":
            charset = set1 + set2 + set3
        case _:
            print("Incorrect option!!!")
            continue
    break

while True:
    pass_len = input("Choose password length (minimum len = 8) : ")
    if pass_len.isdigit() and int(pass_len) < 8:
        print("Password length can not be less than 8")
    elif pass_len.isdigit() and int(pass_len) >= 8:
        pass_len = int(pass_len)
        break
    else:
        print("Invalid input! Must be numbers!")

back = ""
for i in range(pass_len):
    chars = random.randint(0,len(charset))
    back = back + charset[chars]

password = back
print(password)
