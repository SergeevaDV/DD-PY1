import string
import random
from random import sample
def get_random_password() -> str:
    password_random = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

    return password_random

print(get_random_password())
