"""
Run with:

python -m ansys.tools.example_coverage -f "path_to_package"

"""

import argparse

from .example_coverage import create_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate example coverage of a package.')
    parser.add_argument('-f', '--folder',
        help='path of the package to perform coverage analysis on')
    args = parser.parse_args()
    create_report(args.folder)
