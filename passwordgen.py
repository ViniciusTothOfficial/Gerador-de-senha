import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "!@#$%"

length1 = 5
num1 = "".join(random.sample(num,length1))

ans = lower_case + upper_case + num + symbol
length = 12
password = "".join(random.sample(ans,length))
print("Your password: ", password, "\n")
with open(num1 + " password.txt", "w") as arquivo:
    arquivo.write("Your password: " + password + "\n")
