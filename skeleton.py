#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description="test")
parser.add_argument('--foo','-f', action='store_true', help="foo test")
parser.add_argument('--bar','-b', type=int, help="bar test")
args = parser.parse_args()

print(args)
