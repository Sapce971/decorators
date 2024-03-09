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
