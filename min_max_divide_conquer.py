import colorama
from colorama import Fore

colorama.init(autoreset=True)


def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи в масиві за допомогою підходу «розділяй і володарюй».

    :param arr: список чисел
    :return: кортеж (мінімальне значення, максимальне значення)
    """
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


if __name__ == "__main__":
    numbers = [12, 4, 19, 33, 7, 1, 25, 18]
    min_val, max_val = find_min_max(numbers)

    print(Fore.GREEN + "Масив чисел:", numbers)
    print(Fore.CYAN + f"Мінімальне значення: {min_val}")
    print(Fore.MAGENTA + f"Максимальне значення: {max_val}")
