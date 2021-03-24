def cache(func):
    log = {}

    def wrapper(*args, **kwargs):
        cache_key = args
        if cache_key not in log:
            log[cache_key] = func(*args)
        print(f"Key: {cache_key}, Value: {log[cache_key]}")
        return log[cache_key]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
# print(fibonacci.log)