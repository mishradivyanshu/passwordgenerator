
import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZszxcdewrfvbgthynmjukiolp!@#$%^&*.'"
length = input("password length")
length = int(length)
password = ''
for c in range(length):
  password+= random.choice(chars)
print(password)
