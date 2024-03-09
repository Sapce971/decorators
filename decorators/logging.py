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
