def cache(func):
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
def tetranacci(n):
    if n in {1, 2, 3}:
        return 0
    elif n == 4:
        return 1
    else:
        return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)
