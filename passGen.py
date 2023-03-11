import random
import string

len = int(input("Password length: "))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation

all = lower_case + upper_case + nums + symbols

password = "".join(random.sample(all, len))

print("Your password: ", password)