"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from memory_profiler import memory_usage


def fib_gen(n):
    a, b, num = 1, 1, 0
    while num < n:
        num += 1
        yield a

        a, b = b, a + b


def fib(n):
    res = [1, 1]
    cnt = len(res)
    while cnt < n:
        res.append(res[cnt - 2] + res[cnt - 1])
        cnt += 1
    return res


if __name__ == '__main__':
    n = 10000

    # Использовано памяти при работе с генератором 0.00390625
    start = memory_usage()[0]
    for s in fib_gen(n):
        pass
    print(f'Использовано памяти при работе с генератором {memory_usage()[0] - start}')

    # Использовано памяти при накоплении чисел в массиве 0.39453125
    start = memory_usage()[0]
    for s in fib(n):
        pass
    print(f'Использовано памяти при накоплении чисел в массиве {memory_usage()[0] - start}')

    # Вывод: при выполнении через генератор не требуется хранить в памяти массив чисел Фибоначчи
    # для того, чтобы отдать их.
