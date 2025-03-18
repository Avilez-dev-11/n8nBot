from argon2 import PasswordHasher
import random


def password(size=9):
    seed = random.randint(0, 1000)
    random.seed(seed)
    ph = PasswordHasher()
    password = input("Enter your favorite cereal: ")
    hash = ph.hash(password)
    print("Hash: ", hash[30:30+size])

    return hash[30:30+size]


if __name__ == "__main__":
    pwd = password()
    key = password(13)
