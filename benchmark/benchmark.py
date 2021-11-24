import os
import platform
import sys
from timeit import default_timer as timer
import concurrent.futures
from multiprocessing import Pool

environment_data = [('Python version', platform.python_version()),
                    ('Interpreter', platform.python_implementation()),
                    ('Interpreter version', sys.version),
                    ('Operating system', platform.system()),
                    ('Operating system version', platform.release()),
                    ('Processor', platform.processor()),
                    ('CPUs', os.cpu_count()),
                    ]


def function(n):
    i = 0
    _sum = 0
    while i <= n:
        _sum += (n - i) * i
        i += 1
    return _sum


function_arguments = [15972490, 80247910, 92031257, 75940266,
                      97986012, 87599664, 75231321, 11138524,
                      68870499, 11872796, 79132533, 40649382,
                      63886074, 53146293, 36914087, 62770938]


def time(func, ntimes, *args, **kwargs):
    output = []
    for i in range(ntimes):
        print(f"timing function {func.__name__}")
        s = timer()
        func(*args)
        output.append(timer() - s)
    return output


def test_func1(func, args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(func, args)


def test_func2(func, args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(func, args)


def test_func3(func, args):
    if __name__ == '__main__':
        with Pool(processes=4) as pool:
            pool.map(func, args)


def test_func4(func, args):
    if __name__ == '__main__':
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(func, args)


def run():
    outputs = [
        time(test_func1, 5, function, function_arguments),
        time(test_func2, 5, function, function_arguments),
        time(test_func3, 5, function, function_arguments),
        time(test_func4, 5, function, function_arguments),
    ]

    median = [f"{elem[2]:.3f}" for elem in [sorted(out) for out in outputs]]

    data = [[f"{elem[i]:.3f}" for elem in outputs] for i in range(5)]

    return data, median
