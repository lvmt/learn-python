# base.py

import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--ak-id', action="store")
parser.add_argument('--ak-secret', action="store")

