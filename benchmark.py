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

