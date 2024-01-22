from consts import COINS, SEQUENCE
import timeit

from utils import count_coins, generate_random_numbers, generate_dict_structure


def find_coins_greedy(number):
    count = dict()
    for coin in COINS:
        while coin <= number:
            if coin not in count:
                count[coin] = 0
            count[coin] += 1
            number = number - coin
    return generate_dict_structure(count)


def find_min_coins(number):
    max_of_min_coins = number // min(COINS)
    min_of_max_coins = [max_of_min_coins] * (number + 1)
    min_of_max_coins[0] = 0

    coins = [0] * (number + 1)

    for coin in COINS:
        for i in range(coin, number + 1):
            if min_of_max_coins[i - coin] + 1 < min_of_max_coins[i]:
                min_of_max_coins[i] = min_of_max_coins[i - coin] + 1
                coins[i] = coin

    if min_of_max_coins[number] == max_of_min_coins:
        numbers = list()
        for i in range(number + 1):
            if min_of_max_coins[i] != max_of_min_coins:
                numbers.append(i)
        max_possible_number = max(numbers)
        return count_coins(max_possible_number, coins)

    return count_coins(number, coins)


if __name__ == "__main__":
    for number in SEQUENCE:
        generate_random_numbers(number)

        greedy_algorythm = timeit.timeit(
            lambda: print(
                "Method of Greedy Algorythm | sum of money: {} ==> coins: {}".format(
                    number, find_coins_greedy(generate_random_numbers(number))
                )
            ),
            number=1,
        )
        print("greedy_algorythm: ", greedy_algorythm)

        dynamic_programming_algorythm = timeit.timeit(
            lambda: print(
                "Dynamic Programming Algorythm | sum of money: {} ==> coins: {}".format(
                    number, find_min_coins(generate_random_numbers(number))
                )
            ),
            number=1,
        )
        print("dynamic_programming_algorythm: ", dynamic_programming_algorythm)
