# ali.py

import argparse
import base

parser = argparse.ArgumentParser(
    parents=[base.parser],
    add_help=True
)

parser.add_argument('--ros',
    action="store_true",
    default=False,
    help="Using ROS service to orchestrate cloud resouces")

args = parser.parse_args()
