#!/usr/bin/python
import argparse
import requests 



# arguments
parser = argparse.ArgumentParser(description="test")
parser.add_argument('--get','-g', action='store_true', help="use get method", default=True)
parser.add_argument('--show','-s', action='store_true', help="print array", default=True)
parser.add_argument('--url','-u', help="url", default="https://api.chucknorris.io/jokes/random")
args = parser.parse_args()

#print(args)

if args.get == True:
    r = requests.get(args.url)

result = r.json()
if args.show == True:
    #print (result)
    print (result['value'])

