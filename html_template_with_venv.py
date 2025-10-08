#!/bin/python


import dominate
from dominate.tags import *



d = dominate.document()
d += h1("one header only")
d += p("paragraph")
print(d)
