import os
import platform
import sys
import timeit
import function as f

environment_data = [('Python version', platform.python_version()),
                    ('Interpreter', platform.python_implementation()),
                    ('Interpreter version', sys.version),
                    ('Operating system', platform.system()),
                    ('Operating system version', platform.release()),
                    ('Processor', platform.processor()),
                    ('CPUs', os.cpu_count()),
                    ]

function, ntimes, arguments = f.function, f.ntimes, f.function_arguments
