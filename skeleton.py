#!/usr/bin/python3
import sys
import argparse

def main(args = sys.argv[1:]):
    parser = argparse.ArgumentParser()

    parser.add_argument("--square",
                        help="Used for testing",
                        type=int,
                        default=None)

    parser.add_argument("--int_value",
                        help="display a square of a given number",
                        type=int)

    parser.add_argument("--float_value",
                        help="display a square of a given number",
                        type=int)

    parser.add_argument("-f",
                        "--flag",
                        help="Specify a flag",
                        action="store_true")
    parser.add_argument("--rating",
                        help="An option with a limited range of values",
                        choices=[1, 2, 3],
                        type=int)

    # Allow --day and --night options, but not together.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--day",
                       help = "mutually exclusive option",
                       action = "store_true")
    group.add_argument("--night",
                       help = "mutually exclusive option",
                       action = "store_true")

    args = parser.parse_args(args)


if __name__ == '__main__':
    main()




