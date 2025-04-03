import random
import string

val = string.ascii_letters + string.digits + string.punctuation
le = int(input("Enter the length of Password: "))

pa = ""
for i in range(le):
    pa += random.choice(val)

print("Password Generated: ", pa)