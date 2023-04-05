'''Игра угадай число'''

import numpy as np

def game_core_v3(number:int=1) -> int:
    """Угадываем число бинарным алгоритмом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # число попыток
    low = 1 # минимальный порог диапазона
    high = 100 # максимальный порог диапазона
    
    while low <= high: # объявляем цикл, пока границы диапазона не схлопнутся
        mid = (low + high) // 2 # среднее значение диапазона
        count += 1
        # определяем в каком диапазоне находится число
        if mid == number:
            return count
        elif mid > number:
            high = mid - 1
        else:
            low = mid + 1
            
    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
    return (score)

if __name__ == '__main__':
    score_game(game_core_v3)