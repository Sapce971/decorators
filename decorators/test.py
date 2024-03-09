import requests
import time
import re
import functools

from random import randint
BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения функции {func.__name__}: {end - start}")
        return result
    return wrapper

def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функция вызвана с параметрами:{args}, {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция была вызвана: {wrapper.calls} раз")
        result = func(*args, **kwargs)
        return result
    wrapper.calls = 0
    return wrapper

def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
    """
    cache = {}

    def fmemo(*args, **kwargs):
        key = str(*args,**kwargs)
        if key in fmemo.cache:
            return fmemo.cache[key]
        result = func(*args,**kwargs)
        fmemo.cache[key] = result
        return result

    fmemo.cache = cache
    return fmemo


@counter
@logging
@benchmark
@memo
def word_count(word, url=BOOK_PATH):
    """
    Функция для посчета указанного слова на html-странице
    """

    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+' , ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"

print(word_count('whole'))
print(word_count('whole'))
print(word_count('whole'))


@counter
def fib1(n):
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)

@counter
@memo
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)
fib1(10)
fib2(10)

