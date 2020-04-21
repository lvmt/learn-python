# aws.py
import argparse
import base

parser = argparse.ArgumentParser(
    parents=[base.parser],
)

parser.add_argument('--cloudformation',
                    action="store_true",
                    default=False,
                    help='Using CloudFormation service to orchestrate cloud resources')

args = parser.parse_args() 



