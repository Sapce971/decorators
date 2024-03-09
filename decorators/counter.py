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
