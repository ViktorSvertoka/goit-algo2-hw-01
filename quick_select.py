import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def quick_select(arr, k):
    """
    Знаходить k-й найменший елемент у невідсортованому масиві
    за допомогою алгоритму Quick Select.

    :param arr: список чисел
    :param k: позиція (1-індексація), яку потрібно знайти
    :return: k-й найменший елемент
    """
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(mid))


if __name__ == "__main__":
    numbers = [12, 4, 19, 33, 7, 1, 25, 18]
    k = 3  # шукаємо 3-й найменший елемент

    print(Fore.GREEN + "Масив чисел:", numbers)
    kth_element = quick_select(numbers, k)
    print(Fore.YELLOW + f"{k}-й найменший елемент: {kth_element}")
