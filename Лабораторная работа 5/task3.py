from random import randint
def get_unique_list_numbers():
    random_nub = []
    while len(random_nub) < 15:
        x = randint(-10, 10)
        if x not in random_nub:
            random_nub.append(x)
    return random_nub
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
