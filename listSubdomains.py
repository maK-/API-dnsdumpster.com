#!/usr/bin/env python
from DNSDumpsterAPI import DNSDumpsterAPI
from NetcraftAPI import NetcraftAPI
import sys

domain = sys.argv[1]
res = DNSDumpsterAPI({'verbose': False}).search(domain)
res2 = NetcraftAPI({'verbose': False}).search(domain)

for i in res:
	print i+'.'+domain

for i in res2:
	if i not in res:
		print i+'.'+domain


