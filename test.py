#!python
import sys
import subprocess
import pkgutil

if __name__ == '__main__':
    test_args = 'python -m unittest'.split(' ')
    module_names = []

    if len(sys.argv) > 1:
        module_names = sys.argv[1:]
    else:
        module_names = [name for _, name, _ in pkgutil.iter_modules(['test'])]

    for module in module_names:
        subprocess.run(test_args + [f'test.{module}'])
