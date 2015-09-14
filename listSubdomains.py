#!/usr/bin/env python
from DNSDumpsterAPI import DNSDumpsterAPI
import sys

domain = sys.argv[1]
res = DNSDumpsterAPI({'verbose': False}).search(domain)
for i in res:
	print i+'.'+domain
