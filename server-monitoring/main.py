#!/usr/bin/python
# encoding: utf-8

import json
import porttest

from sys import argv

with open(argv[1]) as data_file:    
    data = json.load(data_file)

porttest.test_ports(data['services'])