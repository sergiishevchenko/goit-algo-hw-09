from faker import Faker


def generate_random_numbers(number):
    faker = Faker()

    random = faker.random_int(max=number)
    return random

def generate_dict_structure(in_dict):
    result = { key: value for key, value in in_dict.items() }
    return result

def count_coins(number, coins):
    counts = dict()

    while number > 0:
        coin = coins[number]
        if coin in counts:
            counts[coin] += 1
        else:
            counts[coin] = 1
        number = number - coin
    return generate_dict_structure(counts)
