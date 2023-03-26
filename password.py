import random
import string

def gen_pass(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


password = gen_pass(234)
print(password)

