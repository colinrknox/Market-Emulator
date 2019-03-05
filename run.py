import sys
from src.engine import read_eval_print_loop


# Command line file to run the project
# Usage is described in the README as well as the error message in this file

if __name__ == '__main__':
    if len(sys.argv) == 2:
        read_eval_print_loop(sys.argv[1])
    elif len(sys.argv) == 1:
        read_eval_print_loop()
    else:
        print(f"Invalid number of arguments {len(sys.argv) - 1}")
        print("Usage: run.py {name} (optional)")
        print("No arguments - You will be prompted to create a new portfolio")
        print("{name} - the name of the portfolio that you wish to open should be in /resources")
