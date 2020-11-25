#!/usr/bin/env python
"""
Runs a basic smoke test to check all the .yml files are syntactically OK.
"""
import pprint
import yaml
import os


scripts_dir = os.path.dirname(__file__)
os.chdir(os.path.join(scripts_dir, '..', 'terms'))  # go to the terms/ directory

for filename in os.listdir('.'):
    if filename.endswith('.yml'):
        print('Checking ' + filename + ' ...')
        termsetdata = yaml.safe_load(open(filename))
        assert termsetdata, 'empty termset fixture file'
        assert isinstance(termsetdata, dict)
        # pprint.pprint(data)

print('YAML files seem to be loading OK...')

