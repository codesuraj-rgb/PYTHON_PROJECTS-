import random
import string

def password_generator():
    ask = int(input("Enter the length of the password : "))
    if ask <= 0 :
        print("Password length should be greater than 0")
        return

    character =  string.ascii_letters +  string.digits + string.punctuation

    password = ''.join(random.choice(character) for _ in range(ask))

    print(f"Generated password : {password}")


password_generator()