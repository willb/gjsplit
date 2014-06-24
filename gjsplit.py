#!/usr/bin/env python

import json
import argparse
import itertools
from copy import deepcopy
import sys

def gjsplit(file, criteria):
  struct = json.loads(open(file, "r").read())
  original = deepcopy(struct)
  features = struct['features']
  keyed = sorted([(tuple([feature['properties'][k] for k in criteria]), feature) for feature in features])
  for k, g in itertools.groupby(keyed, lambda x: x[0]):
    ofname = "%s%s" % ("".join([c for c in str(k) if c not in "( )#'\""]).replace(",", "-"), file)
    struct['features'] = list(g)
    outfile = open(ofname, "w")
    outfile.write(json.dumps(struct))
    outfile.close

def main(args=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('--splitby', action='append')
  parser.add_argument('files', metavar='FILE', nargs='+')
  options = parser.parse_args(args)
  for file in options.files:
    gjsplit(file, options.splitby)

if __name__== "__main__":
  main()