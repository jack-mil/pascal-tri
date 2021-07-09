"""
Run pascal triangle generation interactivly

If LINES not specified, runs in interactive loop
"""
import os
import sys
import argparse as argp
from pascal import print_pascal, version


def main():
    parser = argp.ArgumentParser(
        prog="python -m pascal",
        description=__doc__,
        formatter_class=argp.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-l", "--lines", help="The number of lines to print", type=int)
    parser.add_argument(
        "-v", "--version", action="store_true", help="Print the script version and exit"
    )
    args = parser.parse_args()

    if args.version:
        print(f"Pascal Triangle version: {version()}")
        sys.exit(0)

    if args.lines is not None:
        print_pascal(args.lines)
    else:
        while True:  # Emulate do_while loop
            try:
                lines = input("Number of lines: ")

                try:
                    print_pascal(int(lines))
                except ValueError:
                    print("Please enter an integer.")

                response = input(
                    "\n...press enter to continue.... type 'stop' to exit\n"
                )
                if response == "stop":
                    break

                # Clear the console
                os.system("cls" if os.name == "nt" else "clear")
            except KeyboardInterrupt:
                break
        print("\nExited")
        sys.exit(0)


# execute only if run as a script
if __name__ == "__main__":
    try:
        main()
    except Exception as _e:
        print(f"Error: {_e}", file=sys.stderr)
        sys.exit(1)
