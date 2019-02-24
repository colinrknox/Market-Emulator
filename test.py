#!python
import sys
import subprocess
import pkgutil


test_args = 'python -m unittest'.split(' ')
input_modules = []
module_names = []

if len(sys.argv) > 1:
    input_modules = sys.argv[1:]

module_names = [name for _, name, _ in pkgutil.iter_modules(['test'])]

if input_modules:
    module_names = set(input_modules) & set(module_names)

if not module_names:
    err_string = 'No valid test file supplied.\nTry calling with no arguments to run all tests or specify an existing test module.'
    raise ValueError(err_string)

for module in module_names:
    subprocess.run(test_args + [f'test.{module}'])
